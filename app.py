from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

# Dataset for careers and tips
career_data = {
    "Technology": ["Software Engineer", "Data Scientist", "AI Researcher", "Cybersecurity Expert", "Cloud Engineer"],
    "Arts": ["Graphic Designer", "Musician", "Animator", "Film Director", "Fashion Designer"],
    "Business": ["Entrepreneur", "Marketing Manager", "Financial Analyst", "Human Resource Manager", "Investment Banker"],
    "Science": ["Biotechnologist", "Environmental Scientist", "Pharmacist", "Medical Researcher", "Astrophysicist"],
    "Healthcare": ["Doctor", "Nurse", "Physiotherapist", "Healthcare Administrator", "Nutritionist"],
    "Non-Conventional": ["Professional Gamer", "YouTuber", "Freelancer", "Ethical Hacker", "Podcaster"]
}

success_tips = {
    "Professional Gamer": "Build an online presence, participate in tournaments, and network with industry professionals.",
    "YouTuber": "Focus on niche content, stay consistent, and engage with your audience.",
    "Freelancer": "Develop a strong portfolio, use freelancing platforms, and network effectively.",
    "Ethical Hacker": "Get certified (CEH, OSCP), participate in bug bounty programs, and keep updating your knowledge.",
    "Podcaster": "Find your niche, create high-quality content, and use multiple platforms for distribution."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    interest = data.get("interest", "").capitalize()
    
    if interest in career_data:
        career_options = career_data[interest]
        return jsonify({"career": career_options})
    else:
        career_options = random.choice(career_data["Non-Conventional"])
        tips = success_tips.get(career_options, "Stay motivated and keep learning!")
        return jsonify({"career": [career_options], "tips": tips})

if __name__ == '__main__':
    app.run(debug=True)
