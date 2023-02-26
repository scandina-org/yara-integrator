import json
import os
from typing import IO
import yara

def scan(file:IO):
    print(os.path.join("../rules/example.txt"))
    rules = yara.compile(filepaths={"example":os.path.join("app/rules/example.txt")})
    matches = rules.match(data=file.read())
    result = {}
    for match in matches:   
        if match.namespace in result:
            result[match.namespace].append(match.rule)
        else:
            result[match.namespace] = [match.rule]
    return result

    
    
    
    