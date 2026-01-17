favourite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 3.14,
    'Diana': 23,
    'Eve': 11,
    'Shikhar': 71,
    'Mehul': 49,
}

# print(f"Alice's favourite number is {favourite_numbers['Alice']}.")
# print(f"Bob's favourite number is {favourite_numbers['Bob']}.")
# print(f"Charlie's favourite number is {favourite_numbers['Charlie']}.")
# print(f"Diana's favourite number is {favourite_numbers['Diana']}.")
# print(f"Eve's favourite number is {favourite_numbers['Eve']}.")

my_friends = ['Shikhar', 'Mehul']

print("People and their favourite numbers")
print("-"*40)
for name, number in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is {number}")
    if name in my_friends:
        print(f"\t{name.title()}, I see your favourite number is {number}")

if 'Enzo' not in favourite_numbers.keys():
    print("Hey Enzo, please take the poll.")
