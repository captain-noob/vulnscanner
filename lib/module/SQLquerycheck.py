import sqlite3
from .loadConfig import getQuery





def sqlQueryValidator(query):
    temp_db = sqlite3.connect(":memory:")
    try:
        temp_db.execute(query)
        return True
    except Exception as e:
        if "syntax error" in str(e):
            return False
        if "unrecognized token" in str(e):
            return False   
        else:
            return True


def customSQLQueryValidator(query):
    sql = getQuery('sql')
    query = query.lower().split()
    i=0
    for statements in sql:
        if statements.lower() in query:
            i+=1
    
    if i>1:
        return True
    else:
        return False