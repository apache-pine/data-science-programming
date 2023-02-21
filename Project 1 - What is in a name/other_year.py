# %%
# packages are imported for use later in the program
from cProfile import label
import numpy as np
import pandas as pd
import altair as alt
import datetime

# %%
# importing the names_year csv file through a url
url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'

# plugging that url into a csv reader and assigning it to the variable dat
dat = pd.read_csv(url)

# %%
# The Grand Questions that this program should answer:
# 1. How does your name at your birth year compare to its use historically?
# 2. If you talked to someone named Brittany on the phone, what is your guess of their age? 
# What ages would you not guess?
# 3. Mary, Martha, Peter, and Paul are all Christian names. From 1920 - 2000, compare the 
# name usage of each of the four names.
# 4. Think of a unique name from a famous movie. Plot that name and see how increases line 
# up with the movie release.

# %%
# find if my name is within the csv file using the query() function
# but since my name has an uncommon spelling (Kylar), searching for the
# alternate, more common spelling (Kyler)
my_name_df = dat.query("name == 'Andrew'").reset_index(drop = True)

my_name_df
# Commented out because was only necessary to initially display to verify that
# it is working properly and the name Kyler existed. The spelling Kylar did not exist

# %%
# A line chart is created based on my name. The x axis is the year and y axis is
# the total use per year. There is also a line of cyan color marking the year 1998, 
# my birth year.
lines = (
    alt.Chart(my_name_df)
    .mark_line()
    .encode(
        x = alt.X("year", axis = alt.Axis(format = "d", title = "Year (Cyan Line is 2000)")),
        y = "Total"
    )
    .properties(title = "Use of the Name Andrew")
)

xrule = (
    alt.Chart()
    .encode(x = alt.datum(2000))
    .mark_rule(color="cyan", strokeWidth = 2)
)

my_name_chart = lines + xrule

# Save the chart as a png
my_name_chart.save("andrew_name_chart.png")

# %%
# displays the chart made above
my_name_chart

# %%
# Narrowing down the years closer to my birthday for further inspection
# and resetting the index for convenience and easier to read
my_name_year_close_df = my_name_df.query("year > 1990 and year < 2005").reset_index(drop = True)

my_name_year_close_df

# %%
# Make a table with this new info
print(my_name_year_close_df
    .filter(["name", "year", "Total"])
    .to_markdown(index = True))

# %%
# Run a query for the name "Brittany" and save it as a new DataFrame
# and reset the index
brittany_df = dat.query("name == 'Brittany'").reset_index(drop = True)

# Display the new DataFrame
brittany_df

# %%
# Get the current year using datatime and stripping away extra info
current_date_time = datetime.datetime.now()
current_date = current_date_time.date()
current_year = int(current_date.strftime("%Y"))

# %%
# Add an age column to the DataFrame
brittany_df = brittany_df.assign(Age = lambda x: current_year - x.year)

# %%
# Make a chart that shows the number of people named 
# "Brittany" at the given ages
brittany_age_chart = alt.Chart(brittany_df).mark_bar().encode(
    x = "Age:O",
    y = "Total"
).properties(title = "Average Age of People Named Brittany")

# Save the chart
brittany_age_chart.save("brittany_age_chart.png")

# %%
# Display the chart
brittany_age_chart
# %%
# Print a table showing the first 5 years of data
print(brittany_df
    .head()
    .filter(["name", "year", "Age", "Total"])
    .to_markdown(index = True))

# %%
# Call query() to make another DataFrame, this one composed
# of the names Mary, Martha, Peter and Paul between the years
# 1920 and 2000. Index is also reset
christian_names_comparison_df = (dat
    .query("(name == 'Mary' or name == 'Martha' or name == 'Peter' or name == 'Paul') and(year >= 1920 and year <= 2000)")
    .reset_index(drop = True))

# Display the new DataFrame
christian_names_comparison_df

# %%
# Make a chart showing the change in use of these names over the years
christian_names_comparison_chart = (alt.Chart(christian_names_comparison_df)
    .mark_line()
    .encode(
        x = alt.X("year", axis = alt.Axis(format = "d", title = "Year")),
        y = "Total",
        color = "name",
        strokeDash = "name"
    )
).properties(title = "Historical Use of the Names Martha, Mary, Paul, and Peter")

# Save the chart
christian_names_comparison_chart.save("christian_names_comparison_chart.png")
# %%
# Display the chart made above
christian_names_comparison_chart

# %%
# Create a DataFrame for each name individually
martha_df = christian_names_comparison_df.query("name == 'Martha'").reset_index(drop = True)
mary_df = christian_names_comparison_df.query("name == 'Mary'").reset_index(drop = True)
paul_df = christian_names_comparison_df.query("name == 'Paul'").reset_index(drop = True)
peter_df = christian_names_comparison_df.query("name == 'Peter'").reset_index(drop = True)

# %%
# Find the total use for each name from 1920 to 2000
martha_total = int(martha_df.sum(axis = 0, skipna = True).filter(["Total"]))
mary_total = int(mary_df.sum(axis = 0, skipna = True).filter(["Total"]))
paul_total = int(paul_df.sum(axis = 0, skipna = True).filter(["Total"]))
peter_total = int(peter_df.sum(axis = 0, skipna = True).filter(["Total"]))

# %%
# Print the totals
print(f"Total Use of Martha from 1920-2000: {martha_total}")
print(f"Total Use of Mary from 1920-2000: {mary_total}")
print(f"Total Use of Paul from 1920-2000: {paul_total}")
print(f"Total Use of Peter from 1920-2000: {peter_total}")

# %%
# Create a DataFrame including the names and their totals
christian_names_totals_df = pd.DataFrame({
    "Name" : ["Martha", "Mary", "Paul", "Peter"],
    "Total" : [martha_total, mary_total, paul_total, peter_total]
})

# Create a bar graph displaying the total use of each name
christian_names_totals_chart = (alt.Chart(christian_names_totals_df)
    .mark_bar()
    .encode(
        x = "Name",
        y = "Total"
    )
).properties(title = "Total Use of Names from 1920-2000")

# Save the chart
christian_names_totals_chart.save("christian_names_totals_chart.png")

# %%
# Display the chart
christian_names_totals_chart

# %%
# Create a table displaying the totals
print(christian_names_totals_df.to_markdown(index = True))

# %%
# divide all of the totals by 80 years to get the average 
# use per year for each name
martha_average = martha_total / 80
mary_average = mary_total / 80
paul_average = paul_total / 80
peter_average = peter_total / 80

# %%
# Create a DataFrame including the names and their average use per year
christian_names_average_df = pd.DataFrame({
    "Name" : ["Martha", "Mary", "Paul", "Peter"],
    "Average per Year" : [martha_average, mary_average, paul_average, peter_average]
})

# Create a bar graph displaying the average use of each name
christian_names_average_chart = (alt.Chart(christian_names_average_df)
    .mark_bar()
    .encode(
        x = "Name",
        y = "Average per Year"
    )
).properties(title = "Average Use of Names per Year between 1920-2000")

# Save the chart
christian_names_average_chart.save("christian_names_average_chart.png")

# %%
christian_names_average_chart

# %%
# Call the query function and reset_index function to
# create a new DataFrame with a reset index
trinity_df = dat.query("name == 'Trinity'").reset_index(drop = True)

# Display the new DataFrame
trinity_df

# %%
# Create a chart using the trinity_df DataFrame and
# put extra lines over the years that The Matrix movies released
trinity_lines = (
    alt.Chart(trinity_df)
    .mark_line()
    .encode(
        x = alt.X("year", axis = alt.Axis(format = "d", title = "Year (Cyan Line Shows Years Matrix Movies Released)")),
        y = "Total"
    )
).properties(title = "Use of the Name Trinity and Years Matrix Movies Released")

# First movie was released in 1999
xrule1 = (
    alt.Chart()
    .encode(
        x = alt.datum(1999))
    .mark_rule(color = "cyan", strokeWidth = 2)
)

# Second and third movies released in 2003
xrule2 = (
    alt.Chart()
    .encode(
        x = alt.datum(2003))
    .mark_rule(color = "cyan", strokeWidth = 2)
)

# Combine (concatenate) the charts and rules into one chary
trinity_chart = trinity_lines + xrule1 + xrule2

# Save the chart as a png
trinity_chart.save("trinity_chart.png")

# %%
# Display trinity_chart
trinity_chart

# %%
