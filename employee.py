__author__ = 'Luke'
from ss import *

class Slave:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if (last is None) and (first is None) and (start is None) and (pay_rate is None) and (social is None):
            self.last=input("enter last name").capitalize()
            self.first=input("enter first name").capitalize()
            self.start=input("enter start")
            self.pay_rate=input("enter pay rate")
            self.social=SS()
        else:
            self.first = first
            self.last = last
            self.start = start
            self.pay_rate = pay_rate
            self.social = SS(social)

    def __str__(self):
        return "Last Name " +self.last + "\nFirst Name "+self.first+"\nStart "+self.start+\
               "\nPay Rate "+self.pay_rate+"\nSocial "+self.social+"\nEnd of Printout"
