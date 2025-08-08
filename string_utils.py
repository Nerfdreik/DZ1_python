class StringUtils:
    def capitilize(self, string: str) -> str:
        return string.capitalize()
    
    def trim(self, string: str) -> str:
        return string.lstrip()
    
    def to_list(self, string: str, delimiter: str = ",") -> list:
        return string.split(delimiter)
    
    def contains(self, string: str, substring: str) -> bool:
        return substring in string
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        return string.replace(symbol, "")
    
    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)
    
    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)
    
    def is_empty(self, string: str) -> bool:
        return not string.strip()
    
    def list_to_string(self, lst: list, delimiter: str = ", ") -> str:
        return delimiter.join(map(str, lst))