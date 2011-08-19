def index_all(text, sub, start, finish):
    l = []
    #print text[start:finish], sub
    text = text[start:finish]
    i = text.find(sub)
    while i > -1:
        l.append(i)
        i = text.find(sub, i+1)
    #print l
    return l


def make_prompt(string):
    color_escapes = {
                ("(?bla)"  , "(?norm)") : r'\[\033[0;30m\]',
                ("(?red)"    , "(?norm)") : r'\[\033[0;31m\]',
                ("(?grn)"  , "(?norm)") : r'\[\033[0;32m\]',
                ("(?ylw)" , "(?norm)") : r'\[\033[0;33m\]',
                ("(?blu)"   , "(?norm)") : r'\[\033[0;34m\]',
                ("(?mgta)", "(?norm)") : r'\[\033[0;35m\]',
                ("(?cyn)"   , "(?norm)") : r'\[\033[0;36m\]',
                ("(?wht)"  , "(?norm)") : r'\[\033[0;37m\]',

                ("(?bla)"  , "(?bold)") : r'\[\033[1;30m\]',
                ("(?red)"    , "(?bold)") : r'\[\033[1;31m\]',
                ("(?grn)"  , "(?bold)") : r'\[\033[1;32m\]',
                ("(?ylw)" , "(?bold)") : r'\[\033[1;33m\]',
                ("(?blu)"   , "(?bold)") : r'\[\033[1;34m\]',
                ("(?mgta)", "(?bold)") : r'\[\033[1;35m\]',
                ("(?cyn)"   , "(?bold)") : r'\[\033[1;36m\]',
                ("(?wht)"  , "(?bold)") : r'\[\033[1;37m\]' }

    special_escapes = {
            '(?u)' : r'\u',
            '(?h)' : r'\h',
            '(?ds)': r'\w'}

    colors = {'(?bla)', '(?red)', '(?grn)', '(?ylw)', '(?blu)', '(?mgta)', '(?cyn)', '(?wht)'}
    formats = {'(?bold)', '(?norm)'}
    specials = {'(?u)', '(?h)', '(?ds)'}
    current_color = '(?bla)'
    current_style = '(?norm)'
    text_left = True
    itr = enumerate(list(string))
    output = ['PS1="']
    while text_left:
        char = itr.next()
        if char[1] == "(":
            if string[char[0]+1] == "?":
                symbol = ['(']
                while char[1] != ')':
                    try:
                        char = itr.next()
                        symbol.append(char[1])
                    except:
                        print "Unclosed paren, aborting... :("
                        return
                symbol = ''.join(symbol)
                if symbol in colors:
                    current_color = symbol
                    output.append(color_escapes[(current_color, current_style)])
                elif symbol in specials:
                    output.append(special_escapes[symbol])
                elif symbol in formats:
                    current_style = symbol
                    output.append(color_escapes[(current_color, current_style)])

                else:
                    print "Valid symbol not defined, printing plaintext"
                    output.append(symbol)
        else:
            output.append(char[1])

        if len(string)-1 <= char[0]:
            text_left = False

    output.append('"')
    print "Here's your prompt command!\nJust put it into your ~/.*rc file!\n\n", ''.join(output)


