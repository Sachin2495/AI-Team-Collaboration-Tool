from flask import Flask, request, jsonify
from openai_integration import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to AI Collaboration Tool! API is available at /api/generate"

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json(force=True)  # Force JSON parsing
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = generate_response(prompt)
    return jsonify({"response": response})



@app.route('/api/generate', methods=['GET'])
def test_generate():
    return jsonify({"message": "Use POST to send data to this endpoint"})

if __name__ == '__main__':
    app.run(debug=True)

app.debug = True