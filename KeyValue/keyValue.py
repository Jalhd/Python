city = { 'name': 'Toronto', 'country': 'Canada', 'monument': 'CN Tower'}

print(city.get('size','Not found'))

city.update({'name': 'Montreal'})

print(city)

print(city.keys())
print(city.items())

country = city.pop('country')

print(country)

for key,values in city.items():
    print(key, values)