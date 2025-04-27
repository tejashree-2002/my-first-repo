#without ml

# def is_spam_without_ml(message):
#     spam_keywords = ['free', 'win', 'money', 'urgent', 'prize', 'claim', 'cash', 'offer', 'winner', 'exclusive']
#     message = message.lower()

#     for keyword in spam_keywords:
#         if keyword in message:
#             return True
#     return False

# test_messages_without_ml = [
#     "You have won a free prize! Claim now!",
#     "Hi, how are you doing today?",
#     "Limited time offer on our new product, act fast!",
#     "Let's catch up soon, I miss our talks.",
#     "Urgent action required! Your account has been compromised."
# ]

# for msg in test_messages_without_ml:
#     result = is_spam_without_ml(msg)
#     print(f"Message: {msg}\nSpam: {result}\n")

#with ml

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

messages = [
    "Win a free cash prize now!",  
    "Congratulations, you are a winner!",  
    "Dear user, your account has been hacked", 
    "Let's have dinner tomorrow night!",  
    "Meeting at 10 AM, please be on time",  
    "Limited offer! Claim your discount today",
    "Let's catch up soon",  
    "Special offer, buy 1 get 1 free",  
    "Can you send me the report by noon?",  
    "Hurry! Last chance for a free vacation",  
]

labels = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(messages, labels, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)

test_messages_with_ml = [
    "You have won a free prize! Claim now!",
    "Hi, how are you doing today?",
    "Limited time offer on our new product, act fast!",
    "Let's catch up soon, I miss our talks.",
    "Urgent action required! Your account has been compromised."
]

for msg in test_messages_with_ml:
    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)
    result = 'Spam' if prediction == 1 else 'Not Spam'
    print(f"Message: {msg}\nPrediction: {result}\n")