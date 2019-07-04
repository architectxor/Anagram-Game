import random

WORDS = ('evolution', 'speedometer', 'dexterity', 'disease', 'enjoy', 'headphones', 'gamepad', 'environment')
word = random.choice(WORDS)
correct = word
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(jumble)

suggest = input('Type your guess here --->  ')

while suggest != correct and suggest != '':
    print('Sorry, but you\'re wrong.\n Please try again')
    suggest = input('Type your guess here --->  ')
print('You\'re right! \nCongratulations!')
input('Press "Enter" to quit...')
