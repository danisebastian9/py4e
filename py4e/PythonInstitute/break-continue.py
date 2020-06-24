# break - example

print("The break instruction:")
for i in range(1, 7):
    if i == 4:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 7):
    if i == 4:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
