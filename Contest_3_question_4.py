def runningMedian(a):
    def findMedian(left,right):
        if len(left) == len(right):
            return (-1 * left[0] + right[0])/2
        else:
            return -left[0]
    
    # Write your code here
    left = []
    right = []
    ans = []
    
    for i in range(len(a)):
        if len(left) > len(right):
            temp = heapq.heappushpop(left,-a[i])
            heapq.heappush(right,-temp)
        else:
            temp = heapq.heappushpop(right,a[i])
            heapq.heappush(left,-temp)
        ans.append(findMedian(left,right))
    
    return ans
