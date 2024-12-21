# AI-Team-Collaboration-Tool
A real-time collaboration platform powered by Google Cloud and OpenAI for idea generation and design feedback.


# AI Team Collaboration Tool

This project is an AI-powered collaboration tool that uses OpenAI's API to generate text based on user prompts.

## Project Structure
- **backend/**: Contains Flask API and OpenAI integration.
- **frontend/**: Simple HTML interface for user interaction.
- **requirements.txt**: Lists dependencies.
- **README.md**: Documentation.

## Setup and Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI-TEAM-COLLABORATION-TOOL
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
4. Run the Flask server:
   ```bash
   python backend/app.py
   ```
5. Open the frontend in your browser:
   ```bash
   open frontend/index.html
   ```

## Usage
- Enter a prompt in the text area and click 'Generate' to receive AI-generated text.
