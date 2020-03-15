# -*- coding: utf-8 -*-
"""Graduate Admission_EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18EMmbAvN65SmeF9sLzIAL94nD8LhAEEL
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

"""## Knowing the dataset"""

dataset = pd.read_csv("/kaggle/input/graduate-admissions/Admission_Predict_Ver1.1.csv")

"""#### Reviewing 1st five data in the dataset"""

dataset.head()

"""#### Removig Serial No. column bcoz its not adding any value to datatset."""

dataset.drop(['Serial No.'], axis=1,  inplace=True)

column_names = {'GRE Score': 'gre_score', 'TOEFL Score': 'toefl_score', 'University Rating': 'university_rating', \
                'SOP': 'sop', 'LOR': 'lor', 'CGPA': 'cgpa',\
                'Research': 'research', 'Chance of Admit ': 'chance_of_admit'}

"""#### Changing column names"""

dataset = dataset.rename(columns = column_names)
dataset.head()

"""#### Reviewing last five data in the dataset"""

dataset.tail()

"""#### Size of dataset"""

dataset.shape

dataset.dtypes

for data in dataset.columns:
    print(data)
    print(dataset[data].unique())
    print("="*80)

"""#### Five point summury of dataset"""

dataset.describe()

"""#### Checking for any null value in dataset"""

dataset.isnull().any()

"""#### Ploting histogram on dataset"""

plt.subplots(figsize=(10, 5))
sns.heatmap(dataset.corr(), cmap="YlGnBu", annot=True, fmt= '.0%')
plt.show()

"""#### Ploting correlation bar graph based on target variable in ascending order."""

plt.subplots(figsize=(10, 5))
dataset.corr().loc['chance_of_admit'].sort_values(ascending=False).plot(kind='bar')

sns.pairplot(dataset, corner=True, diag_kind="kde")

"""#### How important is Research to get an Admission?"""

print(f"{dataset['research'].value_counts()/len(dataset)}")
print("="*80)
sns.countplot(dataset['research'])

"""#### CGPA vs GRE Score Analysis"""

sns.scatterplot(y="cgpa", x="gre_score", hue="university_rating", data=dataset)

sns.scatterplot(y="cgpa", x="gre_score", hue="research", data=dataset)