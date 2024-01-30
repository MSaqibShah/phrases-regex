from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            text = break_phrase(l.name())
            synonyms.append(text)

    return list(set(synonyms))


def break_phrase(phrase):
    if "_" in phrase:
        return " ".join(phrase.split("_"))
    return phrase


corpus = {
    "PHRASE_IF": ["if"],
    "PHRASE_SUDDEN": ["sudden", "suddenly", "suddenly_you"],
    "PHRASE_NEXT": ["next"],
    "PHRASE_OFTEN": ["often"],
    "PHRASE_SOMETIMES": ["sometimes"],

}


def append_synonyms(corpus, modified_corpus):
    for key, value in corpus.items():
        if (key in modified_corpus):
            for item in value:
                text = break_phrase(item)
                modified_corpus[key].append(text)

    return modified_corpus


def expand_corpus(corpus):
    print("Expanding corpus...")
    modified_corpus = {}
    for key, value in corpus.items():
        modified_corpus[key] = []

        for word in value:
            syn = get_synonyms(word)

            if (syn != []):
                for s in syn:
                    modified_corpus[key].append(s)

    print("Appending synonyms...")
    modified_corpus = append_synonyms(corpus, modified_corpus)

    print("Removing duplicates...")
    for key, value in modified_corpus.items():
        modified_corpus[key] = list(set(value))

    return modified_corpus


# syn = expand_corpus(corpus)

# # syn = get_synonyms("suddenly")

# print(syn)
