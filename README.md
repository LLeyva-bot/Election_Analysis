# Module_Three_Challenge_Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate own.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code, 1.55.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doanes
- The candidates results were:
  - Charles Casper Stockham received "23.0%" of votes and "85,213" number of votes.
  - Diana Degette received "73.8%" of votes and "272,892" number of votes.
  - Raymon Anthony Doanes received "3.1%" of votes and "11,606" number of votes.
 - The winner of the election was:
  - Diana Degettte, who recieved "73.8%" of the vote and "272,892" number of votes.

- Initial Analysis:
![election_analysis.txt](https://github.com/LLeyva-bot/Election_Analysis/blob/main/Analysis/election_analysis.txt)

## Challenge Overview

After submitting the election audit results, the election commision requested some additional data to complete the audit:

1. Calculate the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest turnout.

## Challenge Summary
The additional analysis of the election show that:
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson received "10.5% of votes and ""38,855" number fo votes.
  - Denver receievd "82.8%" of votes and "306,055" number of votes.
  - Arapahoe recieved "6.7%" of votes and "24,801" number of votes.
- The county with the largest turnout was:
  - Denver, which recieved "82.8%" of the votes and "306,055" number of votes.

- Final Analysis:
![election_results.txt](https://github.com/LLeyva-bot/Election_Analysis/blob/main/Analysis/election_results.txt)

## Conclusion
The final script, ![PyPoll_Challenge.py](https://github.com/LLeyva-bot/Election_Analysis/blob/main/PyPoll_Challenge.py),can be used by the Colorado Board of Elections to complete future election audits. The election_results.csv with the current election data can be replaced with a new .csv file and reran for future local congressional elections to obtain the same analysis. If new information is added the the election data, like age of voter, the script can be easily modified to analyze the additional data as seen in the challenge summary when the script was modified to obtain county data.  
