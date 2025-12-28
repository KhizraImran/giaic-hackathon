import os
from typing import Literal

# This would be a placeholder for common agent logic or interfaces
# For this project, a simple placeholder is sufficient as specific agent implementations
# will be handled within their dedicated directories.

class BaseClaudeAgent:
    def __init__(self, name: str, description: str, model: Literal['sonnet', 'opus', 'haiku'] = 'haiku'):
        self.name = name
        self.description = description
        self.model = model

    def run(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement the run method")

    def __str__(self):
        return f"Agent: {self.name} (Model: {self.model})\nDescription: {self.description}"
