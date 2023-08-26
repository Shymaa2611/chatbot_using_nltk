import nltk
from nltk.chat.util import Chat

data = [
    ["hello", ["hi"]],
    ["How are you", ["I'm fine"]],
    ["what's the problem", ["I don't understand how to watch a video"]]
]

print("How can I help you ?")
chat = Chat(data)

while True:
    data_input = input("You : ")
    if data_input.lower() == "exit":
        break
    response = chat.respond(data_input)
    if not response:
        print("I'm sorry, I can'nt help you ")
    else:
        print(response)
