import argparse
import os.path

def nameShuffle (name):
    name = name.split() # Split the white spaces
    print(name[0][0]+name[1])
    print(name[0][0]+'.'+name[1])
    print(name[0]+'.'+name[1])
    print(name[0]+name[1])
    print(name[0]+'_'+name[1])
    print(name[0]+'-'+name[1])
    print(name[0][0]+'-'+name[1])
    print(name[0][0]+'_'+name[1])

def is_valid_file(parser, arg): 
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        with open(inputFile, 'r') as usersList: # return an open file handle
            for line in usersList:
                nameShuffle(line)

parser = argparse.ArgumentParser(description='A script to automate usernames pattern shuffling.')
parser.add_argument("-o", "--output", help="Select output file.")
parser.add_argument("-f", "--file", help="Select users.txt file.", required=True)
args = parser.parse_args()
outputFile = args.output
inputFile = args.file
is_valid_file(parser, inputFile)
