import operator

d = {} # Cost, Damage, Armor
# Weapons (Choose 1)
d['Dagger']=(8,4,0)
d['Shortsword']=(10,5,0)
d['Warhammer']=(25,6,0)
d['Longsword']=(40,7,0)
d['Greataxe']=(74,8,0)

# Armor (Choose 0-1)
d['NoArmor']=(0,0,0)
d['Leather']=(13,0,1)
d['Chainmail']=(31,0,2)
d['Splintmail']=(53,0,3)
d['Bandedmail']=(75,0,4)
d['Platemail']=(102,0,5)

# Rings (Choose 0-2, No duplicate)
r = {} # ring
r['Damage+1']=(25,1,0)
r['Damage+2']=(50,2,0)
r['Damage+3']=(100,3,0)
r['Defense+1']=(20,0,1)
r['Defense+2']=(40,0,2)
r['Defense+3']=(80,0,3)

weapon = ['Dagger','Shortsword','Warhammer','Longsword','Greataxe']
armor = ['NoArmor','Leather','Chainmail','Splintmail','Bandedmail','Platemail']
ring = ['Damage+1','Damage+2','Damage+3','Defense+1','Defense+2','Defense+3']

tworing = []
import itertools
for a1, a2 in itertools.combinations(ring,2): # two ring
    d[a1+a2] = tuple(map(operator.add, r[a1], r[a2]))
    tworing.append(a1+a2)
d.update(r) # one ring
d['NoRing']=(0,0,0) # no ring
ring = ring + ['NoRing'] + tworing

'''
Hit Points: 109
Damage: 8
Armor: 2

You have 100 hit points. The boss's actual stats are in your puzzle input. 
What is the least amount of gold you can spend and still win the fight?
'''

def canWin(h,d,a):
    bh, bd, ba = 109, 8, 2 #boss hit points, boss damage, boss armor
    while h > 0 and bh > 0:
        bh -= max(1, d-ba)
        #print('boss hp', bh)
        if bh <= 0: return True
        h -= max(1, bd-a)
        #print('player hp', h)
        if h <= 0: return False

low_cost = 99999
high_cost = 0
for w,a,r in itertools.product(weapon, armor, ring):
    cost = sum(i for i, j, k in [d[w],d[a],d[r]])
    dam = sum(j for i, j, k in [d[w],d[a],d[r]])
    arm = sum(k for i, j, k in [d[w],d[a],d[r]])
    
    if canWin(100,dam,arm):
        low_cost = min(low_cost, cost)
    else:
        high_cost = max(high_cost, cost)
    
print(low_cost, high_cost)
