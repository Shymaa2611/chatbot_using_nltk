import nltk
from nltk.chat.util import Chat

data = [
    [
        "hello",
        ["Hi there! How can I assist you with our website today?"]
    ],
    [
        "I forgot my password.",
        ["No problem! You can reset your password by clicking on the 'Forgot Password' link on the login page. Follow the instructions to create a new password."]
    ],
    [
        "How do I enroll in a course?",
        ["To enroll in a course, log in to your account, browse the available courses, and click on the 'Enroll' button for the course you're interested in. If you encounter any issues, let me know!"]
    ],
    [
        "Can I change my registered email?",
        ["Sure thing! Please send an email to change@email.com from your registered email address requesting the change. Our support team will assist you further."]
    ],
    [
        "I can't access the course materials.",
        ["I'm sorry to hear that. Please make sure you're logged in and have successfully enrolled in the course. If the issue persists, contact our support team with the course details."]
    ],
    [
        "How do I download resources?",
        ["To download resources, go to the course page and look for the 'Resources' section. You'll find links to download the files provided by the instructor."]
    ],
    [
        "Is there a mobile app?",
        ["Yes, we have a mobile app available for both iOS and Android devices. Search for 'Our Learning App' on the App Store or Google Play Store to download it."]
    ],
    [
        "What payment methods do you accept?",
        ["We accept major credit and debit cards, as well as PayPal. When enrolling in a course, you'll be prompted to choose your preferred payment method."]
    ],
    [
        "How do I contact a course instructor?",
        ["You can usually find a 'Q&A' or 'Discussion' section on the course page where you can post questions for the instructor and interact with other students."]
    ],
    [
        "exit",
        ["Thank you for using our chat service. If you have more questions in the future, feel free to ask. Happy learning!"]
    ]
]


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
