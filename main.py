import sys
from stats import get_num_words, get_char_count, get_sorted_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_num_words(file_contents)
    char_count = get_char_count(file_contents)
    sorted_list = get_sorted_char_count(char_count)

    print(f"{'='*20} BOOKBOT {'='*20}")
    print(f"Analyzing book found at {file_path}")
    print(f"{'-'*20} Word Count {'-'*20}")
    print(f"Found {word_count} total words")
    print(f"{'-'*20} Character Count {'-'*20}")
    for char_item in sorted_list:
        print(f"{char_item['char']}: {char_item['count']}")
    print(f"{'='*20} END {'='*20}")



# Helper Functions
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()
