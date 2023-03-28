

#------------------password generator-----------------------------
#--------------------------------- Jaycode8 -----------------------------


import random
from validate_email import validate_email
class RandomPasswordGenerator:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def setInputs(self):
        print('*'*105)
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\tPROVIDE YOUR DETAILS TO PROCEED\t\t\t\t\t*')
        self.name = input('*\t\t\t\tEnter your user name \t')
        self.email = input('*\t\t\t\tEnter your email Address \t')
        passw = int(input('*\t\t\t\t1 : Generate password\n*\t\t\t\t2 : Use custom password\n*\t\t\t\t'))
        if passw == 1:
            self.password = self.generator()
        else:
            self.password = input('*\t\t\t\tEnter your password \t')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*'*105)

    def generator(self):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '0123456789'
        all = lower + upper + number
        return ''.join(random.sample(all, 10))
    
    def valide_inputs(self):
        is_valid = validate_email(self.email)
        if is_valid == True:
            if len(self.password)!=10:
                print('password is weak')
                res = eval(input('1: Proceed anyway\n2: Back to Regestration\n'))
                if int(res) == 1:
                    self.display()
                else:
                    print()
                    self.setInputs()
            else:
                self.display()
        else:
            print('invalid email address')
            res = eval(input('1: Terminate Regestration\n2: Back to Regestration\n'))
            if int(res) == 1:
                print('Byee...')
            else:
                print()
                self.setInputs()

    def display(self):
        print('*'*105)
        print('*\t\t\t\t\t\tKIWALIRO TEA SACCO\t\t\t\t\t*')
        print('*\t\t\t\t\tWelcome member\t\t\t\t\t\t\t*')
        print('\t\t\t\tName ',self.name)
        print('\t\t\t\tEmail ',self.email)
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\t\t©jaycode8\t\t\t\t\t\t*')
        print('*'*105)

rpg = RandomPasswordGenerator(name='', email='', password='')
rpg.setInputs()
rpg.valide_inputs()