def method4():
    noPrime = [False] * (MAX + 1)
    noPrime[0] = True
    noPrime[1] = True
    for i in range(2, int(math.sqrt(MAX + 1))):
        if not noPrime[i]:
            j = i * i
            while j <= MAX:
                noPrime[j] = True
                if Graph[j] == 1:
                    Graph[j] = j // i   # next node
                j += i