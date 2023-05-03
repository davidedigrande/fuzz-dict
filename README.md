# FuzzDict
FuzzDict extends Python's built-in ```dict``` to offer an extra API for fuzzy logic to match keys.
FuzzDict only supports string values for creating keys.

## Installation
```cmd
pip install fuzz-dict
```

## Usage
```python
from fuzz_dict import FuzzDict

# create a new dictionary
d = FuzzDict({'apple': 1, 'banana': 2, 'orange': 3}, threshold=0.8)

# get the key that are fuzzy matches for a given key
d.fuzz_getkey('appl', None)   # returns 'apple'
d.fuzz_getkey('kiwi', None)   # returns None

# access a value using fuzzy key matching
d.fuzz_getitem('appl')   # returns 1
d.fuzz_getitem('oran')   # returns 3

# update the dictionary using fuzzy key matching
d.fuzz_setitem('appl', 4)   # updates the 'apple' key with value 4
d.fuzz_setitem('oranj', 5)  # updates the 'orange' key with value 5
d.fuzz_setitem('kiwi', 6)   # creates a new item with 'kiwi' key and value 6
```

## Contributing
Contributions are welcome! Please create a pull request with your changes.