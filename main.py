from transformers import pipeline

"""Load the conversational AI model"""
print("Loading chatbot AI...")
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
print("Chatbot ready! Start chatting!\n")

conversation_history = []