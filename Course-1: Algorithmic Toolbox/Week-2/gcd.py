# Uses python3
import sys
import unittest

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    if (a < b):
        (a, b) = (b, a)

    while (a % b) != 0:
        (a,b) = (b, a%b)

    return (b)

class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(gcd_naive(18, 35), 1)
        self.assertEqual(gcd_naive(28851538, 1183019), 17657)

    def test_fast(self):
        self.assertEqual(gcd_fast(18, 35), 1)
        self.assertEqual(gcd_fast(28851538,  1183019), 17657)

if __name__ == '__main__':
    # unittest.main()

    # while True:
    #     a = random.randint(1, 10000)
    #     b = random.randint(2, 10000)
    #
    #     res1 = gcd_naive(a, b)
    #     res2 = gcd_naive(a, b)
    #
    #     if res1 != res2:
    #         print('Wrong Answer: {} {}'.format(res1, res2))
    #         break
    #     else:
    #         print('OK: {} {}'.format(res1, res2))

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
