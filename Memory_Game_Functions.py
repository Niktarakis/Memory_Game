from random import shuffle
def card(face=None,suit=None,value=None,description=None,state=None):
    """object me onoma card pou anaparista ena trapouloxarto
    ta orismata face,suit kai description pairnoun strings gia times eno to state kai to value
     pairnoun times int (gia to state 0 simainei oti einai kleisto eno 1 oti einai anoixto)
    >>> card('A', '♣', 1, 'A♣',' x ')
    ['A', '♣', 1, 'A♣', ' x ']
    """
    return [face,suit,value,description,state]
def face(card):
    return card[0]
def suit(card):
    return card[1]
def value(card):
    return card[2]
def print_card(card):
    print(card[3])
def deck_maker(difficulty):
    """Analoga me ton vathmo diskolias ftiaxnei antostoixa mia lista me antikeimena typou "card"
    poy anaparista ousiastika tin trapoula
    >>> len(deck_maker(3))
    52
    >>> len(deck_maker(2))
    40
    >>> len(deck_maker(1))
    16
    >>> deck_maker(1)
    [['10', '♠', 10, '10♠', ' x '], ['J', '♠', 10, 'J♠', ' x '], ['Q', '♠', 10, 'Q♠', ' x '], ['K', '♠', 10, 'K♠', ' x '], ['10', '♥', 10, '10♥', ' x '], ['J', '♥', 10, 'J♥', ' x '], ['Q', '♥', 10, 'Q♥', ' x '], ['K', '♥', 10, 'K♥', ' x '], ['10', '♦', 10, '10♦', ' x '], ['J', '♦', 10, 'J♦', ' x '], ['Q', '♦', 10, 'Q♦', ' x '], ['K', '♦', 10, 'K♦', ' x '], ['10', '♣', 10, '10♣', ' x '], ['J', '♣', 10, 'J♣', ' x '], ['Q', '♣', 10, 'Q♣', ' x '], ['K', '♣', 10, 'K♣', ' x ']]
    >>> deck_maker(2)
    [['A', '♠', 1, 'A♠', ' x '], ['2', '♠', 2, '2♠', ' x '], ['3', '♠', 3, '3♠', ' x '], ['4', '♠', 4, '4♠', ' x '], ['5', '♠', 5, '5♠', ' x '], ['6', '♠', 6, '6♠', ' x '], ['7', '♠', 7, '7♠', ' x '], ['8', '♠', 8, '8♠', ' x '], ['9', '♠', 9, '9♠', ' x '], ['10', '♠', 10, '10♠', ' x '], ['A', '♥', 1, 'A♥', ' x '], ['2', '♥', 2, '2♥', ' x '], ['3', '♥', 3, '3♥', ' x '], ['4', '♥', 4, '4♥', ' x '], ['5', '♥', 5, '5♥', ' x '], ['6', '♥', 6, '6♥', ' x '], ['7', '♥', 7, '7♥', ' x '], ['8', '♥', 8, '8♥', ' x '], ['9', '♥', 9, '9♥', ' x '], ['10', '♥', 10, '10♥', ' x '], ['A', '♦', 1, 'A♦', ' x '], ['2', '♦', 2, '2♦', ' x '], ['3', '♦', 3, '3♦', ' x '], ['4', '♦', 4, '4♦', ' x '], ['5', '♦', 5, '5♦', ' x '], ['6', '♦', 6, '6♦', ' x '], ['7', '♦', 7, '7♦', ' x '], ['8', '♦', 8, '8♦', ' x '], ['9', '♦', 9, '9♦', ' x '], ['10', '♦', 10, '10♦', ' x '], ['A', '♣', 1, 'A♣', ' x '], ['2', '♣', 2, '2♣', ' x '], ['3', '♣', 3, '3♣', ' x '], ['4', '♣', 4, '4♣', ' x '], ['5', '♣', 5, '5♣', ' x '], ['6', '♣', 6, '6♣', ' x '], ['7', '♣', 7, '7♣', ' x '], ['8', '♣', 8, '8♣', ' x '], ['9', '♣', 9, '9♣', ' x '], ['10', '♣', 10, '10♣', ' x ']]
    """
    deck=[]
    for i in range(52): #Arxika vazo stin lista 52 kena antikeimena "card"
        deck.append(card())
    for i in range(13): #me tin xris aftis tis for loop tha dosoume tis aparaitites idiotites sta kena "card" objects
        deck[i][1]="♠"
        deck[i+13][1]="♥"
        deck[i+26][1]="♦"
        deck[i+39][1]="♣"
        if i==0:
            deck[i][0]='A'
            deck[i][2]=1
            deck[i+13][0]='A'
            deck[i+13][2]=1
            deck[i+26][0]='A'
            deck[i+26][2]=1
            deck[i+39][0]='A'
            deck[i+39][2]=1
        elif i>0 and i<=9:
            deck[i][0]=str(i+1)
            deck[i][2]=i+1
            deck[i+13][0]=str(i+1)
            deck[i+13][2]=i+1
            deck[i+26][0]=str(i+1)
            deck[i+26][2]=i+1
            deck[i+39][0]=str(i+1)
            deck[i+39][2]=i+1
        elif i==10:
            deck[i][0]='J'
            deck[i][2]=10
            deck[i+13][0]='J'
            deck[i+13][2]=10
            deck[i+26][0]='J'
            deck[i+26][2]=10
            deck[i+39][0]='J'
            deck[i+39][2]=10
        elif i==11:
            deck[i][0]='Q'
            deck[i][2]=10
            deck[i+13][0]='Q'
            deck[i+13][2]=10
            deck[i+26][0]='Q'
            deck[i+26][2]=10
            deck[i+39][0]='Q'
            deck[i+39][2]=10
        elif i==12:
            deck[i][0]='K'
            deck[i][2]=10
            deck[i+13][0]='K'
            deck[i+13][2]=10
            deck[i+26][0]='K'
            deck[i+26][2]=10
            deck[i+39][0]='K'
            deck[i+39][2]=10
    for i in range(52):
        deck[i][3]=deck[i][0]+deck[i][1]
        deck[i][4]=' x '
    if difficulty==1:
        active_deck=[i for i in deck if any(k in i[0] for k in ['10','J','Q','K'])]  #me xrisi tis sinartisis any() kano elegxo gia polla stoixeia ftiaxnontas etsi mia lista me ta xartia pou antisoixoun sto epipedo diskolias 
    if difficulty==2:
        active_deck=[i for i in deck if any(k in i[0] for k in ['A','2','3','4','5','6','7','8','9','10'])]
    if difficulty==3:
        active_deck=deck
    return active_deck
def nested_board(deck,difficulty):
    """Anakatevei tin trapoula pou dimiourgise i porigoumeni 
    sinartisi kai epeita dimiourgei ton pinaka pou tha dra os 
    trapezi me ta xartia pano toy aplomena se morfi
    pinaka m*n analoga me to epipedo diskolias"""
    board=[]
    if difficulty==1:  #ksexorizoume periptoseis sxetika me to vathmo diskolias etsi oste na exei i trapoula ta apparaitita filla 
        shuffle(deck)    #me tin sinartisi shuffle anakatevoume tin trapoula  
        for i in range(16)[::4]:
            board.append(deck[i:i+4])   #dimioyrgoume emfoliasmenes listes 4 stoixeion "active_deck[i:i+4]" pou tha anaparistoun ton pinaka me ta xartia
    elif difficulty==2:
        shuffle(deck)
        for i in range(40)[::4]:
            board.append(deck[i:i+4])
    elif difficulty==3: 
        shuffle(deck)
        for i in range(52)[::4]:
            board.append(deck[i:i+4])
    return board
def anaparastasi_pinaka(pinakas):
    """Anaparista ton pinaka me x opou yparxei karta anapoda
    to megethos tou pinaka aftou eksartatai apo to epipedo diskolias
    os orisma pairnei tin anakatemeni trapoula se emfoliasmenes listes
    >>> anaparastasi_pinaka([[['Q', '♦', 10, 'Q♦', ' x '], ['Q', '♣', 10, 'Q♣', ' x '], ['K', '♥', 10, 'K♥', ' x '], ['Q', '♥', 10, 'Q♥', ' x ']], [['10', '♦', 10, '10♦', ' x '], ['J', '♥', 10, 'J♥', ' x '], ['10', '♠', 10, '10♠', ' x '], ['K', '♦', 10, 'K♦', ' x ']], [['Q', '♠', 10, 'Q♠', ' x '], ['J', '♠', 10, 'J♠', ' x '], ['K', '♠', 10, 'K♠', ' x '], ['10', '♣', 10, '10♣', ' x ']], [['J', '♦', 10, 'J♦', ' x '], ['10', '♥', 10, '10♥', ' x '], ['K', '♣', 10, 'K♣', ' x '], ['J', '♣', 10, 'J♣', ' x ']]])
       1  2  3  4 
    1  x  x  x  x 
    2  x  x  x  x 
    3  x  x  x  x 
    4  x  x  x  x 
    >>> anaparastasi_pinaka([[['10', '♥', 10, '10♥', ' x '], ['10', '♠', 10, '10♠', ' x '], ['9', '♠', 9, '9♠', ' x '], ['6', '♠', 6, '6♠', ' x ']], [['8', '♥', 8, '8♥', ' x '], ['2', '♥', 2, '2♥', ' x '], ['A', '♣', 1, 'A♣', ' x '], ['2', '♠', 2, '2♠', ' x ']], [['10', '♣', 10, '10♣', ' x '], ['A', '♥', 1, 'A♥', ' x '], ['5', '♣', 5, '5♣', ' x '], ['A', '♠', 1, 'A♠', ' x ']], [['6', '♥', 6, '6♥', ' x '], ['A', '♦', 1, 'A♦', ' x '], ['9', '♦', 9, '9♦', ' x '], ['9', '♥', 9, '9♥', ' x ']], [['2', '♣', 2, '2♣', ' x '], ['10', '♦', 10, '10♦', ' x '], ['5', '♦', 5, '5♦', ' x '], ['7', '♦', 7, '7♦', ' x ']], [['3', '♥', 3, '3♥', ' x '], ['9', '♣', 9, '9♣', ' x '], ['7', '♣', 7, '7♣', ' x '], ['5', '♥', 5, '5♥', ' x ']], [['5', '♠', 5, '5♠', ' x '], ['8', '♣', 8, '8♣', ' x '], ['2', '♦', 2, '2♦', ' x '], ['4', '♥', 4, '4♥', ' x ']], [['3', '♦', 3, '3♦', ' x '], ['6', '♣', 6, '6♣', ' x '], ['4', '♦', 4, '4♦', ' x '], ['4', '♠', 4, '4♠', ' x ']], [['7', '♠', 7, '7♠', ' x '], ['6', '♦', 6, '6♦', ' x '], ['3', '♣', 3, '3♣', ' x '], ['7', '♥', 7, '7♥', ' x ']], [['8', '♦', 8, '8♦', ' x '], ['8', '♠', 8, '8♠', ' x '], ['3', '♠', 3, '3♠', ' x '], ['4', '♣', 4, '4♣', ' x ']]])
       1  2  3  4  5  6  7  8  9 10 
    1  x  x  x  x  x  x  x  x  x  x 
    2  x  x  x  x  x  x  x  x  x  x 
    3  x  x  x  x  x  x  x  x  x  x 
    4  x  x  x  x  x  x  x  x  x  x 
    """
    output="  "
    for i in range(len(pinakas)): #Ftiaxnoume tin proti grami me tis endikseis "1,2..."
        if i<9:
            output+=" "+str(i+1)+" "
        else:
            output+=str(i+1)+" "
    i=0
    for quad in pinakas:
        for item in quad:  #efoson o pinakas einai se morfi emfoliasmenon liston xrisimopoioume dio for etsi oste na kalesoume ta sosta stoixeia 
            if i==0:
                output+='\n1 '+item[4]
            elif i<len(pinakas):
                output+=item[4]
            elif i==len(pinakas):
                output+='\n2 '+item[4]
            elif i>len(pinakas) and i<2*len(pinakas):
                output+=item[4]
            elif i==2*len(pinakas):
                output+='\n3 '+item[4]
            elif i>2*len(pinakas) and i<3*len(pinakas):
                output+=item[4]
            elif i==3*len(pinakas):
                output+='\n4 '+item[4]
            elif i>3*len(pinakas) and i<4*len(pinakas):
                output+=item[4]
            i+=1
    print(output)
    