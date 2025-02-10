def build_profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

me = build_profile('isaac', 'diniz', field='computer engineering', age=19, occupation='college student')
print(me)