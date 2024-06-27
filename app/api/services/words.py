def count_vowels(word: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)