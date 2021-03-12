import os
from lib.start import main
# import pdb; pdb.set_trace()




if __name__ == "__main__":
    os.environ.setdefault('SETTINGS_MODULE', 'lib.settings')
    os.environ.setdefault('BASE_DIR', os.path.dirname(os.path.abspath(__file__)))

    try:
        # main()
        print('a')
    except Exception as e:
        print("Some Error Occured We cant able to analyze this file/program")
        print(e)