import os, csv

cand = []
ballots=[]
cand_list = []
with open(os.path.join("Resources","election_data.csv"), newline ='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ballots.append(row["Ballot ID"])
        cand.append(row["Candidate"])

    for x in cand:
        if x not in cand_list:
            cand_list.append(x)

    No_of_votes = [0 for row in cand_list]
    Total_votes = 0
    for i in range (0, len(ballots)):
        for j in range (0, len(cand_list)):
            if cand[i] == cand_list [j]:
                No_of_votes[j] = int(No_of_votes[j]) + 1
                Total_votes += 1

    percent_of_votes = []
    winner = 0
    for i in range(0, len(cand_list)):
        percent_of_votes.append(round(((int(No_of_votes[i])/Total_votes) * 100),3))
        if int(No_of_votes[i]) > winner:
            winner = int(No_of_votes[i])
            winner_cand = cand_list[i]


print("Election Results \n")

print("----------------------------------------------\n")

print(f'Total votes: {Total_votes}\n')

print("----------------------------------------------\n")

for i in range (0, 3):
    print(f"{cand_list[i]}: {percent_of_votes[i]}% ({int(No_of_votes[i])})\n")

print("----------------------------------------------\n")

print(f"Winner: {winner_cand}\n")

print("----------------------------------------------\n")

with (open(os.path.join("Analysis", "Pyroll_Analysis.txt"), 'w', newline = '') as csv_write):
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
