#Quesiton: Generate the following pattern given h = 3
#                    1                                                       
#                  1 2 1                      
#                1 2 3 2 1

#time: o(n)  space: o(1)
def main():
    h = 3;
    for i in range(1,h+1):
        for j in range(h - i):
            print(' ', end = "");
        for k in range(1,i + 1):
            print(k,end = "")
        for l in range(i - 1,0,-1):
            print(l,end = "")
        print()

main()
