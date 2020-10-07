#Game class - Parent class for Player & subGame
class Game:
    def __init__(self, name):
        self.name = name


    def Detail(self):
        opt = input("Do you want to enter details of the game(1/0)\n")
        if opt == "1":
            self.Type = input("Enter type of the game (Eg: indoor (or) outdoor (or) indoor-double (or) palyer)")
            self.Origin = input("Enter the game's origin country\n")
            self.Players = input("Enter the range of players reqd. for one team (Eg. 10-15)")
            self.Equipments = input("Enetr the euipments(Eg: bat,ball,hockey-stick)")


    def rules(self):
        print("Eneter the generic/important rules for the game")
        opt = "1"
        self.rule = []
        opt = input("Do you want to enter the rule(1/0)\n")
        while opt!="0":
            rul = input("Enter rule:\n")
            self.rule.append(rul)
            opt = input("Do you want to enter the rule(1/0)\n")

            
    def printGame(self):
        print("Game: "+self.name+"\tType:"+self.Type+"\tOrigin:"+self.Origin+"\tNo. of players:"+self.Players+"\tEquipmets:"+self.Equipments+"\n")
        print("Rules:")
        print(self.rule)
        print("\n\n")



#Player class for players for a particular game, Inherits Game class
class Player(Game):
    def __init__(self,gname,name):
        super().__init__(gname)
        self.pname = name


    def Detail(self):
        opt = input("do you want to enter player details(1/0)\n")
        if opt != "0":
            self.playerAge = input("Enter player age\n")
            self.playerCountry = input("Enter player country\n")
            self.retired = input("is player retired?(Yes/No)\n")
            
        
    def printPlayer(self):
        print("Player Name:"+self.pname+"\t"+self.name+"\t"+self.playerAge+"\t"+self.playerCountry+"\t"+self.retired+"\n\n")
        




#subGame class for different type of Game, inherits Game
#Detail function of Game is used
class subGame(Game):
    def __init__(self,name,subname):
        super().__init__(name)
        self.subName = subname


    def rules(self):
        super().rules()
        opt = "1"
        opt = input("Do you want to add different set of rules for this sub game?(1/0)\n")
        while opt!="0":
            rul = input("Enter rule:\n")
            self.rule.append(rul)
            opt = input("Do you want to add different set of rules for this sub game?(1/0)\n")


    def printSubGame(self):
        print("sub-Game Name:"+self.subName+"\n")
        super().printGame()
            
    

t="1"
games = []
players = []
subGames = []
def createGame():
    gname = input("Enter game name\n")
    g = Game(gname)
    g.Detail()
    g.rules()
    g.printGame()
    games.append(g)

def createPlayer():
    GNAME = input("Enter game Name\n")
    PLAYER = input("Enter player Name\n")
    p1 = Player(GNAME,PLAYER)
    p1.Detail()
    p1.printPlayer()
    players.append(p1)

def createSubGame():
    GNAME = input("Enter game name\n")
    subName =input("Enter subname \n")
    s1 = subGame(GNAME,subName)
    s1.Detail()
    s1.rules()
    s1.printSubGame()
    players.append(s1.append(s1))
    



t = input("Do you want to enter game/player/subGame?(1/0)\n")
while(t!="0"):
    opt = input("Which one you are goign to add, \n1.game\n2.player\n3.subGame\n(Enter 1 or 2 or 3)\n")
    if opt == "1":
        createGame()
    elif opt == "2":
        createPlayer()
    elif opt == "3":
        createSubGame()
    else:
        print("try again!\n")
    t = input("Do you want to enter game/player/subGame?(1/0)\n")
    



    
    
