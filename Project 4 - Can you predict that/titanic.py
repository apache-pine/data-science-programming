# %%
# Loading in packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# %%
# Loading in data
url = "https://byuistats.github.io/CSE250-Course/skill_builders/ml_sklearn/machine_learning.csv"
data = pd.read_csv(url)

# %%