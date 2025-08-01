// Main JavaScript file for ADHD AI Assistant
// Handles frontend interactions and communicates with Python Flask backend

class ADHDAIAssistant {
    constructor() {
        // Track application state
        this.currentMode = 'minimal';        // AI prompt mode: minimal, direct, supportive, structured
        this.testMode = false;               // Toggle between test mode (mock responses) and live API calls

        // Cache DOM elements for use across methods
        this.messageInput = document.getElementById('message-input');
        this.sendButton = document.getElementById('send-button');
        this.chatMessages = document.getElementById('chat-messages');
        this.modeButtons = document.querySelectorAll('.mode-btn');
        this.modeIndicator = document.getElementById('current-mode-text');

        this.initializeApp();
    }

    initializeApp() {
        // Set initial UI state
        this.modeIndicator.textContent = 'Current Mode: ' + this.currentMode.charAt(0).toUpperCase() + this.currentMode.slice(1);
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Mode selection buttons - update UI and internal state
        this.modeButtons.forEach(button => {
            button.addEventListener('click', () => {  // Arrow function preserves 'this' context
                this.modeButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                this.currentMode = button.dataset['mode'];  // Gets data-mode attribute from HTML
                this.modeIndicator.textContent = 'Current Mode: ' + this.currentMode.charAt(0).toUpperCase() + this.currentMode.slice(1);
                this.addMessageToChat('System: Switched to ' + this.currentMode + ' mode');
            });
        });

        // Send message button - process user input
        this.sendButton.addEventListener('click', () => {
            const userMessage = this.messageInput.value;
            if (userMessage.trim() !== '') {
                this.addMessageToChat('You: ' + userMessage);
                this.messageInput.value = '';
                this.sendToBackend(userMessage);  // Send to Flask backend
            }
        });

        // Test mode toggle - switches between mock responses and live API calls
        const testModeButton = document.getElementById('test-mode-btn');
        if (testModeButton) {
            testModeButton.addEventListener('click', () => {
                this.testMode = !this.testMode;
                if (this.testMode) {
                    testModeButton.textContent = '🧪 Test Mode: ON';
                    testModeButton.style.backgroundColor = '#10b981';
                    this.addMessageToChat('System: 🧪 Test mode enabled - no API calls will be made');
                } else {
                    testModeButton.textContent = '🧪 Test Mode: OFF';
                    testModeButton.style.backgroundColor = '';
                    this.addMessageToChat('System: 🔴 Live mode enabled - API calls will be made');
                }
            });
        }
    }

    // Add message to chat display
    addMessageToChat(message) {
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        this.chatMessages.appendChild(messageElement);
        // TODO: Add auto-scrolling for new messages
        // TODO: Add different styling for user/assistant/system messages
    }

    // Send message to Flask backend on localhost:5000
    sendToBackend(message) {
        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                mode: this.currentMode,        // Tells backend which AI prompt mode to use
                test_mode: this.testMode       // Tells backend whether to use mock responses
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                this.addMessageToChat('Assistant: ' + data.response);
            } else {
                this.addMessageToChat('Error: ' + data.error);
            }
        })
        .catch(error => {
            this.addMessageToChat('Error: Could not connect to backend');
        });
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    new ADHDAIAssistant();
});