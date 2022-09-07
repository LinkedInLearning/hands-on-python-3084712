NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

indext = 0
while indext < len(NAMES):
    print(NAMES[indext], AGES[indext])
    indext += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

