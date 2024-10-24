import random

# Predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}
class Chatbot():
 def __init__(self):
     pass
          
# Function to get a response based on user input
 def get_response(self):
    for key in responses:
        if key in self.user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

# Chatbot function
 def chatbot(self):
    print("Chatbot: Hi! How can I assist you today?")
    
    while True:
        self.user_input = input("User: ").lower()
        response = self.get_response()
        print("Chatbot:", response)
        
        if self.user_input == "goodbye":
            break

# Run the chatbot
if __name__ =="__main__":
 answer=Chatbot()
 answer.chatbot()