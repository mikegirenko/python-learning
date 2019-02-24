favorite_languages = {
    'jen': 'python',
    'mike': 'java',
    'tom': 'c',
    'bill': 'python'
}

random_names = ['jen', 'sarah', 'ben', 'sage']

for k, v in favorite_languages.items():
    print(k.title() + "'s favorite language is " + v.title())

for name in random_names:
    if name in favorite_languages.keys():
        print('\nThank you ' + name.title() + ' for taking a poll!')
    else:
        print(name.title() + ', please take a poll ')
