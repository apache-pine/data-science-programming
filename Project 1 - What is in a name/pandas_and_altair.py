# %%
# packages are imported for use later in the program
import numpy as np
import pandas as pd
import altair as al

# data is imported for later use in the program
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

# %%
# assign the columns to a variable called col_list
col_list = dat.columns

# %%
# display the dimensions of the dataframe
# aka, the number of columns and rows
print(dat.shape)
# there are 1173 rows in the dataset and 14 columns

# %%
# dat.head() is run to display the first 5 rows of data
dat.head()
# just from looking at this output, the "unnamed: 0" column 
# is redundant since the rows are counted separately

# %%
# use the drop() function to tidy up the data and get rid 
# of the redundant column. The changes are saved to dat
dat = dat.drop([col_list[0]], axis = 1)

# %%
# dat.head() is ran again to verify that the correct
# column was removed
dat.head()

# %%
# Two expressions are stated
exp1 = 8 > 5
exp2 = dat.violent < 300

# %%
# The above expressions are printed for evaluation
print(exp1)
print(exp2)
# The difference between the two is that exp1 is a 
# single boolean and exp2 is a list of booleans. 
# In exp1, the condition is always true because 8 
# will always be greater than 5. In exp2, it actually 
# evaluates the data and decides the answers based on 
# whether or not the value in the violent column is 
# less than 300

# %%
# dat.violent < 300 and the actual value from the violent
# column in dat are put into a dataframe and displayed
exp = pd.DataFrame({"dat.violent < 300" : exp2,
                    "violent value from dat" : dat.violent})

exp
# The relationship between the two is the one states
# whether or not the value is below 300 and the other
# shows the real value, proving the boolean in dat.violent < 300
# to be accurate

# %%
# the query() function is ran to filter the data in dat to 
# only data for Idaho, then the new dat is printed
dat = dat.query("state == 'Idaho'")

dat

# %%
# dat.shape is printed to verify that the proper number of
# rows and columns are recorded
print(dat.shape)

# %%
# a new column comparing the ratio between murder rate and
# violent rate is created
dat.assign(murder_vs_violent = dat.murder / dat.violent)

# %%
# A scatter plot showing the relationship between murder
# rate and violent rate in the state of Idaho is made
al.Chart(dat).encode(
    x = "murder",
    y = "violent"
).mark_circle()

# %%
# the data in dat is filtered down to only the data
# between the years1993 and 1997
dat = dat.query("year >= 1993 & year <= 1997")

dat

# %%
# dat is reset
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

# %%
# dat is narrowed down to only the data for the
# following states: Idaho, Utah and Oregon
dat = dat.query("state in ['Idaho', 'Utah', 'Oregon']")

# %%
# A line chart is made that shows the change in number of
# prisoners in each state over the years
al.Chart(dat).encode(
    x = al.X("year", axis = al.Axis(format = "d")),
    y = al.Y("prisoners"),
    color = "state"
).mark_line().properties(title = "# of Prisoners per State")

# %%
# dat is reset
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

# %%
# Data is narrowed down to the state of Idaho
# without using the query() function
dat[dat.state == "Idaho"]

# %%
# Data is narrowed down to only data from the 
# years between 1993 and 1997 without using the
# query() function
dat[(dat.year >= 1993) & (dat.year<= 1997)]

# %%
# data is narrowed down to only the data for the
# states of Idaho, Utah and Oregon without using 
# the query() function
dat[dat["state"].isin(["Idaho", "Utah", "Oregon"])]
