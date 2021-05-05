temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


    #What is the score?
    score = int(input("What is your test score?"))

    #Determine the grade.
    if score >= 90:
        print('Your grade is an A.')
    else:
        if score >= 80:
            print('Your grade is a B.')
        else:
            if score >= 70:
                print('Your grade is a C.')
            else:
                if score >= 60:
                    print('Your grade is a D.')
                else:
                    print('Your grade is an F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

x = 0
while x <= 5:
    print(x)
    x = x + 1

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num) 

numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#fstrings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#multiline fstrings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

#multiline fstrings add a thousands seperator
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the elction results and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
    