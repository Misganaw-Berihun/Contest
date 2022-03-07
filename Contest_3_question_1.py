def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    count = 0
    
    if len(A) < 2:
        return 0 if A[0] >= k else -1
    else:   
        if A[0] > k:
            return 0
        
        while len(A) >= 2:
            first = heapq.heappop(A)
            second = heapq.heappop(A)
            new = first + 2 * second
            heapq.heappush(A,new)
            count += 1
            
            if A[0] >= k:
                return count  
      
    return -1
