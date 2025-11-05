def first_n_distinct(s, n):
    for i in range(len(s)-n+1):
        #print(i+n4, s[i:i+n], len(set(s[i:i+n])))
        if (len(set(s[i:i+n])) == n):
            return i+n
def start_of_packet_marker(s):
    return first_n_distinct(s, 4)
def start_of_message_marker(s):
    return first_n_distinct(s, 14)

## Test ##
assert start_of_packet_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
assert start_of_message_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert start_of_message_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert start_of_message_marker('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert start_of_message_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert start_of_message_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

ll = open('./2022/06/input.txt').read().splitlines()
print('A', start_of_packet_marker(ll[0]))
print('B', start_of_message_marker(ll[0]))
