import ply.lex as lex

reserved = {'nil': 'NIL'}

tokens = ['LPAREN',
          'ATOM',
          'INTEGER',
          'RPAREN',
          'COMMENT'] + list(reserved.values())

def lisplexer():
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ignore = ' \t'
    t_ignore_COMMENT = r'\;.*'

    def t_INTEGER(t):
        r'[0-9]+'
        return t

    def t_ATOM(t):
        r'[a-zA-Z_-]+'
        t.type = reserved.get(t.value, 'ATOM')
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    return lex.lex()