import copy

# https://adventofcode.com/2015/day/22

class Ring:


    '''
    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
    '''


    def hitboss(self, damage):
        self.b_hp -= max(1, damage)

    def effect(self):
        if self.timer_shield > 0:
            self.timer_shield -= 1

        if self.timer_poison > 0:
            self.hitboss(3)
            self.timer_poison -= 1

        if self.timer_recharge > 0:
            self.p_mana += 101
            self.timer_recharge -= 1


    def magic_missile(self):
        self.mana_used += 53
        self.p_mana -= 53
        self.hitboss(4)

    def drain(self):
        self.mana_used += 73
        self.p_mana -= 73
        self.hitboss(2)
        self.p_hp += 2

    def shield(self):
        self.mana_used += 113
        self.p_mana -= 113
        self.timer_shield = 6

    def poison(self):
        self.mana_used += 173
        self.p_mana -= 173
        self.timer_poison = 6

    def recharge(self):
        self.mana_used += 229
        self.p_mana -= 229
        self.timer_recharge = 5


    def p_armor(self):
        return 7 if self.timer_shield > 0 else 0

    def print_status(self):
        print('Player hit point {} , {} armor, {} mana'.format(self.p_hp, self.p_armor(), self.p_mana))
        print('  Boss hit point {} '.format(self.b_hp))
        print('Shield {}, Poison {}, Rechage {}'.format(self.timer_shield, self.timer_poison, self.timer_recharge))
        print()

    def turn(self, spell):
        self.spell_used = self.spell_used + spell + ' '

        # Player: Part B
        self.p_hp -= 1
        if self.p_hp <= 0: return 'b' # boss win

        # Player: Effect
        self.effect()
        if self.b_hp <= 0: return 'p' # player win

        # Player: Cast Spell
        getattr(Ring, spell)(self)
        if self.b_hp <= 0: return 'p' # player win

        # Boss: Part B
        self.p_hp -= 1
        if self.p_hp <= 0: return 'b' # boss win

        # Boss: Effect
        self.effect()
        if self.b_hp <= 0: return 'p' # player win

        # Boss: Cast Spell
        self.p_hp -= max(1, self.b_damage - self.p_armor())
        if self.p_hp <= 0: return 'b' # boss win

        return None



    def __init__(self):
        '''
        self.p_hp = 17
        self.p_mana = 250
        self.b_hp = 13
        self.b_damage = 8
        '''
        self.p_hp = 50
        self.p_mana = 500
        self.b_hp = 55
        self.b_damage = 8


        self.timer_shield = 0
        self.timer_poison = 0
        self.timer_recharge = 0

        self.mana_used = 0
        self.spell_used = ''


    def get_avail_spells(self):
        s = []
        m = self.p_mana
        
        if self.timer_recharge > 0:
            m = self.p_mana + 101


        if m >= 53:
            s.append('magic_missile')
        if m >= 73:
            s.append('drain')
        if m >= 113 and self.timer_shield == 0:
            s.append('shield')
        if m >= 173 and self.timer_poison == 0:
            s.append('poison')
        if m >= 229 and self.timer_recharge == 0:
            s.append('recharge')
        return s


min_m = 9999
def fight(ring):
    for f in ring.get_avail_spells():
        #if ring.mana_used > 1800: break
        r = copy.deepcopy(ring)

        # r.print_status()

        result = r.turn(f)
        if result:
            if result == 'p':
                global min_m
                min_m = min(min_m, r.mana_used)
                print(result, r.mana_used, r.spell_used, r.b_hp, r.p_hp)
        else:
            fight(r)


# Part B  1382 too high

r = Ring()

fight(r)

'''
re = ''
r.print_status()
re = r.turn('poison')
print(re)
r.print_status()
re = r.turn('magic_missile')
print(re)
r.print_status()
re = r.turn('magic_missile')
print(re)
r.print_status()
'''

print(min_m)
