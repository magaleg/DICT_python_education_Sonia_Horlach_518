""""Project Dinner-party"""
import random


def add_friends():
    """The main program function. Works by this algorythm:
    1. Asks user to input the number of their friends joining
    the dinner.
    2. Asks user to enter their names.
    3. Initializes a dictionary using this information, initial values
    of the share per person are set to 0.
    4. Asks user to input the bill, calculates the share per peron and updates
    it in the dictionary.
    5. Additionally, it has a "Lucky one" function that randomly chooses a lucky one among the
    friends. This person won't pay their part, instead it will be shared among their friends.
    6. Prints the dictionary with friends' names and their respective bill shares.
    Returns: none.
    """
    num_friends = int(input("Enter the number of friends for your party! (you're included)>"))

    if num_friends <= 0:
        print("Oh no, no one is joining the party! :(")
    else:
        friends_dict = {}

        for i in range(num_friends):
            friend_name = input(f"Enter the name of your friend №{i+1}!>\n!")
            friends_dict[friend_name] = 0
        print(friends_dict)
        total_amount = float(input(f"Enter the total amount!>\n"))
        lucky_choice = str(input("Wanna choose a lucky one? Yes/No>"))

        if lucky_choice == "Yes":
            lucky_one = random.choice(list(friends_dict.keys()))
            print(f"{lucky_one} is the lucky one!")

            for friend in friends_dict:
                if friend != lucky_one:
                    friends_dict[friend] = round(total_amount / (num_friends - 1), 2)
                else:
                    friends_dict[friend] = 0
        else:
            share_per_person = round(total_amount / num_friends, 2)
            for friend in friends_dict:
                friends_dict[friend] = share_per_person

        print(friends_dict)


add_friends()

