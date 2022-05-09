from guess import Guess

try:
    N = int(input('Max: '))
except ValueError:
    print('Value must be a number')
    exit()
guesser = Guess()
trial = guesser.makeEstimate(N)
print('Guessed in', trial, 'tries')