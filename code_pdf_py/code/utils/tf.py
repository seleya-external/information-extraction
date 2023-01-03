import math

def tf(word, count):
    c = count[word] if count[word] <= 2 else 2
    return c / sum(count.values()) if sum(count.values()) > 0 else 0
def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)
def idf(word, count_list):
    return math.log(len(count_list)) / (1 + n_containing(word, count_list))
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)