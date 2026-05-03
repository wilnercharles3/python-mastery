contact ="Contact: john.smith@example.com or call (415) 555-2671 between 9am-5pm."
email=None
for word in contact.split(" "):
    if word.endswith(".com"):
        email=word
print(f'Email: {email}')

        
