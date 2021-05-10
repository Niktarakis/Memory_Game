from Memory_Game_Functions import *
print('Καλωσήλθατε στο Matching Game')
while True: #Πρώτα ελέγχουμε εαν είναι σωστο το input  του αριθμού παικτών
    players=input("Δώστε αριθμό παικτών: ")
    if players.isnumeric() and eval(players)>1: #Με την χρήση της str.isnumeric() εξετάζουμε αν η είσοδος του χρήστη είναι ακέραιος θετικός αφου οι αρνητικοί και οι ακέραιοι έχουν σύμβολα στην αναπαράσταση τους.  
        break
    else:
        print("Λάθος είσοδος, ξαναπροσπάθησε")
        continue
players=eval(players) #Κάνουμε τον αριθμό των παιχτών int εφοσον αρχικά είναι str. Αυτο το κάνουμε γιατί θα χρειαστεί παρακάτω
while True: #Ελέγχουμε το input του χρήστη αυτη την φορά για τον βαθμό δυσκολίας
    difficulty=input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3): ") #με την eval() μετατρέπουμε την είσοδο σε int και εξεταζουμε αν είναι αποδεκτή η τιμή.
    if difficulty.isnumeric():
        difficulty=eval(difficulty)
        if difficulty==1 or difficulty==2 or difficulty==3:
            break
        else:
            print("Λάθος είσοδος, ξαναπροσπάθησε")
            continue
    else:
        print("Λάθος είσοδος, ξαναπροσπάθησε")
        continue
active_deck=deck_maker(difficulty) #δημιουργούμε την τράπουλα
pinakas=nested_board(active_deck,difficulty) #ανακατεύουμε τα φύλλα και τα βάζουμε σε ενα πίνακα που έχει την μορφή εμφολιασμένων λιστών
score=[0 for i in range(players)] #φτιάχνουμε λίστα με τον απαραίτητο αριθμό αρχικων σκόρ παιχτών "αρχικο σκορ ειναι 0".
open_board(pinakas)
for quad in pinakas:
        for item in quad:
            item[4]='x   '
anaparastasi_pinaka(pinakas) #Τυπώνεται κλειστός ο πίνακας
count=0 #Μετρητής που θα βοηήσει στην διαφοροποίηση των ειδικών περιπτώσεων
while True: # Η βασική επανάληψη μέσα στην οποία θα τρέχει ολο το παιχνίδι
    if check_board(pinakas):#Η συνάρτηση αυτή επιστρέφει True εαν όλα τα χαρτιά είναι ανοιχτά
        break # και η βασικη επανάληψη σπάει
    for i in range(players): #Με αυτήν την for θα ξεχωρίζετε ο γύρος καθε παίκτη. Να σημειωθεί οτι η ένδειξη του καθε παίκτη "0,1,2..." θα αντιχτοιχίζεται με την ένδειξη στην λίστα με τα σκορ 
        if check_board(pinakas):#Αυτός ο ελεγχος υπάρχει για τις περιπτώσεις που δεν τελείωνει η for ενώ ανοιγουν όλα τα φύλλα
            break
        while True: #Αυτη η επανάληψη σπαέι σε καθε περιπτωση εκτος απο οταν ο μετρητής count ειναι 3 οπου ο παικτης ξαναπαίζει μια φορά
            if count==0 or count==3:
                count=0 #O μετρητής ξαναγινεται 0 γιατι αμα παραμείνει 3 ο παικτης θα παίζει για πάντα 
                #---------επιλογή 1ης κάρτας-------#
                while True: #Μέσα στην επιλογή γίνονται δύο ελέγχοι. Άμα το input είναι στο σωστό format αλλά και αν το χαρτί που επιλέκτηκε δεν είναι ήδη ανοιχτό
                    while True: #αυτή η while θα τρέχει μέχρι να πάρει σωστό input και να γινει break ενώ η απο πάνω μέχρι να σηκωθεί μια κλειστή κάρτα
                        card1=input('Παίκτη '+str(i+1)+': Δώσε γραμμή και στήλη πρώτης κάρτας (πχ 1 10): ')
                        if check_input(card1,difficulty):
                            break
                        else:
                            print ("Λάθος στοιχεία για επιλογή κάρτας, δοκιμάστε ξανά")
                            continue
                    if elegxos_anoixtis_kartas(pinakas,card_input(card1)[0],card_input(card1)[1]):
                        break
                    else :
                        print("Η κάρτα είναι ήδη ανοικτή, δοκιμάστε ξανά")
                #----------------------------------#
                protikarta=open_card(pinakas,card_input(card1)[0],card_input(card1)[1]) #Με την open_card ανοίγουμε την κάρτα προσδιορίζεται απο τις συντεταγμένες που επιστρέφει η card_input()
                anaparastasi_pinaka(pinakas) #Ο πίνακας εμφανίζεται με το επιλεγμενο φύλλο ανοιχτό
                #---------επιλογή 2ης κάρτας-------#
                while True: #Παρόμοια διαδικασία με την επιλογή της πρώτης κάρτας
                    while True:
                        card2=input('Παίκτη '+str(i+1)+': Δώστε γραμμή και στήλη δεύτερης κάρτας: ')
                        if check_input(card2,difficulty):
                            break
                        else:
                            print ("Λάθος στοιχεία για επιλογή κάρτας, δοκιμάστε ξανά")
                            continue
                    if elegxos_anoixtis_kartas(pinakas,card_input(card2)[0],card_input(card2)[1]):
                        break
                    else :
                        print("Η κάρτα είναι ήδη ανοικτή, δοκιμάστε ξανά")
                #----------------------------------#
                defterikarta=open_card(pinakas,card_input(card2)[0],card_input(card2)[1])#Με την open_card ανοίγουμε την κάρτα προσδιορίζεται απο τις συντεταγμένες που επιστρέφει η card_input()
                anaparastasi_pinaka(pinakas) #Ο πίνακας τυπώνεται με τα δύο ανοιχτα φύλλα 
                if check_cards(protikarta,defterikarta,i,score)==0 :#Η τυπική περπίτωση
                    anaparastasi_pinaka(pinakas)
                    break
                elif check_cards(protikarta,defterikarta,i,score)==1:# Ο παίκτης σηκωσε Κ Κ
                    #Σε αυτη και στις άλλες υποπεριπτώσεις γραφουμε ξεχωριστά το μηνυμα τεριάσματος και δινουμε τους πόντους για να αποφήγουμε σφάλμα 
                    score[i]+=protikarta[2]
                    print("Επιτυχές ταίριασμα +"+str(protikarta[2])+" πόντοι! Παίκτη "+str(i+1)+" έχεις συνολικά "+str(score[i])," πόντους")
                    anaparastasi_pinaka(pinakas)
                    count=1 
                    break
                elif check_cards(protikarta,defterikarta,i,score)==2:#Ο παικτης σήκωσε Κ Q ή Q K και επιέγει τρίτο φυλλο
                    #---------επιλογή 3ης κάρτας-------#
                    while True:#Παρόμοια διαδικασία με την επιλογή της πρώτης κάρτας
                        while True:
                            card3= input('Παίκτη '+str(i+1)+': Δώστε γραμμή και στήλη τρίτης κάρτας: ')
                            if check_input(card3,difficulty):
                                break
                            else:
                                print("Λάθος στοιχεία για επιλογή κάρτας, δοκιμάστε ξανά")
                                continue
                        if elegxos_anoixtis_kartas(pinakas,card_input(card3)[0],card_input(card3)[1]):
                            break
                        else:
                            print("Η κάρτα είναι ήδη ανοικτή, δοκιμάστε ξανά")
                    #----------------------------------#
                    trithkarta=open_card(pinakas,card_input(card3)[0],card_input(card3)[1])
                    anaparastasi_pinaka(pinakas)
                    #Σε αυτη και στις άλλες υποπεριπτώσεις γραφουμε ξεχωριστά το μηνυμα τεριάσματος και δινουμε τους πόντους για να αποφήγουμε σφάλμα 
                    #Ειδικός έλεγχος μεταξύ τριών καρτών
                    if trithkarta[0]=="K":
                        if check_cards(protikarta,trithkarta,i,score)==1:
                            score[i]+=trithkarta[2]
                            print("Επιτυχές ταίριασμα +"+str(trithkarta[2])+" πόντοι! Παίκτη "+str(i+1)+" έχεις συνολικά "+str(score[i])," πόντους")
                            defterikarta[4]="x   "
                        elif check_cards(defterikarta,trithkarta,i,score)==1:
                            score[i]+=trithkarta[2]
                            print("Επιτυχές ταίριασμα +"+str(trithkarta[2])+" πόντοι! Παίκτη "+str(i+1)+" έχεις συνολικά "+str(score[i])," πόντους")
                            protikarta[4]="x   "
                        count=1
                    elif trithkarta[0]=="Q":
                        if check_cards(protikarta,trithkarta,i,score)==0:
                            defterikarta[4]="x   "
                        elif check_cards(defterikarta,trithkarta,i,score)==0:
                            protikarta[4]="x   "
                    else:
                        trithkarta[4]="x   "
                        defterikarta[4]="x   "
                        protikarta[4]="x   "
                    anaparastasi_pinaka(pinakas)
                    break
                elif check_cards(protikarta,defterikarta,i,score)==3:#Ο παίκτης σήκωσε J J και ξαναπαίζει 
                    #Σε αυτη και στις άλλες υποπεριπτώσεις γραφουμε ξεχωριστά το μηνυμα τεριάσματος και δινουμε τους πόντους για να αποφήγουμε σφάλμα 
                    score[i]+=protikarta[2]
                    print("Επιτυχές ταίριασμα +"+str(protikarta[2])+" πόντοι! Παίκτη "+str(i+1)+" έχεις συνολικά "+str(score[i])," πόντους")
                    if check_board(pinakas):
                        break
                    print("Παίκτης "+str(i+1)+" ξανά παίζεις" )
                    count=3    
            elif count==1: #Ο μετρητής είναι 1 άρα ο επόμενος θα χάσει τη σειρά του
                if check_board(pinakas):#Αυτος ο έλεγχος γίνεται για να τελειώσει το παιχνίδι και να μην εμφανιστεί μήνυμα
                    break 
                print("ο παίκτης "+str(i+1)+" έχασε την σείρα του" )
                count=0
                break
score_eval(score)
