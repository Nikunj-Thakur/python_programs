favourite_languages = {
    'Sarah': 'JavaScript',
    'Nikunj': 'Java',
    'Laveena': 'TypeScript',
    'Farhan': 'Python',
    'Venkat': 'Java',
    'Yashwant': 'C',
    'Prakash':'Java'
}

print("\nThis can give repeated values as duplicate values are allowed in dictionary")
for language in favourite_languages.values(): 
    print (language.title())

print("\nThis will give unique values as we are converting the values to a set")
for language in set(favourite_languages.values()):
    print (language.title())