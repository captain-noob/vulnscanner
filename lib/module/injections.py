from .variables import getDeclaredVariableswithData, analyseVariables, splitVariableandData
from .SQLquerycheck import sqlQueryValidator
# import sqlvalidator
import sqlparse

class Injection:
    def __init__(self,filename,content):
        self.filename = filename
        self.content = content

    def sqlInjection(self):
        variables = getDeclaredVariableswithData(self.content) #getting declared variables
        variables = analyseVariables(variables) # verifing the extracted data
        for data in variables:
            value = splitVariableandData(data) #spliting the variable and data
            if len(value['data']) > 1:

                # query = sqlparse.parse(value['data'])
                print(value['data'])

                # sql = sqlvalidator.parse(value['data'])
                query = sqlQueryValidator(value['data'])
                # if   sql.is_valid():
                #     print('valid : '+data)
                # else:
                #     print('Error : '+data)


            