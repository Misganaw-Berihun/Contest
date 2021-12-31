#Question: Given an integer array, move all 0's to the end maintaining the order of the other elements.
#                        Example 1:
#                        Input: nums = [0,1,0,3,12]
#                        Output: [1,3,12,0,0]

#Time: O(n), Memory: O(n)
def main():
    print("Enter the elements of the list (separated by space): ")
    arr = list(map(int,input().split()))
    zeros = 0
    arr2 = []

    for el in arr:
        if el != 0:
            arr2.append(el)#append if not zero
        else:
            zeros += 1

    for i in range(zeros):#append the zeros
        arr2.append(0)

    print(arr2)

main()
