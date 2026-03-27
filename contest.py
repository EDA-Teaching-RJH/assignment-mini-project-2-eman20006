import random
ha = "Tim Host"

topics = {              #dictionary of the 10 topic choices
    "1": "Science",
    "2": "Maths",
    "3": "Pop Culture",
    "4": "Mystery round", 
    "5": "General Knowledge",
    "6": "Food",
    "7": "Animals",
    "8": "Music",
    "9": "History",
    "10": "Sport"
}

prize = {        #dictionary of list of prizes
"1": "£10 gift voucher",
"2": "£50,000 cash prize",
"3": "A Mystery holiday",
"4": "A year supply deodorant",
"5": "A house",
"6": "A new bike",
"7": "A new pair of socks",
"8": "A car",
"9": "Tickets to a movie premiere",
"10": "A year supply of Nike shoes"
}
def incorrect():
        print(ha + ": Incorrect\n You score 0 points for this question") #first try at having a function in my custom library
#def randpoint():  #don't need this function as found a short cut which worked better on my main file
       # numb1 = random.randrange(0, 100,10)   prints random number from 0 to 100 in intervals of 10
       # print(numb1)  
def game_finish():   
    print(ha + ": Enjoy your prize.\nThank you for playing the Big Pub Quiz.")   #congratulates and ends game
    print("GAME END\nSHUTTING DOWN")
    quit()
def prize_collect():
    spins = random.randrange(1, 11) #generate number from 1 to 10
    if spins == 1:       #number correlates to a prize which is printed as won, then calls game finish function
         print(ha + ": You have won " + prize["1"]) 
         game_finish()
    elif spins == 2:
        print(ha + ": You have won " + prize["2"]) 
        game_finish()
    elif spins == 3:
         print(ha + ": You have won " + prize["3"]) 
         game_finish()
    elif spins == 4:
         print(ha + ": You have won " + prize["4"]) 
         game_finish()
    elif spins == 5:
         print(ha + ": You have won " + prize["5"]) 
         game_finish()
    elif spins == 6:
         print(ha + ": You have won " + prize["6"]) 
         game_finish()
    elif spins == 7:
         print(ha + ": You have won " + prize["7"]) 
         game_finish()
    elif spins == 8:
         print(ha + ": You have won " + prize["8"]) 
         game_finish()
    elif spins == 9:
         print(ha + ": You have won " + prize["9"]) 
         game_finish()
    elif spins == 10:
         print(ha + ": You have won " + prize["10"]) 
         game_finish()
def spin_wheel():
       spin = input("Would you like to spin the wheel? ")
       if spin == "yes":
        prize_collect()    #calls function prize collect function
       elif spin == "no":
        print(ha + ": You have forfeited your spin.")
        print("GAME OVER")   #ends game based on user input
        quit()
       else: 
        print("Invalid input")
        spin_wheel() #calls spin wheel function, loops if input isn't yes or no
def spin_prize():
       print(ha + ": Here are the prizes:")
       print("1. " + prize["1"])
       print("2. " + prize["2"])    #prints out variables from dictionary and calls a function
       print("3. " + prize["3"])
       print("4. " + prize["4"])
       print("5. " + prize["5"])
       print("6. " + prize["6"])
       print("7. " + prize["7"])
       print("8. " + prize["8"])
       print("9. " + prize["9"])
       print("10. " + prize["10"])
       print(ha + ": SPIN THAT WHEEL")
       spin_wheel()
def loss():
    print(ha + ": Unfortunately your score has been beaten!") #worked out how to access parts of dictionary in library
    print(ha+ ": That is GAME OVER for you!") #function says player loses and ends game
    print(ha + ": Better luck next time")
    print("SHUTTING DOWN")
    quit()
def tie():
    print(ha + ": It's a tie, we have multiple winners!")   #function with simple prints and calls another function
    print(ha + ": In that case lets spin the prize wheel!")
    spin_prize()
def win():
    print(ha + ": You are the winner")  #function with simple prints and calls another function
    print(ha + ": Time for you to spin the prize wheel!")
    spin_prize()