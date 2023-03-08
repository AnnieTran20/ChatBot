import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random 
import json

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs = []
docs_x = []
docs_y = []
#intent = dict
for intent in data["intents"]:
    #pattern: question -string
    for pattern in intent["patterns"]: 
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)
        docs_x.append(pattern)
        docs_y.append(intent["tag"])
    if intent["tags"] not in labels:
        labels.append(intent["tag"])
words = [setmmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []


