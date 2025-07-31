✋ Gesture Play AI – Touchless Gaming System

Gesture Play AI is an interactive gesture-controlled gaming platform developed using Python, MediaPipe, TensorFlow, and Flask. It enables users to play classic games like 2048, Rock Paper Scissors, and Tic Tac Toe using only hand gestures—no mouse or keyboard needed.

🚀 Built for a smarter, touchless future in gaming and human-computer interaction.

⸻

🎮 Live Demo (Optional)

If hosted: Click here to try
(If not hosted, remove this section)

⸻

📌 Features
	•	🎯 Real-time hand gesture recognition using webcam
	•	🧠 ML-powered gesture detection with MediaPipe & TensorFlow
	•	🎮 Play games:
	•	Rock Paper Scissors
	•	Tic Tac Toe
	•	2048
	•	🌐 Clean, responsive frontend with Flask and HTML/CSS
	•	🔐 Login/Signup system using SQLite
	•	📹 Demo videos and interactive UI
	•	💻 Touchless experience – improves accessibility & user interaction

⸻

🛠 Tech Stack

🔍 AI / ML / CV
	•	MediaPipe – for real-time hand tracking
	•	TensorFlow – model integration (if applicable)
	•	OpenCV – for camera and gesture input
	•	PyAutoGUI – to simulate keyboard actions for gesture control

💻 Web
	•	Flask – backend server
	•	HTML / CSS / JavaScript – frontend
	•	Jinja2 – Flask templating
	•	SQLite – for user authentication

⸻

🧱 Architecture of the Proposed System
	•	Frontend: Built with HTML, CSS, JS and Flask templates
	•	Backend: Flask handles routing, user sessions, and serves gesture output
	•	Gesture Module: MediaPipe processes camera feed to detect hand gestures
	•	Game Logic: Independent Python files for each game respond to gesture input
	•	Database: SQLite stores user login/signup info

⸻

🧩 Modules in Proposed System
	1.	Login/Signup Module
	2.	Gesture Detection Module (MediaPipe-based)
	3.	Game Logic Modules (2048, RPS, Tic Tac Toe)
	4.	Frontend Display Module
	5.	User Dashboard & Navigation
	6.	Gesture-Control Mapping Module

🧠 Machine Learning & Vision Techniques
	•	MediaPipe HandLandmarks for gesture detection (21 landmarks per hand)
	•	Rule-based classification using landmark positions
	•	Thresholding techniques to detect specific gestures (fist, fingers up, etc.)
	•	Optional: TensorFlow used for gesture classification models (if trained)

⸻

🧪 How to Run the Project

⚙ Prerequisites
	•	Python 3.8+
	•	pip
	•	Virtual Environment (recommended)

📦 Install Dependencies
pip install -r requirements.txt

▶ Run Flask App
python app.py

•	Visit http://127.0.0.1:5000 in your browser
	•	Use webcam for gesture detection
	•	Navigate and play games touchlessly

📂 Folder Structure
GESTURE_PLAY_AI/
│
├── app.py
├── auth.py
├── game2048.py
├── rock_paper_scissors_game.py
├── tictactoe_game.py
├── hand_gesture_detection.py
│
├── templates/
│   ├── index.html, login.html, dashboard.html, ...
│
├── static/
│   ├── images/
│   ├── demo_videos/
│   ├── js/
│   └── style.css

📌 Use Cases
	•	👨‍🦽 Touchless gaming for physically challenged users
	•	🧪 Gesture-based HCI research
	•	🖥 Public kiosks without physical touch
	•	🎮 Fun AI-based gaming platform for learning computer vision
	•	🧼 Contactless interaction in post-COVID systems



 
