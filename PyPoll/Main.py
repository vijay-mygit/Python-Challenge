#PyPoll
import os
import csv
poll_csv = os.path.join("C:/Users/vijay/OneDrive/Documents/GitHub/Python-Challenge/PyPoll/03-Python_Instructions_PyPoll_Resources_election_data.csv")
total_votes = 0
#candidates = []
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
    def voting(list):
        for r in list:
            votes_name = candidate_list.count(r)
            fraction_votes = ((votes_name)/(total_votes))
            percent_votes = format(fraction_votes,".2%")
            #yield(f"{r} : {percent_votes} ({votes_name})")
            print(f"{r} : {percent_votes} ({votes_name})")
            
print(f"----------------------------")
print(f"Election Results")
print(f"----------------------------")
print(f"Total votes : {total_votes}")
print(f"----------------------------")
output = voting(final_list)
print(f"----------------------------")
print(f"Winner: {winner_candidate}")
print(f"----------------------------")

#Creating Output Text File

output_file = os.path.join('PyPoll_output.txt')
file = open(output_file, 'w')
file.write(f"----------------------------\n")
file.write(f"Election Results\n")
file.write(f"----------------------------\n")
file.write(f"Total votes : {total_votes}\n")
file.write(f"----------------------------\n")
file.write(f"{output}\n")
file.write(f"----------------------------\n")
file.write(f"Winner: {winner_candidate}\n")
file.write(f"----------------------------\n")

    


