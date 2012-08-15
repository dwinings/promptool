from abstract import Abstract

class Bash(Abstract):

    prompt_header = r'PS1=\''
    supported_variables = [
                    '(?u)',
                    '(?h)',
                    '(?w)',
                    '(?d)',
                    '(?h)',
                    '(?j)',
                    '(?s)',
                    '(?t)',
                    '(?@)',
                    '(?v)',
                    '(?v)',
                    '(?w)',
                    '(?!)',
                   r'(?#)',
                    '(?$)']

    def __init__(self):
        bash_escapes = {
                    "(?bla)"    : r'\[\e[0;30m\]',
                    "(?red)"    : r'\[\e[0;31m\]',
                    "(?grn)"    : r'\[\e[0;32m\]',
                    "(?ylw)"    : r'\[\e[0;33m\]',
                    "(?blu)"    : r'\[\e[0;34m\]',
                    "(?mgta)"   : r'\[\e[0;35m\]',
                    "(?cyn)"    : r'\[\e[0;36m\]',
                    "(?wht)"    : r'\[\e[0;37m\]',

                    "(?bla_b)"  : r'\[\e[1;30m\]',
                    "(?red_b)"  : r'\[\e[1;31m\]',
                    "(?grn_b)"  : r'\[\e[1;32m\]',
                    "(?ylw_b)"  : r'\[\e[1;33m\]',
                    "(?blu_b)"  : r'\[\e[1;34m\]',
                    "(?mgta_b)" : r'\[\e[1;35m\]',
                    "(?cyn_b)"  : r'\[\e[1;36m\]',
                    "(?wht_b)"  : r'\[\e[1;37m\]',

                    '(?u)'      : r'\u', #username
                    '(?h)'      : r'\h', #hostname
                    '(?w)'      : r'\w', #pwd
                    '(?d)'      : r'\d', #date
                    '(?h)'      : r'\h', #full hostname
                    '(?j)'      : r'\j', #number of jobs managed by shell
                    '(?s)'      : r'\s', #the name of the shell.
                    '(?t)'      : r'\t', #current time (24h)
                    '(?@)'      : r'\@', # time 12h
                    '(?v)'      : r'\v', # bash version
                    '(?v)'      : r'\v', # release of bash
                    '(?w)'      : r'\w', # basename of pwd #possibly remove
                    '(?!)'      : r'\!', # history number
                   r'(?#)'      : r'\#',# command number
                    '(?$)'      : r'\$', # magic $
                    '(?reset)'  : r'\e[0m'
                  }
        self.escapes.update(bash_escapes)

