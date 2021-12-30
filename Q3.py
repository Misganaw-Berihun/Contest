#time: O(n^2) memory: o(1)

def main():
    print("Enter an integer:")
    n = int(input())
    ROWS = 2;

    for i in range(ROWS):
        for j in range(n):
            for k in range(n):
                print("#" , end = "")
            print(end = " ");
        print()
main()
