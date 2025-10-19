nums = [int(num) for num in input("Input nums in spaces pls: ").split() if num.isdecimal()]
# appending only valid ones (i think that works)

if not nums:
    print("Error!")
    exit(1)

def get_min(ls: list[int | float]) -> int | float:
    """Returns the smallest element in the list"""
    mini = ls[0]
    for n in ls:
        if mini > n:
            mini = n
    return mini

def get_max(ls: list[int | float]) -> int | float:
    """Returns the biggest element in the list"""
    maxi = ls[0]
    for n in ls:
        if maxi < n:
            maxi = n
    return maxi

def get_average(ls: list[int | float]) -> float:
    """Returns average of all elements in the list"""
    return sum(ls)/len(ls)

def get_median(ls: list[int | float]) -> float | int:
    """Returns the mid-element in the list"""
    ls.sort()

    if len(ls) % 2 == 0:
        return (ls[int(len(ls)/2) - 1] + ls[int(len(ls)/2)])/2
    return ls[int(len(ls)/2)]

print(f"Count: {len(nums)}")
print(f"Min: {get_min(nums)}")
print(f"Max: {get_max(nums)}")
print(f"Average: {get_average(nums)}")
print(f"Median: {get_median(nums)}")