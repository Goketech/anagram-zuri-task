# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.strip()
    anagram = anagram.strip()
    word = sorted(word)
    anagram = sorted(anagram)
    if word == anagram:
        print(True)
    else:
        print(False)
find_anagram('elbow', 'below')
#this will return true
find_anagram('zuri', 'ingressive')
#this will return false
