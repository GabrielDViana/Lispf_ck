import argparse
import ox

# Adding args and description for pyhton3 file call on shell
parser = argparse.ArgumentParser(description='Generate AST for Lispfuck')
parser.add_argument('lfFile')

# Creates a namespace object for the args
ARGUMENTS = parser.parse_args()

# Saves the args (Files) in constants for further use
INPUT_LF = ARGUMENTS.lfFile

# Opening LF file
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

print(lexer(READ_FILE))
