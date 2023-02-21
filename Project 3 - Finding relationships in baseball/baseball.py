# %%
# Import the libraries necessary for this program
import pandas as pd
import altair as alt
import numpy as np
import datadotworld as dw

# %%
# Import the baseball database as db for ease and simplicity throughout the program
db = 'byuidss/cse-250-baseball-database'

# Use the following website to look at the tables from the database
# "https://data.world/byuidss/cse-250-baseball-database/workspace/intro"

# %%

"""
Grand Questions

1. Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. 
The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID 
associated with each salary. Order the table by salary (highest to lowest) and print out 
the table in your report.


2. This three-part question requires you to calculate batting average 
(number of hits divided by the number of at-bats)

    a. Write an SQL query that provides playerID, yearID, and batting average for players with 
    at least one at bat. Sort the table from highest batting average to lowest, and show the 
    top 5 results in your report.

    b. Use the same query as above, but only include players with more than 10 “at bats” 
    that year. Print the top 5 results.

    c. Now calculate the batting average for players over their entire careers 
    (all years combined). Only include players with more than 100 at bats, and print the 
    top 5 results.


3. Pick any two baseball teams and compare them using a metric of your choice 
(average salary, home runs, number of wins, etc.). Write an SQL query to get the 
data you need. Use Python if additional data wrangling is needed, then make a graph 
in Altair to visualize the comparison. Provide the visualization and its description.
"""

# %%
# This is just an example and test to verify the database was successfully imported
results = dw.query(db, 
    'SELECT * FROM allstarfull LIMIT 5')

print(results.dataframe)

# %%

"""
Grand Question One: 
Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. 
The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID 
associated with each salary. Order the table by salary (highest to lowest) and print out 
the table in your report.
"""

# %%
"""
Tables to use: CollegePlaying, Schools, Salaries
Queries should be run to find first, the schoolID from the list of Schools. The players
who played at BYU-I will then be determined by running their playerID in the CollegePlaying
DataFrame. Finally, the teamID, yearID and salary for the year and team will be gathered
for each player.
"""

# %%
# Run a query to print the top 5 results from the Schools table
# to verify the column titles
schools5 = dw.query(db,
    "SELECT * FROM Schools LIMIT 5 ")

print(schools5.dataframe)
# Schools = [schoolid, name_full, city, state, country]

# %%
# Next, run a query to find the schoolID for BYU-I
byu_schoolid = dw.query(db, 
    "SELECT schoolid, name_full FROM Schools WHERE name_full LIKE 'Brigham Young%'")

print(byu_schoolid.dataframe)
# BYU-I schoolID = idbyuid

# %%
# Run a query to print the top 5 results from the 
# CollegePlaying table to verify the column titles
college5 = dw.query(db,
    "SELECT * FROM CollegePlaying LIMIT 5 ")

print(college5.dataframe)
# CollegePlaying = [playerid, schoolid, yearid]

# %%
# Run a query to find all playerIDs of those who played at
# BYU-I based on the schoolID that was learned previously
byu_players = dw.query(db,
    "SELECT DISTINCT playerid, schoolid FROM CollegePlaying WHERE schoolid = 'idbyuid'").dataframe

print(byu_players)
"""
stephga01
catetr01
lindsma01
"""

# %%
# Run a query to print the top 5 results from the 
# Salaries table to verify the column titles
salaries5 = dw.query(db,
    "SELECT * FROM Salaries LIMIT 5").dataframe

print(salaries5)
# Salaries = [yearid, teamid, lgid, playerid, salary]

# %%
# Run a JOIN query with all of the necessary information
q1 = dw.query(db,
    "SELECT DISTINCT Salaries.playerid, schoolid, salary, Salaries.yearid, teamid\
    FROM Salaries\
        JOIN CollegePlaying\
            ON Salaries.playerid = CollegePlaying.playerid\
    WHERE CollegePlaying.schoolid = 'idbyuid'\
    ORDER BY salary DESC").dataframe

print(q1.to_markdown())

# %%

"""
Grand Question Two:
This three-part question requires you to calculate batting average 
(number of hits divided by the number of at-bats)

    a. Write an SQL query that provides playerID, yearID, and batting average for players with 
    at least one at bat. Sort the table from highest batting average to lowest, and show the 
    top 5 results in your report.

    b. Use the same query as above, but only include players with more than 10 “at bats” 
    that year. Print the top 5 results.

    c. Now calculate the batting average for players over their entire careers 
    (all years combined). Only include players with more than 100 at bats, and print the 
    top 5 results.
"""

# %%
"""
Tables to use: Batting
Run a query for players
"""

# %%
# Print the top 5 rows from the Batting table 
# to verify the names of the columns
batting5 = dw.query(db,
    "SELECT * FROM Batting LIMIT 5").dataframe

print(batting5)

# %%
# GQ2 A)
# A query that calculates and prints the requested information
q2a = dw.query(db,
    "SELECT playerid, yearid, h/ab AS batting_avg\
    FROM Batting\
    WHERE ab >= 1\
    ORDER BY batting_avg DESC\
    LIMIT 5").dataframe

print(q2a.to_markdown())

# %%
# GQ2 B)
# A query that calculates and prints the requested information
q2b = dw.query(db,
    "SELECT playerid, yearid, h/ab AS batting_avg\
    FROM Batting\
    WHERE ab >= 10\
    ORDER BY batting_avg DESC\
    LIMIT 5").dataframe

print(q2b.to_markdown())

# %%
# GQ2 C)
# A query that calculates and prints the requested information
q2c = dw.query(db,
    "SELECT playerid, SUM(h) / SUM(ab) AS career_batting_avg\
    FROM Batting\
    GROUP BY playerid\
    HAVING SUM(ab) > 100\
    ORDER BY career_batting_avg DESC\
    LIMIT 5").dataframe

print(q2c.to_markdown())

# %%

"""
Grand Question Three:
Pick any two baseball teams and compare them using a metric of your choice 
(average salary, home runs, number of wins, etc.). Write an SQL query to get the 
data you need. Use Python if additional data wrangling is needed, then make a graph 
in Altair to visualize the comparison. Provide the visualization and its description.
"""

# %%
"""
Tables to use: Salaries
"""

# %%
# Run a query to find the teamID for both teams
teamids = dw.query(db,
    "SELECT teamid, name\
    FROM Teams\
    WHERE name LIKE '%Braves%' or name LIKE '%Yankees%'").dataframe

print(teamids)
# ATL and NYA

# %%
team_names = dw.query(db,
    "SELECT DISTINCT teamid, name,yearid\
    FROM Teams\
    WHERE (teamid = 'CHA' OR teamid = 'PHI') AND yearid > 1990").dataframe

print(team_names)
# %%
# suppress scientific notation so the tables look better
pd.set_option('display.float_format', lambda x: '%.9f' % x)


# %%
# Run a query to find the average salary for 
# the Braves team from the years 2005 to 2016
avg_salary_braves = dw.query(db,
    "SELECT yearid, teamid, ROUND(AVG(salary), 0) AS avg_salary\
    FROM Salaries\
    WHERE yearid >= 2005 AND yearid <= 2016 AND teamid = 'ATL'\
    GROUP BY yearid\
    ORDER BY yearid").dataframe

print(avg_salary_braves)

# %%
# Run a query to find the average salary for 
# the Yankees team from the years 2005 to 2016
avg_salary_yankees = dw.query(db,
    "SELECT yearid, teamid, ROUND(AVG(salary), 0) AS avg_salary\
    FROM Salaries\
    WHERE yearid >= 2005 AND yearid <= 2016 AND teamid = 'NYA'\
    GROUP BY yearid\
    ORDER BY yearid").dataframe

print(avg_salary_yankees)

# %%
# Concatenate the two dataframes, reset the index and reorder the data
avg_salary_both = avg_salary_braves.append(avg_salary_yankees
).sort_values(by = ["yearid", "teamid"], ascending = [1, 1]
).reset_index(drop = True)

# Fix the avg_salary column
avg_salary_both["avg_salary"] = avg_salary_both["avg_salary"].round().astype(int)
avg_salary_both["yearid"] = avg_salary_both["yearid"].astype(str)

# %%
# print the dataframe created above to markdown
print(avg_salary_both.to_markdown())

# %%
# Make a chart using the new dataframe
avg_sal_chart = alt.Chart(avg_salary_both).mark_line().encode(
    x = alt.X("yearid:T", title = "Year", axis = alt.Axis(format='%Y')),
    y = alt.Y("avg_salary:Q", title = "Avg. Player Salary"),
    color = alt.Text("teamid", title = "Team")
).properties(width = 550, title = "Average Player Salary Per Year (Braves vs. Yankees)")

# %%
# Display the chart
avg_sal_chart

# %%
# Save the chart
avg_sal_chart.save("avg_sal_chart.png")

# %%
