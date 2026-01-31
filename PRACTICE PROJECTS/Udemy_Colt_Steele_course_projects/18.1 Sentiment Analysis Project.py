from textblob import TextBlob
import pyttsx3

engine=pyttsx3.init()
# engine.say("Hello friendo. Flip the coin.")
# engine.runAndWait()

print("Enter your employee wellness statement: ")
phrase = input("> ")
blob = TextBlob(phrase)
# print(blob.sentiment)
# print(blob.sentiment.polarity)
while blob.sentiment.polarity < 0.5:
    engine.say("Hello friendo. Say something positive please.")
    print("More positive please: ")
    engine.runAndWait()
    phrase = input("> ")
    blob = TextBlob(phrase)

print("We appreciate you too!")
engine.say("Well done my friend. You're a star role model. Have a wonderful day.")
engine.runAndWait()
