from abstract import Abstract

class Zsh(Abstract):

    prompt_header = 'PS1=$\''

    def __init__(self):
        zsh_escapes = {
                    "(?bla)"    : r'\e[0;30m',
                    "(?red)"    : r'\e[0;31m',
                    "(?grn)"    : r'\e[0;32m',
                    "(?ylw)"    : r'\e[0;33m',
                    "(?blu)"    : r'\e[0;34m',
                    "(?mgta)"   : r'\e[0;35m',
                    "(?cyn)"    : r'\e[0;36m',
                    "(?wht)"    : r'\e[0;37m',
        
                    "(?bla_b)"  : r'\e[1;30m',
                    "(?red_b)"  : r'\e[1;31m',
                    "(?grn_b)"  : r'\e[1;32m',
                    "(?ylw_b)"  : r'\e[1;33m',
                    "(?blu_b)"  : r'\e[1;34m',
                    "(?mgta_b)" : r'\e[1;35m',
                    "(?cyn_b)"  : r'\e[1;36m',
                    "(?wht_b)"  : r'\e[1;37m',
                    '(?u)'      : r'%n',
                    '(?h)'      : r'%m',
                    '(?w)'      : r'%~',
                    '(?d)'      : r'%T',
                    '(?H)'      : r'%M',
                    '(?W)'      : r'%d',
                    '(?!)'      : r'%!',
                   r'(?#)'      : r'', #Needs research
                    '(?$)'      : r'%#',
                    '(?reset)'  : r'\e[0m'}

        self.escapes.update(zsh_escapes)
