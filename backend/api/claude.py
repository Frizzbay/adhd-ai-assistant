# Implementation of Claude API functionality

import os
from typing import Dict, List, Any, Optional
import anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ClaudeAPI:
    """
    Class to handle interactions with Claude API
    """

    def __init__(self):
        """Initialize the Claude API Client."""
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")

    def send_message(self, message: str, system_prompt: str, conversation_history: Optional[list[dict[str, Any]]] - None) -> Dict[str, Any]:
        """
        Send a message to Claude and get a response.

        Args:
            :param message: The user's message
            :param system_prompt: System prompt to guide Claude's behaviour
            :param conversation_history: Optional list of prior messages

        Returns:
            Response from Claude API
        """
        if conversation_history is None:
            conversation_history = []

        messages = conversation_history.copy()
        messages.append({"role": "user", "content": message})

        try:
            # Call the Claude API
            response = self.client.message.create(model=self.model, system = system_prompt, messages=messages, max_tokens=1024)
            # Extract the response text

            result = {
                "content": response.content[0].text,
                "model": self.model,
                "usage": {
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens
                }
            }

            return result

        except Exception as e:
            # Handle any API errors
            print(f"Error calling Claude API: {e}")
            return {"error": str(e), "content": "Sorry I encountered an error processing your request"}