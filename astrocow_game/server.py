"""
SCAN SPACE — AstroCow Flight Simulator Backend
NASA Space Apps Challenge 2026

Standalone Python server that:
  1. Serves game files (HTML, assets)
  2. Receives and processes neuro-telemetry in the background
  3. Calculates cognitive-motor metrics
  4. Automatically records each flight into telemetry_data.json
"""

import http.server
import json
import os
import math
import time
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "telemetry_data.json")

def calculate_neuro_metrics(raw):
    """
    Computes 6 NASA clinical metrics:
    1. Eye-Hand Coordination
    2. Reaction Time (ms)
    3. Motor Control
    4. Visual Pursuit
    5. Sustained Attention
    6. Motor Learning
    """
    taps = raw.get("tapTimestamps", [])
    reactions = raw.get("reactionPairs", [])
    start = raw.get("sessionStartMs", 0)
    end = raw.get("sessionEndMs", 0)
    score = raw.get("score", 0)
    hits = raw.get("hits", 0)
    attempt = raw.get("attempt", 1)

    duration_s = max((end - start) / 1000, 1)

    # 1. Eye-hand coordination — tap interval variance
    intervals = [taps[i] - taps[i-1] for i in range(1, len(taps))]
    if len(intervals) >= 2:
        mean_int = sum(intervals) / len(intervals)
        variance = sum((x - mean_int) ** 2 for x in intervals) / len(intervals)
        sigma_int = math.sqrt(variance)
    else:
        mean_int = 0
        sigma_int = 0
    coord_score = max(0, min(100, 100 - sigma_int / 5))

    # 2. Reaction time — ms between visual reticle and tap response
    rt_values = [r["response"] - r["stimulus"] for r in reactions if "response" in r and "stimulus" in r]
    mean_rt = sum(rt_values) / len(rt_values) if rt_values else 0

    # 3. Motor control
    motor_score = max(0, min(100, 100 - sigma_int / 4)) if intervals else 50

    # 4. Visual pursuit
    beacon_total = raw.get("beaconTotal", 0)
    beacon_hit = raw.get("beaconHit", 0)
    pursuit_pct = (beacon_hit / beacon_total * 100) if beacon_total > 0 else 0

    # 5. Sustained attention
    half = len(intervals) // 2
    if half > 1:
        first_sigma = math.sqrt(sum((x - (sum(intervals[:half]) / half)) ** 2 for x in intervals[:half]) / half)
        second_sigma = math.sqrt(sum((x - (sum(intervals[half:]) / len(intervals[half:]))) ** 2 for x in intervals[half:]) / len(intervals[half:]))
        vigilance_decay = second_sigma - first_sigma
    else:
        vigilance_decay = 0
    attention_score = max(0, min(100, 100 - abs(vigilance_decay) / 3))

    # 6. Motor learning
    learning_index = min(100, score * 5 + attempt * 4)

    def classify(val, good, warn):
        if val >= good: return "NOMINAL"
        elif val >= warn: return "ALERT"
        return "CRITICAL"

    def classify_rt(val):
        if val == 0: return "NOMINAL"
        if val < 420: return "NOMINAL"
        elif val < 700: return "ALERT"
        return "CRITICAL"

    return {
        "eyeHandCoordination": {
            "score": round(coord_score, 1),
            "tapSigmaMs": round(sigma_int, 1),
            "status": classify(coord_score, 60, 35)
        },
        "reactionTime": {
            "meanMs": round(mean_rt, 1),
            "samples": len(rt_values),
            "status": classify_rt(mean_rt)
        },
        "motorControl": {
            "score": round(motor_score, 1),
            "meanIntervalMs": round(mean_int, 1),
            "status": classify(motor_score, 55, 30)
        },
        "visualPursuit": {
            "accuracy": round(pursuit_pct, 1),
            "beaconsHit": beacon_hit,
            "beaconsTotal": beacon_total,
            "status": classify(pursuit_pct, 50, 25)
        },
        "sustainedAttention": {
            "score": round(attention_score, 1),
            "status": classify(attention_score, 55, 30)
        },
        "motorLearning": {
            "index": round(learning_index, 1),
            "attempt": attempt,
            "status": classify(learning_index, 40, 20)
        },
        "flightSummary": {
            "durationS": round(duration_s, 1),
            "score": score,
            "hits": hits,
            "totalTaps": len(taps)
        }
    }


class SpaceHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=BASE_DIR, **kw)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/telemetry":
            self._send_json(self._load_data())
        elif path == "/api/neuro-assessment":
            data = self._load_data()
            self._send_json({"totalFlights": len(data), "recent": data[-10:]})
        elif path in ("/", ""):
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/telemetry":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            metrics = calculate_neuro_metrics(body)
            record = {
                "id": f"flight_{len(self._load_data()) + 1}",
                "participantId": body.get("participantId", "AST001"),
                "stage": body.get("stage", "In-Flight"),
                "evaluationDay": body.get("evaluationDay", "FD030"),
                "dateTime": body.get("dateTime", time.strftime("%Y-%m-%d %H:%M")),
                "module": body.get("module", "AST-01"),
                "difficultyLevel": body.get("difficultyLevel", 1),
                "durationSeconds": body.get("durationSeconds", body.get("flightTimeSeconds", 1)),
                "meanReactionTimeMs": body.get("meanReactionTimeMs", metrics["reactionTime"]["meanMs"]),
                "collisions": body.get("collisions", body.get("hits", 0)),
                "precisionPct": body.get("precisionPct", metrics["visualPursuit"]["accuracy"]),
                "testStatus": body.get("testStatus", "Completed"),
                "handUsed": body.get("handUsed", "Right"),
                "device": body.get("device", "Laptop A"),
                "observations": body.get("observations", "Normal practice session"),
                "behavioralIndicators": body.get("behavioralIndicators", {}),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "crewId": body.get("crewId", "AST001"),
                "attempt": body.get("attempt", 1),
                "flightMetrics": metrics
            }
            data = self._load_data()
            data.append(record)
            self._save_data(data)
            self._send_json(metrics)
        else:
            self.send_error(404)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _send_json(self, obj):
        payload = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.end_headers()
        self.wfile.write(payload)

    def _load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save_data(self, data):
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def log_message(self, fmt, *args):
        # Clean logging
        pass


def run_server():
    ports_to_try = [8000, 8080, 8888]
    for port in ports_to_try:
        try:
            server = http.server.HTTPServer(("", port), SpaceHandler)
            print(f"[SCAN SPACE] AstroCow Server active at http://localhost:{port}/")
            server.serve_forever()
            break
        except OSError:
            continue

if __name__ == "__main__":
    run_server()
