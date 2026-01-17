person_0 = {'name': 'Laveena',
            'hobby': 'chit-chatting', 'location': 'gloucester'}
person_1 = {'name': 'Nikunj', 'hobby': 'Swimming', 'location': 'gloucester'}
person_2 = {'name': 'Joshua', 'hobby': 'coding', 'location': 'bristol'}

people = [person_0, person_1, person_2]
print("Information about some people")
for person in people:
    print(
        f"\t{person['name']}'s hobby is {person['hobby']} and lives in {person['location'].title()}")


pet_0 = {'name': 'Waffle', 'animal': 'dog', 'owners_name': 'Angsingkar\'s'}
pet_1 = {'name': 'Bholu', 'animal': 'tortoise', 'owners_name': 'Tiwari\'s'}
pet_2 = {'name': 'Tiger Shark', 'animal': 'fish', 'owners_name': 'Thakur\'s'}

pets = [pet_0, pet_1, pet_2]
print("\nInformation about pets")
for pet in pets:
    print(f"\t{pet['name']} is a {pet['animal']}. This pet belongs to {pet['owners_name']}")
