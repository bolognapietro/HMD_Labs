import os
import ollama
# import logging

# Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(_name_)

class ModelQuery:
    def __init__(self):
        self.history = []

    def add_to_history(self, message):
        """Add a message to the history."""
        self.history.append(message)

    def action_history_str(self):
        """Return the history as a string."""
        return "\n".join(self.history)

    @staticmethod
    def load_content(content):
        """Load content from a file or return the string itself."""
        if os.path.isfile(content):  
            with open(content, 'r') as f:
                return f.read()
        return content  

    def query_model(self, system_prompt, input_file, model_name="llama3.2"):
        # Load system prompt and user input
        system_prompt = self.load_content(system_prompt)
        user_input = self.load_content(input_file)

        # Ensure the user environment is correct
        user_env = os.getenv('USER')

        if user_env == 'pietro.bologna':
            # Add user input to history
            self.add_to_history(user_input)

            # Combine history with the system prompt
            consolidated_system_prompt = f"{self.action_history_str()}\n{system_prompt}"

            # Prepare messages with a single system prompt
            messages = [
                {'role': 'system', 'content': consolidated_system_prompt},
                {'role': 'user', 'content': user_input}
            ]

            # Call the model
            response = ollama.chat(
                model=model_name,
                messages=messages
            )
            return response['message']['content']
        else:
            raise ValueError('Unknown user environment. Please set the USER environment variable.')

os.environ['USER'] = "pietro.bologna"
model = ModelQuery()
system_prompt = "You are a helpful assistant specializing in artificial intelligence."
user_input = "What are the latest advancements in AI?"
response = model.query_model(system_prompt, user_input)
print(f"Model Response: {response}")