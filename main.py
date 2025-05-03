from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Hardcoded AI reply (Garou-inspired workout plan)
HARDCODED_RESPONSE = """
<strong>Okay, aiming for a physique like Garou from One Punch Man is a great goal!</strong><br>
He has a very lean, ripped, and athletic build – focusing on definition, agility, and functional strength rather than massive bulk.<br><br>

Given your stats (170 lbs, 5'10"), 5 workout days per week, and gym access, here's a plan designed to help you build lean muscle, improve definition, and develop that athletic look.<br><br>

💪 <strong>Weekly Split:</strong><br><br>

<strong>Monday – Push (Chest, Shoulders, Triceps)</strong><br>
• Bench Press – 4 sets x 8–10 reps<br>
• Dumbbell Shoulder Press – 3 sets x 10–12 reps<br>
• Incline Dumbbell Press – 3 sets x 10 reps<br>
• Triceps Pushdowns – 3 sets x 12 reps<br>
• Lateral Raises – 3 sets x 15 reps<br>
• Light Cardio (10 min incline walk)<br><br>

<strong>Tuesday – Pull (Back, Biceps)</strong><br>
• Deadlifts – 4 sets x 5 reps<br>
• Pull-ups (weighted if possible) – 3 sets x max reps<br>
• Barbell Rows – 3 sets x 10 reps<br>
• Face Pulls – 3 sets x 15 reps<br>
• Dumbbell Curls – 3 sets x 12 reps<br>
• Light Cardio (5–10 min jog or bike)<br><br>

<strong>Wednesday – Active Recovery / Mobility</strong><br>
• Dynamic Stretching – 15 mins<br>
• Foam Rolling<br>
• Optional: Light Cardio (15 min jog)<br>
• Core Work: Planks, Hanging Leg Raises<br><br>

<strong>Thursday – Legs</strong><br>
• Squats – 4 sets x 8 reps<br>
• Romanian Deadlifts – 3 sets x 10 reps<br>
• Walking Lunges – 3 sets x 20 steps<br>
• Leg Press – 3 sets x 12 reps<br>
• Standing Calf Raises – 4 sets x 15 reps<br>
• Light Core Work<br><br>

<strong>Friday – Full Body Athletic Training</strong><br>
• Power Cleans or Kettlebell Swings – 3 sets x 6 reps<br>
• Battle Ropes – 3 rounds x 30 seconds<br>
• Jump Squats – 3 sets x 15 reps<br>
• Box Jumps – 3 sets x 10 reps<br>
• Pull-ups – 3 sets x max reps<br>
• Ab Wheel Rollouts – 3 sets x 12<br><br>

💡 <strong>Notes:</strong><br>
• Focus on <em>form and controlled movement</em>.<br>
• Nutrition: Eat high-protein meals, stay lean, and hydrate.<br>
• Consistency and sleep are key to recovery.<br><br>

<strong>Ready to go? Track your weekly progress in the Progress tab and hit your goals like Garou.</strong>
"""


@app.route("/", methods=["GET"])
def index():
    return "💪 AI Workout Backend is running. Use POST /chat to get a response."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    print(f"Received prompt: {prompt}")  # helpful for debugging
    return jsonify({"reply": HARDCODED_RESPONSE})

if __name__ == "__main__":
    app.run(debug=True)


