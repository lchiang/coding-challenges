ll = open('in16.txt').read().splitlines()

for l in ll:
    if (('children: 3' in l or 'children' not in l) and
        ('cats: 7' in l or 'cats' not in l) and
        ('samoyeds: 2' in l or 'samoyeds' not in l) and
        ('pomeranians: 3' in l or 'pomeranians' not in l) and
        ('akitas: 0' in l or 'akitas' not in l) and
        ('vizslas: 0' in l or 'vizslas' not in l) and
        ('goldfish: 5' in l or 'goldfish' not in l) and
        ('trees: 3' in l or 'trees' not in l) and
        ('cars: 2' in l or 'cars' not in l) and
        ('perfumes: 1' in l or 'perfumes' not in l)) :
        print('A', l)


for l in ll:
    if (('children: 3' in l or 'children' not in l) and
        #('cats: 7' in l or 'cats' not in l) and
        ('cats: 0' not in l and 'cats: 1' not in l and 'cats: 2' not in l and 'cats: 3' not in l) and
        ('cats: 4' not in l and 'cats: 5' not in l and 'cats: 6' not in l) and
        ('samoyeds: 2' in l or 'samoyeds' not in l) and
        #('pomeranians: 3' in l or 'pomeranians' not in l) and
        ('pomeranians: 0' in l or 'pomeranians: 1' in l or 'pomeranians: 2' in l or 'pomeranians' not in l) and
        ('akitas: 0' in l or 'akitas' not in l) and
        ('vizslas: 0' in l or 'vizslas' not in l) and
        #('goldfish: 5' in l or 'goldfish' not in l) and
        ('goldfish: 0' in l or 'goldfish: 1' in l or 'goldfish: 2' in l or 'goldfish: 3' in l or 'goldfish: 4' in l) and
        #('trees: 3' in l or 'trees' not in l) and
        ('trees: 0' not in l and 'trees: 1' not in l and 'trees: 2' not in l and 'trees: 3' not in l) and
        ('cars: 2' in l or 'cars' not in l) and
        ('perfumes: 1' in l or 'perfumes' not in l)) :
        print('B', l)

