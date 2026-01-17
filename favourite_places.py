favourite_places = {
    'Nikunj': ['Como', 'Wengen', 'Mallorca', 'Monaco'],
    'Laveena': ['Pune', 'Indore', 'Ratlam'],
    'Steve': ['Dubrovnik', 'Ibiza', 'Santorini'],
}
for name,places in favourite_places.items():
    print(f"\n{name}'s favourite places are:")
    for place in places:
        print(place)