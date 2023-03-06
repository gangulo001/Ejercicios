import os, cards, games

class BJ_Card(cards.Card):
    
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))
    

class BJ_Hand(cards.Hand):
    
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        
        for card in self.cards:
            if not card.value:
                return None
        
        t = 0
        for card in self.cards:
            t += card.value

        
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True    
       
        if contains_ace and t <= 11:
            
            t += 10   
        return t
    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", desea otra carta? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "SE PASO.")
        self.lose()

    def lose(self):
        print(self.name, "PIERDE.")

    def win(self):
        print(self.name, "GANA.")
        return(self.name)

    def push(self):
        print(self.name, "EMPATA.")

        
class BJ_Dealer(BJ_Hand):
    
    def is_hitting(self):
        return self.total < 19

    def bust(self):
        print(self.name, "se paso.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
        
    def play(self):
        
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    
        for player in self.players:
            print(player)
        print(self.dealer)

       
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    

        if not self.still_playing:
            
            print(self.dealer)
        else:
            
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                
                for player in self.still_playing:
                    winner = player.win()     
                    return (winner)               
            else:
                
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        winner = player.win()
                        return (winner)
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        
        for player in self.players:
            player.clear()
        self.dealer.clear()
        

def main():
        
    game = BJ_Game(names)

    winner = game.play()

    return (winner)
        

Salir = False
os.system('cls')
names = []
number = games.ask_number("Cuantos usuarios desean jugar? (1 - 2): ", low = 1, high = 3)
for i in range(number):
    name = input("Digite el nombre o usuario del jugador: ")
    names.append(name)
print()

print("Bienvenido al juego de BLACKJACK\nSus estadisticas de juego seran mostradas cuando desee salir\nUn empate es considerado un gane para la casa")
if len(names) == 1:
    print(names[0], ":")
else:
    print(names[0], names[1], ":")

contador = 0
winsPlayer1 = 0
winsPlayer2 = 0

while not Salir:
    


    menu = input("Si desea continuar digite si ('y')\nSi desea salir del juego digite no ('n')\n")

    if menu == 'y':
        winner = main() 
        if winner == names[0]:
            winsPlayer1 = winsPlayer1 + 1
        if len(names) == 2:
            if winner == names[1]:
                winsPlayer2 = winsPlayer2 + 1
    
        contador = contador + 1

        
    elif menu == 'n':
        try:
            os.system('cls')
            print("\nGracias por jugar BLACKJACK sus estadisticas son:")
            print(names[0], ":")
            print("Partidas ganadas: " + str(winsPlayer1) + "    " + str((winsPlayer1 / contador) * 100) + "%")
            print("Partidas perdidas: " + str(contador - winsPlayer1) + "    " + str(100 - (winsPlayer1 / contador) * 100) + "%")
            if len(names) == 2:
                print(names[1], ":")
                print("Partidas ganadas: " + str(winsPlayer2) + "    " + str((winsPlayer2 / contador) * 100) + "%")
                print("Partidas perdidas: " + str(contador - winsPlayer2) + "    " + str(100 - (winsPlayer2 / contador) * 100) + "%")
        
            Salir = True
        except:
            print("Por favor intente de nuevo")