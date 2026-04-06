# FreshEye — Computer Vision Produce Scanner

Extend a production ML pipeline to build a web-based produce freshness scanner.

## Team: [Your Team Name]
| Name | Role | GitHub |
|------|------|--------|
| | Team Lead | |
| | Backend/ML | |
| | Frontend | |
| | ML/Data | |
| | Testing/Integration | |

## What This Does
Upload a photo of any fruit or vegetable → get AI-powered freshness classification:
- **Fresh** (75-100) — Peak quality, eat anytime
- **Markdown** (50-74) — Discount recommended, use within days
- **Conversion** (25-49) — Best for cooking/smoothies
- **Waste** (0-24) — Very ripe, use immediately or discard

Plus: confidence score, days remaining, storage tips, and top-3 alternatives.

## Baseline Code (from production platform)
You receive real production code to build on:
- `two_model_service.py` — EfficientNet-B0 (77 produce types, 99%+ accuracy) + MobileNetV3 (freshness scoring)
- `ai_classifier.py` — GPT-4o vision fallback with circuit breaker
- `image_optimizer.py` — HEIF/HEIC support, illumination normalization
- `produce_classifier_labels.json` — 77 produce classes

## Architecture
```
Photo Upload → Image Optimizer → EfficientNet-B0 → MobileNetV3 → Results
               (resize, HEIC,    (produce type,    (freshness     (color-coded,
                normalize)        77 classes)        0-100 score)   with tips)
                                       ↓ (low confidence)
                                  GPT-4o Vision Fallback
```

## Tech Stack
- **Backend:** Python + FastAPI
- **ML Models:** EfficientNet-B0 (produce classification) + MobileNetV3 (freshness scoring)
- **Frontend:** HTML/CSS/JavaScript
- **Visualization:** Plotly
- **AI Tools:** GitHub Copilot, Cursor

## What You Build (Weeks 5-10)
1. Web scanning interface (upload + camera capture)
2. Multi-item detection (multiple items in one photo)
3. Produce variety classifier (Fuji vs Gala vs Granny Smith)
4. Freshness timeline visualization (decay curves)
5. Confidence dashboard with top-3 alternatives
6. Batch scanning (10+ images at once)
7. Image quality check (too dark, blurry, not produce)
8. User feedback loop (correct wrong classifications)

## Quick Start
```bash
git clone https://github.com/LawrenceHua/es-intern-fresheye.git
cd es-intern-fresheye
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
# Open http://localhost:8000
```

## Project Structure
```
es-intern-fresheye/
├── app.py              # FastAPI server
├── model/
│   └── classifier.py   # ML model inference
├── static/
│   ├── index.html      # Upload page
│   ├── style.css
│   └── script.js
├── data/
│   └── sample_images/
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```
