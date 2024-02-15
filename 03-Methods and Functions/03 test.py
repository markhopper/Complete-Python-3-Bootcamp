
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    elif a % 2 != 0 or b % 2 != 0:
        if a < b:
            return b
        else:
            return a


lesser_of_two_evens(2, 4)


def animal_crackers(string):
    words = string.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False

animal_crackers("lfhje fhrhs")


def laughter(pattern, string):
    num = 0
    first_letter = pattern[0]
    indices = [i for i, letter in enumerate(string) if letter == first_letter]
    for index in indices:
        substring = string[index: index+len(pattern)]
        if substring == pattern:
            num += 1


def spy_game(integers):
    index_0 = [i for i, num in enumerate(integers) if num == 0]
    index_7 = [i for i, num in enumerate(integers) if num == 7]

    if len(index_0) >= 2 and len(index_7) >= 1:
        if index_0[1] < index_7[0]:
            return True

    return False


def count_primes(a):
    num = 0
    for i in range(2, a+1):
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            num += 1

    return num
