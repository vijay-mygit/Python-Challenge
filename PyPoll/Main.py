#Python code to solve the PyPoll challenge
import os
import csv
poll_csv = os.path.join("C:/Users/vijay/OneDrive/Documents/GitHub/Python-Challenge/PyPoll/03-Python_Instructions_PyPoll_Resources_election_data.csv")
total_votes = 0
output_results = []
with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    candidate_list = []
    vote_count = []
    for row in csvreader:
        vote_count.append(int(row[0]))
        candidate_list.append(row[2])
    total_votes = len(vote_count)
    candidates = set(candidate_list)
    winner_candidate = max(candidates,key=candidate_list.count)
    final_list = list(candidates)

    #Function to count the number and percentage of votes for each candidate

    def voting(list_candidates):
        for r in list_candidates:
            votes_num = candidate_list.count(r)
            fraction_votes = ((votes_num)/(total_votes))
            percent_votes = format(fraction_votes,".2%")
            print(f"{r} : {percent_votes} ({votes_num})")
            output_results.append(f"{r} : {percent_votes} ({votes_num})")
       
print(f"----------------------------")
print(f"Election Results")
print(f"----------------------------")
print(f"Total votes : {total_votes}")
print(f"----------------------------")
voting(final_list)
print(f"----------------------------")
print(f"Winner: {winner_candidate}")
print(f"----------------------------")

#Creating Output Text File

f = open('PyPoll_output.txt','w')
print(f"----------------------------",file=f)
print(f"Election Results",file=f)
print(f"----------------------------",file=f)
print(f"Total votes : {total_votes}",file=f)
print(f"----------------------------",file=f)
print(*output_results, sep='\n',file=f)
print(f"----------------------------",file=f)
print(f"Winner: {winner_candidate}",file=f)
print(f"----------------------------",file=f)
f.close()
