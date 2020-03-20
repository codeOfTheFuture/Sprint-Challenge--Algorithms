'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    sub_str = word[:2]

    if len(word) < 2:
        return count
    elif sub_str == 'th':
        count += 1
        count += count_th(word[2:])
    else:
        count += count_th(word[1:])
    return count


print(count_th('thababthabthtttth'))
