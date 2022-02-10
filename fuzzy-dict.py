from typing import Any
from fuzzywuzzy import process


class FuzzyDict(dict):
    def __new__(cls, threshold:int=90, dict:dict={}):
        if not type(threshold) is int:
            raise ValueError("Threshold must be an integer.")

        if 0 >= threshold >= 100:
            return dict

        else:
            return super(FuzzyDict, cls).__new__(cls, threshold, dict)

    def __init__(self, threshold:int=90, dict:dict={}, *args, **kwargs):
        self.threshold = threshold
        super().__init__(*args, **kwargs)
        self.update(dict)
         
    def __getitem__(self, key):
        value = super().get(key, None)
        if value:
            return value

        match, score = process.extractOne(key, self.keys())
        if score > self.threshold:
            return super().__getitem__(match)
        
        raise KeyError(key)
    
    def __setitem__(self, __k:str, v:Any) -> None:
        if type(__k) is not str:
            raise ValueError(f"{type(self)} only supports string objects as keys. Received {type(__k)} instead.")

        return super().__setitem__(__k, v)

