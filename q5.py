#Question : a) Given a number find its alphabetical representation 
#Question : b) Given an alphabet find its numeric representation where
#                                    A -> 1
#                                    B -> 2
#                                    C -> 3
#                                    ...
#                                    Z -> 26
#                                    AA -> 27
#                                    AB -> 28

#Time: O(n) , Memory: O(1)
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

#Time: O(1)  , Memory: O(1)
def main():
    print("Enter a digit or an alphabet:")
    let = input()
    if(let[0].isdigit()):
        print(digToChar(int(let)))
    else:
        print(charToDig(let))

main()
