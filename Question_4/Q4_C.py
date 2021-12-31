#Question: Generate the following pattern given h = 3
#                    ##  ##  ##
#                      ##  ##
#                    ##  ##  ##
#                      ##  ##
#                    ##  ##  ##

#Time:O(n) memory: O(1)
def main():
    h = 3
    for i in range(2*h - 1):
        if i % 2 == 0:
            for j in range(3):
                print("##",end ="  ")
            print()
        else:
            for k in range(2):
                print("  ",end = "##")
            print()

main()
