#time: O(n^2) space: O(1)
def main():
    n = 4
    for i in range(4):
        for j in range(i + 1):
            print('*',end = "")
        print()
main()
