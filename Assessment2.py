import contest
import re    
import random
import csv
pos = ["1", "2", "3", "4", "5"]
cont = ["Bella", "Charlie", "Kian", "Max", "Zak"]
ha = contest.host["name"]
def main():
    print("Hello everyone and welcome to ...\nThe Big Pub Quiz!")
    
    print(ha + ": I am your host " + ha)

    def pick22():
        pick2 = input(ha + ": Are you ready for the categories? ")
        if pick2 == "yes":
                print(ha + ": Wonderful, let's get on with the games!")
                topics()
        elif pick2 == "no":
                print(ha + ": GAME OVER")
                print("SHUTTING DOWN ...")

        else:   
                print(ha + ": Invalid input")
                pick22()
    def age():
        x = (input("Age: "))
        xx = re.sub(r'[^0-9 ]', '', x)
        print(ha + ": Confirmed age is " + xx)
        contest.cont6.update({"age": xx})
           
    def intro():
        
        pick1 = input(ha + ": Would you like to continue? ")

        if pick1 == "yes":

            print(ha + ": Here are your contestants for the night:")
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
            print(ha + ": And finally, our special guest for the evening: ")
            y = input("Name: ").capitalize() #make sure input has no added spaces or error adds
            yy = re.sub(r'[^a-zA-Z ]', '', y).capitalize()
            def hello(to="world"):
                print(ha + ": Hello ", to)
            if __name__ == "__intro__":
                intro()

            hello(yy)

            age()
            z = input("Country: ") #same as for name
            zz = re.sub(r'[^a-zA-Z ]', '', z).capitalize()
            print(ha + ": Confirmed country is " + zz)
            contest.cont6.update({"name": yy})
            contest.cont6.update({"country": zz})
            
            pos.append("6")
            cont.append(yy)
            cont6 = input(ha + ": How are we all feeling contestants? ")
            cont66 = re.sub(r'[^a-zA-Z ]', '', cont6).capitalize()
            contest.cont6.update({"feeling": cont66})
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
            print(cont[5],": " + cont66)
           
            pick22()
                    
        elif pick1 == "no":
            print(ha + ": GAME OVER")
            print("SHUTTING DOWN ...")
            

        else:
            print(ha + ": Invalid input")
            intro()

    def science():
        print(ha + ": You have chosen " + contest.topics["1"])
        
    def maths():
        print(ha + ": You have chosen " + contest.topics["2"])
    
    def pop_culture():
        print(ha + ": You have chosen " + contest.topics["3"])

    def mystery_round():
        print(ha + ": You have chosen " + contest.topics["4"])

    def general_knowledge():
        print(ha + ": You have chosen " + contest.topics["5"])

    def food():
        print(ha + ": You have chosen " + contest.topics["6"])

    def animals():
        print(ha + ": You have chosen " + contest.topics["7"])

    def music():
        print(ha + ": You have chosen " + contest.topics["8"])

    def history():
        print(ha + ": You have chosen " + contest.topics["9"])

    def sport():
        print(ha + ": You have chosen " + contest.topics["10"])
    

    def topics():
        print(ha + ": Here are your categories:")
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
        randcont()
    def randcont():
        numb1 = random.randrange(1, 6)
        print(ha + ": We will start with contestant number "  + str(numb1))
        if numb1 == 1:
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 2:
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 3:
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 4:
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 5:
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5()
        if numb1 == 6:
            choice6()
        else:
            print(ha + ": Technical difficulty")
            

    def choice1_5():
        number = random.randint(1, 10)
        print(ha + ": Contestant has chosen: " + str(number))
        
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
            print(ha + ": Experiencing technical issue")

            
    def choice6():
        numbr = input(ha + ": Which topic would you like contestant 6? ")
        print(ha + ": You chose: " + str(numbr))
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
            print(ha + ": Please stand by")

    intro()

    
    
   
main()