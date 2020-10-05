# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    numrefill, currentrefill = 0 ,0
    stops = [0] + stops + [distance]    #include the start and end points in the stops list
    if distance <= tank:
        return 0
    else:
        while currentrefill < len(stops)-1:
            lastrefill = currentrefill

            while currentrefill < len(stops)-1 and stops[currentrefill+1] - stops[lastrefill]<=tank:
                currentrefill += 1

            if currentrefill == lastrefill:
                return -1
            if currentrefill < len(stops)-1:
                numrefill +=1

        return numrefill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
