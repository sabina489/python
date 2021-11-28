# Making a Game
#Adventure game
print("""
    WELCOME TO THE ADVENTURE GAME!
    Let's start the action!
     Asmita wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
    Now she has two choices she can either stay in the room or check what the sound might be about.
     Type your choice: Stay or Evaluate?
"""
)
# We need to make sure our game has answers to all types of inputs made by users.
def scene1():
    import time
    print("""
    welcome to the ADVENTURE GAME!
    LET'S START THE ACTION:
    Asmita wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
    NOw, she has two choices that she can either stay in the room or check what the sound might be about.
    Type choice: Stay or Evaluate?
    """)

# We take the first choice input and then we will create a variable that will confirm if our answer is correct or not.
    c1 = input()
    time.sleep(2)
    ans = 'wrong'
    while(ans=='wrong'):
        if(c1.upper()=="STAY"):
            print("\n Asmita decides to stay in the room and ends up staying inside forever as noone seems to come to helpher.")
            ans = 'right'  # then, we create the conditional loop and if-else statement.
        elif(c1.upper()=="EVALUATE"):
            print("Asmita exits the room and reaches in the main hall.")

            ans = 'right'
            scene2()
        else:
            print("ENTER THE RIGHT CHOICE! Stay or Evaluate?")
            c1 = input()

# Now the first scene is complete, we can move on to the next scene.
def scene2():
    import time
    print(""" 
        In the main hall, she finds a strange but cute teddy bear on the floor.
        She wanted to pick the teddy up.
        But should she? It doesn't belong to her.
        Type choice: Pick or Ignore?
    """)
    time.sleep(2)
    c1 = input()
    ans = 'wrong'
    while(ans=='wrong'):
        if(c1.upper()=="PICK"):
            print(""" \nThe moment Asmita picked up the teddy bear. The teddy bear starts TALKING. The bear tells Asmita that she is in danger as there is a monster in the house and that monster will kill her.""")
            time.sleep(2)
            print("""\n The bear handed Asmita a magical potion which can weaken the moster and make him run away and Asmita moved Forward.""")
            ans = 'right'
            pick="Yes"
        elif(c1.upper()=='IGNORE'):
            print("""\n Asmit decided not to pick up the bear and walked forward.""")
            ans = 'right'
            pich="No"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1=input()
    time.sleep(2)
    scene3(pick)

# The third scene depends on the choice made in scene2 which is if the teddy bear was picked or ignored.
def scene3(pick_value):
    import time
    print("""\n After walking for a while, Asmita saw the Monster in front of her!
    It had red eyes and evil looks. she got very scared!
    """)
    time.sleep(2)
    if(pick_value=="False"):
        time.sleep(2)
        print(""" But she remembered, Well she had nothing to lose""")
        time.sleep(2)
        print("\n The monster SCREAMED in pain but he managed to make a portal and Asmita to a new world!")
    elif(pick_value=="No"):
        print("THe monster attacked Asmita and hurt her! She was then put into a new world")

scene1()
print("\n\n\n")
print("===========END")