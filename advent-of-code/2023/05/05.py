seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

line_num = 2
l_iter = iter(ll)  
seeds = [int(x) for x in next(l_iter).split(':')[1].split()]

next(l_iter)


def read(name):
    s = []

    while (l:=next(l_iter,'END')) != name:
        print('1',l)

    while (l:=next(l_iter,'END')) != '':
        if l == 'END':
            break;
        elif l:
            s.append(tuple([int(x) for x in l.split()]))
    return s


seed_to_soil = read('seed-to-soil map:')
soil_to_fertilizer = read('soil-to-fertilizer map:')
fertilizer_to_water = read('fertilizer-to-water map:')
water_to_light = read('water-to-light map:')
light_to_temperature = read('light-to-temperature map:')
temperature_to_humidity = read('temperature-to-humidity map:')
humidity_to_location = read('humidity-to-location map:')
'''
print('seed_to_soil', seed_to_soil)
print('soil_to_fertilizer', soil_to_fertilizer)
print('fertilizer_to_water', fertilizer_to_water)
print('water_to_light', water_to_light)
print('light_to_temperature', light_to_temperature)
print('temperature_to_humidity', temperature_to_humidity)
print('humidity_to_location', humidity_to_location)
'''
print('===')

def to_map(mapping, i):
    
    o = i
    for m in mapping:
    
        if m[1] <= i and i <= m[1]+m[2]-1:
    
            o += (m[0]-m[1])
            break;
    
    return o

def min_loc(mi, ma):
    min_location = 92916488878
    for x in range(mi, ma+1):
        
        
        
        soil = to_map(seed_to_soil, x)   
        fertilizer = to_map(soil_to_fertilizer, soil)   
        water = to_map(fertilizer_to_water, fertilizer)   
        light = to_map(water_to_light, water)     
        temperature = to_map(light_to_temperature, light)
        humidity = to_map(temperature_to_humidity, temperature)   
        location = to_map(humidity_to_location, humidity)   

        min_location = min(min_location, location)
        
    return min_location



        

# part a
mm = 92916488878
for seed in seeds:
    mm = min(mm, min_loc(seed, seed))
print('a', mm)


# part b
print(len(seeds))
mm = 92916488878
for i in range(len(seeds)//2):
    
    start = seeds[i*2]
    rng = seeds[i*2+1]
    print(start, start + rng - 1)
    ml = min_loc(start, start + rng - 1)
    #print(ml)
    mm = min(mm, ml)
print('b', mm)

## part b shall be correct but too slow



