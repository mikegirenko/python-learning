def build_profile(first, last, age='', gender='', city=''):
    user_profile = {}
    user_profile['first_name'] = first.title()
    user_profile['last_name'] = last.title()
    user_profile['age'] = age
    user_profile['gender'] = gender
    user_profile['city'] = city.title()
    return user_profile


print(build_profile('mike', 'girenko', age='38', gender='male', city='Denver'))
