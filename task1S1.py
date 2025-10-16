# T1
# S1
t_in_c = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]

print("Celsius | Fahrenheit")
print("------- | -----------")
for t in t_in_c:
    print(f"{t:<7} | {t*9/5 + 32:<10}")