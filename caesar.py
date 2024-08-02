string = list(map(str, input().split()))

for i in range(26):
    for word in string:
        for j in range(len(word)):
            temp = ord(word[j]) - i
            if(temp < 65):
                temp += 26
            print(chr(temp), end = "")
        print("",end = " ")
    print()