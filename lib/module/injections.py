from .variables import getDeclaredVariableswithData, analyseVariables, splitVariableandData
from .SQLquerycheck import sqlQueryValidator,customSQLQueryValidator
import sqlvalidator
import re

class Injection:
    def __init__(self,filename,content):
        self.filename = filename
        self.content = content

    def sqlInjection(self): ##tobe reedit
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

                        variableptt = re.compile(r"(\$\w*[A-Za-z0-9_\]\[])")
                        cour = variableptt.finditer(value['data'])
                        param =[]
                        for i in cour:                            
                            param.append(i.group())
                        if len(param)>0:
                            print('[+] : SQL injection might me possible \t - Severity : High' )
                            print('\tFile : '+self.filename)
                            print('\tCode : '+data )
                            for i in param:
                                print('\tParam : '+i)
                            
                            print('\tFix : Use PDO insted of direct SQL execution')
                            print('\tReffer : https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#escaping-sqli-in-php')
                            print('\n')
                        else:
                            print('[+] : SQL injection might me possible \t - Severity : Low' )
                            print('\tFile : '+self.filename)
                            print('\tCode : '+data )
                            print('\tFix : Use PDO insted of direct SQL execution')
                            print('\tReffer : https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#escaping-sqli-in-php')
                            print('\n')



    def commandInjection(self):
        print(self.content)
        variable_pattern = re.compile(r'(\$.*?[;\{])',re.DOTALL)
        value = variable_pattern.search(str(self.content))
        print(value)
        exit()   
        # variables = getDeclaredVariableswithData(self.content) #getting declared variables
        # # variables = analyseVariables(variables) # verifing the extracted data
        # for variable in variables:
        #     print(variable)  


            