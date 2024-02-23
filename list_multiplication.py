def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    total = []
    i = 0
    while i < len(a):
        total.append(a[i]*b[i])
        i += 1
    return total
    
def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    total = []
    for i in range(len(a)):
        total.append(a[i]*b[i])
    return total
    
def list_multiply_foreach(a: list[int], b: list[int]) -> list[int]:
    total = []
    for num1, num2 in zip(a, b):
        total.append(num1*num2)
    return total

def main():
    a = [1, 2, 3]
    b = [4, 5, 6]

    print(list_multiply_while(a, b))
    print(list_multiply_for(a, b))
    print(list_multiply_foreach(a, b))

main()

