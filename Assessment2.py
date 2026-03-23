import contest #this imports my custom library
import re      #import allows for support working with regex
import random   # allows me to make random number generators for random events
import csv          # allows me to implement classes and work in csv format
pos = ["1", "2", "3", "4", "5"]   #here are my 2 lists, outside my main function so it is convenient to call and use them
cont = ["Bella", "Charlie", "Kian", "Max", "Zak"]
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # this list is for the points per topic
ha = contest.host["name"]  #accessing data from dictionary from custom import
def main():
    print("Hello everyone and welcome to ...\nThe Big Pub Quiz!")
    
    print(ha + ": I am your host " + ha)
    def incorrect():
        print(ha + ": Incorrect\n You score 0 points for this question")
        
    def forward():
        choice = input(ha + ": Would you like to continue? ")
        if choice == "yes":
                print(ha + ": Great, on we go!")
                topics()
        elif choice == "no":
                print(ha + ": GAME OVER")
                print("SHUTTING DOWN ...")

        else:   
                print(ha + ": Invalid input")
                forward()
        
    def pick22():   #a function that gets called later, allows player to continue or end game
        pick2 = input(ha + ": Are you ready for the categories? ")
        if pick2 == "yes":
                print(ha + ": Wonderful, let's get on with the games!")
                topics() #function is later in code
        elif pick2 == "no":
                print(ha + ": GAME OVER")
                print("SHUTTING DOWN ...")

        else:   
                print(ha + ": Invalid input")
                pick22()
    def age(): #this function also gets called later
        x = (input("Age: "))
        xx = re.sub(r'[^0-9 ]', '', x) #regex used to ensure only numbers are recieved
        #any added characters such as letters or symbols are discarded
        if xx == "": #used empty apostrophe as if only letters or symbols input, stored input would be blank
            #made it so i can have user retry input
            print(ha + ": Invalid input")
            age()
            
        else:
            print(ha + ": Confirmed age is " + xx)
            contest.cont6.update({"age": xx}) #when input confirmed as only number, updates data in dictionary
            
    def intro(): #also function that gets called later, allows player to continue or end game
                 #additionally, has the intro to the game with interactive start-up
        pick1 = input(ha + ": Would you like to continue? ")

        if pick1 == "yes": #runs code if player chooses to continue

            print(ha + ": Here are your contestants for the night:")
            #previusly i accessed dictionary data and made it equal to a variable to then add to a print function
            #cut out middle-man and added dictinary data access code straight in the print function
            print(pos[0], ": "+ cont[0] + " " + str(contest.cont1["age"])) #calls both list positions and dictionary data from custom import
            print(pos[1], ": "+ cont[1] + " " + str(contest.cont2["age"]))
            print(pos[2], ": "+ cont[2] + " " + str(contest.cont3["age"]))
            print(pos[3], ": "+ cont[3] + " " + str(contest.cont4["age"]))
            print(pos[4], ": "+ cont[4] + " " + str(contest.cont5["age"]))
            print(ha + ": And finally, our special guest for the evening: ")
            y = input("Name: ").capitalize() #make sure input has no added spaces or error adds
            yy = re.sub(r'[^a-zA-Z ]', '', y).capitalize() #regex, makes input limited to letters and captilizes first word
                                                           #gets rid of symbols and numbers
            def hello(to="world"):   #example of testing without just printing something, using a def function
                print(ha + ": Hello ", to)   #this will greet player after inputting chosen name
            if __name__ == "__intro__":
                intro()

            hello(yy) #calls the greeting def function

            age()  #calls age function from earlier
            z = input("Country: ") 
            zz = re.sub(r'[^a-zA-Z ]', '', z).capitalize() #regex similar written code as earlier
            print(ha + ": Confirmed country is " + zz)
            contest.cont6.update({"name": yy})  #updates data in specific dictionary, stores new data
            contest.cont6.update({"country": zz}) #updates data in specific dictionary, stores new data
            
            pos.append("6") #adds to position number list
            cont.append(yy) # adds to contestant name list, now parallel with number above
            points.append(0)
            cont6 = input(ha + ": How are we all feeling contestants? ") #prompts plaer input
            cont66 = re.sub(r'[^a-zA-Z ]', '', cont6).capitalize() #regex aims to remove input errors
            contest.cont6.update({"feeling": cont66}) #updates data in specific dictionary, stores new data
            #previusly i accessed dictionary data and made it equal to a variable to then add to a print function
            #cut out middle-man and added dictinary data access code straight in the print function
            print(cont[0],": " + contest.cont1["feeling"]) 
            print(cont[1],": " + contest.cont2["feeling"]) 
            print(cont[2],": " + contest.cont3["feeling"]) 
            print(cont[2],": " + contest.cont4["feeling"]) 
            print(cont[4],": " + contest.cont5["feeling"]) 
            print(cont[5],": " + contest.cont6["feeling"])
           
            pick22() #calls function 
                    
        elif pick1 == "no": #prints and ends code
            print(ha + ": GAME OVER")
            print("SHUTTING DOWN ...")
            

        else: #if neither "yes" or "no" are input, makes user try again
            print(ha + ": Invalid input")
            intro() #calls back to start of def function where choice to continue or end

    def science(): #currently empty functions soon to be filled with questions and answers, not sure how I will display this tho
        print(ha + ": You have chosen " + contest.topics["1"]) # considering I am grabbing dictionaries, probs should add to said dictionaries
        print(ha + ": What is the most abundant gas in the Earth's atmosphere? ")
        print("A: " + contest.science1["A"])
        print("B: " + contest.science1["B"])
        print("C: " + contest.science1["C"])
        print("D: " + contest.science1["D"])
        answr = input("Choice: ").strip().capitalize()
        if answr == "B":
            print(ha + ": " + contest.science1["B"] + " is correct")
            print(ha + ": You have won 10 points")
            points[0] = 10
            forward()
        elif answr == "A" or answr == "C" or answr == "D":
            incorrect()
            forward()
        else:
            incorrect()
            forward()
         

    def maths():
        print(ha + ": You have chosen " + contest.topics["2"]) 
        print(ha + ": The product of which 2 options, makes 64?\n Answer for each must be a one of the provided numbers")
        print("A: " + contest.maths1["A"])
        print("B: " + contest.maths1["B"])
        print("C: " + contest.maths1["C"])
        print("D: " + contest.maths1["D"])
        a = int(input("Choice: "))
        b = int(input("Choice: "))
        product = lambda a, b: a * b  #defines a small anonymous function, takes 2 inputs and returns product
        print(f"The product is: {product(a, b)}") #prints product
        if a == 16 and b == 4:
            print(ha + ": Correct you have won 10 points")
            points[1] = 10
            forward() #calls function to determine if game continues
        if a == 4 and b == 16:
            print(ha + ": Correct you have won 10 points")
            points[1] = 10
            forward()

        if a == "" or b == "":
            incorrect()
            forward()
        else:
            incorrect()
            forward()

    def pop_culture():
        print(ha + ": You have chosen " + contest.topics["3"])
        print(ha + ": What year was the first animated transformers film released? ")
        print("A: " + contest.pop1["A"])
        print("B: " + contest.pop1["B"])
        print("C: " + contest.pop1["C"])
        print("D: " + contest.pop1["D"])
        answr = input("Choice: ").strip().capitalize()
        if answr == "C":
            print(ha + ": " + contest.pop1["C"] + " is correct")
            print(ha + ": You have won 10 points")
            points[2] = 10
            forward()
        elif answr == "A" or answr == "B" or answr == "D":
            incorrect()
            forward()
        else:
            incorrect()
            forward()

    def mystery_round():
        print(ha + ": You have chosen " + contest.topics["4"])
        print(ha + ": Fill in the missing lyric to this Bruno Mars song: ")
        print("24-karat _____ in the air")
        answr = input("Answer: ")
        answrr = re.sub(r'[^a-zA-Z ]', '', answr).strip()
        if answr == "magic":
            print(ha + ": " + answrr + " is correct")
            print(ha + ": You have won 10 points")
            points[3] = 10
            forward()
        else:
            incorrect()
            forward()

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
    

    def topics(): #produces lis of categories which players can choose
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
        randcont() #calls function
    def randcont():
        numb1 = random.randrange(1, 6) #picks a random numbe btween 1-6 representing contestants
        print(ha + ": We will start with contestant number "  + str(numb1))
        if numb1 == 1 or numb1 == 2 or numb1 == 3 or numb1 == 4 or numb1 == 5: #formatting like this 
            #meant less repeated lines of similar code
            print(ha + ": Which topic would you like contestant " + str(numb1) + "? ")
            choice1_5() #as 1-5 arent users, I call this function
        
        if numb1 == 6: #this is user number
            choice6() #calls this function
        else:
            print("")
            

    def choice1_5():
        #number = random.randint(1, 10) # random number generator to pick 1 of the 10 topics at random
        number = 2
        #so the game is never completely the same each time
        print(ha + ": Contestant has chosen: " + str(number))
        
        if number == 1:
            science() #each one of these calls a specific topic function
           
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
            print(ha + ": Experiencing technical issue") #added this as keep getting issue where code finishes
            #on this print output when it isn't meant to

            
    def choice6():
        numbrr = input(ha + ": Which topic would you like contestant 6? ")
        numbr = re.sub(r'[^0-9 ]', '', numbrr)
        print(ha + ": You chose: " + str(numbr)) #asks user to choose a topic and depending on input
        #depends on which category
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