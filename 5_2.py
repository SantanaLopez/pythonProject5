food = 'burger'
if 'carrot' in food:
    print('true')
else:
    print('false')

age = 21
if (age <= 20) or (age >= 22):
    print("this equals = 1")
else:
    print('0')

if (age != 22) and (age >= 12):
    print('1')
else:
    print('0')

movies = ['godfather', 'scarface', '1912', 'batman']
film = 'duck'
for movie in movies:
    if movie == 'godfather':
        print(movie.upper())
    else:
        print(movie.lower())

if film not in movies:
    print(film.title() + ', this should be in the hall of fame')