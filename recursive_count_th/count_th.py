'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    length = len(word)
    if length == 0 or length < 2:
        return 0
    if word[0:2] == 'th':
        return count_th(word[1:]) + 1
    return count_th(word[1:])


print(count_th('this th th th th th  th th   th th '))