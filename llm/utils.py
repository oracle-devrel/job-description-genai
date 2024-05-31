# utils.py
import toml
from typing import Any

class LLMConfig():
    try:
        with open('./config.toml', 'r') as f:
            CONFIGS = toml.load(f)
    except FileNotFoundError:
        print("config.toml not found. The program expect the file in same folder.")
    def __init__(self, config=CONFIGS) -> None:
        self.__config = config
    
    def __getattr__(self, attr:str)->Any:
        try: 
            value = self.__config[attr]
            if isinstance(value, dict):
                return LLMConfig(value)
            return value
        except KeyError:
            raise AttributeError(f"No such configuration: {attr}")
    
    def keys(self):
        return self.__config.keys()
    def todict(self):
        return self.__config
