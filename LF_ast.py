import argparse

# Adding args and description for pyhton3 file call on shell
parser = argparse.ArgumentParser(description='Generate AST for Lispfuck')
parser.add_argument('lfFile')
parser.add_argument('-o')

# Creates a namespace object for the args
ARGUMENTS = parser.parse_args()

# Saves the args (Files) in constants for further use
INPUT_LF = ARGUMENTS.lfFile
OUTPUT_TXT = ARGUMENTS.o
