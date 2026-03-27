Mini RTI Generator (AI-Assisted)

##  Overview
This project is a simple full-stack application that helps users generate a properly formatted RTI (Right to Information) application without needing to know legal writing formats.

Users can enter their issue in simple language, and the system converts it into a formal RTI letter and generates a downloadable PDF.

---

## Tech Stack

- **Frontend:** React + Tailwind CSS
- **Backend:** Flask (Python)
- **Database:** SQLite (via SQLAlchemy)
- **PDF Generation:** FPDF
- **AI Logic:** Rule-based structured content generation (AI-assisted design)

---

##  Problem Statement

Many citizens in India are unaware of how to properly draft RTI applications.  
This leads to:
- Incorrect formats
- Rejected applications
- Lack of access to government information

---

## Solution

This system simplifies the process by:
- Taking user input in plain language
- Structuring it into a formal RTI letter
- Generating a clean PDF document

---

##  Architecture
                     User (Browser)
                           ↓
                     React Frontend (UI)
                           ↓
                     Flask API (Backend)
                           ↓
                     AI Logic (ai.py) 
                           ↓
                      PDF Generator 
                           ↓
                    Database (SQLite) 
----------------

##  Repository Structure

Task/
│
├── backend/
│ ├── app.py # Flask API entry point
│ ├── ai.py # RTI content generation logic
│ ├── pdfgen.py # PDF creation logic
│ ├── rti.db # SQLite database
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ ├── index.html # Main HTML file (Vite entry)
│ ├── package.json # Frontend dependencies
│ ├── public/ # Static assets
│ └── src/
│ ├── assets/
│ │ └── bg.png # Background image
│ ├── App.jsx # Main React component
│ ├── main.jsx # React entry point
│ ├── App.css # Component styles
│ └── index.css # Tailwind/global styles
│
└── README.md # Project documentation

----------------

##  Features

-  Generate RTI letter from simple input
-  Download as PDF
-  Store user requests in SQLite database
-  Modern UI (Tailwind + Glassmorphism)
-  Input validation
-  Simple and maintainable structure

------------------

##  AI Usage

AI is used in a controlled and structured manner:

- Converts user issue → formal RTI language
- Ensures proper legal formatting
- Applies consistent template structure

> Note: This project simulates AI behavior and is designed to be easily extendable with real LLM APIs like Gemini or OpenAI.

---

## Key Technical Decisions

- **Flask over Django:** Lightweight and faster for small APIs  
- **SQLite:** Simple and sufficient for MVP  
- **Structured generation instead of raw AI:** Ensures correctness and avoids unpredictable outputs  
- **Single-page PDF design:** Improves readability and usability  

--------------------------

## Limitations

- Multilingual PDF rendering not implemented (planned enhancement)
- No authentication system
- No department auto-detection

------------------------------------

##  Future Enhancements

-  Multilingual support (Kannada, Hindi, etc.)
-  Voice input support
-  Integration with real AI APIs (Gemini/OpenAI)
-  Automatic department detection
-  RTI request tracking dashboard

---

##  How to Run

### Backend
cd Task
cd backend
pip install -r requirements.txt
python app.py

#Fontend 
cd Fontend 
npm run rev 


Conclusion

This project focuses on building a simple, reliable, and extensible system rather than a feature-heavy one, aligning with engineering best practices.
