import os
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def load_dataset():
    messages = []
    labels = []
   
    with open('spam_data.txt', 'r') as file:
        for line in file:
            label, message = line.strip().split('\t')
            messages.append(message)
            labels.append(label)
   
    return messages, labels
   
messages, labels = load_dataset()



def preprocess_text(messages):
    stop_words = set(stopwords.words('english'))
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
   
    preprocessed_messages = []
   
    for message in messages:
        tokens = tokenizer.tokenize(message)

        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
   
        preprocessed_message = ' '.join(filtered_tokens)
   
        preprocessed_messages.append(preprocessed_message)
   
    return preprocessed_messages
   
preprocessed_messages = preprocess_text(messages)




def extract_features(preprocessed_messages):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(preprocessed_messages)
   
    return features
   
features = extract_features(preprocessed_messages)



x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)



def train_model(x_train, y_train):
    model = SVC(kernel='linear')
    model.fit(x_train, y_train)
   
    return model
   
model = train_model(x_train, y_train)



def test_model(model, x_test, y_test):
    predictions = model.predict(x_test)
    accuracy = (predictions == y_test).mean()
   
    return accuracy
   
accuracy = test_model(model, x_test, y_test)
print(f"Accuracy: {accuracy}")





