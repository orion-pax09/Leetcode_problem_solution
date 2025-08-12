def combineletter(x):
    digits=input("Enter the digits:")
    result=[]
    def backtrack(index,path):
        if index==len(digits):
            result.append("".join(path))
            return
        letter_combination=x.get(digits[index],"")
        for letter in letter_combination:
            path.append(letter)
            backtrack(index+1,path)
            path.pop()
    backtrack(0,[])
    return f"{result} , {len(result)}"
num_letter=combineletter({"2":"abc",
                         "3":"def",
                          "4":"ghi",
                          "5":"jkl",
                          "6":"mno",
                          "7":"pqrs",
                          "8":"tuv",
                          "9":"wxyz"})
print(num_letter)