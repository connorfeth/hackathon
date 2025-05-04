# Hero's Physique 🦸‍♂️💪

Hero's Physique is a motivational fitness web app designed for anime fans and fitness enthusiasts who want to work out like their favorite characters. Whether you’re feeling stuck or need a creative spark, this app gives you personalized weekly fitness routines inspired by the physiques of popular anime heroes.

## 🌟 Features

- 🧠 Gemini AI-powered fitness plan generation
- 📅 Weekly workout breakdown (Monday–Sunday)
- 📝 Easy-to-read formats for daily workout tasks
- ✅ Save your workout plan locally and track progress
- 🖥️ Clean, simple UI with a navbar to navigate pages

## 🚀 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/heros-physique.git
   cd heros-physique
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_google_generative_ai_key_here
   ```

5. **Run the app**  
   ```bash
   python main.py
   ```

6. **Visit in your browser**  
   Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
├── static/
│   └── styles.css
├── templates/
│   ├── home.html
│   ├── AIWorkout.html
│   └── Progress.html
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## 👥 Contributors

- Ricardo Lazo 
- Connor Feth 
