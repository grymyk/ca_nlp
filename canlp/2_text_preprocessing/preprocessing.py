# regex for removing punctuation!
import re

# nltk preprocessing magic
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# grabbing a part of speech function:
# nltk.pos_tag(text)

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

cleaned = re.sub('\W+', ' ', text)
#print(cleaned)

tokenized = word_tokenize(cleaned)
#print(tokenized)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]
#print(stemmed)


## -- CHANGE these -- ##
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)

