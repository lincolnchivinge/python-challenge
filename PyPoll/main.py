# import library
import pandas as pd

# read a file
data_file = pd.read_csv("c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/python-challenge/PyPoll/Resources/election_data.csv")

print(data_file)

# calculate the total number of votes
total_votes = len(data_file)
total_votes

# list of candidates who received votes
candidates_count = data_file["Candidate"].value_counts()
candidates_count

# percentage of votes each candidate won
percentage_votes = (candidates_count/total_votes)*100
percentage_votes

# announce the winner
winner = candidates_count.idxmax()
winner

# print the results
print("Election results")

print("---------------------------------------------------------------------------")

print("Total votes: " + str(total_votes))

print("----------------------------------------------------------------------------")

print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
      
print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
      
print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
      
print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")

print("----------------------------------------------------------------------------------------")
      
print("winner: " + winner)


# convert the output into a text file
file = open('c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/python-challenge/PyPoll/analysis/pypoll.txt','w')
file.write("Election results")
file.write("\n....................................................................................")
file.write("\nTotal votes: " + str(total_votes))
file.write("\n----------------------------------------------------------------------------")
file.write("\nKhan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
file.write("\nCorrey:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
file.write("\nLi:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
file.write("\nO'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")
file.write("\n----------------------------------------------------------------------------------------")
file.write("\nwinner: " + winner)
file.close()
