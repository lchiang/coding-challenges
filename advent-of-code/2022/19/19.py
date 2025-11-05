ll = open('./2022/19/test.txt').read().splitlines()
#ll = open('./2022/19/input.txt').read().splitlines()

import re

from collections import namedtuple
'''
o = ore, c = clay, b = obsidian, g = geode
a_b = a bot cost b resources
'''
Blueprint = namedtuple('Blueprint', ['num','o_o','c_o','b_o','b_c','g_o','g_b'])
blurprint = []

World = namedtuple('World', ['o_bot','c_bot','b_bot','g_bot','o','c','b','g'])

class World1:
    def __init__(self):
        self.ore_bot = 1
        self.cla_bot = 0
        self.obs_bot = 0
        self.geo_bot = 0

        self.ore = 0
        self.cla = 0
        self.obs = 0
        self.geo = 0

    def print(self):
        print("Bot number: ore {}, clay {}, obsidian {}, geode {}".format(self.ore_bot, self.cla_bot, self.obs_bot, self.geo_bot))
        print("Resources: ore {}, clay {}, obsidian {}, geode {}".format(self.ore, self.cla, self.obs, self.geo))




for l in ll:
    result = re.search(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l)
    bp = Blueprint._make([int(x) for x in result.groups()])
    blurprint.append(bp)


def run_with_bp(bp_num):

    bp = blurprint[bp_num-1]
    print(bp)
    w = World(1,0,0,0,0,0,0,0)
    next(w,bp,0,0,0,0,0)


def next(w, bp, t, o, c, b, g): # world, time, new bot number
    if t < 24:
        t += 1
        # collect
        w = w._replace(o = w.o + w.o_bot)
        w = w._replace(c = w.c + w.c_bot)
        w = w._replace(b = w.b + w.b_bot)
        w = w._replace(g = w.g + w.g_bot)

        # robot ready
        w = w._replace(o_bot = w.o_bot + o)
        w = w._replace(c_bot = w.c_bot + c)
        w = w._replace(b_bot = w.b_bot + b)
        w = w._replace(g_bot = w.g_bot + g)

        # print status
        if t == 24 and w.g_bot>0:
            print('{:3d}'.format(t), w)

        # build bot or not

        if (w.o >= bp.g_o) and (w.b >= bp.g_b):
            new_g_bot = min(w.o//bp.g_o, w.b//bp.g_b)
            wg = w._replace(o = w.o - (new_g_bot*bp.g_o))
            wg = wg._replace(b = wb.b - (new_g_bot*bp.g_b))
            next(wg,bp,t,0,0,0,new_g_bot)

        if (w.o >= bp.c_o) and (w.b >= bp.b_c):
            new_b_bot = min(w.o//bp.b_o, w.c//bp.b_c)
            wb = w._replace(o = w.o - (new_b_bot*bp.b_o))
            wb = wb._replace(b = wb.b - (new_b_bot*bp.b_c))
            next(wb,bp,t,0,0,new_b_bot,0)

        if (w.o >= bp.c_o):
            new_c_bot = w.o//bp.c_o
            wc = w._replace(o = w.o - (new_c_bot*bp.c_o))
            next(wc,bp,t,0,new_c_bot,0,0)

        if (w.o >= bp.o_o):
            new_o_bot = w.o//bp.o_o
            wo = w._replace(o = w.o - (new_o_bot*bp.o_o))
            next(wo,bp,t,new_o_bot,0,0,0)

        next(w,bp,t,0,0,0,0)


#,'c_o','b_o','b_c','g_o','g_b'])
        '''

        1 ore-collecting robot collects 1 ore; you now have 1 ore.
        1 clay-collecting robot collects 1 clay; you now have 2 clay.
        The new clay-collecting robot is ready; you now have 2 of them.

        Spend 2 ore to start building a clay-collecting robot.
        '''


    return None

run_with_bp(1)
'''
print(w)
w1 = w._replace(o_bot = 21)
w1 = w1._replace(c_bot = 71)
print('000', w)
print(w1)
#pt = pt._replace(x=100)
'''