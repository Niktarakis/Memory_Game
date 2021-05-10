from Memory_Game_Functions import *
print('Welccome \n__________Matching Game__________')
while True: #tha eksetasoume an i eisodos toy programmatos einai apodekth  
    difficulty=eval(input("Choose game difficulty between Easy(1), Medium(2) and Hard(3): ")) #me tin eval eksasfalizete oti an i eisodos den einai int den tha prokipsei sfalma
    if difficulty==1 or difficulty==2 or difficulty==3:
        break
    else:
        print("Wrong input please try again")
        continue
while True:
    players=input("Number of players: ")
    if players.isnumeric():   #me tin xrisi tis string.isnumeric eksteazoume an i eisodos toy xrhsth einai akeraios thetikos afoy oi arnitikoi kai oi akeraioi exoun simvola stin apeikonisi toys
        break
    else:
        print("wrong input please try again")
        continue
active_deck=deck_maker(difficulty)
pinakas=nested_board(active_deck,difficulty)
while True:
    anaparastasi_pinaka(pinakas)
    break
