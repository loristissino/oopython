import os
def clearscreen():
    commands={
        'posix':'clear',
        'nt':'cls',
        }
    try:
        os.system(commands[os.name])
    except Exception as err:
        print(err)
        
    

