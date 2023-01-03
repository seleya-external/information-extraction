import re
import os
from collections import Counter
import PyPDF2
from utils import *

def cal_tfidf_tight(text, value_word, keywords_idf):
    text_stemmed = normalize(text)
    count = Counter(text_stemmed)
    score = 0
    for word in value_word:
        word_normalize = normalize(word)
        if len(word.split()) == 2:
            distance = get_distance(word_normalize[0], word_normalize[1], text_stemmed)
            tight = get_proximity(distance["min"])
        elif len(word.split()) == 1:
            tight = 0.01
        else:
            # todo
            tight = 0.01
        word_stemmed = list(set(normalize(word)))
        score += sum(tf(w, count) * keywords_idf[w] for w in word_stemmed) * tight
    return score

def cal_relevance(page, text, position_record_text, metrics, keywords_idf):
    for key_word, value_words in metrics.items():
        position_record_text[key_word].append((str(page),cal_tfidf_tight(text, value_words, keywords_idf)))

def parseText(input_path, file, metrics, keywords_idf):
    print("parsing text from " + file)
    position_record_text = {key_word:[] for key_word in metrics.keys()}
    object = PyPDF2.PdfFileReader(os.path.join(input_path, file))
    num_pages = object.getNumPages()
    for i in range(0, num_pages):
        page = object.getPage(i)
        text = page.extractText()
        text = text.replace('\n',' ')
        text = text.replace(str(i+1), "", 1) 
        cal_relevance(i+1, text, position_record_text, metrics, keywords_idf)
    return position_record_text