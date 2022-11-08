def permuteation(string, answer):
    if (len(string) == 0):
        print(answer, end=" ")
        return

    for i in range(len(string)):
        ch = string[i]
        left_substr = string[0:i]
        right_substr = string[i + 1:]
        rest = left_substr + right_substr
        permuteation(rest, answer + ch)



answer = ""
string = input("Enter the string : ")
print("All possible strings are : ")
permuteation(string, answer)