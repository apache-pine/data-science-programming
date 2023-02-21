# %%
# Import the libraries necessary for this program
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats

# %%
# Import the JSON file through a URL
url = "https://byuistats.github.io/CSE250-Course/skill_builders/json_missing/json_missing.json"

# Read that URL and assign it to the variable df
df = pd.read_json(url)

# %%
df

# %%
