def char_count_while(target: str, c: str) -> int:
    i = 0
    count = 0
    while i < len(target):
        if target[i] == c:
            count += 1 
        i += 1
    return count

def char_count_for(target: str, c: str) -> int:
    count = 0
    for i in range(len(target)):
        if target[i] == c:
            count += 1 
    return count

def char_count_foreach(target: str, c: str) -> int:
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count

def main():
    s = "hello"
    c = "l"

    print(char_count_while(s,c))
    print(char_count_for(s,c))
    print(char_count_foreach(s,c))

main()
