f = open('in9c.txt')
il = f.read().splitlines()

l = []
for ii in il:
    l.append(ii.split(':')[1])

print(len(l))

def is_kid_of(k,p1,p2):
  for i in range(len(k)):
    if (k[i] != p1[i]) and (k[i] != p2[i]):
      return False
  return True

def deg_of_similarity(a,b):
  return sum(x==y for x,y in zip(a,b))

print('part i', deg_of_similarity(l[0], l[2])*deg_of_similarity(l[1], l[2]))

fam_list = []

b_cnt = 0
for i in range(len(l)):
  #print(i, l[i])
  for ai in range(len(l)):
    if ai != i:
      for bi in range(ai, len(l)):
        if bi != i and bi != ai:
          #print('1=', ai, l[ai])
          #print('2=', bi, l[bi])
          if is_kid_of(l[i], l[ai], l[bi]):
            print(i, ai, bi)
            fam_list.append((i, ai, bi))
            #print(i, l[i])
            #print(ai, l[ai])
            #print(bi, l[bi])
            #print()

            b_cnt += deg_of_similarity(l[i], l[bi])*deg_of_similarity(l[i], l[ai])
print('part ii', b_cnt)


#print('fam_list', fam_list)

fam2bsort = fam_list[1:]
#print('fam2bsort', fam2bsort)
fam_grp = []
remaining = [x for x in range(1, len(l))]

#print('remaining', remaining)

#print('fam_grp', fam_grp)
print()
j = 0

for fam in fam_list:
  fam_found_group = False
  for fg in fam_grp:
    if fam[0] in fg or fam[1] in fg or fam[2] in fg:
      fam_found_group = True
      if fam[0] not in fg: fg.append(fam[0])
      if fam[1] not in fg: fg.append(fam[1])
      if fam[2] not in fg: fg.append(fam[2])
  if not fam_found_group:
    fam_grp.append(list(fam))
  #print('fam_grp', fam_grp)


print('== fam_grp', fam_grp)


have_action = True
while have_action:
  i = 0
  have_action = False
  while i <= len(fam_grp):
    to_merge = []
    for j in range(i+1, len(fam_grp)):

      merge_this = False
      for k in fam_grp[i]:
        #print(k,fam_grp[j])
        if k in fam_grp[j]:
          merge_this = True
          have_action = True
      if merge_this:
        to_merge.append(fam_grp[j])


    for m in to_merge:
      fam_grp[i].extend([x for x in m if x not in fam_grp[i]])
      fam_grp.remove(m)
      print(fam_grp)
      print()
    i += 1


largest_fam_size = 0
for f in fam_grp:
  if len(f) > largest_fam_size:
    #print(f)
    print('part c', sum(x+1 for x in f))
    largest_fam_size = max(largest_fam_size, len(f))




