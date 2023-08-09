import os, csv   # Importing OS and CSV modules required for the analysis

# Defining lists for storing data
cand = []
ballots=[]
cand_list = []

# Reading csv file located in the resource folder with csv module and saving the column data to lists

with open(os.path.join("Resources","election_data.csv"), newline ='') as csvfile: # Defining the path to the csv file folder i.e. path to Resource folder
    reader = csv.DictReader(csvfile)
    for row in reader:
        ballots.append(row["Ballot ID"])
        cand.append(row["Candidate"])

# Getting the unique candidate list

    for x in cand:
        if x not in cand_list:            # checking to make sure that name is unique
            cand_list.append(x)           # Adding the name to "cand_list" list

# Estimating total number of votes polled as well as votes polled for each candidate

    No_of_votes = [0 for row in cand_list]  # Defining a null list
    Total_votes = 0
    for i in range (0, len(ballots)):
        for j in range (0, len(cand_list)):
            if cand[i] == cand_list [j]: # checking the name of the candidate in csv file with the name in the candidate list
                No_of_votes[j] = int(No_of_votes[j]) + 1  # assigning the votes to the candidate
                Total_votes += 1 # Counting the total number of votes

# Estimating the percentage of votes each candidate received and finding the winner candidate

    percent_of_votes = [] # Declaring an empty list
    winner = 0
    for i in range(0, len(cand_list)):
        percent_of_votes.append(round(((int(No_of_votes[i])/Total_votes) * 100),3)) # Estimating percentage of votes each candidate received based on the total votes polled and rounding the percentage value to nearest third decimals
        if int(No_of_votes[i]) > winner: # Checking if number of votes of current candidate is higher than the "winner" variable
            winner = int(No_of_votes[i])  # if statement is TRUE, assigning the current number of votes value to "winner" variable
            winner_cand = cand_list[i]   #  if statement is TRUE, assigning the current candidate list string value in the "winner_cand" variable

csvfile.close()

# Procedure/commands for printing the results to screen/terminal

print("Election Results \n")

print("----------------------------------------------\n")

print(f'Total votes: {Total_votes}\n')

print("----------------------------------------------\n")

for i in range (0, 3):
    print(f"{cand_list[i]}: {percent_of_votes[i]}% ({int(No_of_votes[i])})\n")

print("----------------------------------------------\n")

print(f"Winner: {winner_cand}\n")

print("----------------------------------------------\n")

#  Writing the analysis results to a txt file and saving it to Analysis folder

with (open(os.path.join("Analysis", "Pyroll_Analysis.txt"), 'w', newline = '') as csv_write):   # Defining the path for saving the analysis results as txt file to a folder i.e. path to Analysis folder
    writer = csv.writer(csv_write, delimiter = ',', quoting = csv.QUOTE_MINIMAL)

    writer.writerow(['Election Results'])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])
    writer.writerow(['                      '])
    writer.writerow(['Total votes: '+ str(Total_votes)])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])
    writer.writerow(['                      '])
    for i in range (0,3):
        writer.writerow([str(cand_list[i]+':'+ ' '+str(percent_of_votes[i])+'%'+ " "+'('+ str(No_of_votes[i])+')')])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])
    writer.writerow(['                      '])
    writer.writerow(['Winner:'+' '+ str(winner_cand)])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])

csv_write.close()      #  Closing the  text file after writing all the information