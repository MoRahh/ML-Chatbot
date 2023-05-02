import random
import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

model = load_model('chatbot_model.h5')

intents_file = open('intents.json').read()
intents = json.loads(intents_file)

words = []
classes = []
documents = []
ignore_words = ['?', '!']
lemmatizer = WordNetLemmatizer()

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        words_list = nltk.word_tokenize(pattern)
        words.extend(words_list)
        # add the sentence and its tag to documents
        documents.append((words_list, intent['tag']))
        # add the tag to classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# sort classes
classes = sorted(list(set(classes)))

# create the bag of words
def create_bag_of_words(sentence, words):
    bag = [0] * len(words)
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

# define the chatbot response function
def predict_class(sentence, model):
    p = create_bag_of_words(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0][0]
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# run the chatbot
print("Welcome to the chatbot! Type 'quit' to exit")
while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        break

    intents_list = predict_class(user_input, model)
    response = get_response(intents_list, intents)
    print('Chatbot: ' + response)
