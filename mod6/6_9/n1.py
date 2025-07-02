from collections import ChainMap
import json

with open('zoo.json', 'r') as f:
    zoo = json.load(f)
    chainmap = ChainMap(*zoo)
    print(sum(chainmap.values()))