import nltk
from nltk.chat.util import Chat

data = [
    [
        "hello",
        ["Hi there! How can I assist you with our website today?"]
    ],
    [
        r".*password.*",
        ["No problem! You can reset your password by clicking on the 'Forgot Password' link on the login page. Follow the instructions to create a new password."]
    ],
    [
        r".*enroll.*course.*",
        ["To enroll in a course, log in to your account, browse the available courses, and click on the 'Enroll' button for the course you're interested in. If you encounter any issues, let me know!"]
    ],
    [
        r".*download.*resources.*",
        ["To download resources, go to the course page and look for the 'Resources' section. You'll find links to download the files provided by the instructor."]
    ],
    [
        r".*payment.*methods.*",
        ["We accept major credit and debit cards, as well as PayPal. When enrolling in a course, you'll be prompted to choose your preferred payment method."]
    ]
]
chat = Chat(data)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.respond(user_input)
    if not response:
        print("I'm sorry, I can't help you.")
    else:
        print(response)
