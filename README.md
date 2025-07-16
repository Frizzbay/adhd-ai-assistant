# ADHD AI Assistant

A Python-based AI assistant application designed to support individuals with ADHD.

## Project Overview

This project connects a Flask backend with the Claude AI API to create a supportive assistant for ADHD needs. Currently in early development stage.

## Technology Stack

- **Backend**: Python with Flask, Flask-CORS
- **AI Integration**: Anthropic's Claude API
- **Frontend**: HTML, CSS, JavaScript
- **Development**: Test mode system for API cost management

## Features

### Multi-mode Conversation System
- **Minimal Mode**: Basic testing prompt (saves API credits during development)
- **Direct Mode**: Reality-focused, action-oriented responses  
- **Supportive Mode**: Gentle, encouraging guidance
- **Structured Mode**: Step-by-step, organized assistance

### Development Features
- **Test Mode**: Toggle between mock responses and live API calls
- **Mode Selection**: Real-time switching between conversation modes
- **Chat Interface**: Basic messaging interface

## Installation

### Prerequisites
- Python 3.x
- Git
- Anthropic API key (from [console.anthropic.com](https://console.anthropic.com))

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/adhd-ai-assistant.git
   cd adhd-ai-assistant
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file and add your Anthropic API key
   ANTHROPIC_API_KEY=your_actual_key_here
   ```

## Usage

1. **Start the backend server**
   ```bash
   cd backend
   python app.py
   ```

2. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Select conversation mode and start chatting
   - Use test mode toggle to switch between mock and live responses

## Project Structure

```
adhd-ai-assistant/
├── backend/
│   ├── app.py                 # Main Flask application with test mode support
│   ├── api/
│   │   ├── __init__.py
│   │   └── claude.py          # Claude API implementation
│   ├── utils/
│   │   ├── __init__.py
│   │   └── prompts.py         # System prompts and context
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variables template
└── frontend/
    ├── index.html             # Main HTML interface with mode selector and test mode
    ├── styles/
    │   └── main.css           # Stylesheet
    └── scripts/
        └── main.js            # Frontend JavaScript with class-based architecture
```

## Development Status

This project is in active development. Current status:
- ✅ Basic project structure and architecture established
- ✅ Claude API connection implemented 
- ✅ Flask backend with API endpoints created
- ✅ Multi-mode prompt system designed
- ✅ Frontend chat interface implemented
- ✅ Frontend-backend connection established
- ✅ Test mode system implemented (mock responses)
- ✅ Mode selection functionality working

Next planned feature:
- Conversation history implementation