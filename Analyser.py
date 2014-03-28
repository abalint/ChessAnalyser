''' piece value
    King: priceless
    Queen: 9
    Rook: 5
    Bishop: 3
    Knight: 3
    pawn: 1
    Total (-king) : 39

    pgn
    King: K
    Queen: Q
    Rook: R
    Bishop: B
    Knight: N


'''

__author__ = 'Andrew'
import shlex
import itertools


class Analyser():
    def __init__(self, filePath):
        self.filePath = filePath

    def analyse(self):

        pgn_text = open(self.filePath).read() #read the pgn
        gameStart = (pgn_text.find("1.")) #find the start of the game
        game = pgn_text[gameStart:] #gets rid of the headers
        print(game)

        lexer = (shlex.shlex(game)) #make a shlex object
        lexer.wordchars  = lexer.wordchars + "-" #+ "+" #tells the shlex not to split on - and +
        '''the + sign was throwing off my calculations, the quick fix was to remove it here, the better solution is to parse it out when looking for pieces'''
        gameList = list(lexer)#get a list based off of shlex

        gameList = [value for value in gameList if len(value)>=2] #gets rid of all periods
        gameList = [value for value in gameList if value.isdigit() == False] #gets rid of all turn numbers, i already know the turn by the index


        takenIndexList = []
        i = 0
        for value in gameList:
            if "x" in value:
                takenIndexList.append(i)
            i += 1
        #
        # print(takenIndexList)

        splitTrades = self.get_sub_list(takenIndexList)

        tradeScores = []
        for value in splitTrades:
            score = self.analyse_trade(value, gameList)
            tradeScores.append(score)

        print("splitTrades: ",splitTrades)
        print("tradeScores: ", tradeScores)

        analysis_list = []
        index = 0
        for value in tradeScores:
            if value == 0: #trade was tied
                if splitTrades[index][0]%2 == 0: #trade was tied and white initiated
                    line = ("%s %s" %("Neutral trade on turn ",int(((splitTrades[index][0]+2)/2))))
                    analysis_list.append(line)
                else:
                    line = ("%s %s" % ("Neutral trade on turn ",int(((splitTrades[index][0]+1)/2))))
                    analysis_list.append(line)
            if value > 0: #white won trade
                if splitTrades[index][0]%2 == 0: #if white won the trade and white initiated
                    line = ("%s %s" %("Good move white on turn ",int(((splitTrades[index][0]+2)/2))))
                    analysis_list.append(line)
                else: #white won trade and black initiated
                    line = ("%s %s" % ("Bad move black on turn ",int(((splitTrades[index][0]+1)/2))))
                    analysis_list.append(line)
            if value < 0: #black won trade
                if splitTrades[index][0]%2 == 0: #if black won the trade and white initiated
                    line = ("%s %s" %("Bad move white on turn ",int(((splitTrades[index][0]+2)/2))))
                    analysis_list.append(line)
                else: #black won trade and black initiated
                    line = ("%s %s" %("Good move black on turn ",int(((splitTrades[index][0]+1)/2))))
                    analysis_list.append(line)
            index = index + 1

        print(analysis_list)
        return analysis_list





    def get_sub_list(self,my_list):
        """will split the list base on the index"""
        my_index = [(x+1) for x,y in zip(my_list, my_list[1:]) if y-x != 1]
        output = list()
        prev = 0
        for index in my_index:
            new_list = [ x for x in my_list[prev:] if x < index]
            output.append(new_list)
            prev += len(new_list)
        output.append([ x for x in my_list[prev:]])
        return output

    #returns white's delta score - black's delta score; positive score = white won trade
    def analyse_trade(self, trade_index, gameList):
        '''
            find first letter from game list,
            find second letter
            turn into a score
            subtract score with white first
            return score
            - means black won trade
        '''

        trade_score = 0
        blackScore = 0
        whiteScore = 0
        moveIndex = 0
        for value in trade_index:
            move = gameList[value] #look at the move that took a piece
            move = move[2:] #get the location of that piece
            end = value #set the end value for the for loop
            i=0 #set an index to 0
            for line in itertools.islice(gameList , 0, end): #go through the entire game list and find the most recent move that contains the same location
                if move in line: #if i found a move that contained the location
                    moveIndex = i #then save the index
                i = i+1 #iterate index
            #print("index: ", moveIndex, " move: ", gameList[moveIndex])
            if value %2 == 0: #it was a white piece to move
                ''' get the first letter, find its value, and add it to the white score '''
                takenPiece = gameList[moveIndex]
                print("piece: ",takenPiece[0])
                points = self.piece_to_score(takenPiece[0])
                print("score: ", points)
                whiteScore = whiteScore + points
            else:
                takenPiece = gameList[moveIndex]
                print("piece: ",takenPiece[0])
                points = self.piece_to_score(takenPiece[0])
                print("score: ", points)
                blackScore = blackScore + points

        trade_score = whiteScore - blackScore
        #print(trade_score)
        return trade_score


    ''' piece value
    King: priceless
    Queen: 9
    Rook: 5
    Bishop: 3
    Knight: 3
    pawn: 1
    Total (-king) : 39

    pgn
    King: K
    Queen: Q
    Rook: R
    Bishop: B
    Knight: N
'''

    def piece_to_score(self, piece):
        if piece == 'Q':
            return 9
        if piece == 'R':
            return 5
        if piece == 'B':
            return 3
        if piece == 'N':
            return 3
        else:
            return 1