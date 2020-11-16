# returns string of possible 2-letter combinations with givenletter + X
def setValue(letter):
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
        'Z': "JX"
        #total: 61
        #Letters that are not keys in this are A, E, I, L, M, N, O, R, U,Y. So AEILMNORUY can take any letter
    }
    #only call on a cell that has a letter determined ...
    #"__str__" means to call the converter from the grid class defined as __str__(self).
    #[row][col].__str__ = initialLetter
    initialLetter = letter.upper()
    if initialLetter in NonFollows:
        shutOff = NonFollows.get(initialLetter)
        returnValue = shutOff
    if initialLetter not in NonFollows:
        doNothing = "All letters possible to follow"
        returnValue = doNothing

    for letter in NonFollows.get('B'):
        print(letter)
        # ALPHABET[letter] = 1




"""
def indicateErrorFollows(row, col):
    currentBitCount = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
            return "Nothing can follow horizontally because cell argument is in rightmost column"

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
"""
# returns string of not possible 2-letter combinations with ? + givenletter
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
        result1 = NonPrecedes.get(latterLetter)
        return result1
    if latterLetter not in NonPrecedes:
        result2 = "All letters may precede"
        return result2


"""
def indicateErrorPrecedes(row, col):
    currentBitCount = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
            return "Nothing can precede because cell argument is in leftmost column"

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
            return "Nothing can precede because cell is in topmost row."
"""