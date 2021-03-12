from .variables import getDeclaredVariableswithData

class Injection:
    def __init__(self,filename,content):
        self.filename = filename
        self.content = content

    def sqlInjection(self):
        variables = getDeclaredVariableswithData(self.content)
        for i in variables:
            print(i) #till get variables