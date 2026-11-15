# NASA HFBP-EM: Mood, Affect & Social Dynamics (20-Item Assessment)

Interactive offline tool designed for spaceflight behavioral health monitoring, based on the **NASA HFBP-EM Suite (Bell et al., 2022)**, the **UCLA Loneliness Scale Short Form (Hughes et al., 2004)**, and **NIMH RDoC Social Process Criteria**.

---

## 🚀 Overview

The **HFBP-EM 20-Item Assessment** is a specialized, daily micro-instrument developed to capture daily fluctuations in astronaut emotional resilience, workload strain, and group integration in Isolated, Confined, and Extreme (ICE) environments.

* **Mode of Administration:** Daily evaluation measuring affective state *"in this exact moment"* (intra-individual variation).
* **Rating Scale:** 5-point Likert scale from `0 = Not at all` to `4 = Extremely`.
* **Execution:** 100% offline, standalone HTML/JS client with zero external dependencies.

---

## 📐 Architecture: Two-Block Structure

### Block 1: Individual Mood & Affect (Items 1–16)
Four intra-individual subscales (4 items each, 0–16 pts):
1. **Tension / Anxiety ($T$):** Items 1 (*Tense*), 5 (*Anxious*), 9 (*Nervous*), 13 (*Restless*).
2. **Depression / Motivation ($D$):** Items 2 (*Disengaged*), 6 (*Unenthusiastic*), 10 (*Sad*), 14 (*Discouraged*).
3. **Anger / Hostility ($C$):** Items 3 (*Angry*), 7 (*Annoyed*), 11 (*Resentful*), 15 (*Furious*).
4. **Fatigue / Inertia ($F$):** Items 4 (*Tired*), 8 (*Exhausted*), 12 (*Fatigued*), 16 (*Worn out*).

### Block 2: Team & Social Dynamics (Items 17–20)
One group living and cohesion subscale (4 items, 0–16 pts):
5. **Loneliness & Social Isolation ($S$):** Items 17 (*Isolated*), 18 (*Lonely*), 19 (*Left out*), 20 (*Unsupported*).
   * *Methodological Note:* Items 17–20 are phrased in negative polarity ("Unsupported" rather than "Supported") to maintain directional alignment across all items.

---

## 🧮 Psychometric Scoring (Base 80 Points)

### Global Psychosocial Load Index ($I_{\text{total}}$)
$$I_{\text{total}} = T + D + C + F + S \quad (\text{Range: } 0 \text{ to } 80 \text{ points})$$

### Operational Decision Thresholds
* **0 – 20 pts (Mean 0.0 – 1.0):** 🟢 **FIT FOR FLIGHT / Nominal State** — Optimal emotional stability and group integration.
* **21 – 40 pts (Mean 1.1 – 2.0):** 🟡 **MONITORING REQUIRED / Caution** — Moderate psychosocial load. Identify subscales exceeding 8 points.
* **41 – 80 pts (Mean > 2.0):** 🔴 **RESTRICTED DUTY / Critical Alert** — High acute distress, fatigue, or social isolation. Workload adjustment and rest mandated.

---

## 📁 Files Included

* `cuestionario_iws.html`: Standalone interactive application with non-linear spatial option layout, anti-habituation engine, and background calculation pipeline.
* `vaca_pixel_transparente.png`: Pixel-art mascot asset (Dr. Moo, Space Psychologist).
* `README.md`: Technical documentation and clinical scoring guidelines.

## 💻 How to Run
Simply double-click `cuestionario_iws.html` to open it in any modern browser (Chrome, Edge, Firefox, Safari).
No installation, internet connection, or server required.
