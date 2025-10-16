nums = [int(num) if num.isnumeric() else exit(1) for num in input("Input nums in spaces pls: ").split()]

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
    count = {}
    for n in ls:
        count[n] = count.get(n, 0) + 1
    maxcount = get_max(list(count.values()))
    max_list = [x[0] for x in count.items() if x[1] == maxcount]
    return get_average(max_list)

print(f"Count: {len(nums)}")
print(f"Min: {get_min(nums)}")
print(f"Max: {get_max(nums)}")
print(f"Average: {get_average(nums)}")
print(f"Median: {get_median(nums)}")