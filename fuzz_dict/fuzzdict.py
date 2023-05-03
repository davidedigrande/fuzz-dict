from __future__ import annotations
from typing import Any, Iterable, Mapping
from fuzzywuzzy import process

class StringKeysDict(dict):
    def __init__(self, mapping:dict={}):
        for __key in mapping:
            self.key_typecheck(__key)

        super().__init__(mapping)

    def __setitem__(self, __key: Any, __value: Any) -> None:
        self.key_typecheck(__key)
        return super().__setitem__(__key, __value)

    @staticmethod
    def key_typecheck(__key:Any):
        """Helper function to check if given key is a string."""
        if type(__key) is not str:
            raise ValueError(f"Keys can only be {str}. Received {type(__key)} instead.")

    @classmethod
    def from_mixed_keys_with_conversion(cls, mapping:dict={}) -> StringKeysDict:
        obj = cls()
        for __key, __value in mapping.items():
            obj[str(__key)] = __value

        return obj

    @staticmethod
    def from_mixed_keys_with_discard(cls, mapping:dict={}) -> StringKeysDict:
        obj = cls()
        for __key, __value in mapping.items():
            if type(__key) is str:
                obj[str(__key)] = __value

        return obj

class FuzzDict(StringKeysDict):
    """
    FuzzDict extends Python's built-in dict to offer an extra API for fuzzy logic to match keys.
    FuzzDict only supports string values for creating keys.
    """
    def __init__(self, iterable:Iterable={}, threshold:int=80):
        self._threshold = threshold
        super().__init__(iterable)

    @property
    def threshold(self) -> int:
        return self._threshold

    def fuzz_getkey(self, key:str, threshold:float=0) -> str:
        """Implements logic for keys fuzz-match."""  
        threshold = threshold or self.threshold
        match, score = process.extractOne(key, self.keys(), score_cutoff=threshold) or (None, 0)
        return match or key
         
    def fuzz_getitem(self, __k:str, threshold:float=0) -> Any:
        self.key_typecheck(__k)
        __k = self.fuzz_getkey(__k, threshold or self.threshold)
        return super().__getitem__(__k)
    
    def fuzz_setitem(self, __k:str, v:Any, threshold:float=0) -> None:
        self.key_typecheck(__k)
        __k = self.fuzz_getkey(__k, threshold or self.threshold)
        return super().__setitem__(__k, v)
    
    def fuzz_get(self, __k:str, __default:Any=None, threshold:float=0) -> Any:
        self.key_typecheck(__k)
        __k = self.fuzz_getkey(__k, threshold or self.threshold)
        return super().get(__k, __default)

    def fuzz_update(self, other:dict) -> None:
        other = self(other)

        for k, v in other.items():
            self.__setitem__(k, v)