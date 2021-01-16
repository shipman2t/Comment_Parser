__author__ = "Terry Shipman"
__version__ = "1.0.4"
# Original
# __date__ = "April 20, 2020"
#Updated
__date__ = "January 16, 2021"
copyright()


"""                                  ----------Project Summary Commentary----------
This project has been designed to take the topics that are being covered in CSC4101 Programming Languages
        regarding grammar and the parsing problem.  This project simulates the parsing of a C Language
        program comment section that is represented by the pattern /* comment */.  The project
        identifies the leading prefix /* and ending suffix */ markers and determine if the section of text is a valid
        comment.  Additional commentary below detailing each function purpose.
"""

def start_assignment_2():
    """ Starting function for program.

    Function executes user input and validation.

    """
    valid_selection = False
    demo_choice = 0
    while not valid_selection:
        demo_choice = input(
        "Would you like to input your own text or use a sample? \n 1. Input my text\n 2. Use a sample\n")
        if demo_choice.isdigit():
            if int(demo_choice) < 3:
                valid_selection = True
        else:
            print("Please select 1 or 2...")

    if user_choice == '2':
        print("\n\n")
        print(
            "This is an example from Ruyard Kipling's poem \'If\' \nComment grammar was added at select points--- \n")
        sample_comment_demo()
    else:
        user_comment()


def comment_print(comment_sample, valid):
    """
    comment_print("A comment Sample", valid = a boolean value)
    :param comment_sample: A comment sample as a String
    :param valid: A boolean value from comment_validator indicating a valid or invalid comment format from parser.

    Print function for program:
    Comment sample is printed as a \"Valid\" or \"Invalid\" comment depending on the valid boolean variable.
    """
    if valid:
        print("   Valid Comment:\t\t" + comment_sample)
    else:
        print("Invalid Comment:\t\t" + comment_sample)


def comment_validator(comment_sample):
    """
    comment_validator("A comment sample"):
    :param comment_sample: A string that passes the comment test from the comment_parser.
    Function used by comment_print to validate the comment sample as a valid comment sample.

    """
    valid = False
    if comment_sample[0:2:1] == comment_sample[-1:-3:-1] == '/*':
        valid = True
    else:
        pass
    comment_print(comment_sample, valid)


def comment_parser(text_sample):
    """
    comment_parser(text_sample):

    :param text_sample:  A string sample to identify if there is a correctly formatted comment in the string.

    Parser function for program.
    Determines if the leading prefix /* and trailing suffix */ makes a valid comment.

    """
    begin_cmt = end_cmt = 0
    for i in range(0, len(text_sample) - 1):
        # Check for comment prefix
        if text_sample[i] == chr(47) and text_sample[i + 1] == chr(42):
            begin_cmt = i
        # Check for comment suffix
        elif text_sample[i] == chr(42) and text_sample[i + 1] == chr(47):
            end_cmt = i + 1
            comment_validator(text_sample[begin_cmt:end_cmt + 1])
        # Check for no comment
        elif i == len(text_sample) - 2:
            begin_cmt = end_cmt + 1
            comment_validator(text_sample[begin_cmt - 1:])
        else:
            pass


def user_comment():
    """
    user_comment():

    Sends text sample as a string to the comment_parser to identify if there is a correctly formatted comment in the
    text.
    """
    text_sample = input("Enter your text to determine if it is a comment line:  ")
    comment_parser(text_sample)


def sample_comment_demo():
    """
    sample_comment_demo():

    A sample from R Kipling's 'If' to be used as a demo comment sample for the user.
    :return:
    """
    kipling = "/* If you can keep your head when all about you Are losing theirs */ and blaming it on you, If you can trust yourself when all men doubt you, But make allowance for their doubting too; /* If you can wait and not be tired by waiting */, Or being lied about, don’t deal in lies, Or being hated, don’t give way to hating,And yet don’t look too good, nor talk too wise:/* If you can dream—and not make dreams your master;*/ If you can think—and not make thoughts your aim; /* If you can meet with Triumph and Disaster*/ And treat those two impostors just the same; If you can bear to hear the truth you’ve spoken Twisted by knaves to make a trap for fools, Or watch the things you gave your life to, broken, And stoop and build ’em up with worn-out tools: If you can make one heap of all your winnings And risk it on one turn of pitch-and-toss, /* And lose, and start again at your beginnings And never breathe a word about your loss */; If you can force your heart and nerve and sinew To serve your turn long after they are gone, And so hold on when there is nothing in you Except the Will which says to them: ‘Hold on!’ If you can talk with crowds and keep your virtue, Or walk with Kings—nor lose the common touch, If neither foes nor loving friends can hurt you, If all men count with you, but none too much;  If you can fill the unforgiving minute With sixty seconds’ worth of distance run,  Yours is the Earth and everything that’s in it, And—which is more—you’ll be a Man, my son!"
    comment_parser(kipling)


#   Main function area.  I challenged myself to compartmentalize as much of this project as possible to fully understand
#       the parsing problem, as well as, to insure that syntax errors could be resolved efficiently.
if __name__ == "__main__":
    start_assignment_2()

