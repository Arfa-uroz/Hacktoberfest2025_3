def fact(n): 
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
def findRank(str):
    n = len(str)
    mul = fact(n)
    rank = 1
    
    count = [0] * 26

    for i in range(n):
        count[ord(str[i]) - ord('a')] += 1

    for i in range(1, 26):
        count[i] += count[i - 1]

    for i in range(n):
        mul //= (n - i)

        charIndex = ord(str[i]) - ord('a')

        if charIndex > 0:
            rank += count[charIndex - 1] * mul

        for j in range(charIndex, 26):
            count[j] -= 1

    return rank

if __name__ == "__main__":
    str = "string"
    print(findRank(str))


    print(findRank(str))
