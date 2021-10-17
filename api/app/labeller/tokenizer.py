from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Tokenizer:

    def __init__(self, stop_words):
        self.stop_words = stop_words

    def _tokenize(self, sentence):
        return word_tokenize(sentence)

    def _filter_punc(self, sentence):
        return [word for word in sentence if word.isalpha()]

    def _filter_stop_words(self, sentence):
        return [word for word in sentence if word not in self.stop_words]

    def _to_lower_case(self, sentence):
        return [word.lower() for word in sentence]

    def clean(self, sentence):
        order = [
            self._tokenize,
            self._to_lower_case,
            self._filter_punc,
            self._filter_stop_words
        ]
        for func in order:
            sentence = func(sentence)
        return sentence