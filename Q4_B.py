def main():
    h = 3;
    for i in range(1,h+1):
        for j in range(h - i):
            print(" ",end = "")
        for k in range(1,i+1):
            print(k,end = "")
        for l in range(i - 1,0,-1):
            print(l,end = "")
        print()
    for x in range(h-1,0,-1):
        for a in range(h-x):
            print(' ', end = "")
        for y in range(1,x+1):
            print(y,end = "")
        for z in range(x - 1,0,-1):
            print(z,end = "")
        print()

main()
