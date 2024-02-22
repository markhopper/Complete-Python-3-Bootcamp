import numpy as np
import string

def volume(r):
    print((4/3)*np.pi*r**3)


def ran_bool(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False


def up_low(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    print("No of uppercase letters is ", upper)
    print("No of lowercase letters is ", lower)


def unique_list(lst):
    unique = set(lst)
    print(list(unique))


def multiply(numbs):
    res = 1
    for num in numbs:
        res = res * num

    print(res)


def palindrome(s):
    s = s.replace(" ", "")
    reverse = s[::-1]
    if s == reverse:
        print(True)
    else:
        print(False)


def ispangram(s):
    alphabet = string.ascii_lowercase

    s = s.lower().replace(" ", "")
    for letter in s:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")

    if len(alphabet) == 0:
        print(True)
    else:
        print("Length of alphabet is still ", len(alphabet))




# volume(2)

res = ran_bool(2, 2, 7)
#print(res)

#up_low("Hello Mr Rogers, How are Tuesday?")

#unique_list([1,1,1,2,2,3,3,4,4,5,5,6])

#multiply([1,2,3,5])

#palindrome("racde car")

ispangram("The quick brown  jumps over the lazy dog")

