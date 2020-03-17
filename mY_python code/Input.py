prompt = 'Type some city you\'d like to go to'
prompt += '\n(type "quit" once finished)'

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("i'd like to go to: " + city.title())
