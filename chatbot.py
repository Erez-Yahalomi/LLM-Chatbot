from openai import OpenAI
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# 🔑 Insert your API key directly here
API_KEY = "your_api_key_here"

client = OpenAI(api_key=API_KEY)

def chat():
# UI defenitions
    print(Fore.CYAN + Style.BRIGHT + "🤖 ChatGPT Assistant".center(50, " "))
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    print(Fore.YELLOW + "Type your message below. Type 'quit' to exit.\n")

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)
        if user_input.lower() in ["quit", "exit"]:
            print(Fore.CYAN + "\n👋 Goodbye! Thanks for chatting.\n")
            break
        
# OpenAI API call. Input from user and output from AI.
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        print(Fore.MAGENTA + "Assistant:" + Style.RESET_ALL, Fore.WHITE + reply + "\n")

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
