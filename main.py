import sys
from src.generator import Generator
from src.lexer.error import UnclosedEnvironmentError

extension = "inj"

if (__name__ == '__main__'):
    try:
        Generator.generates(sys.argv[1]) # file path
    except IndexError as e:
        print("Haven't you forgot to specify a '."+extension+"' file ?")
    except UnclosedEnvironmentError as e:
        print("Are you sure that you have closed all your python environments ?")
    except Exception as e:
        print("Well... Something really unexpected happened.")
        print("Hint : "+str(e))
