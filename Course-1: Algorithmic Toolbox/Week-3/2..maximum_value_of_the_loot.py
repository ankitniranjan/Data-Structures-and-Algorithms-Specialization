# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    n = len(values)
    lst = []

    if capacity == 0:
        return(0)

    for _ in range(len(values)):
        if values[_] == 0:
            continue
        lst.append((values[_], weights[_]))

    lst.sort(key = lambda x: x[0]/x[1], reverse = True)

    total_value = 0
    for value,weight in lst:
        if capacity==0:
            return(total_value)
        amt = min(weight, capacity)
        total_value += amt*value/weight
        capacity -= amt

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
