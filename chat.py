import nltk
from nltk.chat.util import Chat

pairs=[
  [
      "hello",
      ["hi"]
  ],
    [
      "How are You",
      ["i ' am fine"]
  ],

]

print("How can help you ? ")
chat=Chat(pairs)
chat.converse()