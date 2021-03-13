import sqlite3





def sqlQueryValidator(query):
    temp_db = sqlite3.connect(":memory:")
    try:
        temp_db.execute(query)
        return True;
    except Exception as e:
        print(e)
        input()
        if "syntax error" in str(e):
            return False
        if "unrecognized token" in str(e):
            return False   
        else:
            return True