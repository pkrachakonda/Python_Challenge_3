# Python_Challenge_3
This section decsribes the python coding developed for 
  * estimating *total profit and losses* over a certain duration using ***PyBank***; and 
  * counting *total number of votes* polled as part of an election process and declaring the winning candidate based on *percentage* using ***PyRoll*** as an example

## PyBank

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/70dc5055-381b-491e-aab2-77e43b74ad39)

Line 1 imports packages *OS* and *CSV* modules required for the analysis into environment.

Lines 8 - 12, using join, path functions of the OS module and DictReader function of CSV module, ***budget_data.csv*** file located in the Resource folder is read as *csvfile* and it's data (in column format) are stored in *data* and *values* lists.

In lines 4, 5, 15-18, various ***variables*** and an **empty lists*** are declared for *storing values*.

### Estimating Total months and Change in Profit and Losses over the duration 

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/282ab493-ef11-43c3-9850-e9e1b05f39c6)

As "*i*" iterates through each row in the csv starting from second row *(line 22)*, variable *count* which counts the months is increased by 1 *(line 27)* to count the total months in the duration of period. The total sum of profit/losses is also calculated by suming the consecutive rows and this value is store as "*total*" variable *(line 23)*. Difference in profit or loss value between two rows were estimated and were stored in the *diff* list *(line 25)* and total change in profit/loss for the entire duration of csv file record is stored as *"change"* variable *(line 26)*. *Average value* is estimated for the duration *(line 28)*.   

### Estimating Highest and Lowest increase in Profit/Losses over the duration

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/6546e47a-7d6d-43ea-bc12-da6276d708a7)

Initially two variable *"lower_profit"* & *"higher_profit"* are defined as zero and they are compared with the profit/loss difference value for each month *(line 32 -34)*. As *"i"* progress through each row of the csv file both variable values were re-assigned (lines 36 - 41) and respective month were stored in *"day_low"* and *"day_high"* variables respectively. 
After obtaining highest and lowest incease in profit/loss information, the file is closed for reading *(line 43)*

### Printing Analysis results to Terminal

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/8bf9e238-c3be-4553-8c54-de1028a8ca61)

Lines 46 - 58 print the analysis results to terminal/ screen, using *f-string* format.

### Writing the Analysis results to a text file and saving it to a folder

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/16d23a17-c3c1-477b-b030-86ae837b43b2)

Using writer function of csv module the analysis results are written to *"PyBank_Analysis.txt" (line 63)*. Using join and path functions of OS module, the path to Analysis folder is defined and joined in the coding (line 62). Various results obtained *(lines 65 - 77)* as part of the analysis are written in text as rows. After completing the writing process the file is closed *(line 79)*.

## PyRoll

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/4c9b71ac-1b66-403a-ba59-b5db3958aa8c)

Line 1 imports packages *OS* and *CSV* modules required for the analysis into environment.

Lines 10 - 14, using join, path functions of the OS module and DictReader function of CSV module, ***election_data.csv*** file located in the Resource folder is read as *csvfile* and it's data (in column format) are stored in *ballots* and *cand* lists.

For generating a unquie list of camdidates, for loop is used *(line 18)*. Line 19 checks if name string while looping through the csv file, already exists in the *cand_list*. If name string does not exist in the list, then it is appended to the *cand_list* list file as row *(line 20)*.

In lines 4 -6, various ***variables*** and an **empty lists*** are declared for *storing values*.

### Estimating Total number of votes each candidate received and Polled

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/5beed73e-8f70-4557-9ab7-a808227e4745)

An null list *No_of_votes* and an variable * Total_Votes* are declared to stored the values from the analysis *(lines 24 -25)*. As "*i*" iterates through each row in the csv  *(line 26)*, variable *Total_votes* which counts the total number of votes casted is increased by 1 *(line 30)*. The candidate names in the csv file are compared with there row location in the *cand_list* and votes casted for them are increased as *i* progress through the csv file *(lines 28-29)*.

### Estimating the Percentage of votes each candidate received and Finding the winner candidate 

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/55cff25c-9541-441a-9cd2-f2083f62ae46)

Initially a variable *"winner"*  and an empty list *"percent_of_votes"* are defined  *(lines 34 - 35)* and list is appended with the percentage of vote each candidate received as *i* progress through the csv file *(line 37)*. As *"i"* progress through each row of the csv file, votes received received by each candidate are compared and the variables *winner* and *winner_cand* values were re-assigned (lines 41 - 42) respectively. 
After obtaining candidate with highest votes and name, the file is closed for reading *(line 44)*


### Printing Analysis results to Terminal

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/bb1457a7-e1d3-4017-8408-665bd63e1032)

Lines 48 - 63 print the analysis results to terminal/ screen, using *f-string* format.

### Writing the Analysis results to a text file and saving it to a folder

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/7cccb339-3c30-4758-8c24-0b6404472bef)

Using writer function of csv module the analysis results are written to *"PyRoll_Analysis.txt" (line 68)*. Using join and path functions of OS module, the path to Analysis folder is defined and joined in the coding (line 67). Various results obtained *(lines 70 - 85)* as part of the analysis are written in text as rows. After completing the writing process the file is closed *(line 87)*.
