# Jarvis Virtual Assistant

Jarvis is a voice-activated virtual assistant built in Python. It listens to voice commands, processes speech using Google Speech Recognition, communicates using Google Text-to-Speech (gTTS), and leverages Google Gemini AI for advanced conversation and queries. It also integrates with external APIs to fetch real-time news headlines, handles custom music playback, and opens common web portals.

---

## 🚀 Features

- **Wake Word Detection:** Responds to the wake word `"Jarvis"` to activate and listen for commands.
- **Voice Synthesis:** Speaks back to you using Google Text-to-Speech (`gTTS`) played via the `pygame` audio mixer.
- **Web Navigation:** Opens popular web portals directly from voice commands (e.g., Google, Facebook, YouTube, LinkedIn).
- **Music Playback:** Looks up voice commands starting with `"play"` (e.g., "play skyfall") and launches the corresponding link from a custom library mapping.
- **Real-Time News:** Fetches the top headlines regarding a topic (e.g., India) using the NewsAPI.
- **AI-Powered Conversations:** Defaults fallback queries to the Google Gemini API (`gemini-3-flash-preview` model) to handle open-ended questions intelligently.

---

## 🛠️ Tech Stack & Dependencies

- **Programming Language:** Python 3.x
- **Audio Output:** `pygame` (for seamless MP3 loading and playback)
- **Text-to-Speech:** `gTTS` (Google Text-to-Speech)
- **Speech Recognition:** `SpeechRecognition` (using the Google API wrapper)
- **AI Processing:** `google-genai` (Gemini API Client)
- **API Requests:** `requests` (for fetching news headlines)
- **Environment Management:** `python-dotenv` (for loading API credentials)

---

## 📂 Code Structure & File Description

The codebase consists of the following key files:

- **[main.py](file:///C:/Users/pjha9/Documents/ALL%20Coding/Projects/Mega%20Project%201%20-%20Jarvis/main.py):** Contains the core logic for the speech recognition loop, voice response system, action parsing, and integration with external APIs (Gemini & NewsAPI).
- **[musicLibrary.py](file:///C:/Users/pjha9/Documents/ALL%20Coding/Projects/Mega%20Project%201%20-%20Jarvis/musicLibrary.py):** Simple lookup dictionary containing a map of song names to their respective streaming URLs (e.g., YouTube videos).
- **[requirements.txt](file:///C:/Users/pjha9/Documents/ALL%20Coding/Projects/Mega%20Project%201%20-%20Jarvis/requirements.txt):** List of all python dependencies needed for setup.
- **`.env.local`:** Configuration file to store sensitive keys such as `GEMINI_API_KEY` and `NEWS_API_KEY`.

---

## ⚙️ Setup and Installation

### 1. Clone/Download the Project
Download the repository files to your local workspace directory:  
`C:/Users/pjha9/Documents/ALL Coding/Projects/Mega Project 1 - Jarvis`

### 2. Set Up Virtual Environment
Initialize and activate your virtual environment:
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

### 3. Install Dependencies
Install all required libraries using `pip`:
```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env.local` in the project root and add your API credentials:
```env
NEWS_API_KEY=YOUR_NEWS_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Running Jarvis
Execute the main driver script to initialize the assistant:
```powershell
python main.py
```
Upon startup, the assistant will say *"Initializing Jarvis..."* and print `"Listening..."` to the terminal. Speak *"Jarvis"* to activate, wait for the assistant's response (*"Yes?"*), and then speak your command.

---

## 👤 Author

Developed by **Prince Jha**
