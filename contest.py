
import random
ha = "Tim Host"

host = {
    "name": "Tim Host",     
    "age": 42,              
    "country": "England"    
}

cont1 = {
    "name": "Bella Spooner",   
    "age": 24,              
    "country": "Germany",   
    "feeling": "Confident",  
    "favesubj": "Food"      
}

cont2 = {
    "name": "Charlie Beer",
    "age": 36,  
    "country": "France",
    "feeling": "A little nervous",
    "favesubj": "Sport"
}

cont3 = {
    "name": "Kian Franklin",
    "age": 28,  
    "country": "England",
    "feeling": "Good thank you",
    "favesubj": "History"
}

cont4 = {
    "name": "Max Hilling",
    "age": 31,  
    "country": "Greece",
    "feeling": "Ready-ish",
    "favesubj": "Pop Culture"
}

cont5 = {
    "name": "Zak Cuts",
    "age": 25,  
    "country": "Spain",
    "feeling": "Good",
    "favesubj": "Animals"
}

cont6 = {
    "name": "Unkown",
    "age": "Unknown",  
    "country": "Unknown",
    "feeling": "Unknown",
    "favesubj": "Uknown"
}

topics = {
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

maths1 = {
"A": "16",
"B": "8",
"C": "4",
"D": "14"
}

science1 = {
"A": "Oxygen",
"B": "Nitrogen",
"C": "Carbon Dioxide",
"D": "Hydrogen"
}

pop1 = {
"A": "1991",
"B": "1979",
"C": "1986",
"D": "2003"
}

general1 = {
"A": "Auguste Rodin",
"B": "Michelangelo",
"C": "Gian Lorenzo Bernini",
"D": "Donatello"
}

food1 = {
"A": "Walnut",
"B": "Cashew",
"C": "Hazlenut",
"D": "Almond"
}

animal1 = {
"A": "Lion",
"B": "Cheetah",
"C": "Leopard",
"D": "Pronghorn"
}

music1 = {
"A": "System of a down",
"B": "Hum",
"C": "Fontaines D.C",
"D": "Pierce the Veil"
}

history1 = {
"A": "1044",
"B": "1060",
"C": "1116",
"D": "1066"
}

sport1 = {
"A": "Germany",
"B": "Italy",
"C": "Brazil",
"D": "Argentina"
}

prize = {
"1": "£10 gift voucher",
"2": "£1000 cash prize",
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
        print(host["name"] + ": Incorrect\n You score 0 points for this question") #first try at having a function in my custom library

def randpoint():
        numb1 = random.randrange(0, 100,10)
        print(numb1)  
    
def game_finish():
    print(host["name"] + ": Enjoy your prize")
    print("GAME END\nSHUTTING DOWN")
    quit()

def prize_collect():
    spins = random.randrange(1, 11) #generate number 1 to 10
    print(spins)
    if spins == 1:
         print(host["name"] + ": You have won" + prize[1]) 
         game_finish()
    elif spins == 2:
        print(host["name"] + ": You have won" + prize[2]) 
        game_finish()
    elif spins == 3:
         print(host["name"] + ": You have won" + prize[3]) 
         game_finish()
    elif spins == 4:
         print(host["name"] + ": You have won" + prize[4]) 
         game_finish()
    elif spins == 5:
         print(host["name"] + ": You have won" + prize[5]) 
         game_finish()
    elif spins == 6:
         print(host["name"] + ": You have won" + prize[6]) 
         game_finish()
    elif spins == 7:
         print(host["name"] + ": You have won" + prize[7]) 
         game_finish()
    elif spins == 8:
         print(host["name"] + ": You have won" + prize[8]) 
         game_finish()
    elif spins == 9:
         print(host["name"] + ": You have won" + prize[9]) 
         game_finish()
    elif spins == 10:
         print(host["name"] + ": You have won" + prize[10]) 
         game_finish()

def spin_wheel():
       spin = input("Would you like to spin the wheel? ")
       if spin == "yes":
        prize_collect()
       elif spin == "no":
        print(host["name"] + ": You have forfeited your spin.")
        print("GAME OVER")
        quit()
       else: 
        print("Invalid input")
        spin_wheel()

def spin_prize():
       print(host["name"] + ": Here are the prizes:")
       print("1. " + prize["1"])
       print("2. " + prize["2"])
       print("3. " + prize["3"])
       print("4. " + prize["4"])
       print("5. " + prize["5"])
       print("6. " + prize["6"])
       print("7. " + prize["7"])
       print("8. " + prize["8"])
       print("9. " + prize["9"])
       print("10. " + prize["10"])
       print(host["name"] + ": SPIN THAT WHEEL")
       spin_wheel()
              


def loss():
            print(host["name"] + ": Unfortunately your score has been beaten!") #worked out how to access parts of dictionary in library
            print(host["name"] + ": That is GAME OVER for you!")
            print(host["name"] + ": Better luck next time")
            print("SHUTTING DOWN")
            quit()

def tie():
    print(host["name"] + ": It's a tie, we have multiple winners!")
    print(host["name"] + ": In that case lets spin the prize wheel!")
    spin_prize()

def win():
    print(host["name"] + ": You are the winner")
    print(host["name"] + ": Time for you to spin the prize wheel!")
    spin_prize()