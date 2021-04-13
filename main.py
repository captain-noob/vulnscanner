import os , time ,sys
import argparse
from lib.start import fileRunner , runner
# import pdb; pdb.set_trace()



def begin():
    start = time.perf_counter() # timer start.

    description ='''
    This is the vuln scanner 
    '''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f','--file',help='Analize with a file')
    parser.add_argument('-F','--folder',help='Analize file with in a folder')
    args = parser.parse_args() #read args

    if args.file:
        fileRunner(args.file)
    elif args.folder:
        runner(args.folder)
    else:
        parser.print_help()
        sys.exit()
    

    end = time.perf_counter()
    fin = str(round(end-start,2))
    print(f'Finished in '+ fin + ' second(s)')



if __name__ == "__main__":
    os.environ.setdefault('SETTINGS_MODULE', 'lib.settings')
    os.environ.setdefault('BASE_DIR', os.path.dirname(os.path.abspath(__file__)))
    try:
        begin()
    except Exception as e:
        print("Some Error Occured We cant able to analyze this file/program")
        print(e)