import numpy, subprocess, random

class tournament(object):
    """A tournament for 'The Game of Life'. Every combination of two players
    
    
    Attributes:
        contestants:    A list of program names that enter the tournament.
    """
    
    ROUNDS = 100
    
    def __init__(self, contestants):
         self.contestants = contestants
         self.wins = {}
     
    def run_tournament(self):
        for idx1,p1 in enumerate(self.contestants[:-2]):
            for p2 in self.contestants[idx+1:-1]:
                competition=game([p1,p2],self.ROUNDS)
                for p in competition.players:
                    self.wins[p.get_name()] += p.get_wins()
     
    def print_results(self):
         print(self.wins)

class game(object):
    """Simulate a multi-player game-of-life
    
    Attributes:
        players:    A list of names of programs that will enter as tcontestants
    """

    BOARD_SIZE_COLUMNS = 10 #24
    BOARD_SIZE_ROWS = 10 #24 
    MAXMOVES = 30
    MAXITER = 10000
    
    def __init__(self, players):
        self.error_found = False
        self.players = []
        for playername in players:
            self.players.append(player(playername))
            if self.players[-1] == False:
                raise("Failed to init program: " + playername)
                self.error_found = True
        shuffle(self.players)
        self.board = numpy.zeros((BOARD_SIZE_COLUMNS, BOARD_SIZE_ROWS), dtype=numpy.int)
        self.round = 0

    def board_init(self):
        self.board = numpy.zeros((BOARD_SIZE_COLUMNS, BOARD_SIZE_ROWS), dtype=numpy.int)

    def get_board(self):
        return self.board
    
    def play_rounds(self,numer_of_rounds):
        self.board_init()
        pass
    
    def play_game(self):
        while( not self.error_found and self.round <= self.MAXITER ):
            for i,p in enumerate(self.players):
                self.process_move(i, p.play(self.board))
        self.step()
    
    def process_move(self,playerid,moves):
        pass
        
    def step(self):
        count = sum(self.game(i,j)
                         for i in (-1, 0, 1) for j in (-1, 0, 1)
                         if (i != 0 or j != 0))
        return (count == 3) | (self.game & (count == 2))

class player(object):
    """Act as a player in the multi player game of life

    Attributes:
        name:    the name of the program for the player
    """
    
    INTERPRETER = 'python3.4'
    
    def __init__(self, name):
        self.name = name
        if subprocess.call(self.INTERPRETER + ' ' + self.name) != "OK":
            raise("Failed to init program: " + self.name)
            return False
        self.wins = 0
        return self
        
    def play(self, board):
        pass
    
    def add_win(self):
        self.wins += 1
    
    def get_wins(self):
        return self.wins
    
    def get_name(self):
        return self.name

if __name__ == '__main__':
    contestants = ["random.py", "still_life.py"]
    
    competition = tournament(contestants)
    competition.run_tournament()
    competition.print_results()    
