import sys
from src.u1act1 import signals1
from src.u1act2 import signals2
from src.u1act3 import signals3

def main(options):
    if options[1] == "u1act1":
        signals1()
    elif options[1] == "u1act2":
        if len(options) > 2:
            signals2(options[2])
        else:
            print("Please give a frequency. Example: python main.py u1act2 freq")
    elif options[1] == "u1act3":
        if len(options) > 4:
            signals3(options[2], options[3], options[4])
        else:
            print("Please give amplitude, frequency and phase. Example: python main.py u1act3 amp freq phas")
    else:
        print("Invalid option. Use 'u1act1', 'u1act2', 'u1act3', etc.")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example (run unit 1 - activity 1 ): python main.py u1act1")
        print("Example (run unit 1 - activity 2 ): python main.py u1act2 2")
        print("Example (run unit 1 - activity 3 ): python main.py u1act3 1 2 0.7854")
