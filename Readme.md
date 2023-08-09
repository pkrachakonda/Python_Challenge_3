# Python_Challenge_3
This section decsribes the python coding developed for 
  * estimating *total profit and losses* over a certain duration using ***PyBank***; and 
  * counting *total number of votes* polled as part of an election process and declaring the winning candidate based on *percentage* using ***PyRoll*** as an example

## PyBank

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/70dc5055-381b-491e-aab2-77e43b74ad39)

Line 1 imports packages *OS* and *CSV* modules required for the analysis into environment.

Lines 8 - 12, using join, path functions of the OS module and DictReader function of CSV module, budget_data.csv file located in the Resource folder is read as *csvfile* and it's data (in column format) are stored in *data* and *values* lists.

In lines 4, 5, 15-18, various ***variables*** and an **empty lists*** are declared for *storing values*.

### Estimating Total months and Change in Profit and Losses over the duration 

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/282ab493-ef11-43c3-9850-e9e1b05f39c6)

As "*i*" iterates through each row in the csv starting from second row *(line 22)*, variable *count* which counts the months is increased by 1 *(line 27)* to count the total months in the duration of period. The total sum of profit/losses is also calculated by suming the consecutive rows and this value is store as "*total*" variable *(line 23)*. Difference in profit or loss value between two rows were estimated and were stored in the *diff* list *(line 25)* and total change in profit/loss for the entire duration of csv file record is stored as *"change"* variable *(line 26)*. *Average value* is estimated for the duration *(line 28)*.   

### Estimating Highest and Lowest increase in Profit/Losses over the duration

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/6546e47a-7d6d-43ea-bc12-da6276d708a7)

Initially two variable *"lower_profit"* & *"higher_profit"* are defined as zero and they are compared with the profit/loss difference value for each month *(line 32 -34)*. As *"i"* progress through each row of the csv file both variable values were re-assigned (lines 36 - 41) and respective month were stored in *"day_low"* and *"day_high"* variables respectively. 
After obtaining highest and lowest incease in profit/loss information, the file is closed for reading *(line 43)*

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/8bf9e238-c3be-4553-8c54-de1028a8ca61)

Lines 46 - 58 print the analysis results to terminal/ screen, using *f-string* format.

### Writing the Analysis results to a text file and saving it to a folder

![image](https://github.com/pkrachakonda/Python_Challenge_3/assets/20739237/16d23a17-c3c1-477b-b030-86ae837b43b2)

Using writer function of csv module the analysis results are written to *"PyBank_Analysis.txt" (line 63)*. Using join and path functions of OS module, the path to Analysis folder is defined and joined in the coding (line 62). Various results obtained *(lines 65 - 77)* as part of the analysis are written in text as rows. After completing the writing process the file is closed *(line 79)*.
