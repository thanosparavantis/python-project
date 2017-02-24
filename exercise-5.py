harshad = []

for i in range(1, 1001):
    digitsum = sum(map(int, str(i)))
    if i % digitsum == 0:
        harshad.append(i)

print "Harshad:"
print ", ".join(map(str, harshad))

other = []

for i in range(1, 1001):
    digits = map(int, str(i))
    total = 1
    for j in range(0, len(digits)):
        total *= digits[j]
    if total != 0 and i % total == 0:
        other.append(i)

print "\nProduct:"
print ", ".join(map(str, other))
