t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))

def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    sw, sh, ew, eh = map(int, readl().split())
    map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
    return W, H, sw, sh, ew, eh, map_maze