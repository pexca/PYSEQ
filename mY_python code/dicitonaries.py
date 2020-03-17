aliens = []

for alienNumber in range(30):
    alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien)
for alien in aliens[:5]:
    print(alien)
print('total number of aliens: ' + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:3]:
    print(alien)

favorite_languages = {
    'zhenya': ['java'],
    'gena':['c++', 'haskell'],
    'alla': ['python', 'english']
}
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are: ")
    for language in languages:
        print('\t' + language.title())