from fuzdict.fuzdict import FuzDict

from fuzdict import FuzDict
import requests
import random


dishes = requests.get("https://random-data-api.com/api/food/random_food?size=100", headers={"Content-type": "application/json"}).json()
keys = [dish["dish"] for dish in dishes]
values = [n for n in range(len(keys))]

print("pass")
