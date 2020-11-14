# returns string of possible 2-letter combinations with givenletter + ?
# store possibilities at the cell identified by ( Grid, row, col)
def followWith([row][col]):
    #currentLoopThrough is how far along the alphabet you are in asking is __insertletterhere__ in this cell
    #is next cell able to take this _th loopThrough letter, ie does this 2-letter combination exist?
    possibilitiesforNext = []
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    NonFollows = {
        #can have key be just a letter and value be series of all letters that can't go after it
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
    }
    #only call on a cell that has a letter determined ...
    #"__str__" means to call the converter from the grid class defined as __str__(self).
    # I don't exactly know how to pythonly call __str__ on the cell I'd like
    [row][col].__str__ = initialLetter
    if initialLetter in NonFollows:
        impossibilities = NonFollows[initialLetter]
        possibilitiesForNext = alpha not in NonFollows[initialLetter]
    if initialLetter not in NonFollows:
            impossibilities = None
            possibilitiesForNext = alpha
    return possibilitiesForNext

def indicateErrorFollows(row, col):
    currentBitCount = 0
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    if orientation == horizontal:
        if (col < totalColumns-1):
            while(currentBitCount < 26):
                #if bit in ALPHABET is on (increment until you find a bit that is on)
                #enter next cell 's ALPHABET array
                if [row][col+1].ALPHABET[currentBitCount] == 1:
                    #problemLetter assigned to ABCD... where index of ABC... = currentBitCount
                    #because you incremented across alpha until you found an ON bit
                    problemLetterHorizontal = alpha[currentBitCount]
                    #problem letter is assigned the letter at index corresponding to currentBitCount in alpha
                    #IF problemLetterHorizontal in NonFollows[[row][col].__str__]:
                    #OR
                    if problemLetterHorizontal in FollowWith(row, col).impossibilities:
                    #if a letter you find in the next cell is in the non-existent combinations for the key of the letter locked to interested cell
                        returnvalue += problemLetterHorizontal
                    #if problemLetterHorizontal not in NonFollows[[row][col].__str__]:
                    #don't do anything, just return problem letters
                currentBitCount += 1
            if(returnvalue != None): return returnvalue
            else: return "No error"
        if (col == totalColumns-1):
            return "Nothing can follow horizontally because rightmost column"

    if orientation == vertical:
        if(row < totalRows-1):
            while(currentBitCount <26):
                if[row+1][col].ALPHABET[currentBitCount] ==1:
                    problemLetterVertical = alpha[currentBitCount]:
                        if problemLetterHorizontal in FollowWith(row, col).impossibilities:
                            returnvalue += problemLetterHorizontal
                currentBitCount += 1
            if(returnvalue != None): return returnvalue
            else: return "No error"
        if(row == totalRows-1):
            return "Nothing can follow vertically because lowest row"

#give the possibilities for the cells that under and to the right, store possibilites of row+1, col and row, col+1
#can set nonpossibilities to 0's
#updating grid class with possible combinations
#JK: check if any values that are 100% impossible, eg CX, return false? return that this specific word found causes error, cannot add this word

# returns string of possible 2-letter combinations with ? + givenletter
def precedeWith(row, col):  # pass in a Grid, row # and column # that reprsent the position that you're looking to fill left or up
    possibilitiesForPrevious = []
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
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
    }
    [row][col].__str__ = latterLetter
    if latterLetter in NonPrecedes:
        impossibilities = NonPrecedes[latterLetter]
        possibilitiesForPrevious = alpha not in NonPrecedes[latterLetter]
    if latterLetter not in NonPrecedes:
        impossibilities = None
        possibilitiesForPrevious = alpha
    return possibilitiesForPrevious

def indicateErrorPrecedes(row, col):
    currentBitCount = 0
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    if orientation == horizontal:
        if(col > 0):
            while (currentBitCount < 26):
                # if bit in ALPHABET is on; increment until you find a bit that is on
                # enter previous cell 's ALPHABET array
                if [row][col -1].ALPHABET[currentBitCount] == 1:
                    # problemLetter assigned to ABCD... where index of ABC... = currentBitCount
                    # because you incremented across alpha until you found an ON bit
                    problemLetterHorizontal = alpha[currentBitCount]
                    # problem letter is assigned the letter at index corresponding to currentBitCount in alpha
                    # IF problemLetterHorizontal in NonFollows[[row][col].__str__]:
                    # OR
                    if problemLetterHorizontal in precedeWith(row, col).impossibilities:
                        # if a letter you find in the previous cell is in the non-existent combinations for the key of the letter locked to interested cell
                        returnvalue += problemLetterHorizontal
                    # if problemLetterHorizontal not in NonFollows[[row][col].__str__]:
                    # don't do anything, just return problem letters
                currentBitCount += 1
            if (returnvalue != None):
                return returnvalue
            else:
                return "No error"
        if(col ==0):
            return "Nothing can precede because leftmost column"

    if orientation == vertical:
        if(row >0):
            while (currentBitCount < 26):
                if [row -1][col].ALPHABET[currentBitCount] == 1:
                    problemLetterVertical = alpha[currentBitCount]:
                        if problemLetterVertical in precedeWith(row, col).impossibilities:
                            returnvalue += problemLetterVertical
                currentBitCount += 1
            if (returnvalue != None):
                return returnvalue
            else:
                return "No error"
        if(row ==0):
            return "Nothing can precede because topmost row."