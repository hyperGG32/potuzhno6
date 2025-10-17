nums = [int(num) for num in input("Input nums in spaces pls: ").split() if num.isnumeric()]
# appending only valid ones (i think that works)

if not nums:
    print("Error!")
    exit(1)

def get_min(ls):
    mini = ls[0]
    for n in ls:
        if mini > n:
            mini = n
    return mini

def get_max(ls):
    maxi = ls[0]
    for n in ls:
        if maxi < n:
            maxi = n
    return maxi

def get_average(ls):
    return sum(ls)/len(ls)

def get_median(ls):
    ls.sort()

    if len(ls) % 2 == 0:
        return (ls[int(len(ls)/2) - 1] + ls[int(len(ls)/2)])/2
    return ls[int(len(ls)/2)]

print(f"Count: {len(nums)}")
print(f"Min: {get_min(nums)}")
print(f"Max: {get_max(nums)}")
print(f"Average: {get_average(nums)}")
print(f"Median: {get_median(nums)}")