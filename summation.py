def summation_while(n):
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    return total

def summation_for(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def main():
    print(summation_while(5))
    print(summation_for(5))

main()
