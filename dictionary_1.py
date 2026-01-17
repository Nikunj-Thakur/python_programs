person = {'first_name': 'Laveena',
          'last_name': 'Tiwari', 'age': 25, 'city': 'Pune'}

print(f"Miss {person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")

print("\nThe Keys and Values of this dictrionary are:")
for key, value in person.items():
    print(f"{key} : {value}")

print("\nThe Keys of this dictionary are:")
for key in person.keys():
    print(key)

print("\nThe Values of this dictionary are:")
for value in person.values():
    print(value)