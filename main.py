from prompt_generator import PromptGenerator


def main():
   #Main function to run the AI Prompt Generator program.
    prompt_gen = PromptGenerator()

    print("Welcome to the AI Prompt Generator!")
    print("Categories:", ", ".join(PromptGenerator.PROMPT_CATEGORIES.keys()))

    category = input("Enter a category: ").strip().lower()
    prompt = prompt_gen.generate_prompt(category)

    print("\nGenerated Prompt:\n" + prompt)

    save_option = input("Do you want to save this prompt? (yes/no): ").strip().lower()
    if save_option == "yes":
        prompt_gen.save_prompt()


if __name__ == "__main__":
    main()
