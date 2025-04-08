#2. Voter Turnout Insights

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\ASUS\Downloads\python Dataset 2.csv")

#(a) Calculate the average voter turnout percentage
average_turnout = df['turnout_percentage'].mean()
print(f"Average Voter Turnout Percentage: {average_turnout:.2f}%")

#(b) Identify the constituency with the highest and lowest voter turnout
highest_turnout = df.loc[df['turnout_percentage'].idxmax(), ['candidate_name', 'turnout_percentage']]
lowest_turnout = df.loc[df['turnout_percentage'].idxmin(), ['candidate_name', 'turnout_percentage']]
print("Highest Voter Turnout:")
print(highest_turnout)
print("\nLowest Voter Turnout:")
print(lowest_turnout)

#(c) Find the total number of electors and valid votes in the dataset
total_electors = df['total_electors'].sum()
total_valid_votes = df['valid_votes'].sum()
print(f"Total Electors: {total_electors}")
print(f"Total Valid Votes: {total_valid_votes}")

#(d) Calculate the overall voter turnout percentage across all constituencies
overall_turnout = (total_valid_votes / total_electors) * 100
print(f"Overall Voter Turnout Percentage: {overall_turnout:.2f}%")
