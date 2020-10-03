# Uses python3
import sys
import unittest

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    if (a < b):
        (a, b) = (b, a)

    while (a % b) != 0:
        (a,b) = (b, a%b)

    return (b)

def lcm_fast(a, b):
    return (a * b) // gcd(a, b)


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(lcm_naive(6, 8), 24)
        self.assertEqual(lcm_naive(28851538, 1183019), 1933053046)

    def test_fast(self):
        self.assertEqual(lcm_fast(6, 8), 24)
        self.assertEqual(lcm_fast(28851538, 1183019), 1933053046)


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
