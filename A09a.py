# -----------------------------------
# Programmer:   Michael Barreto
# Course:       COSC 1315 Section 10
# Project:      Class Details
#------------------------------------

def main():
    # Declare variable and dictionaries
    rooms = {"CS101":3004, "CS102":4501, "CS103":6755,
             "NT110":1244, "CM241":1411}

    instructors = {"CS101":"Haynes", "CS102":"Castaneda",
                   "CS103":"Rich", "NT110":"Burke",
                   "CM241":"Lee"}

    times = {"CS101":"8:00 am", "CS102":"9:00 am",
             "CS103":"10:00 am","NT110":"11:00 am",
             "CM241":"12:00 pm"}

    keepLooping = 1

    # Keep looping as long as the user
    # wishes to enter course numbers
    while keepLooping != 0:
        # Prompt the user for a course number
        course = input("\nEnter a course number: ")

        # Convert course number to upper case
        course = course.upper()

        # Course does not exist
        if course not in rooms:
            print(course, "is an invalid course number.")

        # Course does exist
        else:
            # Print information about this course
            print("\nThe details for course", course, "are:\n")
            print("Room:", rooms[course])
            print("Instructor:", instructors[course])
            print("Time:", times[course])

        # Prompt the user to see if they
        # wish to continue. Extract out
        # the first character and convert
        # it to lower case
        answer = input("\nDo you wish to continue (yes/no)?")
        answer = answer[0:1]
        answer = answer.lower()

        # User wants to stop
        if answer == "n":
            # Set variable to exit while loop
            keepLooping = 0

    # Call the function 'printGoodbye' to
    # print out closing remarks
    printGoodbye()

# Define the function 'printGoodbye'. It will
# simply display the goodbye message for
# this program.
def printGoodbye():
    print("\nThis program was written by Michael Barreto.")
    print("End of program")

# Call the main function
main()
            
        
        
