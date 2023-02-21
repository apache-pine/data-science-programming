# %%
# Import libraries
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scikitplot as skplt

# %%
# import sklearn subsections
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import classification_report

# %%
# Import the three dataframes
denver = pd.read_csv("dwellings_denver.csv")
dwellings_ml = pd.read_csv("dwellings_ml.csv")
neighborhoods_ml = pd.read_csv("dwellings_neighborhoods_ml.csv")

alt.data_transformers.enable("json")

# %%
# Print the first 5 rows
denver.head()

# %%
# Print the first 5 rows
dwellings_ml.head()

# %%
# Print the first 5 rows
neighborhoods_ml.head()

# %%
"""
GRAND QUESTIONS:

1. Create 2-3 charts that evaluate potential relationships 
between the home variables and before1980.

2. Can you build a classification model (before or after 1980) 
that has at least 90% accuracy for the state of Colorado to 
use (explain your model choice and which models you tried)?

3. Will you justify your classification model by detailing 
the most important features in your model (a chart and a 
description are a must)?

4. Can you describe the quality of your classification 
model using 2-3 evaluation metrics? You need to provide an 
interpretation of each evaluation metric when you provide the value.
# Confusion Matrix
"""

# %%
"""
Steps:
0. Load Data
1. Exploratory Data Analysis
2. Split Data
3. Train Classifiers
4. Test Classifiers
5. Assess Classifier Performance
6. Repeat Steps 2-5 Until Desired "Accuracy" Achieved
"""

# %%
# Create a subset to begin exploratory data analysis and find relationships
# between home variables and before1980
h_subset = dwellings_ml.filter(["livearea", "finbsmnt", "basement", "stories", 
    "nocars", "numbdrm", "numbaths", "yrbuilt", "before1980"]).sample(500)
sns.pairplot(h_subset, hue = "before1980")

# %%
# More exploratory data analysis
corr = h_subset.drop(columns = "before1980").corr()

# %%
# More exploratory data analysis
sns.heatmap(corr)

plt.savefig("heatmap_chart1.jpg", dpi = 200, bbox_inches = "tight")

# %%
"""
Grand Question One

Create 2-3 charts that evaluate potential relationships 
between the home variables and before1980.
"""

# %%
# Find all correlations between variables in the data set.
# Keep only "before1980" because that's our variable of interest.
correlations = dwellings_ml.corr().before1980.sort_values()

correlations.drop(["before1980", "yrbuilt", "abstrprd"], inplace = True)

# Prepare the dataset for charting
correlations = pd.DataFrame(correlations.reset_index())

# Make the chart
chart = (alt.Chart(correlations).mark_bar().encode(
    x = alt.X("before1980",
      axis = alt.Axis(title = "Correlation")),
    y = alt.Y("index:N",
      axis = alt.Axis(title = "Features"),
      sort = None),
    color=alt.condition(
        alt.datum.before1980 > 0,
        alt.value("steelblue"),  # The positive color
        alt.value("orange")  # The negative color
    )
  )
  .configure_axis(
    labelFontSize=20,
    titleFontSize=30)
  .configure_title(fontSize=35)
  .properties(
      width = 1200,
      height = 1500,
      title = "Correlations of Home Features with Target (before1980)"
  ))

# Save the chart into a file
chart.save("correlations.png")

# %%
# Find all correlations between variables in the data set.
# Keep only "before1980" because that's our variable of interest.
correlations = dwellings_ml.corr().before1980.sort_values()

# Using the previous chart, filter down to the ten most usefull features
correlations = correlations.filter(["stories", "numbaths", "arcstyle_TWO-STORY", 
    "gartype_Att", "livearea", "arcstyle_ONE-STORY", "quality_C", "status_I", 
    "gartype_Det", "condition_Good"])

correlations = pd.DataFrame(correlations.reset_index())

chart = (alt.Chart(correlations).mark_bar().encode(
    x = alt.X("before1980",
      axis = alt.Axis(title = "Correlation")),
    y = alt.Y("index:N",
      axis = alt.Axis(title = "Features"),
      sort = None),
    color=alt.condition(
        alt.datum.before1980 > 0,
        alt.value("steelblue"),  # The positive color
        alt.value("orange")  # The negative color
    )
  )
  .configure_axis(
    labelFontSize=20,
    titleFontSize=20)
  .configure_title(fontSize=25)
  .properties(
      width = 800,
      height = 900,
      title = "Correlations of Home Features with Target (before1980)"
  ))

# Save the chart into a file
chart.save("correlations2.png")

# %%
# Make a new heatmap and pairplot with the same features
p_subset = dwellings_ml.filter(["stories", "numbaths", "arcstyle_TWO-STORY", 
    "gartype_Att", "livearea", "arcstyle_ONE-STORY", "quality_C", "status_I", 
    "gartype_Det", "condition_Good", "yrbuilt", "before1980"]).sample(500)
sns.pairplot(p_subset, hue = "before1980")

# %%
# More exploratory data analysis
corr = p_subset.drop(columns = "before1980").corr()

# %%
# More exploratory data analysis
sns.heatmap(corr)

# Save the heatmap
plt.savefig("heatmap_chart.jpg", dpi = 200, bbox_inches = "tight")

# %%
"""
Grand Question Two

Can you build a classification model (before or after 1980) 
that has at least 90% accuracy for the state of Colorado to 
use (explain your model choice and which models you tried)?
"""

# %%
# Drop the target column as well as yrbuilt as that is used to get the target. 
# Parcel is an id number, of sorts, and not needed
X_pred = dwellings_ml.drop(dwellings_ml.filter(regex = 'before1980|yrbuilt|parcel'
    ).columns, axis = 1)
y_pred = dwellings_ml["before1980"]
X_train, X_test, y_train, y_test = train_test_split(
    X_pred, y_pred, test_size = .34, random_state = 76)

# %%
# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_probs = clf.predict_proba(X_test)

# %%
# Comparing predictions to actual values
metrics.accuracy_score(y_test, y_pred)

# %%
# Print a classification report to check accuracy
print(metrics.classification_report(y_pred, y_test))

# %%
# Convert classification report to DataFramea and 
# print it in markdown to display for client
clf_report = metrics.classification_report(y_pred, y_test, output_dict = True)

clf_df = pd.DataFrame(clf_report).transpose()

print(clf_df.to_markdown())

# %%
# Create a plot chart to review accuracy
metrics.plot_roc_curve(clf, X_test, y_test)

# Save the plot
plt.savefig("clf_plot_curve.jpg")

# %%
# Make a dataframe to find which features were most important
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': clf.feature_importances_}).sort_values('f_values', ascending = False)

#%%
# Graph the dataframe in a chart and save it
chart2 = (alt.Chart(df_features.query('f_values > .011'))
    .encode(
        alt.X('f_values'),
        alt.Y('f_names', sort = '-x'))
    .mark_bar())

chart2.save("decision_tree_features.png")

# %%
# Print the most important features and their scores to a markdown table
feat_imports = (pd.DataFrame({"feature names": X_train.columns,
                              "importances": clf.feature_importances_})
                .sort_values("importances", ascending=False)).query("importances > 0.03")

print(feat_imports.to_markdown(index=False))

# %%
# Print a confusion matrix to show false positives and false negatives
print(confusion_matrix(y_test, y_pred))

# %%
# Create a confusion matrix display and save it
cf_matrix = confusion_matrix(y_test, y_pred, labels = clf.classes_)

disp = ConfusionMatrixDisplay(confusion_matrix = cf_matrix, display_labels = clf.classes_)

disp.plot()

plt.savefig("confusion_matrix_clf.jpg")

# %%
"""Run the same data through a random forrest classifier"""

# Drop the target column as well as yrbuilt as that is used to get the target. 
# Parcel is an id number, of sorts, and not needed
X_pred = dwellings_ml.drop(dwellings_ml.filter(regex = 'before1980|yrbuilt|parcel'
    ).columns, axis = 1)
y_pred = dwellings_ml["before1980"]
X_train, X_test, y_train, y_test = train_test_split(
    X_pred, y_pred, test_size = .34, random_state = 76)

# %%
# Creating random forest object
rf = RandomForestClassifier(random_state=24)

# Fit with the training data
rf.fit(X_train, y_train)

# Using the features in the test set to make predictions
y_pred = rf.predict(X_test)

# %%
# Comparing predictions to actual values
metrics.accuracy_score(y_test, y_pred)

# %%
# Print a classification report to check accuracy
print(metrics.classification_report(y_pred, y_test))

# %%
# Convert classification report to DataFrame and 
# print it in markdown to display for client
rf_report = metrics.classification_report(y_pred, y_test, output_dict = True)

rf_df = pd.DataFrame(rf_report).transpose()

print(rf_df.to_markdown())

# %%
# Create a plot chart to review accuracy
metrics.plot_roc_curve(rf, X_test, y_test)

# Save the plot
plt.savefig("rf_plot_curve.jpg")

# %%
# Make a dataframe to find which features were most important
df_features2 = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': rf.feature_importances_}).sort_values('f_values', ascending = False)

#%%
# Graph the dataframe in a chart and save it
chart3 = (alt.Chart(df_features2.query('f_values > .011'))
    .encode(
        alt.X('f_values'),
        alt.Y('f_names', sort = '-x'))
    .mark_bar())

chart3.save("random_forrest_features.png")

# %%
# Print the most important features and their scores to a markdown table
feat_imports = (pd.DataFrame({"feature names": X_train.columns,
                              "importances": rf.feature_importances_})
                .sort_values("importances", ascending=False)).query("importances > 0.05")

print(feat_imports.to_markdown(index=False))

# %%
# Print a confusion matrix to show false positives and false negatives
print(confusion_matrix(y_test, y_pred))

# %%
# Create a confusion matrix display and save it
cf_matrix = confusion_matrix(y_test, y_pred, labels = rf.classes_)

disp = ConfusionMatrixDisplay(confusion_matrix = cf_matrix, display_labels = rf.classes_)

disp.plot()

plt.savefig("confusion_matrix_rf.jpg")

# %%

