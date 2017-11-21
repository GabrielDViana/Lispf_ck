import argparse
import pprint

import ox

# Adding args and description for pyhton3 file call on shell
parser = argparse.ArgumentParser(description='Generate AST for Lispfuck')
parser.add_argument('lfFile')

# Creates a namespace object for the args
ARGUMENTS = parser.parse_args()

# Saves the args (Files) in constants for further use
INPUT_LF = ARGUMENTS.lfFile

# File manipulation
FILE_LF = open(INPUT_LF, 'r')
READ_FILE = FILE_LF.read()
FILE_LF.close()

# Lexer rules used for lispfuck
lexer_rules = [
    ('OPEN_PAR', r'\('),
    ('CLOSE_PAR', r'\)'),
    ('NUMBER', r'\d+'),
    ('COMMENT', r';[^\n]*'),
    ('KEYWORD', r'[-\w]+'),
    ('WHITESPACE', r'\s+')
]

tokens_simple = ['OPEN_PAR', 'CLOSE_PAR', 'NUMBER', 'KEYWORD']

# Generating initial
_lexer = ox.make_lexer(lexer_rules)

# This function removes WHITESPACE and COMMENT from original token list
def lexer(src):
    return [tk for tk in _lexer(src) if tk.type not in ('WHITESPACE', 'COMMENT') ]

# Generates the token list by reading the file
TOKEN_LIST = lexer(READ_FILE)
print("\nToken list:\n" + str(TOKEN_LIST) + "\n")

# Parser rules to be applied in token_list
parser_rules = [
    ('expr : OPEN_PAR CLOSE_PAR', lambda x,y: '()'),
    ('expr : OPEN_PAR term CLOSE_PAR', lambda x,y,z: y),
    ('term : atom term', lambda x,y: (x,) + y),
    ('term : atom', lambda x: (x,)),
    ('atom : expr', lambda x: x),
    ('atom : NUMBER', lambda x: x),
    ('atom : KEYWORD', lambda x: x)
]

# Generates a valid parser
parser = ox.make_parser(parser_rules, tokens_simple)

# Generates the final AST
FINAL_AST = parser(TOKEN_LIST)

print('\nGenerated AST:')
pprint.pprint(FINAL_AST)
