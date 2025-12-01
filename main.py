from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    chars_dict = get_chars_dict(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)

    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()