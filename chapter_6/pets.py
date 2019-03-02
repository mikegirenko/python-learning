tootsie = {'animal_type': 'dog', 'owner': 'mike'}
boots = {'animal_type': 'cat', 'owner': 'eric'}
babu = {'animal_type': 'turtle', 'owner': 'unknown'}

pets = [tootsie, boots, babu]
print('The number of pets is ' + str(len(pets)))
for pet in pets:
    for k, v in pet.items():
        print(str(k) + ' : ' + str(v))
    print(" ")
