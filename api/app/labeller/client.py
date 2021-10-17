from collections import defaultdict

from .constants import (
    MaterialConstant,
    TypeConstant,
    ColorConstant,
    SizeConstant,
    LocationConstant
)
from .trie import Trie
from .tokenizer import Tokenizer

class LabelerClient: 

    def __init__(self, stop_words):
        self.trie = Trie()
        self.tokenizer = Tokenizer(stop_words)
        self.init_constants( 
            MaterialConstant,
            TypeConstant,
            ColorConstant,
            SizeConstant,
            LocationConstant
        )
        
        
    def init_constants(self, *args):
        for constant in args:
            self.trie.insert_constant(constant)

    def update_model(self, model, labels):
        tags = model.tags
        for k, v in labels.items():
            tags[k] = v
        model.tags = tags
        return model

    def label(self, model):
        title = self.tokenizer.clean(model.title)
        desc = self.tokenizer.clean(model.description)
        title_labels = self.find_labels(title)
        desc_labels = self.find_labels(desc)
        merged_labels = self.merge_dicts(desc_labels, title_labels)
        return self.update_model(model, merged_labels)
    
    def find_labels(self, sentence):
        res = defaultdict(set)
        pairs = self.trie.search_sentence(sentence)
        for key, word in pairs:
            res[key].add(word)
        return res

    def merge_dicts(self, *args):
        res = defaultdict(set)
        for to_merge in args:
            for k, v in to_merge.items():
                res[k] = res[k] | v
        return res
        
