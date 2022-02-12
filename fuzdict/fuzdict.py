from typing import Any
from fuzzywuzzy import process


class FuzDict(dict):
    """
    FuzDict is a python dictionary that implements Fuzzy Logic as a way to match keys.
    This is implies that suitable values for creating keys are only of str type.
    """
    def __new__(cls, threshold:int=80, get_only:bool=False, *args, **kwargs) -> dict:
        if not type(threshold) is int:
            raise ValueError("Threshold must be an integer.")

        if 0 >= threshold >= 100:
            return super(*args, **kwargs)

        else:
            return super(FuzDict, cls).__new__(cls, threshold, dict, get_only, *args, **kwargs)

    def __init__(self, threshold:int=80, dict:dict={}, get_only:bool=False, *args, **kwargs):
        self._threshold = threshold
        self._get_only = get_only
        super().__init__(*args, **kwargs)
        self.update(dict)

    @property
    def threshold(self):
        return self._threshold
    
    @property
    def get_only(self):
        return self._get_only
         
    def __getitem__(self, __k:str) -> Any:
        if type(__k) is not str:
            raise ValueError(f"{type(self)} only supports string objects as keys. Received {type(__k)} instead.")

        value = super().get(__k, None)
        if value:
            return value

        match, score = process.extractOne(__k, self.keys()) or ("", 0)
        if score > self.threshold:
            return super().__getitem__(match)
        
        raise KeyError(__k)
    
    def __setitem__(self, __k:str, v:Any) -> None:
        if type(__k) is not str:
            raise ValueError(f"{type(self)} only supports string objects as keys. Received {type(__k)} instead.")

        if self.get_only:
            return super().__setitem__(__k, v)

        match, score = process.extractOne(__k, self.keys()) or ("", 0)
        if score > self.threshold:
            return super().__setitem__(match, v)

        return super().__setitem__(__k, v)
    
    def get(self, __k:str, __default:Any=None, exact:bool=False):
        if type(__k) is not str:
            raise ValueError(f"{type(self)} only supports string objects as keys. Received {type(__k)} instead.")

        value = super().get(__k, None)
        if value:
            return value

        if exact:
            return value or __default

        match, score = process.extractOne(__k, self.keys()) or ("", 0)
        if score > self.threshold:
            return super().__getitem__(match)
        
        return __default
    


