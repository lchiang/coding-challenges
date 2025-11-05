name = "Ascalparth,Myraris,Nysssar,Wynnixis,Zorgoril,Urithsarix,Urjor,Ulkix,Xaralhal,Paldkael,Dorural,Zarathkynar,Brynzris,Nyrixther,Balthendris,Caeltaril,Malsaral,Zalnixis,Eldensyron,Laznix,Skarulth,Urithlorath,Agnarloris,Pyrnarel,Aelvynar,Kyris,Larnarith,Felmaraxar,Gorathther,Gavnylor".split(',')
inst = "L21,R22,L20,R33,L19,R44,L29,R9,L40,R40,L48,R29,L12,R11,L30,R9,L10,R34,L49,R6,L5,R33,L5,R15,L5,R6,L5,R15,L5,R33,L5,R42,L5,R47,L5,R33,L5,R17,L5,R23,L29,R29,L45,R39,L22,R40,L42,R39,L38,R9,L35,R10,L20,R47,L24,R39,L46,R20,L35".split(',')

#name = "Vyrdax,Drakzyph,Fyrryn,Elarzris".split(',')
#inst = "R3,L2,R3,L3".split(',')

for i in inst:
    dest = (int(i[1:]) if i[0] == 'R' else int(i[1:])*-1) % len(name)
    name[0], name[dest] = name[dest], name[0]
print(name[0])
  