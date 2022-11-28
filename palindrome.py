
'''
Write a function that tests whether a string is a palindrome.
'''

#Code:
#  A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def remove_special_chars(thisString):
    return(''.join(e for e in thisString if e.isalnum()))

def isPalindrome(word):
    isPalindrome = True
    backwards = word [::-1]
    backwards_letters = []
    backwards_letters.extend(backwards)
    count = 0
    letters = []
    letters.extend(word)
    while count < len(letters):
        thisLetter = letters[count]
        thisLetter = thisLetter.lower()
        if thisLetter != backwards_letters[count].lower():
            isPalindrome = False
            return isPalindrome
        count += 1
    return isPalindrome

word = input()
word = remove_special_chars(word)

print(isPalindrome(word))