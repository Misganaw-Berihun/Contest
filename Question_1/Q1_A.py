# time: O(n^2)  space:O(1)
#Question:         Generate the following patterns
#                                * 
#                              * * *
#                            * * * * * 
#                          * * * * * * * 

def main():
    n = 5;
    for i in range(n):
            # print( ('*'*(2 * i + 1)).center(n*2 ,' '))
            for j in range(n - i):
                print(" ",end = "")
            for k in range(2*i + 1):
                print("*",end = "")
            print()


main()
