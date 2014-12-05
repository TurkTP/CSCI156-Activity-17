__author__ = 'Luke'
class InvalidSocial():
        pass
class SS:
    class InvalidSocial(ValueError):
        pass

    def __init__(self, ss=None):
        if ss is None:
            self.getss()
        else:
            self.ss=ss
    def __str__(self):
        return self.ss

    def validatess(self):
        if self.ss.strip('-') is True:
            return self.ss
        else:
            raise self.InvalidSocial('Invalid Social')

    def getss(self):
        self.ss = input("Social: ")
        try:
            self.validatess()
        except InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getss()


