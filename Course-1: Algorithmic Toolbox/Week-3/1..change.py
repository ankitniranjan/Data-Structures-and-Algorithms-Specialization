# Uses python3
import sys

def get_change(m):
    #write your code here
    # 10 5 1 # 28
    n10 = m // 10
    m = m - (10 * n10)
    n5 = m // 5
    m = m - (5 * n5)
    n1 = m

    return (n10 + n5 + n1)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
