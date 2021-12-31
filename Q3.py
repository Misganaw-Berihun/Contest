#Question: generate the following pattern given N
#                    N = 2
#                    #  #
#                    #  #
#                    N = 3
#                    ## ## ##
#                    ## ## ##
#                    N = 4
#                    ### ### ### ###
#                    ### ### ### ###

#time: O(n^2) memory: o(1)
def main():
    print("Enter an integer:")
    n = int(input())
    ROWS = 2;

    for i in range(ROWS):
        for j in range(n):
            for k in range(n - 1):
                print("#" , end = "")
            print(end = " ");
        print()
main()
