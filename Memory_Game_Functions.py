from random import shuffle
def card(face=None,suit=None,value=None,description=None,back=None):
    """ Οbject με όνομα card που αναπαριστά ένα τραπουλόχαρτο
    όλα τα ορσίσματα είναι strings εκτός απο το value που
    είναι integer. To στοιχείο "face" είναι string με το
    γράμμα που αντιστοχει στο φύλλο. Το στοχειο suit
    είναι το "χρώμα" σε string. Το στοιχείο value 
    είναι αριθμητική τιμή που αντιστοιχεί στην αξία του 
    φύλλου. Το desc string με το γράμμα και χρώμα πορεύεται
    να ειναι αυτο που βλέπει ο χρήστης. Τέλος το στοιχείο 
    back απεικονίζει το "πίσω μέρος μιας κάρτας" η χρήση 
    αυτου του στοιχείου θα γίνει εμφανής αργότερα.
    >>> card('A', '♣', 1, 'A♣ ','x  ')
    ['A', '♣', 1, 'A♣ ', 'x  ']
    """
    return [face,suit,value,description,back]
def deck_maker(difficulty):
    """ Ανάλογα με τον βαθμό δυσκολίας φτιάχνει μια λίστα με
    52 στοχεία τυπου card που ειναι ουσιαστικά η τράπουλα.
    >>> len(deck_maker(3))
    52
    >>> len(deck_maker(2))
    40
    >>> len(deck_maker(1))
    16
    >>> deck_maker(1)
    [['10', '♠', 10, '10♠ ', 'x   '], ['J', '♠', 10, 'J♠  ', 'x   '], ['Q', '♠', 10, 'Q♠  ', 'x   '], ['K', '♠', 10, 'K♠  ', 'x   '], ['10', '♥', 10, '10♥ ', 'x   '], ['J', '♥', 10, 'J♥  ', 'x   '], ['Q', '♥', 10, 'Q♥  ', 'x   '], ['K', '♥', 10, 'K♥  ', 'x   '], ['10', '♦', 10, '10♦ ', 'x   '], ['J', '♦', 10, 'J♦  ', 'x   '], ['Q', '♦', 10, 'Q♦  ', 'x   '], ['K', '♦', 10, 'K♦  ', 'x   '], ['10', '♣', 10, '10♣ ', 'x   '], ['J', '♣', 10, 'J♣  ', 'x   '], ['Q', '♣', 10, 'Q♣  ', 'x   '], ['K', '♣', 10, 'K♣  ', 'x   ']]
    >>> deck_maker(2)
    [['A', '♠', 1, 'A♠  ', 'x   '], ['2', '♠', 2, '2♠  ', 'x   '], ['3', '♠', 3, '3♠  ', 'x   '], ['4', '♠', 4, '4♠  ', 'x   '], ['5', '♠', 5, '5♠  ', 'x   '], ['6', '♠', 6, '6♠  ', 'x   '], ['7', '♠', 7, '7♠  ', 'x   '], ['8', '♠', 8, '8♠  ', 'x   '], ['9', '♠', 9, '9♠  ', 'x   '], ['10', '♠', 10, '10♠ ', 'x   '], ['A', '♥', 1, 'A♥  ', 'x   '], ['2', '♥', 2, '2♥  ', 'x   '], ['3', '♥', 3, '3♥  ', 'x   '], ['4', '♥', 4, '4♥  ', 'x   '], ['5', '♥', 5, '5♥  ', 'x   '], ['6', '♥', 6, '6♥  ', 'x   '], ['7', '♥', 7, '7♥  ', 'x   '], ['8', '♥', 8, '8♥  ', 'x   '], ['9', '♥', 9, '9♥  ', 'x   '], ['10', '♥', 10, '10♥ ', 'x   '], ['A', '♦', 1, 'A♦  ', 'x   '], ['2', '♦', 2, '2♦  ', 'x   '], ['3', '♦', 3, '3♦  ', 'x   '], ['4', '♦', 4, '4♦  ', 'x   '], ['5', '♦', 5, '5♦  ', 'x   '], ['6', '♦', 6, '6♦  ', 'x   '], ['7', '♦', 7, '7♦  ', 'x   '], ['8', '♦', 8, '8♦  ', 'x   '], ['9', '♦', 9, '9♦  ', 'x   '], ['10', '♦', 10, '10♦ ', 'x   '], ['A', '♣', 1, 'A♣  ', 'x   '], ['2', '♣', 2, '2♣  ', 'x   '], ['3', '♣', 3, '3♣  ', 'x   '], ['4', '♣', 4, '4♣  ', 'x   '], ['5', '♣', 5, '5♣  ', 'x   '], ['6', '♣', 6, '6♣  ', 'x   '], ['7', '♣', 7, '7♣  ', 'x   '], ['8', '♣', 8, '8♣  ', 'x   '], ['9', '♣', 9, '9♣  ', 'x   '], ['10', '♣', 10, '10♣ ', 'x   ']]
    >>> deck_maker(3)
    [['A', '♠', 1, 'A♠  ', 'x   '], ['2', '♠', 2, '2♠  ', 'x   '], ['3', '♠', 3, '3♠  ', 'x   '], ['4', '♠', 4, '4♠  ', 'x   '], ['5', '♠', 5, '5♠  ', 'x   '], ['6', '♠', 6, '6♠  ', 'x   '], ['7', '♠', 7, '7♠  ', 'x   '], ['8', '♠', 8, '8♠  ', 'x   '], ['9', '♠', 9, '9♠  ', 'x   '], ['10', '♠', 10, '10♠ ', 'x   '], ['J', '♠', 10, 'J♠  ', 'x   '], ['Q', '♠', 10, 'Q♠  ', 'x   '], ['K', '♠', 10, 'K♠  ', 'x   '], ['A', '♥', 1, 'A♥  ', 'x   '], ['2', '♥', 2, '2♥  ', 'x   '], ['3', '♥', 3, '3♥  ', 'x   '], ['4', '♥', 4, '4♥  ', 'x   '], ['5', '♥', 5, '5♥  ', 'x   '], ['6', '♥', 6, '6♥  ', 'x   '], ['7', '♥', 7, '7♥  ', 'x   '], ['8', '♥', 8, '8♥  ', 'x   '], ['9', '♥', 9, '9♥  ', 'x   '], ['10', '♥', 10, '10♥ ', 'x   '], ['J', '♥', 10, 'J♥  ', 'x   '], ['Q', '♥', 10, 'Q♥  ', 'x   '], ['K', '♥', 10, 'K♥  ', 'x   '], ['A', '♦', 1, 'A♦  ', 'x   '], ['2', '♦', 2, '2♦  ', 'x   '], ['3', '♦', 3, '3♦  ', 'x   '], ['4', '♦', 4, '4♦  ', 'x   '], ['5', '♦', 5, '5♦  ', 'x   '], ['6', '♦', 6, '6♦  ', 'x   '], ['7', '♦', 7, '7♦  ', 'x   '], ['8', '♦', 8, '8♦  ', 'x   '], ['9', '♦', 9, '9♦  ', 'x   '], ['10', '♦', 10, '10♦ ', 'x   '], ['J', '♦', 10, 'J♦  ', 'x   '], ['Q', '♦', 10, 'Q♦  ', 'x   '], ['K', '♦', 10, 'K♦  ', 'x   '], ['A', '♣', 1, 'A♣  ', 'x   '], ['2', '♣', 2, '2♣  ', 'x   '], ['3', '♣', 3, '3♣  ', 'x   '], ['4', '♣', 4, '4♣  ', 'x   '], ['5', '♣', 5, '5♣  ', 'x   '], ['6', '♣', 6, '6♣  ', 'x   '], ['7', '♣', 7, '7♣  ', 'x   '], ['8', '♣', 8, '8♣  ', 'x   '], ['9', '♣', 9, '9♣  ', 'x   '], ['10', '♣', 10, '10♣ ', 'x   '], ['J', '♣', 10, 'J♣  ', 'x   '], ['Q', '♣', 10, 'Q♣  ', 'x   '], ['K', '♣', 10, 'K♣  ', 'x   ']]
    """
    deck=[]
    for i in range(52): # Αρχικά βαζω σε μια λίστα 52 κενά ανρικείμενα "card"
        deck.append(card())
    for i in range(13): # Με αυτό το λουπ θά βάλουμε ολα τα απαραίτητα στοιχεία στα cards για να έχουμε μια πλήρη τράπουλα
        deck[i][1]="♠"
        deck[i+13][1]="♥"
        deck[i+26][1]="♦"
        deck[i+39][1]="♣"
        if i==0: # προσθέτουμε τους άσσους στην τράπουλα 
            deck[i][0]='A'
            deck[i][2]=1
            deck[i+13][0]='A'
            deck[i+13][2]=1
            deck[i+26][0]='A'
            deck[i+26][2]=1
            deck[i+39][0]='A'
            deck[i+39][2]=1
        elif i>0 and i<=9: #Πρσοθέτουμε τα νούμερα απο το 2 μέχρι το 10
            deck[i][0]=str(i+1)
            deck[i][2]=i+1
            deck[i+13][0]=str(i+1)
            deck[i+13][2]=i+1
            deck[i+26][0]=str(i+1)
            deck[i+26][2]=i+1
            deck[i+39][0]=str(i+1)
            deck[i+39][2]=i+1
        elif i==10: # Το ίδιο για τους βαλέδες
            deck[i][0]='J'
            deck[i][2]=10
            deck[i+13][0]='J'
            deck[i+13][2]=10
            deck[i+26][0]='J'
            deck[i+26][2]=10
            deck[i+39][0]='J'
            deck[i+39][2]=10
        elif i==11: #Ντάμες
            deck[i][0]='Q'
            deck[i][2]=10
            deck[i+13][0]='Q'
            deck[i+13][2]=10
            deck[i+26][0]='Q'
            deck[i+26][2]=10
            deck[i+39][0]='Q'
            deck[i+39][2]=10
        elif i==12: #Ρίγες
            deck[i][0]='K'
            deck[i][2]=10
            deck[i+13][0]='K'
            deck[i+13][2]=10
            deck[i+26][0]='K'
            deck[i+26][2]=10
            deck[i+39][0]='K'
            deck[i+39][2]=10
    for i in range(52):
        if deck[i][0]=='10':
            deck[i][3]=deck[i][0]+deck[i][1]+' '
        else :
            deck[i][3]=deck[i][0]+deck[i][1]+'  '
        deck[i][4]='x   '
    if difficulty==1:
        active_deck=[i for i in deck if any(k in i[0] for k in ['10','J','Q','K'])]     #Με την χρήση της any() σε αυτό το list comprehension κάνω ελεγχο για πολλαπλά στοιχεία μέσα στην λιστα deck και δημιουργό με αυτό τον τρόπο λίστα του επιθυμιτού μεγέθους 
    if difficulty==2:
        active_deck=[i for i in deck if any(k in i[0] for k in ['A','2','3','4','5','6','7','8','9','10'])]
    if difficulty==3:
        active_deck=deck
    return active_deck
def nested_board(deck,difficulty):
    """ Ανακατεύει το deck που επιστρέφει η συνάρτηση
    deck_maker και βάζει της κάρτες σε εμφολιασμένες λίστες
    που θα δρά ως πίνακας με στοιχεία m*n ανάλογα με το 
    επίπεδο δυσκολίας. Επειδή η συνάρτηση ανακατεύει την 
    τράπουλα δεν μπορούν να υπάρχουν doctests."""
    board=[]
    if difficulty==1:  #Ελέγχουμε το επίπεδο δυσκολίας για να γνωρίζουμε τον αριθμο τον εμφολιαμένων λιστών
        shuffle(deck)    #Με την συνάρτηση shuffle ανακατεύουμε την τράπουλα    
        for i in range(16)[::4]:
            board.append(deck[i:i+4])   #Δημιουργούμε εμφολιασμένες λίστες 4 στοιχείων "active_deck[i:i+4]" που θα αναπαρισούν τον πίνακα 
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
    """ Τυπώνει τον πίνακα με τις κάρτες ανάποδα "x"
    το μέγεθος του πίνακα εξαρτάται απο το βαθμό δυσκολίας
    ως όρισμα παιρνει την ανακατεμένη τράπουλα οπως τη δίνει
    η συνάρτηση nested_board. Λογο τον κενων δεν μπορέσαμε να 
    κανουμε τα doctest να δουλέψουν σωστα. το ιδιο υσχύει και
    στην συνάρτηση open_board.
    
    """
    output="  "
    for i in range(len(pinakas)): #Φτιάχνουμε την πρώτη γραμμή με τις ενδείξεις "1,2..."
        if i<9:
            output+="  "+str(i+1)+" "
        else:
            output+="  "+str(i+1)
    i=0
    for x in range(len(pinakas)):
        for quad in pinakas: # Καλούμε τα σωστά στοιχεία χρησημοποιώντας 2 for για την εμφολιασμένη λίστα
            if i==0:
                output+='\n1   '+quad[x][4]
            elif i<len(pinakas):
                output+=quad[x][4]
            elif i==len(pinakas):
                output+='\n\n2   '+quad[x][4]
            elif i>len(pinakas) and i<2*len(pinakas):
                output+=quad[x][4]
            elif i==2*len(pinakas):
                output+='\n\n3   '+quad[x][4]
            elif i>2*len(pinakas) and i<3*len(pinakas):
                output+=quad[x][4]
            elif i==3*len(pinakas):
                output+='\n\n4   '+quad[x][4]
            elif i>3*len(pinakas) and i<4*len(pinakas):
                output+=quad[x][4]
            i+=1
    print(output,'\n')

def open_board(pinakas):
    """ Δουλεύει παρόμοια με την open_card
    που ακολουθεί απλώς εμφανίζει όλα τα χαρτιά
    στον πίνακα στην αρχη του παιχνιδιού
    
    """
    output="  "
    for i in range(len(pinakas)): #Φτιάχνουμε την πρώτη γραμμή με τις ενδείξεις "1,2..."
        if i<9:
            output+="  "+str(i+1)+" "
        else:
            output+="  "+str(i+1)
    for quad in pinakas: # Ανοίγουμε όλα τα φύλλα βάζοντας στο τελευταίο στοιχείο που ειναι "x   " τα χαρακτηριστικά της κάρτας π.χ('3♠  ')
        for item in quad:
            item[4]=item[3] 
    i=0
    for x in range(len(pinakas)):
        for quad in pinakas: # Καλούμε τα σωστά στοιχεία χρησημοποιώντας 2 for για την εμφολιασμένη λίστα
            if i==0:
                output+='\n1   '+quad[x][4]
            elif i<len(pinakas):
                output+=quad[x][4]
            elif i==len(pinakas):
                output+='\n\n2   '+quad[x][4]
            elif i>len(pinakas) and i<2*len(pinakas):
                output+=quad[x][4]
            elif i==2*len(pinakas):
                output+='\n\n3   '+quad[x][4]
            elif i>2*len(pinakas) and i<3*len(pinakas):
                output+=quad[x][4]
            elif i==3*len(pinakas):
                output+='\n\n4   '+quad[x][4]
            elif i>3*len(pinakas) and i<4*len(pinakas):
                output+=quad[x][4]
            i+=1
    print(output,'\n')      

def open_card(pinakas,grammi,stili):
    """ Παίρνει ως όρισματα τον πίνακα που
    επιστρεφει η συναρτηση nested_board, την επιθυμητη γραμμή
    και στήλη. Έπειτα "αναποδογυρίζει" την κάρτα δίνοντας
    στην θεση με ενδειξη 4 μιας καρτας που ειναι
    το "πισω μέρος της καρτας" το στοιχειο της θέσης
    με ενδειξη 3 που ειναι το description (δηλαδη '3♥ ').
    >>> open_card([[['10', '♠', 10, '10♠', 'x  '], ['J', '♠', 10, ' J♠', ' x ']], [['Q', '♠', 10, ' Q♠', ' x '], ['K', '♠', 10, ' K♠', ' x ']]],1,2)
    ['Q', '♠', 10, ' Q♠', ' Q♠']
    """
    pinakas[stili-1][grammi-1][4]=pinakas[stili-1][grammi-1][3]  #Κάθε στήλη περιέχει 4 στοχεια όπως σε φωλιασμένες λίστες
    return pinakas[stili-1][grammi-1] #το '-1' στις ενδείξεις της λίστας υπάρχει γιατι ο χρήστης επιλέγει απο 1,1 και μεγαλύτερα  

def elegxos_anoixtis_kartas(pinakas,grammi,stili):
    """ Ελέγχει εαν η κάρτα είναι ανοιχτή
    >>> deck=deck_maker(1)
    >>> board=nested_board(deck,1)
    >>> elegxos_anoixtis_kartas(board,1,2)
    True
    >>> x=open_card(board,1,2) #H ανάθεση γίνεται γιατι η συνάρτηση επιστρέφει κάρτα την οποια δεν μπορούμε να ξέρουμε καθώς η τράπουλα είναι ανακάτεμενη
    >>> elegxos_anoixtis_kartas(board,1,2)
    False
    """
    if pinakas[stili-1][grammi-1][4]=="x   ":
        return True
    else:
        return False
    
def check_input(input_str,difficulty):
    """Παίρνει ως ορίσματα το input του χρήστη και 
    το επίπεδο δυσκολίας επιστρέφει τιμή boolean.
    True εαν η μορφή της εισόδου είναι σώστη 
    και False εαν η είσοδος είναι λάθος.
    Ο λόγος που επιστρέφει τιμες αληθής ψευδής 
    είναι γιατι στο πρόγραμμα χρσησημοποιείται 
    ως συνθήκη για if
    >>> check_input("5 3",1)
    False
    >>> check_input("4 13",3)
    True
    >>> check_input("hello world",2)
    False
    """ 
    if difficulty==1:
        if len(input_str)==3 and input_str[0].isnumeric() and input_str[2].isnumeric() and 0<eval(input_str[0])<5 and 0<eval(input_str[2])<5:#Για να είναι σωστό το input και να προχωρήσει το πρόγραμμα πρέπει να τειρούνατι βασικές προυποθέσεις όπως το μήκος του str να ειναι συγκεκριμμένο, τα ψηφία που δίνονται να ειναι αριθμοί και οι αριθμοί αυτοι να είναι επιτρεπτοί στο αντιδτοιχο βαθμο δυσκολίας 
            return True             
        else: #αμα δεν τηρείται έστω και μια απο τις παραπάνω προυποθέσεις το input είναι λάθος
            return False 
    elif difficulty==2:
        if (len(input_str)==4 or len(input_str)==3) and input_str[0].isnumeric() and input_str[2:].isnumeric() and input_str[1]==" " and 0<eval(input_str[0])<5 and 0<eval(input_str[2:])<11:
            return True 
        else:
            return False
    else:
        if (len(input_str)==4 or len(input_str)==3) and input_str[0].isnumeric() and input_str[2:].isnumeric() and input_str[1]==" " and 0<eval(input_str[0])<5 and 0<eval(input_str[2:])<14:
            return True 
        else:
            return False

def card_input(input_str):
    """Παίρνει ως όρισμα το input του
    χρήστη που έχει ελεγχθεί απο την
    συνάρτηση check_input οτι ειναι σε 
    μορφή 'γραμμή στήλη' και το επιστρέφει
    σε tuple (γραμμή,στήλη) που είναι ουσιαστικά
    οι συντεταγμένες τις επιλεγμένης κάρτας
    στον πίνακα  
    >>> card_input("1 2")
    (1, 2)
    >>> card_input("1 10")
    (1, 10)
    """
    if len(input_str)==4:#an to mhkos tou str exei pano apo 3 xaraktires afto simainei oti o arithmos tis stilis einai dipsifios
        syntetagmenes=(eval(input_str[0]),eval(input_str[2:]))
    elif len(input_str)==3:
        syntetagmenes=(eval(input_str[0]),eval(input_str[2]))
    return syntetagmenes

def check_cards(first_open_card,second_open_card,paiktis,scoreboard):
    """ Παίρνει ως ορίσματα την πρώτη και 
    δεύτερη επιλεγμένη κάρτα,την ένδειξη του
    παίκτη και τον πινακα του σκορ ελέγχει. 
    Αμα τα δυο φύλλα ταιρίαζουν τοτε δίνει
    τους αντίστοιχους πόντους και τα αφήνει
    ανοιχτά, αλλιώς τα αναποδογυρίζει αναθετωντας
    παλι στο "πισω" μερος τις κάρτας (card[4])
    το string 'χ  '.Τελος ελεγχει για τις υποπεριπτώσεις
    και επιστρεφει μια αριθμητικη τιμή απο το 0-3
    με τις οποίες το πρόγραμμα θα μπορει να αναγνωρίσει
    την περίπτωση
    >>> check_cards(['K', '♠', 10, 'K♠  ', 'x   '],['K', '♣', 10, 'K♣  ', 'x   '],1,[0,0,0,0])
    1
    >>> check_cards(['2', '♠', 10, 'K♠  ', 'x   '],['2', '♣', 10, 'K♣  ', 'x   '],1,[0,0,0,0])
    Επιτυχές ταίριασμα +10 πόντοι! Παίκτη 2 έχεις συνολικά 10  πόντους
    0
    """
    if (first_open_card[0]=="K" and second_open_card[0]=="K") or (first_open_card[0]=="K" and second_open_card[0]=="Q") or (first_open_card[0]=="Q" and second_open_card[0]=="K") or (first_open_card[0]=="J" and second_open_card[0]=="J"):
        if (first_open_card[0]=="K" and second_open_card[0]=="K"):
            counter=1
            return counter
        elif (first_open_card[0]=="K" and second_open_card[0]=="Q") or (first_open_card[0]=="Q" and second_open_card[0]=="K"):
            counter=2
            return counter
        elif(first_open_card[0]=="J" and second_open_card[0]=="J"):
            counter=3
            return counter
    else:
        if first_open_card[0]==second_open_card[0]:
            scoreboard[paiktis]+=first_open_card[2]
            print("Επιτυχές ταίριασμα +"+str(first_open_card[2])+" πόντοι! Παίκτη "+str(paiktis+1)+" έχεις συνολικά "+str(scoreboard[paiktis])," πόντους")
        else:
            first_open_card[4]="x   " #Ξαναγυρνάμε ανάποδα τα φύλλα εφόσον δεν ταίριαξαν
            second_open_card[4]="x   "
        counter=0
        return counter

def score_eval(scoreboard):
    """ Συγκρίνει τα τελικά σκορ 
    και ανακοινώνει τον νικητή.
    >>> score_eval([10,20,30,40])
    Ο παίκτης  4  κέρδισε με 40  πόντους!
    >>> score_eval([40,40,40,40])
    Ισοπαλία μεταξυ παικτών 1 2 3 4 Με 40 ο καθένας.
    """
    if scoreboard.count(max(scoreboard))==1:
        winner=scoreboard.index(max(scoreboard))
        print('Ο παίκτης ',str(winner+1),' κέρδισε με',str(max(scoreboard)),' πόντους!')
    else:
        output="Ισοπαλία μεταξυ παικτών "
        winner=max(scoreboard)
        for s in range(len(scoreboard)):
            if winner==scoreboard[s]:
                output+=str(s+1)+' '
        output+="Με "+str(max(scoreboard))+" ο καθένας."
        print(output)

def check_board(pinakas):
    """ Σύμφωνα με το μηχανισμό που χρησημοποιείται
    εαν το τρίτο στοιχείο desc μιας κάρτας είναι
    ίσο με το τέταρτο back τότε αυτή η καρτα είναι
    σηκωμένη. Αυτή η συνάρτηση ελέγχει εαν όλες
    οι κάρτες είναι σηκωμένες εαν ειναι επιστρέφει True
    και λόγω συνθήκης του προγράμματος τελειώνει το παιχνίδι
    >>> deck=deck_maker(1)
    >>> board=nested_board(deck,1)
    >>> check_board(board)
    False
    """
    for quad in pinakas:
        for item in quad:
           if  item[4]!=item[3] :
                return False
    return True