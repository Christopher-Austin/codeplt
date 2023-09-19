def deaf_grandma():
    goodbye_counter = 0
    while True:
        response = input("What to say to grandma? ")
        if not response:
            print("WHAT!")
        elif response[0] == response[0].lower():
            print("SPEAK UP, KID!")
        elif response == "GOODBYE!" and goodbye_counter < 1:
            print("LEAVING SO SOON?")
            goodbye_counter += 1
        elif goodbye_counter == 1:
            print("LATER, SKATER!")
            break
        else:
            print("NO, NOT SINCE 1946!")

deaf_grandma()
