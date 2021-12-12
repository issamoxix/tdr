from app import app
from app2 import app1
import sys


def main():
    print('1: High School \n2: College\n3: Primaire\n0: Exit')
    x = int(input(''))
    if x == 1:
        scraping = app()
    elif x == 2:
        scraping = app1(1)
    elif x == 3:
        scraping = app1(0)
    elif x == 0:
        print('Bye !')
        sys.exit()
    else:
        main()


if __name__ == "__main__":
    main()
