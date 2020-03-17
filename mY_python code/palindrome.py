word = 'banana'


def if_palindrome(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        print(word + " is a palindrome")
    else:
        print(word + ' isn\'t a palindrome')


if_palindrome(word)
