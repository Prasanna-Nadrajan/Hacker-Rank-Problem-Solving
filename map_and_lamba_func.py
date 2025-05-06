cube = lambda x:x**3

def fibonacci(n):
    if n <= 0:
        return [] 
    elif n == 1:
        return [0] 
    
    fib_sequence = [0, 1] 
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence 

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
