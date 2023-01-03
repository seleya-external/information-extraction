from nltk.corpus import wordnet as wn

def find_synonyms(word):
    """
    find the synonyms for given word
    """
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms