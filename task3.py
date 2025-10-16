ls = [int(n) for n in input("2 nums pls in spaces: ").strip().split() if n.isnumeric()]
ls.sort()

def is_prime(n):
    for d in range(2, int(n ** 0.5 + 1)): # математіка
        if n % d == 0:
            return False
    return True

def list_primes(start, end):
    lsofprimes = []
    lsofgap = []
    for n in range(start, end+1):
        if is_prime(n):
            lsofprimes.append(n)

    for i in range(1, len(lsofprimes)):
        lsofgap.append(lsofprimes[i] - lsofprimes[i-1])

    return lsofprimes, len(lsofprimes), sum(lsofgap)/len(lsofgap)

result = list_primes(ls[0], ls[1])

print(f"Range: {ls[0]}-{ls[1]}")
print(f"Primes: {result[0]}")
print(f"Count: {result[1]}")
print(f"Average gap: {result[2]}")