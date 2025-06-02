# ADHD AI Assistant

# ADHD AI Assistant

A Python-based AI assistant application designed to support individuals with ADHD.

## Project Overview

This project connects a Flask backend with the Claude AI API to create a supportive assistant for ADHD needs. Currently in early development stage.

## Technology Stack

- **Backend**: Python with Flask
- **AI Integration**: Anthropic's Claude API
- **Frontend**: HTML, CSS, JavaScript

## Installation

### Prerequisites
- Python 3.x
- Git
- Anthropic API key (from [console.anthropic.com](https://console.anthropic.com))

### Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/YOUR-USERNAME/adhd-ai-assistant.git
   cd adhd-ai-assistant
   ```

2. **Set up Python environment**
   ```
   cd backend
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file and add your Anthropic API key
   ```

## Project Structure

```
adhd-ai-assistant/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── api/
│   │   ├── __init__.py
│   │   └── claude.py          # Claude API implementation
│   ├── utils/
│   │   ├── __init__.py
│   │   └── prompts.py         # System prompts and context
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variables template
└── frontend/
    ├── index.html             # Main HTML interface
    ├── styles/
    │   └── main.css           # Stylesheet
    └── scripts/
        └── main.js            # Frontend JavaScript
```

## Development Status

This project is in active development. Current status:
- ✅ Basic project structure and architecture established
- ✅ Claude API connection implemented 
- ✅ Flask backend with API endpoints created
- ✅ Multi-mode prompt system designed

In progress:
- Frontend user interface development
- Conversation history implementation
