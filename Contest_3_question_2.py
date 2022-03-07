import heapq

heap = []
q = int(input())
deleted = set()


for i in range(q):
    inp = input()
    #input
    if inp[0] == '1' or inp[0] == '2':
        l,r = map(int,inp.split())
    else:
        r = int(inp)
        
    #process
    if inp[0] == '1':
        heapq.heappush(heap,r)
        if r in deleted:
            deleted.discard(r)
    elif inp[0] == '2':
        deleted.add(r)
    elif inp[0] == '3':
        while heap[0] in deleted:
            tmp = heapq.heappop(heap)
            deleted.discard(tmp)
            
        print(heap[0])
