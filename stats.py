from typing import Dict, TypedDict, List

# Return number of words in a String
def get_num_words(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)

# Returns a Dict<Char, Int>
# Counts of each character apperence
def get_char_count(file_content: str) -> Dict[str, int]:
    char_dict = {}
    for char in file_content.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# Returns a sorted list with char and their respective count
# Class for sort_on() function
class CharIndex(TypedDict):
    char: str
    count: int
# Key for sorting values
def sort_on(items: CharIndex) -> int:
    return items["count"]
# Return sorted dictionary
def get_sorted_char_count(char_dict: Dict[str, int]) -> List[CharIndex]:
    char_list = []
    for char in char_dict:
        if char.isalpha():
            item = {
                "char": char,
                "count": char_dict[char]
                }
            char_list.append(item)
    char_list.sort(reverse=True, key=sort_on)
    return char_list