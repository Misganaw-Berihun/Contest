def charToDig(let):
    sum = 0
    for i  in range(len(let)):
        digit_i = ord(let[i]) - ord("A") + 1#alphabet to digit
        sum += digit_i * (26 ** (len(let) - i - 1))
    return sum

#Time O(n) memory : O(1)
def digToChar(num):
    strg = ""
    while(num > 0):
        if num % 26 == 0:
            rem = 26
            if(num == 26):
                num = num // 26 #remove the next reaminder
        else:
            rem = num % 26
        ord_let = chr(rem + ord('A') - 1)#convert to alphabet
        strg = ord_let + strg
        num = num//26
    return strg

def main():
    print("Enter a digit or an alphabet:")
    let = input()
    if(let[0].isdigit()):
        print(digToChar(int(let)))
    else:
        print(charToDig(let))

main()
