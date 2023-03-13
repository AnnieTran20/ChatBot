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
        wrds = nltk.word_tokenize(pattern) #break out the sentence into tokens
        words.extend(wrds) #words has all the tokens
        docs.append(pattern) #docs contains all the patterns - the whole sentence
        docs_x.append(pattern) #docs_x has the patterns
        docs_y.append(intent["tag"]) #docs_y has the tag allign with the pattern in docs_x
    if intent["tags"] not in labels:
        labels.append(intent["tag"]) #labels has all the labels (same like docs_y?)
words = [stemmer.stem(w.lower()) for w in words] #get all the roots for each token
words = sorted(list(set(words)))
labels = sorted(labels)

#create training and testing output
training = []
output = []
out_empty = [0 for _ in range(len(classes))]
#we have string now but network only understands number, so we need to deal with it
#create a bag of words that represent all of the words -- arr with the length of 
#the amount of words that we have
for x, doc in enumerate(docs_x): #add number in front of each element
    bag = []
    wrds = [stemmer.stem(w) for w in doc]

    for w in words:



