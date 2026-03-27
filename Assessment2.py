import contest #this imports my custom library
import re      #import allows for support working with regex
import random   # allows me to make random number generators for random events
import csv          # allows me to implement classes and work in csv format
pos = ["1", "2", "3", "4", "5"]   #here are my 2 lists, outside my main function so it is convenient to call and use them
cont = ["Bella", "Charlie", "Kian", "Max", "Zak"]
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # this list is for the points per topic
score = [0, 0, 0, 0, 0] #this is a list for each other contestant total
top = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #numbers related to topic amount
def main():
    with open("intro.txt") as intro_file:  #added a basic file which is read and printed for an intro
        print(intro_file.read()) 

    class Host:
        def __init__(self, name, age, country, favsubj):
            self.name = name
            self.age = age
            self.country = country
            self.favsubj = favsubj
    host = Host("Tim Host", 42, "England", "Sharks")

    class Contestant: #created a class for contestants and replaced the dictionaries from the contes.py file
        def __init__(self, name, age, country,feeling, favsubj): #makes it easier and neater to grab the information from the class
            self.name = name
            self.age = age
            self.country = country
            self.feeling = feeling
            self.favsubj = favsubj
    contestant1 = Contestant("Bella Spooner", 24, "Germany","Confident", "Food")
    contestant2 = Contestant("Charlie Beer", 36, "France","A little nervous", "Sport")
    contestant3 = Contestant("Kian Franklin", 28, "England","Good thank you", "History")
    contestant4 = Contestant("Max Hilling", 31, "Greece","Ready-ish", "Pop culture")
    contestant5 = Contestant("Zak Cuts", 25, "Spain","Good", "Animals")
    contestant6 = Contestant("Unknown", "Unknown", "Unknown","Unknown", "Unknown")

    class Topics:
        def __init__(self, A, B, C, D): #makes it easier and neater to grab the information from the class
            self.A = A
            self.B = B
            self.C = C
            self.D = D
    maths1 = Topics("16", "8", "4", "14")
    science1 = Topics("Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen")
    pop1 = Topics("1991", "1979", "1986", "2003")
    general1 = Topics("Auguste Rodin", "Michelangelo", "Gian Lorenzo Bernini", "Donatello")
    food1 = Topics("Walnut", "Cashew", "Hazlenut", "Almond")
    animal1 = Topics("Lion", "Cheetah", "Leopard", "Pronghorn")
    music1 = Topics("System of a down", "Hum", "Fontaines D.C", "Pierce the Veil")
    history1 = Topics("1044", "1060", "1116", "1066")
    sport1 = Topics("Germany", "Italy", "Brazil", "Argentina")
    
    def forward():
        choice = input(host.name + ": Would you like to continue? ")
        if choice == "yes":
                print(host.name + ": Great, on we go!")
                randcont()
        elif choice == "no":
                print(host.name + ": GAME OVER")
                print("SHUTTING DOWN ...")
                quit()
        else:   
                print(host.name + ": Invalid input")
                forward()
        
    def pick22():   #a function that gets called later, allows player to continue or end game
        pick2 = input(host.name + ": Are you ready for the categories? ")
        if pick2 == "yes":
                print(host.name + ": Wonderful, let's get on with the games!")
                print(host.name + ": Unless specified, answer each question via the letter corresponding the answer.\nFailure to do so will result in 0 points on that question, regardless of a right answer.")
                topics() #function is later in code
        elif pick2 == "no":
                print(host.name)
                print("SHUTTING DOWN ...")
        else:   
                print(host.name)
                pick22()

    def age(): #this function also gets called later
        x = (input("Age: "))
        xx = re.sub(r'[^0-9 ]', '', x) #regex returns a match for any digit between 0-9
        #any added characters such as letters or symbols are discarded
        if xx == "": #used empty apostrophe as if only letters or symbols input, stored input would be blank
            #made it so i can have user retry input
            print(host.name + ": Invalid input")
            age()
        else:
            print(host.name + ": Confirmed age is " + xx)
            contestant6.name  = xx 
    def troop():
            pick1 = input(host.name + ": Would you like to continue? ").strip()
            if pick1 == "yes": #runs code if player chooses to continue
                print(host.name + ": Here are your contestants for the night:")
                #previusly i accessed dictionary data and made it equal to a variable to then add to a print function
                #cut out middle-man and added dictinary data access code straight in the print function
                print(pos[0], ": "+ contestant1.name + " " + str(contestant1.age)) #calls both list positions and dictionary data from custom import
                print(pos[1], ": "+ contestant2.name + " " + str(contestant2.age))
                print(pos[2], ": "+ contestant3.name + " " + str(contestant3.age))
                print(pos[3], ": "+ contestant4.name + " " + str(contestant4.age))
                print(pos[4], ": "+ contestant5.name + " " + str(contestant5.age))
                print(host.name + ": And finally, our special guest for the evening: ")
                y = input("Name: ").capitalize() #make sure input has no added spaces or error adds
                yy = re.sub(r'[^a-zA-Z ]', '', y).capitalize() #regex, returns a match for letters a to z upper and lower, code also captilizes first word
                                                            #gets rid of symbols and numbers
                def hello(to="world"):   #example of testing without just printing something, using a def function
                    print(host.name + ": Hello ", to)   #this will greet player after inputting chosen name
                if __name__ == "__intro__":
                    intro()
                hello(yy) #calls the greeting def function
                age()  #calls age function from earlier
                z = input("Country: ") 
                zz = re.sub(r'[^a-zA-Z ]', '', z).capitalize() #regex similar written code as earlier
                print(host.name + ": Confirmed country is " + zz)
                contestant6.name = yy
                contestant6.country = zz
                pos.append("6") #adds to position number list
                cont.append(yy) # adds to contestant name list, now parallel with number above
                points.append(0) 
                cont6 = input(host.name + ": How are we all feeling contestants? ") #prompts plaer input
                cont66 = re.sub(r'[^a-zA-Z ]', '', cont6).capitalize() #regex aims to remove input errors
                contestant6.feeling = cont66 
                #previusly i accessed dictionary data and made it equal to a variable to then add to a print function
                #cut out middle-man and added dictinary data access code straight in the print function
                print(cont[0],": " + contestant1.feeling) 
                print(cont[1],": " + contestant2.feeling) 
                print(cont[2],": " + contestant3.feeling) 
                print(cont[2],": " + contestant4.feeling) 
                print(cont[4],": " + contestant5.feeling) 
                print(cont[5],": " + contestant6.feeling)
                pick22() #calls function       
            elif pick1 == "no": #prints and ends code
                print(host.name + ": GAME OVER")
                print("SHUTTING DOWN ...")
            else: #if neither "yes" or "no" are input, makes user try again
                print(host.name + ": Invalid input")
                troop() #calls back to start of def function where choice to continue or end        
            
    def intro(): #also function that gets called later, allows player to continue or end game
                 #additionally, has the intro to the game with interactive start-up
        print(host.name + " Stats:")
        print("Age: " + str(host.age))
        print("Country: " + host.country)
        print("Favourite subject: " + host.favsubj)
        print(host.name + ": Umm, actually, my favourite subject currently is Monkeys.") 
        x = "Monkeys"
        host.favsubj = x
        print("Favourite subject: " + host.favsubj)
        troop()

    def science(): #currently empty functions soon to be filled with questions and answers, not sure how I will display this tho
        print(host.name + ": You have chosen " + contest.topics["1"]) # considering I am grabbing dictionaries, probs should add to said dictionaries
        print(host.name + ": What is the most abundant gas in the Earth's atmosphere? ")
        print("A: " + science1.A)    #calls variables from science dictionary as options for answers
        print("B: " + science1.B)
        print("C: " + science1.C)
        print("D: " + science1.D)
        answr = input("Choice: ").strip().capitalize() #capitalize answer and gets rid of any unecessary spaces
        if answr == "B":  #this is correct answer
            print(host.name + ": " + science1.B + " is correct")  #if inputted, highlights as correct, gives 10 points
            print(host.name + ": You have won 10 points")
            points[0] = 10   #changes variable in specific part of list to number 10, required for later
            forward()  #to continue game, calls forward function
        elif answr == "A" or answr == "C" or answr == "D": #if either of these chosen, calls function from seperate file
            contest.incorrect()
            forward()  #then calls forward function to continue
        else:
            contest.incorrect()  #if ungiven answer is inputted or mistake then given as incorrect and calls forward function
            forward()
         
    def maths():
        print(host.name + ": You have chosen " + contest.topics["2"]) 
        print(host.name + ": The product of which 2 options, makes 64?\n Answers must be individually submitted as numbers.")
        #specified above to make eaiser for me to produce the product of the 2 numbers after the answer
        print("A: " + maths1.A)
        print("B: " + maths1.B) 
        print("C: " + maths1.C)
        print("D: " + maths1.D)
        aaa = (input("Choice: ")) #prompts input
        bbb = (input("Choice: "))
        aa = (re.sub(r'[^0-9 ]', '', aaa)) #gets rid of anything that isn't a number
        bb = (re.sub(r'[^0-9 ]', '', bbb))
        if aa == "" or bb == "": #if answer had no number then incorrect and is left as just an empty space
            contest.incorrect() #prompts function
            forward() #prompts function
        else:
            a = int(aa) #if there is a number left it records as an integer
            b = int(bb)
            product = lambda a, b: a * b  #defines a small anonymous function, takes 2 inputs and returns product
            print(f"The product is: {product(a, b)}") #prints product
            if a == 16 and b == 4: #if both correct answers are chosen in one way it awards points
                print(host.name + ": Correct you have won 10 points") #states correct
                points[1] = 10 #updates list with points
                forward() #calls function to determine if game continues
            if a == 4 and b == 16: #same as above if statement but if correct numbers were input the other way
                print(host.name + ": Correct you have won 10 points")
                points[1] = 10
                forward()
            else: #if alternative asnwer which wasn't covered is input. failsafe to test nothing slipped through
                contest.incorrect() #calls incorrect function
                forward() #continues on

    def pop_culture():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["3"])
        print(host.name + ": What year was the first animated transformers film released? ")
        print("A: " + pop1.A)
        print("B: " + pop1.B)
        print("C: " + pop1.C)
        print("D: " + pop1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "C":
            print(host.name + ": " + pop1.C + " is correct")
            print(host.name + ": You have won 10 points")
            points[2] = 10
            forward()
        elif answr == "A" or answr == "B" or answr == "D":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def mystery_round():
        print(host.name + ": You have chosen " + contest.topics["4"])
        print(host.name + ": Fill in the missing lyric to this Bruno Mars song: ")
        print("24-karat _____ in the air")
        answr = input("Answer: ") #prompts user input
        answrr = re.sub(r'[^a-zA-Z ]', '', answr).strip()   #makes sure input is only letters, gets rid of any other characters and rid of spaces
        if answrr == "magic":  #if answer matches exactly
            print(host.name + ": " + answrr + " is correct")   #states correct
            print(host.name + ": You have won 10 points") #awards points
            points[3] = 10  #updates points list
            forward() #calls forward function
        else:
            contest.incorrect()
            forward()

    def general_knowledge():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["5"])
        print(host.name + ": Question: Who made the sculpture, The Thinker? ")
        print("A: " + general1.A)
        print("B: " + general1.B)
        print("C: " + general1.C)
        print("D: " + general1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "A":
            print(host.name + ": " + general1.A + " is correct")
            print(host.name + ": You have won 10 points")
            points[4] = 10
            forward()
        elif answr == "B" or answr == "C" or answr == "D":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def food():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["6"])
        print(host.name + ": Which nut is used to make marzipan? ")
        print("A: " + food1.A)
        print("B: " + food1.B)
        print("C: " + food1.C)
        print("D: " + food1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "D":
            print(host.name + ": " + food1.D + " is correct")
            print(host.name + ": You have won 10 points")
            points[5] = 10
            forward()
        elif answr == "A" or answr == "B" or answr == "C":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def animals():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["7"])
        print(host.name + ": Which land animal can run the fastest? ")
        print("A: " + animal1.A)
        print("B: " + animal1.B)
        print("C: " + animal1.C)
        print("D: " + animal1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "B":
            print(host.name + ": " + animal1.B + " is correct")
            print(host.name + ": You have won 10 points")
            points[6] = 10
            forward()
        elif answr == "A" or answr == "C" or answr == "D":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def music():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["8"])
        print(host.name + ": Which music group released the song, Stars, in 1995? ")
        print("A: " + music1.A)
        print("B: " + music1.B)
        print("C: " + music1.C)
        print("D: " + music1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "B":
            print(host.name + ": " + music1.B + " is correct")
            print(host.name + ": You have won 10 points")
            points[7] = 10
            forward()
        elif answr == "A" or answr == "C" or answr == "D":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def history():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["9"])
        print(host.name + ": When was the battle of Normandy? ")
        print("A: " + history1.A)
        print("B: " + history1.B)
        print("C: " + history1.C)
        print("D: " + history1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "D":
            print(host.name + ": " + history1.D + " is correct")
            print(host.name + ": You have won 10 points")
            points[8] = 10
            forward()
        elif answr == "A" or answr == "B" or answr == "C":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def sport():  #similar to def science function but with respective information and data used
        print(host.name + ": You have chosen " + contest.topics["10"])
        print(host.name + ": Which country has won the most FIFA world cup titles? ")
        print("A: " + sport1.A)
        print("B: " + sport1.B)
        print("C: " + sport1.C)
        print("D: " + sport1.D)
        answr = input("Choice: ").strip().capitalize()
        if answr == "C":
            print(host.name + ": " + sport1.C + " is correct")
            print(host.name + ": You have won 10 points")
            points[9] = 10
            forward()
        elif answr == "A" or answr == "B" or answr == "D":
            contest.incorrect()
            forward()
        else:
            contest.incorrect()
            forward()

    def topics(): #produces lis of categories which players can choose
        print(host.name + ": Here are your categories:") #makes easier for user to visualise if they get prompted to pick a topic
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
        numb1 = random.randrange(1, 7) #picks a random number from 1, upto but not including 7, representing contestants
        if numb1 == 1: #formatting like this 
            #meant less repeated lines of similar code
            print(host.name + ": Contestant "  + contestant1.name + " has been chosen")
            print(host.name + ": Which topic would you like contestant " + contestant1.name + "? ")
            choice1_5() #as 1-5 arent users, I call this function
        elif numb1 == 2:
            print(host.name + ": Contestant "  + contestant2.name + " has been chosen")
            print(host.name + ": Which topic would you like contestant " + contestant2.name + "? ")
            choice1_5()
        elif numb1 == 3:
            print(host.name + ": Contestant "  + contestant3.name + " has been chosen")
            print(host.name + ": Which topic would you like contestant " + contestant3.name + "? ")
            choice1_5()
        elif numb1 == 4:
            print(host.name + ": Contestant "  + contestant4.name + " has been chosen")
            print(host.name + ": Which topic would you like contestant " + contestant4.name + "? ")
            choice1_5()
        elif numb1 == 5:
            print(host.name + ": Contestant "  + contestant5.name + " has been chosen")
            print(host.name + ": Which topic would you like contestant " + contestant5.name + "? ")
            choice1_5()
        elif numb1 == 6: #this is user number
            choice6() #calls this function
        else:
            print("") #if this happened and nothing was printed, would know there was a code issue
            
    def choice1_5():  #this is function for contestants 1 to 5
        if len(top) == 0: #top is topic list if there are no topic numbers in list then you can't call a topic function
            point_sum() #this is useful for later as we will go down from 10 topics to 0
            #when we get to 0 we call point sum function
        else: #if there are variables in the list then there are topics to call
            numb = random.choice(top) #randomly choses a variable in the list which furhter down, coresponds to calling a specific function
            print(host.name + ": Topic " + str(numb) + " has been chosen")
            if numb in top:
                top.remove(numb) #this removes the randomly generated number variable so the same topic can't be re produced
                #made it so there was no endless question loop and the game can end eventually
                if numb == 1:   
                    science() 
                elif numb == 2:
                    maths()
                elif numb == 3:
                    pop_culture()    
                elif numb== 4:
                    mystery_round()    
                elif numb== 5:
                    general_knowledge()
                elif numb == 6:
                    food()
                elif numb == 7:
                    animals()
                elif numb== 8:
                    music()
                elif numb == 9:
                    history() 
                elif numb == 10:
                    sport()
                else:
                    print(host.name + ": Experiencing technical issue") #added this as keep getting issue where code finishes
                    #on this print output when it isn't meant to
            elif numb not in top: #unlickly this could happen but a failsafe if number was called that had already been
                print("Topic has already been chosen.\nTry again.")
                choice1_5() #calls back to the top as input was invalid
            else:
                print("panic") #failsafe word i could come back to if a part of the function was not working properly

    def choice6():   #similar layout to choice 1-5 except it prompts a user input number
        if len(top) == 0: #if there are no more numbers to call from a list then goes to point summary
            point_sum()
        else:
            numbers = input(host.name + ": Which topic would you like contestant " + contestant6.name + "? ")
            numbnumb = (re.sub(r'[^0-9 ]', '', numbers)) #made this int so read it as number for if statements
            if numbnumb == "":
                    print("Incorrect or unavailable option input\nPlease try again")
                    choice6() #if the input had no number then it will be blank and function loops to try again
            else:
                numb = int(numbnumb) #reads input as integer
                print(host.name + ": Topic " + str(numb) + " has been chosen") #asks user to choose a topic and depending on input
                #depends on which category find a way for this to work
                if numb in top: #if the input is in the list it is removed from list and calls a specific function
                    top.remove(numb)
                    if numb == 1:
                        science()
                    elif numb == 2:
                        maths()
                    elif numb == 3:
                        pop_culture()
                    elif numb == 4:
                        mystery_round()
                    elif numb == 5:
                        general_knowledge()
                    elif numb == 6:
                        food()
                    elif numb == 7:
                        animals()
                    elif numb == 8:
                        music()
                    elif numb == 9:
                        history()
                    elif numb == 10:
                        sport()
                    else:
                        print(host.name + ": Please stand by")  #if input was not accepted due to it not being a number either in topic list or not a number at all,
                        print("Incorrect or unavailable option input\nPlease try again") #prompts user to try again and calls function to do so
                        choice6()
                elif numb not in top:
                 print("Topic has already been chosen.\nTry again.") #if chosen number was already used then prompts retry
                 choice6()
                elif numb == "": #prompts retry if input was incorrect
                 print("Invalid input")
                 choice6()
                else:
                    print("ISSUE") #failsafe if any if statements weren't working properly
    
    def point_sum(): #when random numb can no longer generate, make it so it calls this function
        print(host.name + ": I'm afraid that's the end of the questions\nLet's see how you did.")
        total = 0  #starts total = 0
        for num in points: #for numbers in the list points
            total += num  #adds numbers together and to total
        print(host.name + ": " + contestant6.name + f", your total points are: {total}/100") #prints user total
        print(host.name + ": Let's see what our other contestants got:")
        print("Generating results:")
        cont1 = random.randrange(0, 110,10) #randomly generates a number between 0 and 100 in intervals of 10, similar to points system
        cont2 = random.randrange(0, 110,10)
        cont3 = random.randrange(0, 110,10)
        cont4 = random.randrange(0, 110,10)
        cont5 = random.randrange(0, 110,10)
        print(host.name + ": " + contestant1.name + " scored " + str(cont1)) #as random number is integer, prints it as a str
        print(host.name + ": " + contestant2.name + " scored " + str(cont2)) #refers to player and their points
        print(host.name + ": " + contestant3.name + " scored " + str(cont3))
        print(host.name + ": " + contestant4.name + " scored " + str(cont4))
        print(host.name + ": " + contestant5.name + " scored " + str(cont5))
        score[0] = cont1 #makes random number a variable in score list
        score[1] = cont2
        score[2] = cont3
        score[3] = cont4
        score[4] = cont5
        x = sorted(score) #sorts score list from lowest to highest
        big = x[4] #x[4] is going to be biggest number in score list
        if big == total: #if highest contestant points is equal to overall user total points  
            contest.tie() #calls tie function
        elif big >= total: #if highest contestant points is greater than overall user total points
            contest.loss() #calls loss function
        elif total >= big: #if overall user total points is greater than highest contestant points
            contest.win() #call win function
        else:
            print("ISSUE PLEASE STAND BY") #failsafe if there was an above error
        
    intro() 

main()