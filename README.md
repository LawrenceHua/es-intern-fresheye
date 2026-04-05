# FreshEye — Computer Vision Produce Scanner

An AI-powered web app that classifies produce freshness from photos.

## Team: [Your Team Name]
| Name | Role | GitHub |
|------|------|--------|
| | Team Lead | |
| | Backend | |
| | Frontend | |
| | ML/Data | |
| | Backend | |

## What This Does
Upload a photo of any fruit or vegetable → get a freshness classification:
- 🟢 Fresh
- 🟡 Slightly Aged  
- 🔴 Expired

Plus a confidence score and storage tips.

## Tech Stack
- **Backend:** Python + FastAPI
- **Frontend:** HTML/CSS/JavaScript
- **ML Model:** Pre-trained image classifier (ResNet50)
- **AI Tools:** GitHub Copilot, Cursor

## Quick Start
```bash
# Clone the repo
git clone https://github.com/LawrenceHua/es-intern-fresheye.git
cd es-intern-fresheye

# Set up Python environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# Run the app
python3 app.py

# Open http://localhost:8000 in your browser
```

## Project Structure
```
es-intern-fresheye/
├── app.py              # FastAPI server
├── model/
│   └── classifier.py   # ML model inference
├── static/
│   ├── index.html      # Upload page
│   ├── style.css       # Styles
│   └── script.js       # Frontend logic
├── data/
│   └── sample_images/  # Test images
├── tests/
│   └── test_api.py     # API tests
├── requirements.txt
└── README.md
```

## Sprint Goals
- **Sprint 1 (Weeks 5-6):** Model inference working, API endpoint built
- **Sprint 2 (Weeks 7-8):** Frontend connected, image upload working
- **Sprint 3 (Weeks 9-10):** Batch processing, UI polish, confidence visualization
