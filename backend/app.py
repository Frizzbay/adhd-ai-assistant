from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import your existing modules
from api.claude import ClaudeAPI
from utils.prompts import get_system_prompt

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app)  # This allows your frontend to talk to your backend

# Initialize Claude API
claude_api = ClaudeAPI()


# Basic route to test if the server is running
@app.route('/')
def home():
    return jsonify({"message": "ADHD AI Assistant Backend is running!"})


# Main chat endpoint - this is where POST requests come
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Extract user message, prompt mode, and test mode
        user_message = data.get('message', '')
        prompt_mode = data.get('mode', 'minimal')  # Default to minimal for testing
        test_mode = data.get('test_mode', False)

        # Validate input
        if not user_message.strip():
            return jsonify({"error": "Message cannot be empty"}), 400

        if test_mode:
            # Return mock response without calling Claude API
            mock_responses = {
                "minimal": "This is a mock minimal response.",
                "direct": "Mock direct response - straight to the point.",
                "supportive": "Mock supportive response - you're doing great!",
                "structured": "Mock structured response:\n1. Step one\n2. Step two"
            }
            return jsonify({
                "response": mock_responses.get(prompt_mode, "Mock response"),
                "mode": prompt_mode,
                "model": "mock-model",
                "usage": {"input_tokens": 0, "output_tokens": 0},
                "success": True
            })

        # Get the appropriate system prompt for the selected mode
        system_prompt = get_system_prompt(prompt_mode)

        # Call Claude API with the prompt and user message
        response = claude_api.send_message(
            message=user_message,
            system_prompt=system_prompt,
            conversation_history=None  # For now, no conversation history
        )

        # Check if there was an error from Claude API
        if "error" in response:
            return jsonify({
                "error": response["content"],
                "success": False
            }), 500

        # Return the successful response
        return jsonify({
            "response": response["content"],
            "mode": prompt_mode,
            "model": response.get("model", "unknown"),
            "usage": response.get("usage", {}),
            "success": True
        })

    except Exception as e:
        # Handle any errors
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": "Something went wrong processing your message",
            "success": False
        }), 500


# Optional: endpoint to get available prompt modes
@app.route('/modes', methods=['GET'])
def get_modes():
    return jsonify({
        "modes": ["minimal", "direct", "supportive", "structured"],
        "default": "minimal",
        "success": True
    })


# Optional: endpoint to check API status
@app.route('/status', methods=['GET'])
def status():
    try:
        # Try to create ClaudeAPI instance to check if API key is configured
        claude_api = ClaudeAPI()
        return jsonify({
            "api_configured": True,
            "model": claude_api.model,
            "success": True
        })
    except ValueError as e:
        return jsonify({
            "api_configured": False,
            "error": str(e),
            "success": False
        }), 500


# Run the app
if __name__ == '__main__':
    # Check if API key is set
    try:
        test_api = ClaudeAPI()
        print("✅ Claude API successfully initialized")
    except ValueError as e:
        print(f"⚠️  Warning: {e}")
        print("Make sure to set your ANTHROPIC_API_KEY in the .env file")

    # Run in debug mode for development
    print("🚀 Starting ADHD AI Assistant Backend...")
    app.run(debug=True, host='127.0.0.1', port=5000)