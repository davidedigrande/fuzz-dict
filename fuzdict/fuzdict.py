from typing import Any
from fuzzywuzzy import process


class FuzDict(dict):
    """
    FuzDict is a simple python dictionary that implements Fuzzy Logic as a way to match keys.
    This implies that suitable values for creating keys are only of string type.
    It also implies that at any time, the dictionary cannot have two or more similar strings, which means in turn that the input order matters.
    """
    def __init__(self, threshold:int=80, get_only:bool=False):
        self._threshold = threshold
        super().__init__()

    @property
    def threshold(self):
        return self._threshold

    def _key_typecheck(self, __k):
        if type(__k) is not str:
            raise ValueError(f"{type(self)} only supports string objects as keys. Received {type(__k)} instead.")

    def _match_key(self, key:str) -> str:       
        match, score = process.extractOne(key, self.keys()) or ("", 0)
        if score > self.threshold:
            key = match
        return key
         
    def __getitem__(self, __k:str) -> Any:
        self._key_typecheck(__k)

        __k = self._match_key(__k)
        return super().__getitem__(__k)
    
    def __setitem__(self, __k:str, v:Any) -> None:
        self._key_typecheck(__k)
        
        __k = self._match_key(__k)
        return super().__setitem__(__k, v)
    
    def get(self, __k:str, __default:Any=None) -> Any:
        self._key_typecheck(__k)
        
        __k = self._match_key(__k)
        return super().get(__k, __default)

    def update(self, other:dict) -> None:
        if not isinstance(other, dict):
            raise ValueError(f"{type(self)} only supports updating from another {type(self)} instance. Received {type(other)} instead.")

        for k, v in other.items():
            self.__setitem__(k, v)
    
    def __iadd__(self, other:dict) -> FuzDict:
        self.update(other)
        return self
        
    def extend(self, other:dict) -> FuzDict:
        return self.__iadd__(other)