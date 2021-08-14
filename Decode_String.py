nums_set = {str(i) for i in range(0,10)}
char_set = {chr(char) for char in range(ord("a"),ord("z") + 1)}
brak_set = {"[","]"}


def decode()

def detect(string, index, m):
    global nums_set, char_set, brak_set
    if index >= m:
        return ("",None)
    
    if string[index] in nums_set:
        return detect_nums(string,index,m)
    elif string[index] in char_set:
        return detect_char(string,index,m)
    elif string[index] in brak_set:
        return detect_brak(string,index,m)

def detect_nums(string, index, m):
    global nums_set
    s1 = ""
    while index < m and string[index] in nums_set :
        s1 += string[index]
        index += 1
    s1 = int(s1)
    s2,i = detect(string,index,m)
    s3 = ""
    if i is not None:
        s3,_ = detect (string,i,m)
    new_string = "".join([s2 for _ in range(s1)]) + s3
    return (new_string, None)

def detect_char(string, index, m):
    global char_set
    s1 = ""
    while index < m and string[index] in char_set:
        s1 += string[index]
        index += 1
    s2,i = detect(string,index,m)
    s3 = ""
    if i is not None:
        s3,_ = detect(string,i,m)
    return (s1 + s2 + s3, None)

def detect_brak(string,index, m):
    if string[index] == "[":
        return detect(string, index + 1, m)
    else:
        return ("",index + 1)

class Solution:
    def decodeString(self, s: str) -> str:
        maximum = len(s)
        result = detect(s, 0, maximum)
        return result

sol = Solution()
res = sol.decodeString("3[a]a2[bc]")
print(res)
