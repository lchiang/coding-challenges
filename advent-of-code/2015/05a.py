import string
ll = open('in05.txt').read().splitlines()

vowel = ['a','e','i','o','u']
twice = [x+x for x in list(string.ascii_lowercase)]
bad = ['ab', 'cd', 'pq', 'xy']

def vowel_cnt_at_least(s, n):
    c = 0
    for v in vowel:
        c += s.count(v)
    return (c >= n)

def has_twice(s):
    for t in twice:
        if t in s:
            return True
    return False

def nice_word_only(s):
    for b in bad:
        if b in s:
            return False
    return True

def is_nice(s):
    return vowel_cnt_at_least(s,3) and has_twice(s) and nice_word_only(s)

'''
Sample Case
print(is_nice('ugknbfddgicrmopn'))
print(is_nice('aaa'))
print(is_nice('jchzalrnumimnmhp'))
print(is_nice('haegwjzuvuyypxyu'))
print(is_nice('dvszwmarrgswjxmb'))
'''

nice_cnt = 0
for l in ll:
    if is_nice(l):
        nice_cnt += 1
print(nice_cnt)