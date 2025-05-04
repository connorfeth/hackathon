from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/AIWorkout", methods=["GET", "POST"])
def workout():
    if request.method == "POST":
        character = request.form["character"]
        prompt = f"Create a personalized weekly fitness plan based on {character}'s physique. Structure it day-by-day. Use bullet points."
        response = model.generate_content(prompt)
        return render_template("AIWorkout.html", output=response.text, character=character)
    return render_template("AIWorkout.html")

@app.route("/Progress")
def progress():
    return render_template("Progress.html")

if __name__ == "__main__":
    app.run(debug=True)