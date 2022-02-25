import argparse
import os.path
import sys

# contextlib

print(
    """
                                                                                        \n                             -_-/  ,,            /\\   /\\ ,,                             \n        _                   (_ /   ||           ||   ||  ||                             \n\\\\/\\\\  < \\, \\\\/\\\\/\\\\  _-_  (_ --_  ||/\\\\ \\\\ \\\\ =||= =||= ||  _-_  ,._-_    -_-_  \'\\\\/\\\\ \n|| ||  /-|| || || || || \\\\   --_ ) || || || ||  ||   ||  || || \\\\  ||      || \\\\  || ;\' \n|| || (( || || || || ||/    _/  )) || || || ||  ||   ||  || ||/    ||      || ||  ||/   \n\\\\ \\\\  \\/\\\\ \\\\ \\\\ \\\\ \\\\,/  (_-_-   \\\\ |/ \\\\/\\\\  \\\\,  \\\\, \\\\ \\\\,/   \\\\,  <> ||-\'   |/    \n                                     _/                                    |/    (      \n                                                                           \'      -_-   """
)


def nameShuffle(name):
    if "-d":
        name = name.split()  # Split the white spaces
        print(name[0][0] + name[1] + "@" + domain)
        print(name[0][0] + "." + name[1] + "@" + domain)
        print(name[0] + "." + name[1] + "@" + domain)
        print(name[0] + name[1] + "@" + domain)
        print(name[0] + "_" + name[1] + "@" + domain)
        print(name[0] + "-" + name[1] + "@" + domain)
        print(name[0][0] + "-" + name[1] + "@" + domain)
        print(name[0][0] + "_" + name[1] + "@" + domain)
    else:
        name = name.split()  # Split the white spaces
        print(name[0][0] + name[1])
        print(name[0][0] + "." + name[1])
        print(name[0] + "." + name[1])
        print(name[0] + name[1])
        print(name[0] + "_" + name[1])
        print(name[0] + "-" + name[1])
        print(name[0][0] + "-" + name[1])
        print(name[0][0] + "_" + name[1])


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        with open(inputFile, "r") as usersList:  # return an open file handle
            if args.output is not None:
                original_stdout = sys.stdout
                with open(outputFile, "w+") as o:
                    for line in usersList:
                        sys.stdout = o
                        nameShuffle(line)
                        sys.stdout = original_stdout
                        nameShuffle(line)
            else:
                for line in usersList:
                    nameShuffle(line)


parser = argparse.ArgumentParser(
    description="A script to automate usernames pattern shuffling."
)
parser.add_argument("-o", "--output", help="Select output file.")
parser.add_argument("-d", "--domain", help="Select a target domain.")
requiredNamed = parser.add_argument_group("required named arguments")
requiredNamed.add_argument("-f", "--file", help="Select users.txt file.", required=True)
args, leftovers = parser.parse_known_args()
outputFile = args.output
inputFile = args.file
domain = args.domain
is_valid_file(parser, inputFile)
