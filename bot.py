from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
bot = Flask(__name__)

# Set up Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # or just paste your key here for now
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@bot.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")

        try:
            response = model.generate_content(question)
            answer = response.text
        except Exception as e:
            answer = f"Error: {str(e)}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    bot.run(debug=True, port=5000)
