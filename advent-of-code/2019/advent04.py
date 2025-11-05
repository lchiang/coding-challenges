
# 248345-746315

cnt = 0
for x in range(248345,746315+1):
    #print(x)
    li = [int(i) for i in str(x)]
    increasing = True
    for i in range(0,5):
        if (li[i]-li[i+1]>0):
            increasing = False

	# part 1
    # double = False
    # for i in range(0,5):
    #    if (li[i]==li[i+1]):
    #        double = True
			
    double = False
    for i in range(0,6):
        c = li.count(li[i])
        if (c == 2):
            double = True       

     
    if (increasing and double):
        #print(x)
        cnt += 1
        
print(cnt)


    
