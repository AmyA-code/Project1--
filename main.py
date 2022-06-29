import sys

def display(superhero_personality):
    print(f"Your superpower should be -> {superhero_personality}")
def run():
    questions: list = [
        """
Question 1: When you are outside, you like to:
a.Climb trees
b.Race your friends
c.Play hide-and-seek
d.Watch people
e.Stare at clouds
f.Organize role playing games
""",
        """
Question 2: What word best describes you:
a.Curious
b.Fearless
c.Thoughtful
d.Motivated
f.Independent
""",
        """
Question 3: Which animal would you most like to be:
a.Cheetah
b.Octopus
c.Tyrannosaurus rex
d.Dog
e.Elephant
f.Falcon
""",
        """
Question 4: What's your favorite subject:
a.Gym
b.Foreign language
c.Health
d.Science
e.Art
f.History
""",
        """
Question 5: You're stranded on an island. What do you do to pass the time:
a.Write in a journal
b.Run around the beach
c.Build a hut
d.Talk with animals
e.Make sand castles
f.Pick coconuts from trees
""",
        """
Question 6: When you want to ride in style, what's your ideal mode of transportation:
a.Horse and buggy
b.Motorcycle
c.Truck
d.Tandem bike
e.Helicopter
f.Scooter
""",
        """
Question 7: What's the coolest thing at a carnival:
a.Fun house
b.Fortune teller
c.Carousel
d.Giant slide
e.Hammer game
f.Swing ride
""",
        """
Question 8: Choose a breakfast:
a.Tea and crumpets
b.Steak and eggs
c.Granola bar
d.Waffle
e.Grapefruit
f.Pancakes
"""
    ]

    count_of_a: int = 0
    count_of_b: int = 0
    count_of_c: int = 0
    count_of_d: int = 0
    count_of_e: int = 0
    count_of_f: int = 0
    superhero_personality: str = ' '
    count = 0

    for question in questions:
        answer = ' '
        while not (answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D' or answer == 'E' or answer == 'F'):
            count_of_a = 0
            count_of_b = 0
            count_of_c = 0
            count_of_d = 0
            count_of_e = 0
            count_of_f = 0
            try:
                answer = input(question).upper()
                if not (answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D' or answer == 'E' or answer == 'F'):
                    raise ValueError("Invalid Input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a = count_of_a + 1
                if answer == 'B':
                    count_of_b = count_of_b + 1
                if answer == 'C':
                    count_of_c = count_of_c + 1
                if answer == 'D':
                    count_of_d = count_of_d + 1
                if answer == 'E':
                    count_of_e = count_of_e + 1
                if answer == 'F':
                    count_of_f = count_of_f + 1
                count = count + 1
        if count == 9:
            if count_of_a > count_of_b:
                superhero_personality = superhero_personality + 'Super-speed '
        else:
            if count == 8:
                if count_of_b > count_of_a:
                    superhero_personality = superhero_personality + 'Shape-shifter '
            else:
                if count == 7:
                    if count_of_c > count_of_d:
                        superhero_personality = superhero_personality + 'Time-travel '

                else:
                    if count == 6:
                        if count_of_d > count_of_c:
                            superhero_personality = superhero_personality + 'Mind-reader '
                    else:
                        if count == 5:
                            if count_of_e > count_of_f:
                                superhero_personality = superhero_personality + 'Super-strength '
                        else:
                            if count == 10:
                                if count_of_f > count_of_e:
                                    superhero_personality = superhero_personality + 'Flight '

    display(superhero_personality)


    def exit_application():
        print("Exiting application. . . ")
        sys.exit(0)


def main():
    user_input = input("""
    Welcome to the Superhero Personality Test for Kids
    Press 1 to take test
    Press 2 to exit application -> """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": run,
            "2": exit
        }
        return switcher.get(user_input)()


if __name__ == "__main__":
    main()


