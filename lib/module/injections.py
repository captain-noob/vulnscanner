from .variables import getDeclaredVariableswithData, analyseVariables, splitVariableandData
from .SQLquerycheck import sqlQueryValidator,customSQLQueryValidator
import sqlvalidator
import re

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
                sql = customSQLQueryValidator(value['data'])
                query = sqlQueryValidator(value['data'])
                if sql or query:
                    pattern = re.compile(r'prepare\(.*?[\);]')
                    prepare=pattern.findall(value['data'])
                    if len(prepare) < 1:

                        variableptt = re.compile("(\$\w*[A-Za-z0-9_])")
                        print('[*] : Filename : '+self.filename)
                        cour = variableptt.finditer(value['data'])
                        print('[+] : SQL injection might me possible with variables' )
                        for i in cour:
                            print('\t'+i.group())
                        print('[x] : '+data )
                


            