def reverse_while(s: str)-> str:
    new_str = ""
    i = 0
    while i < len(s):
        new_str += s[-i-1]
        i += 1
    return new_str

def reverse_for(s: str)-> str:
    new_str = ""
    for i in range(len(s)):
        new_str += s[-i-1]
    return new_str

def reverse_foreach(s: str)-> str:
    new_str = ""
    for char in s:
        new_str = char + new_str 
    return new_str


def main():
    s = "hello world"

    print(reverse_while(s))
    print(reverse_for(s))
    print(reverse_foreach(s))

main()
