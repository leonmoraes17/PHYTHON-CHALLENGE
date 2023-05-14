import os
import csv

total_votes = 0
total_candidates = []
distinct_candidate = []
votes =[]
percentage_list = []
xyz=[]


csvdata = os.path.join("..","Resources","election_data.csv")

with open (csvdata, encoding ="UTF-8") as csv_file:
    csv_contents =csv.reader(csv_file,delimiter=",")

    election_text = os.path.join("..","Analysis","election_data.txt")
    with open (election_text, "w") as outputfile:
#oreading contents and then writing to text file 
#      
        csv_header =next(csv_contents)

        for row in csv_contents:
            total_votes = total_votes +1
            candidates = row[2]
            total_candidates.append(candidates )
            #total candidates will contains name of the candidates appearing n number of time  in row[2] of the csv file.
            # this will help in counting the number of time the candidate name appears in the csv file and append it to the list
            if candidates not in distinct_candidate:
                distinct_candidate.append(candidates)
                #further making a list of having candidate appearing only once 
        candicount = len(distinct_candidate)
        #candicount variable is used to get the length of distinct candidate names so we can use it to iterate in future code below
        
        #counting votes of each candidate 
        for j in range(0, candicount):
            name = distinct_candidate[j]
            votes.append(total_candidates.count(name))
    
        #when j = 0 (index 0)
        #name = charles ( first candidate in distinct candidate list)
        #votes(counts the name charles appearing in total_candidates which is a list containing all
        # all the number of times the candidate name appears in csv file)

        for p in range(0, candicount):
            percentage = round((votes[p]*100) /sum(votes),3)
            percentage_list.append(percentage)

#time to format and print the results
        print( "Election Results")
        outputfile.write("Election Results\n")
        print("-----------------------------")
        outputfile.write("---------------------\n")
        print("Total Votes : " + str(total_votes))
        outputfile.write("Total Votes : " + str(total_votes)+"\n")
        outputfile.write("---------------------\n")
        print("-------------------------------")
  

        for results in range(0, candicount):
            xa= distinct_candidate[results] 
            xb= percentage_list[results]
            xc = votes[results] 
            xd = print(xa, ":" , xb,"%  (",xc,")")
            outputfile.write(str(xa))
            outputfile.write(":")
            outputfile.write(str(xb))
            outputfile.write("(")
            outputfile.write(str(xc))
            outputfile.write(")\n")
        outputfile.write("------------------------\n")
            # outputfile.write( distinct_candidate[results],":",percentage_list[results], "(", votes[results] ,")\n")
    
        winner = votes.index(max(votes))
#basically we using max function to determine who has the max votes in the Votes List.
#then we using votes.index to return the index value. This index value will then be used
# insert it in the distinct _candiate list to pull up by index. 
    

        print("------------------------------------")

        print("Winner: ", distinct_candidate[winner]) # from distinc_list, we using the index value of Votes List, which was got from the Winnner Vairbale
        # outputfile.write("Winner: ", distinct_candidate[winner])
        outputfile.write("Winner:")
        outputfile.write(distinct_candidate[winner])

        print("-------------------------------------")
        outputfile.write("\n--------------------------")

    
      