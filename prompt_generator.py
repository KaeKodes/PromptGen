import random


class PromptGenerator:


    PROMPT_CATEGORIES = {
        "storytelling": [
            "Write a short story about an AI that develops emotions.",
            "Describe a futuristic city where humans and AI coexist.",
            "Create a dialogue between a human and an AI debating ethics."
        ],
        "coding": [
            "Write a Python script that generates random poetry.",
            "Create an AI-powered chatbot using Python.",
            "Build a web app that suggests coding project ideas."
        ],
        "design": [
            "Sketch a UI for an AI-powered personal assistant.",
            "Design an app that helps people improve their creativity.",
            "Create a Figma mockup for an AI-driven art tool."
        ]
    }

    def __init__(self):
        #Initialize the PromptGenerator.
        self.generated_prompt = None

    def generate_prompt(self, category):
        #Generates a random AI prompt based on the chosen category.
        if category in self.PROMPT_CATEGORIES:
            self.generated_prompt = random.choice(self.PROMPT_CATEGORIES[category])
            return self.generated_prompt
        else:
            return "Category not found. Please choose from: " + ", ".join(self.PROMPT_CATEGORIES.keys())

    def save_prompt(self, filename="ai_prompts.txt"):
        #Saves the last generated prompt to a text file.
        if self.generated_prompt:
            with open(filename, "a") as file:
                file.write(self.generated_prompt + "\n")
            print(f"Prompt saved to {filename}")
        else:
            print("No prompt generated to save.")
