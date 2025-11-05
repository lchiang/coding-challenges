import re

f = open('in04_2.txt')
inputfile = f.read().split('\n\n')

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # no cid
fields_with_colon = [ii+':' for ii in fields]

def validate(field, elem):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    
    if not elem:
        return False
    value = elem[0].split(':')[1]
    if field == 'byr':
        return 1920 <= int(value) <= 2002        
    elif field == 'iyr':
        return 2010 <= int(value) <= 2020
    elif field == 'eyr':
        return 2020 <= int(value) <= 2030
    elif field == 'hgt':        
        if value[-2:] == 'cm':
            return 150 <= int(value[:-2]) <= 193
        else:
            return 59 <= int(value[:-2]) <= 76
    elif field == 'hcl':
        return True if re.match(r'#[0-9a-f]{6}',value) else False
    elif field == 'ecl':
        return value in ['amb','blu','brn','gry','grn','hzl','oth']
    elif field == 'pid':
        return True if re.fullmatch(r'[0-9]{9}',value) else False
    elif field == 'cid':
        return True
         


valid_cnt = 0

for l in inputfile:
    #print(l)
    passport = re.split(' |\n',l)
    #print(passport)
    
    valid = True
    for field in fields:        
        elem = list(filter(lambda x: x.startswith(field), passport))        
        valid = validate(field, elem)
        #print(field, elem, valid)
        if not valid:
            break

    #valid = all(item in l for item in fields_with_colon)
    if valid:
        valid_cnt += 1
    
    
print(valid_cnt)



    
