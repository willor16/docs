# HFBP-EM & APA DSM-5-TR: Mood, Affect & Social Dynamics (20-Item Assessment)

Interactive offline tool designed for spaceflight behavioral health monitoring and remote rural telemedicine, integrating the **HFBP-EM Suite (Bell et al., 2022)**, the **UCLA Loneliness Scale Short Form (Hughes et al., 2004)**, **NIMH RDoC Social Process Criteria**, and the **American Psychiatric Association (APA) DSM-5-TR Severity Measures (Adult GAD & PHQ-9)**.

---

## 🚀 Overview

The **HFBP-EM 20-Item Assessment** is a specialized daily micro-instrument developed to capture intra-individual fluctuations in astronaut emotional resilience, workload strain, and group integration in Isolated, Confined, and Extreme (ICE) environments, with an automatic **APA DSM-5-TR Clinical Severity Cross-Walk** for terrestrial and flight medical officers.

* **Mode of Administration:** Daily evaluation measuring affective state *"in this exact moment"* (intra-individual variation), paired with a 7-day DSM-5-TR clinical follow-up trigger.
* **Rating Scale:** 5-point scale from `0 = Not at all` to `4 = Extremely` (aligned with the 0–4 mean severity metric of the APA DSM-5-TR GAD measure).
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

## 🏥 APA DSM-5-TR Clinical Severity Cross-Walk (GAD & PHQ-9)

To bridge spaceflight telemetry with standard terrestrial psychiatry and rural telemedicine, the background engine maps subscales $T$, $D$, and $F$ onto the official **APA DSM-5 / DSM-5-TR Severity Measures**:

### 1. Comparison of Reference APA Instruments
| Instrument | Evaluates | Target Age | Items | Score Range | Inclusion in System |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **GAD (DSM-5-TR)** | Generalized Anxiety Severity | Adults (18+ yrs) | 10 | 0–40 (Mean 0–4) | ✅ Integrated via Subscale $T$ Cross-Walk |
| **PHQ-9 (DSM-5-TR)** | Depressive Symptom Severity | Adults (18+ yrs) | 9 | 0–27 | ✅ Integrated via Subscales $D + F$ Cross-Walk |
| **GAD-7** | General Anxiety Screening | Adults | 7 | 0–21 | ℹ️ Distinct from the 10-item DSM-5-TR GAD Severity Measure |
| **GAD-C** | Pediatric Anxiety | 11–17 yrs | 10 | 0–40 | ❌ Excluded (Adult Crew Population) |

### 2. APA Mean Severity Metric (0–4 Scale) & PHQ-9 Severity Tiers
* **GAD (DSM-5-TR) Mean Score ($0.00 \text{ to } 4.00$):** Calculated by dividing the subscale sum by the number of items:
  * `0` (`0.00–0.49`): **None**
  * `1` (`0.50–1.49`): **Mild**
  * `2` (`1.50–2.49`): **Moderate**
  * `3` (`2.50–3.49`): **Severe**
  * `4` (`3.50–4.00`): **Extreme**
* **PHQ-9 (DSM-5-TR) Equivalent Tiers ($0 \text{ to } 27$):**
  * `0–4`: **Minimal or Absent**
  * `5–9`: **Mild**
  * `10–14`: **Moderate**
  * `15–19`: **Moderately Severe**
  * `20–27`: **Severe**
  * *Temporal Window Note:* The original PHQ-9 evaluates the past **14 days**, whereas the **DSM-5-TR adapted version evaluates the past 7 days** to align with the GAD 7-day window.

### 3. Evaluated Clinical Variables & Stage-2 Trigger Matrix
| Clinical Dimension | GAD (DSM-5-TR) | PHQ-9 (DSM-5-TR) | HFBP-EM Daily Link |
| :--- | :---: | :---: | :--- |
| **Excessive worry** | Yes | Not directly | Subscale $T$ (*Anxious*, *Tense*) |
| **Nervousness and fear** | Yes | Not directly | Subscale $T$ (*Nervous*, *Restless*) |
| **Somatic anxiety symptoms** | Yes | Not directly | Stage-2 7-Day Protocol Trigger |
| **Avoidance due to anxiety** | Yes | Not directly | Stage-2 7-Day Protocol Trigger |
| **Sleep alterations** | Yes | Yes | Cross-checked with Sleep Telemetry |
| **Difficulty concentrating** | Indirectly | Yes | Stage-2 Cognitive Alert |
| **Fatigue or loss of energy** | Indirectly | Yes | Subscale $F$ (*Tired*, *Exhausted*, *Fatigued*, *Worn out*) |
| **Loss of interest or pleasure (Anhedonia)** | No | Yes | Subscale $D$ (*Disengaged*, *Unenthusiastic*) |
| **Depressed mood** | No | Yes | Subscale $D$ (*Sad*, *Discouraged*) |
| **Thoughts of death or self-harm** | No | Yes (Item 9) | ⚠️ **Critical Rule:** Any non-zero score on PHQ-9 Item 9 requires immediate clinical evaluation regardless of total score. |

### 4. Official APA DSM-5-TR Reference Forms
* [APA DSM-5-TR Severity Measure for Generalized Anxiety Disorder — Adult (PDF)](https://www.psychiatry.org/getmedia/b1a256c4-1304-4610-8aca-0cc70b46ff53/APA-DSM5TR-SeverityMeasureForGeneralizedAnxietyDisorderAdult.pdf)
* [APA DSM-5-TR PHQ-9 Severity Measure for Depression — Adult (PDF)](https://www.psychiatry.org/getmedia/a3986be5-94af-42e7-afce-19234c2f4998/APA-DSM5TR-SeverityMeasureForDepressionAdult.pdf)

> **Clinical Disclaimer:** These instruments quantify symptom severity and guide longitudinal clinical follow-up, but do not establish a standalone DSM-5-TR diagnosis on their own.

---

## 📁 Files Included

* `cuestionario_iws.html`: Standalone interactive application with non-linear spatial option layout, anti-habituation engine, and background HFBP-EM + APA DSM-5-TR calculation pipeline.
* `vaca_pixel_transparente.png`: Pixel-art mascot asset (Dr. Moo, Space Psychologist).
* `README.md`: Technical documentation and clinical scoring guidelines.
