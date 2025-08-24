#Sorting with (O(n log n))

def anargramvalid(word,specific):
    words=len(word)
    specifics=len(specific)
    if words == specifics:
        sorted_Word=sorted(word.lower())
        sorted_Specific=sorted(specific.lower())
        if sorted_Word == sorted_Specific:
            return "They are valid anagram"
        else:
            return "They are invalid anagram "
    else:
        return f"Their length of string don't match each other"

input=anargramvalid("Hamza","amzaz")
print(input)


# valid anagram of (O(n))
def anagramvalid(s,t):
    if len(s) != len(t):
        return False
    count={}
    for charc in s.lower():
        count[charc]=count.get(charc,0)+1
    for charc in t.lower():
        if charc not in count or count[charc]==0:
            return False
        else:
            count[charc]-=1
    return all(val==0 for val in count.values())
Input=anagramvalid("hamza","amzho")
print(Input)






