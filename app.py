from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Add your Gemini API key here
genai.configure(api_key="YOUR_API_KEY")
AIzaSyAHJVqy2_cP98S1ndMwL_z10uHBVl_bUG0
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = model.generate_content(user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
    