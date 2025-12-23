from transformers import pipeline

# Load text generation model
print("Loading chatbot AI...")
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
print("Chatbot ready! Start chatting!\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Chatbot: Goodbye! Nice talking to you!")
        break
    
    # Generate response
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    bot_reply = response[0]['generated_text']
    
    print(f"Chatbot: {bot_reply}\n")