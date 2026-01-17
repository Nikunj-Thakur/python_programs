poll_list=['Nilesh','Neethu','Shivangi','Prakash','Nikunj']

favourite_languages = {
    'Sarah': 'JavaScript',
    'Nikunj': 'Java',
    'Laveena': 'TypeScript',
    'Farhan': 'Python',
    'Venkat': 'Java',
    'Yashwant': 'C',
    'Prakash':'Java'
}

for person in poll_list:
    if person in favourite_languages.keys():
        print(f"Thanks {person.title()} for taking the poll")
    else:
        print(f"{person.title()}, please take the poll.")