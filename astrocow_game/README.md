# AST-01: AstroCow Sensorimotor & Reflex Telemetry Simulator

Interactive sensorimotor, eye-hand coordination, and stimulus-adaptation simulator designed for spaceflight behavioral and cognitive-motor monitoring (**Module `AST-01`**).

---

## 🚀 Overview

The **AST-01 AstroCow Simulator** evaluates dual-task sensorimotor performance: continuous micro-thruster flight control combined with timed peripheral visual target interception under progressive environmental load.

* **Dual-Task Paradigm:** Simultaneous vertical flight stabilization (`[W]`, `[Shift]`, `[Ctrl]`, `[Space]`, or Left Click) and peripheral target acquisition (`Mouse Move / Hover`, `Click`, or `[E]` / `[Enter]`).
* **Radar Pre-Warning System (`Key R`):** Optional 2.5-second pre-spawn radar indicator showing the trajectory vector to upcoming targets.
* **Time-Based Progressive Difficulty (Levels 1 to 5):** Starts in an ultra-accessible warm-up configuration (`620 px` pillar spacing, `310 px` vertical corridor, `1.35` scroll speed) and automatically steps up difficulty every **15 seconds** of flight time.
* **Live Behavioral JSON Telemetry:** Exports real-time and post-flight clinical JSON records (`💾 SAVE / DOWNLOAD JSON`) with full adaptation and recovery indicators.

---

## 📊 Behavioral & Clinical Indicators Recorded

| Recorded Metric | Unit | Clinical Interpretation |
| :--- | :---: | :--- |
| **Reaction Time to Changes** | `ms` | Speed of adaptation to a newly spawned target or level shift |
| **Errors After Change** | `count` | Collisions or missed stimuli immediately following a change |
| **Recovery Time ($T_{\text{recovery}}$)** | `s` | Time required to return to stable flight/target performance |
| **Omitted Responses** | `count` | Timed targets that expired without crew response |
| **Reaction Time Variability** | `ms` | Standard deviation ($\sigma$) measuring sensorimotor consistency |
| **Performance per Minute** | `%` | Minute-by-minute evolution of accuracy across the test |

### Recovery Time Formula
$$T_{\text{recovery}} = t_{\text{stable\_performance}} - t_{\text{change}}$$

---

## 🗂️ Standardized Session JSON Schema

```json
{
  "participantId": "AST001",
  "stage": "In-Flight",
  "evaluationDay": "FD030",
  "dateTime": "2026-11-14 10:00",
  "module": "AST-01",
  "difficultyLevel": 2,
  "durationSeconds": 120,
  "meanReactionTimeMs": 370,
  "collisions": 4,
  "precisionPct": 87,
  "testStatus": "Completed",
  "handUsed": "Right",
  "device": "Tablet A",
  "observations": "Normal practice session"
}
```

---

## 📁 Files Included

* `index.html`: Widescreen (`900 × 560`) interactive simulator with time-based progressive difficulty, radar preview, simultaneous keyboard/mouse input, and JSON export.
* `server.py`: Standalone Python HTTP & telemetry server (`/api/telemetry`).
* `telemetry_data.json`: Standardized clinical and behavioral telemetry store.
* `iniciar_servidor.bat`: One-click local server launcher for Windows.
* `assets/`: Stage backgrounds (`bg_stage_1.png`–`bg_stage_4.png`) and astronaut cow sprite (`vaca_sprite.png`).
