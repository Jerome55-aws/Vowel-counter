"""vowel = ['a', 'e', 'i', 'o', 'u'], counts the number of vowels in a string"""

def vowel_counter(word):
    num_vowel = 0
    for letter in word:
        if letter in 'aeiouAEIOU':
            num_vowel += 1
    return num_vowel

print(vowel_counter(''))
