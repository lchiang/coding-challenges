def worker(conn,qq):
    
    i = 0 
    while True:
        i += 1
        inq = conn.recv()
        if inq != 'END':
            print(qq, i, inq)
        else:
            break            
    conn.send('DONE')

def workerq(q,qq):
    
    i = 0 
    while True:
        i += 1
        inq = q.get()
        if inq != 'END':
            print(qq, i, inq)
        else:
            break
    print(q.get())
    q.put('DONE')

