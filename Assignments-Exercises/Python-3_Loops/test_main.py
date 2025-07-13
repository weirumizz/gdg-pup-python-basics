#list of favorite foods
foods = ['ramen', 'halo-halo', 'chicken', 'adobo', 'ice cream']

print("My favorite foods are:")
for food in foods:
    print(food)  # print list

print("\n--- Countdown Timer ---")
try:
    num = input("Enter a positive integer to start: ")
    start_num = int(num)

    if start_num <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        while start_num >= 0:
            print(start_num)
            start_num -= 1
        print("Countdown complete!")

except ValueError:
    print("Invalid input: Please enter a positive integer.")