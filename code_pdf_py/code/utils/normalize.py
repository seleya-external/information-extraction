import nltk
import math
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

def get_tokens(text):
    """
    tokenize the text
    """
    lower = text.lower()
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lower.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

def stem_tokens(tokens, stemmer):
    """
    remove morphological affixes from words, leaving only the word stem
    """
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def normalize(text):
    """
    applement the tokenize and stem
    """
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = SnowballStemmer("english") # PorterStemmer
    stemmed = stem_tokens(filtered, stemmer)
    return stemmed