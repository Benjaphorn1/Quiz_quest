import math
import random


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        # print error message if something isn't valid
        print(error)
        print()


def instructions():
    """prints instructions"""
    print("""
 *** Instructions ***

 To begin choose the number of rounds(or play infinite mode)

There will be a pythagoras theorem question
find C and get it right or wrong

Remember to find c and not c².

Good Luck!
    """)


def int_checker(question, low=None, high=None, exit_code=None):
    """checks users enters an integer"""
    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low
            if low is not None and response < low:
                if high is not None:
                    print(f"Please enter and integer that is between {low} and {high} (inclusive)")
                else:
                    print(f"Please enter an integer that is more than / equal to {low}")
                continue

            # check response is more than the low number
            if high is not None and response > high:
                print(f"Please enter and integer that is between {low} and {high} (inclusive)")
                continue

            # if response is valid return it
            return response

        except ValueError:
            if low is None and high is None:
                print("Please enter an integer.")
            elif high is None:
                print(f"Please enter an integer that is more than / equal to {low}")
            else:
                print(f"Please enter and integer that is between {low} and {high} (inclusive)")


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_won = 0
rounds_lost = 0
rounds_played = 0
quiz_history = []
end_quiz = "no"

print()
print("--Quiz Quest--")
print()

# ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

# if user says yes display instructions
if want_instructions == "yes":
    instructions()

# Main game loop
while True:
    # ask users for the amount of questions / or infinite
    num_ques = int_checker("How many questions would you like? press <enter> for infinite mode: ",
                           low=1, exit_code="")

    if num_ques == "":
        mode = "infinite"
        num_ques = 5

    # Quiz loop starts here
    while rounds_played < num_ques:
        # Rounds heading
        if mode == "infinite":
            rounds_heading = f"\n Round {rounds_played + 1} (Infinite mode)"
            num_ques += 1  # Increase number of questions for infinite mode
        else:
            rounds_heading = f"\n Round {rounds_played + 1} of {num_ques}"

        print(rounds_heading)
        print()

        # Generate question
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        a2 = a * a
        b2 = b * b
        eq = a2 + b2
        ans = math.sqrt(eq)
        ans2 = round(ans, 2)

        print("hint",ans2)
        print(f"find 'c' from: {a}² + {b}² = c")

        # ask user to answer the question
        guess = input("answer? ").lower()

        # Check if the user wants to quit
        if guess == "xxx":
            end_quiz = "yes"
            break

        # otherwise, just turn guess into float
        guess = float(guess)

        # Check if correct
        if guess == ans2:
            feedback = "good job! You got it correct."
            rounds_won += 1
            result = "won"
        else:
            feedback = "Sorry. You got it wrong."
            rounds_lost += 1
            result = "lost"

        if end_quiz == "yes":
            break

        # Check that it is correct
        if round(guess, 2) == ans2:  # Compare rounded values to avoid floating point precision issues
            feedback = "Good job! You got it correct."
            rounds_won += 1
            result = "won"
        else:
            feedback = f"Sorry. You got it wrong. The correct answer was {ans2}."
            rounds_lost += 1
            result = "lost"

        # print feedback back to user
        print(feedback)
        rounds_played += 1

        # Add round to game history
        quiz_history.append(f"Round {rounds_played}: {result} - Answer: {ans2}, Your guess: {guess}")

        if end_quiz == "yes":
            break

    # if end_quiz == "yes":
    #     break

    print("\nEnd of round")

    # Game history / Statistics area
    if rounds_played > 0:
        # Calculate statistics
        percent_won = rounds_won / rounds_played * 100
        percent_lost = rounds_lost / rounds_played * 100

        # Output game statistics
        print("\n📊📊📊 Game Statistics 📊📊📊")
        print(f"👍 Won: {percent_won:.2f}% \t 😢 Lost: {percent_lost:.2f}%")

        # Ask user if they want to see game history
        want_history = string_checker("\nDo you want to see game history? ")

        # Output history if user says yes
        if want_history == "yes":
            print("\n---Game History---")
            for item in quiz_history:
                print(item)

    print("\nThanks for playing!")

    # Ask if user wants to play again
    play_again = string_checker("Do you want to play again? (yes/no) ")
    if play_again == "no":
        print("Thanks for playing!")
        break
    else:
        # Reset game variables for a new game
        mode = "regular"
        rounds_won = 0
        rounds_lost = 0
        rounds_played = 0
        quiz_history = []
        end_quiz = "no"
