#!/bin/python3
import argparse
import os.path
import contextlib

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
            if '-o':
                with open(args.output, 'w+') as outputFile:
                    for line in usersList:
                        nameShuffle(line)
                        with contextlib.redirect_stdout(outputFile):
                            nameShuffle(line)
            else:
                for line in usersList:
                    with contextlib.redirect_stdout(outputFile):
                        nameShuffle(line)

parser = argparse.ArgumentParser(description='A script to automate usernames pattern shuffling.')
parser.add_argument("-o", "--output", help="Select output file.")
requiredNamed = parser.add_argument_group('Required arguments')
requiredNamed.add_argument("-f", "--file", help="Select users.txt file.", required=True)
args = parser.parse_args()
outputFile = args.output
inputFile = args.file
is_valid_file(parser, inputFile)
