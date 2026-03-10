import contest
pos = ["1", "2", "3", "4", "5"]
cont = ["Bella", "Charlie", "Kian", "Max", "Jessy"]
def main():
    def intro():
        print("Hello everyone and welcome to\n...\nThe Big Pub Quiz!")
        ha = contest.host["name"]
        print("I am your host: " + ha)
        print("Here are your contestants for the night:")
        print(pos[0], ": "+ cont[0])
        print(pos[1], ": "+ cont[1])
        print(pos[2], ": "+ cont[2])
        print(pos[3], ": "+ cont[3])
        print(pos[4], ": "+ cont[4])
        y = input("And finally, our special guest for the evening: ")
        pos.append("6")
        cont.append(y)
        sixe = input("How are we all feeling contestants? ")
        xx = contest.cont1["feeling"]
        xy = contest.cont2["feeling"]
        xz = contest.cont3["feeling"]
        ff = contest.cont4["feeling"]
        rt = contest.cont5["feeling"]

        print(cont[0],":" + xx) 
        print(cont[1],":" + xy) 
        print(cont[2],":" + xz) 
        print(cont[2],":" + ff) 
        print(cont[4],":" + rt) 
        print(cont[5],":" + sixe)
        print("Wonderful, let's get on with the games!")
    intro()

    
main()