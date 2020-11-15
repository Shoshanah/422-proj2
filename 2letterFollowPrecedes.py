#followWith:
# if no letters can not-come after argument-letter, then returns "all letters possible"
# if at least one letter cannot come after argument letter, then returns string of letters not possible, plus "are not possible"
def followWith(letter):
    #is next cell able to take this _th loopThrough letter, ie does this 2-letter combination exist?
    NonFollows = {
        'B': "QX",
        'C': "FJVX",
        'D': "X",
        'F': "QXZ",
        'G': "QX",
        'H': "X",
        'J': "BCFGQVXZ",
        'K': "QZ",
        'P': "QX",
        'Q': "CDGHJKLMNPQRVXYZ",
        'S': "X",
        'T': "X",
        'V': "BCFJMPQTWX",
        'W': "QX",
        'X': "DJXZ",
        'Z': "JX",
        #total: 61
        #Letters that are not keys are A, E, I, L, M, N, O, R, U,Y. So AEILMNORUY can take any letter
    }

    initialLetter = letter.upper()
    if initialLetter in NonFollows:
        returnValue = NonFollows.get(initialLetter) + " Not Possible to follow"
    if initialLetter not in NonFollows:
        returnValue = "All letters possible to follow"
    return returnValue
#precedeWith:
#if no letters can not-come before argument-letter, then returns "all letters possible"
#if at least one letter cannot precede argument-letter, then returns string of those letters that cannot precede plus "are not possible"
def precedeWith(letter):  # pass in a Grid, row # and column # that reprsent the position that you're looking to fill left or up
    NonPrecedes = {
        'B': "JV",
        'C': "JQV",
        'D': "QX",
        'F': "CJV",
        'G': "JQ",
        'H': "Q",
        'J': "CQVXZ",
        'K': "Q",
        'L': "Q",
        'M': "QV",
        'N': "Q",
        'P': "QV",
        'Q': "BFGJKPQVW",
        'R': "Q",
        'T': "V",
        'V': "CJQ",
        'W': "V",
        'X': "BCDFGHJPQSTVWXZ",
        'Y': "Q",
        'Z': "FJKQX"
        #total: 61
        #letters not keys are AEIOSU
    }
    latterLetter = letter.upper()
    if latterLetter in NonPrecedes:
        returnValue = NonPrecedes.get(latterLetter) + " Not Possible to precede"
    if latterLetter not in NonPrecedes:
        returnValue = "All letters may precede"
    return returnValue
