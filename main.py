names = ['Jennifer', 'Jack', 'David', 'Daemon']

l = []

for person in names:
  l.append(person)
print(l)

print([person for person in names])

l = []
for person in names:
  l.append(person + 'dumped in.')
print(l)

print([person for person in names])


movies_and_ratings = {'Interstellar': 9, 'Dark Knight': 8, 'Do little': 7, '50 shades': 5, '50 shades darker': 4}

l = []
for movie in movies_and_ratings:
  if movies_and_ratings[movie] > 5:
    l.append(movie)

print(l)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 5])
