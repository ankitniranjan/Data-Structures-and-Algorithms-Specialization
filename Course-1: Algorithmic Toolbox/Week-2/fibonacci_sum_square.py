#Uses python3

def fibonacci_sum(n):
    if n <= 1:
        return(n)

    previous = 0
    current = 1
    sum = 1

    for _ in range(n-1):
        (previous, current) = (current, previous + current)
        sum += current * current

    return(sum % 10)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    # n, m = map(int, input.split())
    print(get_fibonacci_huge(n,m))
