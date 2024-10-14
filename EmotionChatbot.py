class EmotionChatbot:
    def respond_to_emotion(self, user_input):
        user_input = user_input.lower()

        if "sad" in user_input:
            return "I'm sorry to hear that you're feeling sad. It’s okay to feel that way sometimes. Would you like to talk about what's bothering you?"

        elif "happy" in user_input:
            return "That’s great! Happiness is a wonderful emotion. What’s making you feel happy right now?"

        elif "angry" in user_input:
            return "Feeling angry can be tough. It’s important to find a healthy way to express that anger. What’s making you feel this way?"

        elif "confused" in user_input:
            return "Confusion is a common emotion, especially in challenging situations. What’s on your mind that’s making you feel confused?"

        else:
            return "I’m here to listen! Tell me more about how you're feeling."

# Example of using the chatbot interactively
chatbot = EmotionChatbot()

print("Welcome to the Emotion Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Take care!")
        break
    response = chatbot.respond_to_emotion(user_input)
    print("Chatbot:", response)
