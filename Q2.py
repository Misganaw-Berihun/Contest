#Time: O(n^2) Space: O(1)
def main():
    n = 4
    for i in range(n):
        for j in range(i + 1):
            print('*' , end ="")
        for k in range(n - 2*(i - 1)):
            print(' ', end = "")
        for l in  range(i + 1):
            print('*', end = "")
        print()
main()
