from sys import argv
from imageParser import imageParser

def main():
    firstarg = argv[1]
    print(firstarg)
    imageParser(firstarg)

if __name__ == "__main__":
    main()