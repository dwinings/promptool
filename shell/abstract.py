

class Abstract:
  
  #Note that these are the bash escapes and also the defaults
  prompt_header = 'PS1=\''
  escapes = {
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

                  '(?u)'      : r'', #Username
                  '(?h)'      : r'', #Hostname
                  '(?w)'      : r'', #pwd
                  '(?d)'      : r'', #date
                  '(?H)'      : r'', #full hostname
                  '(?j)'      : r'', #number of jobs managed by shell
                  '(?s)'      : r'', #the name of the shell.
                  '(?t)'      : r'', #current time (24h)
                  '(?@)'      : r'', # time 12h
                  '(?v)'      : r'', # bash version
                  '(?V)'      : r'', # release of bash
                  '(?W)'      : r'', # basename of pwd #POSSIBLY REMOVE
                  '(?!)'      : r'', # history number
                 r'(?#)'      : r'',# command number
                  '(?$)'      : r'', # magic $
                  '(?reset)'  : r''
                }


