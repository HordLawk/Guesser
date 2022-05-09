from random import Random

class Guess:
    def makeEstimate(self, max, min = 0, trial = 1):
        estimate = min + ((max - min) >> 1)
        print('I guess', estimate)
        answer = input('"lower", "higher", or "right": ')
        if(answer == 'lower'):
            return self.makeEstimate(estimate, min, trial + 1)
        elif(answer == 'higher'):
            return self.makeEstimate(max, estimate + 1, trial + 1)
        elif(answer == 'right'):
            return trial
        else:
            print('Invalid answer')
            exit()
