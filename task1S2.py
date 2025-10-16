def c_to_f(celsius):
    return celsius*9/5 + 32

def f_to_c(fahrenheit):
    return 5/9*(fahrenheit-32)

t_in_c = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]

print("Celsius | Fahrenheit")
print("------- | -----------")
for t in t_in_c:
    print(f"{t:<7} | {c_to_f(t):<10}")