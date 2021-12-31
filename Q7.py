#Question: Given a Roman number, change to its corresponding integer value given
#       Symbol       Value
#           I             1
#           V             5
#           X             10
#           L             50
#           C             100
#           D             500
#           M             1000
#           Example :
#           Input: s = "LVIII"
#           Output: 58
#           Explanation: L = 50, V= 5, III = 3.

#Time O(n) , memory: O(1)
def main():
    ROMAN = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }

    s =  input()
    sum = 0

    for i in range(len(s)):
        if i!= len(s) - 1 and ROMAN[s[i]] < ROMAN[s[i + 1]]:
            sum += ROMAN[s[i+1]] - 1
        elif i!= 0 and ROMAN[s[i]] > ROMAN[s[i - 1]]:
            continue
        else:
            sum += ROMAN[s[i]]
    print(sum)

main()
