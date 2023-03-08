import nltk
nltk.download('punkt')
pattern = "Hello it'me. I was wondering what we used to be."
words = nltk.word_tokenize(pattern)
print(words)