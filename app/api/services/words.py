def count_vowels(word: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)


def sort_words(words: list, order: str) -> list:
    return sorted(words, reverse=(order == "desc"))
