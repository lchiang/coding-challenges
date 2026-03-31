
def letter_to_bit(letter):
    """Convert uppercase to 1, lowercase to 0"""
    return 1 if letter.isupper() else 0

def component_to_value(component):
    """Convert a 6-letter color component to its decimal value"""
    if len(component) != 6:
        return 0
    value = 0
    for i, letter in enumerate(component):
        bit = letter_to_bit(letter)
        value = value * 2 + bit
    return value

total_sum = 0
max_shine = 0
max_group = ''
max_group_num = 0
from collections import defaultdict
group_dict = defaultdict(list)
with open('q1_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        # Parse the line: "ID:component1 component2 component3"
        if ':' not in line:
            continue

        identifier_part, colors_part = line.split(':', 1)
        identifier = int(identifier_part.strip())

        # Split the three color components
        colors = colors_part.strip().split()
        if len(colors) != 4:
            continue

        red_str, green_str, blue_str, shine_str = colors

        # Convert each component to value
        red_val = component_to_value(red_str)
        green_val = component_to_value(green_str)
        blue_val = component_to_value(blue_str)
        shine_val = component_to_value(shine_str)

        # max_shine = max(max_shine, shine_val)
        # if shine_val == 63:
        #     print(identifier, 'shine', shine_val, 'colour sum', red_val+green_val+blue_val )

        # Check if green is dominant (greater than both red and blue)

        group = ''
        if green_val > red_val and green_val > blue_val:
            # total_sum += identifier
            group = 'G'
        elif red_val > green_val and red_val > blue_val:
            group = 'R'
        elif blue_val > red_val and blue_val > green_val:
            group = 'B'

        if len(group) == 1 and shine_val <= 30:
            group += 'M'
        elif len(group) == 1 and shine_val >= 33:
            group += 'S'



        if len(group) == 2:
            if len(group_dict[group]) > max_group_num:
                max_group_num = len(group_dict[group])
                max_group = group

            group_dict[group].append(identifier)


        # print(f"{identifier}: {red_val:>3} {green_val:>3} {blue_val:>3}, {shine_val:>3}, {group}")

# print(group_dict.items())
print(max_group, max_group_num, sum(group_dict[max_group]))

# print(f"\nFinal sum of identifiers where green is dominant: {total_sum}")
# print(total_sum)
