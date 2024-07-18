from typing import Dict, TypedDict, Union, Optional, Tuple
import pprint

class Data2(TypedDict):
    a: int
    b: int

Key = Union[int, str]

Value = Union[str,Data2]

data: Dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "cde": {"a": 1, "b": 2}
}

# print(data["cde"]["a"]) # This is giving error because string is not indexable.
#only dictionary is indexable, thats why we coinfirm if its  a dictionary in below code 


if isinstance(data["cde"], dict) :
    print(data["cde"]["a"])
else:
    print("Key 'a' not found in 'cde'")

if isinstance(data["cde"], dict) and "a" in data["cde"]:
    print(data["cde"]["a"])
else:
    print("Key 'a' not found in 'cde'")