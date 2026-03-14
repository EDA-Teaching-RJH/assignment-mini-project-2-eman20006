import contest
import re    
import random
pos = ["1", "2", "3", "4", "5"]
cont = ["Bella", "Charlie", "Kian", "Max", "Zak"]
 
def main():

    def intro():
        print("Hello everyone and welcome to\n...\nThe Big Pub Quiz!")
        ha = contest.host["name"]
        print("I am your host: " + ha)
        print("Here are your contestants for the night:")
        aa = contest.cont1["age"]
        bb = contest.cont2["age"]
        cc = contest.cont3["age"]
        dd = contest.cont4["age"]
        ee = contest.cont5["age"]
        print(pos[0], ": "+ cont[0] + " " + str(aa))
        print(pos[1], ": "+ cont[1] + " " + str(bb))
        print(pos[2], ": "+ cont[2] + " " + str(cc))
        print(pos[3], ": "+ cont[3] + " " + str(dd))
        print(pos[4], ": "+ cont[4] + " " + str(ee))
        print("And finally, our special guest for the evening: ")
        y = input("Name: ") #make sure input has no added spaces or error adds
        x = input("Age: ") #same as above but make just numbers
        z = input("Country: ") #same as for name
        contest.cont6.update({"name": y})
        contest.cont6.update({"age": x})
        contest.cont6.update({"country": z})
        
        res1 = re.sub(r'[^a-zA-Z0-9 ]', '', y).capitalize()
        pos.append("6")
        cont.append(res1)
        cont6 = input("How are we all feeling contestants? ")
        res2 = re.sub(r'[^a-zA-Z0-9 ]', '', cont6).capitalize()
        contest.cont6.update({"feeling": res2})
        a = contest.cont1["feeling"]
        b = contest.cont2["feeling"]
        c = contest.cont3["feeling"]
        d = contest.cont4["feeling"]
        e = contest.cont5["feeling"]
        
        print(cont[0],": " + a) 
        print(cont[1],": " + b) 
        print(cont[2],": " + c) 
        print(cont[2],": " + d) 
        print(cont[4],": " + e) 
        print(cont[5],": " + res2)
        print("Wonderful, let's get on with the games!")
        topics()


    def science():
        print(" You have chosen " + contest.topics["1"])
        
    def maths():
        print("You have chosen " + contest.topics["2"])
    
    def pop_culture():
        print("You have chosen " + contest.topics["3"])

    def mystery_round():
        print("You have chosen " + contest.topics["4"])

    def general_knowledge():
        print("You have chosen " + contest.topics["5"])

    def food():
        print("You have chosen " + contest.topics["6"])

    def animals():
        print("You have chosen " + contest.topics["7"])

    def music():
        print("You have chosen " + contest.topics["8"])

    def history():
        print("You have chosen " + contest.topics["9"])

    def sport():
        print("You have chosen " + contest.topics["10"])
    

    def topics():
        print("Here are your categories:")
        print("1." + contest.topics["1"])
        print("2." + contest.topics["2"])
        print("3." + contest.topics["3"])
        print("4." + contest.topics["4"])
        print("5." + contest.topics["5"])
        print("6." + contest.topics["6"])
        print("7." + contest.topics["7"])
        print("8." + contest.topics["8"])
        print("9." + contest.topics["9"])
        print("10." + contest.topics["10"])

        numb1 = random.randint(1, 6)
        print("We will start with contestant number "  + str(numb1))
        if numb1 == 1:
            print("Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 2:
            print("Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 3:
            print("Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 4:
            print("Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 5:
            print("Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 6:
            choice6()
        else:
            print("Technical difficulty")
            

    def choice1_5():
        number = random.randint(1, 10)
        print("Contestant has chosen: " + str(number))
        if number == 1:
            science()
           
        elif number == 2:
            maths()
           
        elif number == 3:
            pop_culture()
            

        elif number == 4:
            mystery_round()
            

        elif number == 5:
            general_knowledge()
            

        elif number == 6:
            food()
            

        elif number == 7:
            animals()
            

        elif number == 8:
            music()
            

        elif number == 9:
            history()
            
        elif number == 10:
            sport()

        else:
            print("Experiencing technical issue")
            
        
    def choice6():
        numbr = input("Which topic would you like contestant 6? ")
        print("You chose: " + str(numbr))
        if numbr == 1:
            science()

        elif numbr == 2:
            maths()

        elif numbr == 3:
            pop_culture()

        elif numbr == 4:
            mystery_round()

        elif numbr == 5:
            general_knowledge()

        elif numbr == 6:
            food()

        elif numbr == 7:
            animals()

        elif numbr == 8:
            music()

        elif numbr == 9:
            history()

        elif numbr == 10:
            sport()

        else:
            print("Please stand by")

    intro()

    
    
   
main()