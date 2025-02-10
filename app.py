from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Your OpenAI API key (you can store this securely later)
openai.api_key = 'your_openai_api_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    user_input = request.form['user_input']
    
    # Call OpenAI GPT model to generate resume content
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a professional resume with the following information: {user_input}",
        max_tokens=500
    )

    resume = response.choices[0].text.strip()
    return jsonify({"resume": resume})

if __name__ == '__main__':
    app.run(debug=True)
