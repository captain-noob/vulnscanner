import re


def removeunwanted(data):
    balcklist =[
    '.',"'",'"','{',"}",',','+','-','>','<',';','(',')','!',
    ]
    for elem in balcklist:
        if elem =='"' or elem == "'":
            if ('['  in data) and (']'  in data):
                continue
        if elem  in data :
            return(data)



def getDeclaredVariableswithData(content):
    #get declared variables in file;
    ret_data=[]
    for code in content:
        variable_pattern = re.compile(r'(\$.*?[;\{])',re.DOTALL)
        value = variable_pattern.finditer(code)
        for match in value:
            data=match.group(0)
            if data: #data has value
                variable =data.split('=')
                if len(variable)>0: #get all splited variables
                    variable = variable[0] #first element is variable
                    if '$' in variable[0]: #first letter start from $
                        space = variable.split() #split by space
                        space = [elem for elem in space if elem.strip()] #remove empty or space elements
                        if len(space) == 1:  # space length <1 or >1 will be contains spaces
                            val = removeunwanted(space[0]) #remove blacklit items
                            if not val: #no data while return
                                # print(data) #print variable with data
                                ret_data.append(data)

    return ret_data


def analyseVariables(variables):
    resp_data=[]
    for data in variables:
        if "{" in data[-1]:
            value = data.split('=')
            if len(value) ==2 :
                resp_data.append(data)
        else:
            resp_data.append(data)
    
    return resp_data



def splitVariableandData(data):
    # for data in variables:
    data = data.split('=',1)
    if len(data) == 2 :
        value={}
        value['variable'] = data[0].replace('$','')
        value['data'] = data[1].replace('"','').replace("'",'').replace(';','')
        return value
