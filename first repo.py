import random

class SimpleAIBot:
    def __init__(self, name="AI Bot"):
        self.name = name
        self.responses = {
            "hello": ["Hello! How can I help you?", "Hi there!", "Hey!"],
            "how are you": ["I'm doing great, thanks!", "Feeling smart today!", "All systems operational!"],
            "bye": ["Goodbye!", "See you later!", "Bye, have a great day!"],
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "I'm not sure about that. Can you rephrase?"

def chat():
    bot = SimpleAIBot()
    print(f"{bot.name}: Hi! I'm your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print(f"{bot.name}: {response}")
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chat()
    # hello nahid
