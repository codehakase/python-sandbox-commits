# A simple OOP console game
class Wordie(object):
    def __init__(self):
        self.score = 0

    def trace(self):
        print "Welcome to a simple Word guessing game written in \n Python"
        print "=========================================================\
                =========================================="
        words = ['sweet', 'bitter']
        for i in range(1, 1000):
            g1 = raw_input('You take a bite of and an apple, and i ask you the taste: ')
            g2 = raw_input('You take a sip of lemon: ')
            for i in range(1, len(words)):
                if g1 in words and g2 in words:
                    self.score += 20
                    return ('Correct!!!. Your total score for this is %s')%(self.score)
                    trace()
                else:
                    return 'Opps!! you got none fella'

    def main():
        return trace()

a = Wordie()
a.trace()
