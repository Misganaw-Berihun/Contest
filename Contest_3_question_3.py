def minimumAverage(customers):
    # Write your code here
    customers.sort()
    curTime = customers[0][0]
    time = 0
    total = 0
    heap = []
    i = 0
    
    while i < len(customers):
        while not heap or \
                (i < len(customers) and customers[i][0] <= curTime):
            heapq.heappush(heap,(customers[i][1],customers[i][0]))
            i += 1
        
        p = heapq.heappop(heap)
        if curTime - p[1] < 0:
            curTime = p[1]
        time = (curTime - p[1] + p[0]) 
        total += time
        curTime += p[0]
        
    while heap:
        p = heapq.heappop(heap)
        time = (curTime - p[1] + p[0]) 
        total += time
        curTime += p[0]
            
    return total // len(customers)
