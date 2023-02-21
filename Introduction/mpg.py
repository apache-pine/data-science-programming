# %%
# importing libraries
import pandas as pd 
import altair as alt
from altair_saver import save
import numpy as np

# %%
# importing the mpg csv file through a url
url = 'https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv'

# plugging that url into a csv reader and assigning that parsed file to the variable 'mpg'
mpg = pd.read_csv(url)

# %%
# using the 'mpg' file to make Altair scatterplots
chart = alt.Chart(mpg).encode(x = 'displ', y = 'hwy').mark_circle()
hwy_cyl_chart = alt.Chart(mpg).encode(x = 'hwy', y = 'cyl').mark_circle()
class_drv_chart = alt.Chart(mpg).encode(x = 'class', y = 'drv').mark_circle()

# %%
# saving the charts we just made as a png
chart.save('screenshots/altair_viz_1.png')
hwy_cyl_chart.save('screenshots/hwy_cyl_chart.png')
class_drv_chart.save('screenshots/class_drv_chart.png')

# %%
# viewing the chart we just made in a preview window
chart

# %%
# viewing the chart we just made in a preview window
hwy_cyl_chart

# %%
# viewing the chart we just made in a preview window
class_drv_chart

# each of these charts were broken up into individual cells to control which ones
# were viewed and when they were viewed.

# %%
# making a table of some of the data included in the 'mpg' file.
# the specific data included in the table is not important, it is just 
# a proof of concept
print(mpg
    .head(5)
    .filter(['manufacturer', 'model', 'year', 'hwy'])
    .to_markdown(index=False))

# %%
