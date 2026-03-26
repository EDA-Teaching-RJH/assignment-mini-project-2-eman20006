
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



def incorrect():
        print(host["name"] + ": Incorrect\n You score 0 points for this question") #first try at having a function in my custom library

def randpoint():
        numb1 = random.randrange(0, 100,10)
        print(numb1)  

def wheels_spin():
       
       print(sport1["A"])

def loss():
            print(host["name"] + ": Unfortunately your score has been beaten!") #worked out how to access parts of dictionary in library
            print(host["name"] + ": That is GAME OVER for you!")
            print(host["name"] + ": Better luck next time")
            print("SHUTTING DOWN")
            quit()

def tie():
    print(host["name"] + ": It's a tie, we have multiple winners!")
    print(host["name"] + ": In that case lets spin the prize wheel!")

def win():
    print(host["name"] + ": You are the winner")
    print(host["name"] + ": Time for you to spin the prize wheel!")
