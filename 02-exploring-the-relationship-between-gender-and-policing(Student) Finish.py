# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <p style="text-align: center;"><img src="https://docs.google.com/uc?id=1lY0Uj5R04yMY3-ZppPWxqCr5pvBLYPnV" class="img-fluid" alt="CLRSWY"></p>
# 
# ___
# %% [markdown]
# <h1><p style="text-align: center;">Data Analysis with Python <br>Project - 1</p><h1> - Traffic Police Stops <img src="https://docs.google.com/uc?id=17CPCwi3_VvzcS87TOsh4_U8eExOhL6Ki" class="img-fluid" alt="CLRSWY" width="200" height="100"> 
# %% [markdown]
# Does the ``gender`` of a driver have an impact on police behavior during a traffic stop? **In this chapter**, you will explore that question while practicing filtering, grouping, method chaining, Boolean math, string methods, and more!
# %% [markdown]
# ***
# %% [markdown]
# ## Examining traffic violations
# %% [markdown]
# Before comparing the violations being committed by each gender, you should examine the ``violations`` committed by all drivers to get a baseline understanding of the data.
# 
# In this exercise, you'll count the unique values in the ``violation`` column, and then separately express those counts as proportions.
# %% [markdown]
# > Before starting your work in this section **repeat the steps which you did in the previos chapter for preparing the data.** Continue to this chapter based on where you were in the end of the previous chapter.

# %%
import numpy as np
import pandas as pd


# %%
ri = pd.read_csv("police.csv")

# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Count the unique values in the ``violation`` column, to see what violations are being committed by all drivers.
# *   Express the violation counts as proportions of the total.

# %%
ri["violation"].value_counts()


# %%
ri["violation"].value_counts()/ri["violation"].count()

# %% [markdown]
# ## Comparing violations by gender
# %% [markdown]
# The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.
# 
# You'll first create a ``DataFrame`` for each gender, and then analyze the ``violations`` in each ``DataFrame`` separately.
# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, female, that only contains rows in which ``driver_gender`` is ``'F'``.
# *   Create a ``DataFrame``, male, that only contains rows in which ``driver_gender`` is ``'M'``.
# *   Count the ``violations`` committed by female drivers and express them as proportions.
# *   Count the violations committed by male drivers and express them as proportions.

# %%
fri = ri[ri['driver_gender'] == 'F']


# %%
fri


# %%
mri = ri[ri['driver_gender'] == 'M']  


# %%
mri


# %%
fri['violation'].value_counts()/131138


# %%
mri['violation'].value_counts() / 349446

# %% [markdown]
# ## Comparing speeding outcomes by gender
# %% [markdown]
# When a driver is pulled over for speeding, many people believe that gender has an impact on whether the driver will receive a ticket or a warning. Can you find evidence of this in the dataset?
# 
# First, you'll create two ``DataFrames`` of drivers who were stopped for ``speeding``: one containing ***females*** and the other containing ***males***.
# 
# Then, for each **gender**, you'll use the ``stop_outcome`` column to calculate what percentage of stops resulted in a ``"Citation"`` (meaning a ticket) versus a ``"Warning"``.
# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, ``female_and_speeding``, that only includes female drivers who were stopped for speeding.
# *   Create a ``DataFrame``, ``male_and_speeding``, that only includes male drivers who were stopped for speeding.
# *   Count the **stop outcomes** for the female drivers and express them as proportions.
# *   Count the **stop outcomes** for the male drivers and express them as proportions.

# %%
female_and_speeding = fri[fri['violation'] == 'Speeding']


# %%
female_and_speeding


# %%
male_and_speeding = fri[fri['violation'] == 'Speeding']


# %%
male_and_speeding


# %%
fri['stop_outcome'].value_counts() / 86198 


# %%
mri['stop_outcome'].value_counts() / 182538

# %% [markdown]
# ## Calculating the search rate
# %% [markdown]
# During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the **search rate**.
# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Check the data type of ``search_conducted`` to confirm that it's a ``Boolean Series``.
# *   Calculate the search rate by counting the ``Series`` values and expressing them as proportions.
# *   Calculate the search rate by taking the mean of the ``Series``. (It should match the proportion of ``True`` values calculated above.)

# %%
ri["search_conducted"].dtypes


# %%
ri['search_conducted'].value_counts()


# %%
sri = ri['search_conducted'].mean()

# %% [markdown]
# ***
# %% [markdown]
# ## Comparing search rates by gender
# %% [markdown]
# You'll compare the rates at which **female** and **male** drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about **3.8%**.
# 
# First, you'll filter the ``DataFrame`` by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a ``.groupby()``.
# %% [markdown]
# **INSTRUCTIONS 1/3**
# 
# *   Filter the ``DataFrame`` to only include **female** drivers, and then calculate the search rate by taking the mean of ``search_conducted``.

# %%
fri['search_conducted'].value_counts() / 131138

# %% [markdown]
# **INSTRUCTIONS 2/3**
# 
# *   Filter the ``DataFrame`` to only include **male** drivers, and then repeat the search rate calculation.

# %%
mri['search_conducted'].value_counts() / 349446

# %% [markdown]
# **INSTRUCTIONS 3/3**
# 
# *   Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)

# %%
ri.groupby('driver_gender')['search_conducted'].value_counts() / 480584 * 100

# %% [markdown]
# ***
# %% [markdown]
# ## Adding a second factor to the analysis
# %% [markdown]
# Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.
# 
# For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.
# 
# You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Find out below if that's the case!
# %% [markdown]
# **INSTRUCTIONS 1/2**
# 
# *   Use a ``.groupby()`` to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?

# %%
ri.groupby('driver_gender')['violation'].value_counts()

# %% [markdown]
# **INSTRUCTIONS 2/2**
# 
# *   Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way.

# %%
ri.groupby('violation')['driver_gender'].value_counts()

# %% [markdown]
# ***
# %% [markdown]
# ## Counting protective frisks
# %% [markdown]
# During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a ``"protective frisk."``
# 
# You'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.
# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Count the ``search_type`` values to see how many times ``"Protective Frisk"`` was the only search type.
# *   Create a new column, frisk, that is ``True`` if ``search_type`` contains the string ``"Protective Frisk"`` and ``False`` otherwise.
# *   Check the data type of frisk to confirm that it's a ``Boolean Series``.
# *   Take the sum of frisk to count the total number of frisks.

# %%
ri['search_type'].value_counts()

# %% [markdown]
# ***

# %%
for i in ri['search_type']:
    if 'Protective Frisk' < str(i):
        ri['frisk'] = True 


# %%
ri['frisk']

# %% [markdown]
# ## Comparing frisk rates by gender
# %% [markdown]
# You'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?
# 
# Before doing any calculations, it's important to filter the ``DataFrame`` to only include the relevant subset of data, namely stops in which a search was conducted.
# %% [markdown]
# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, searched, that only contains rows in which ``search_conducted`` is ``True``.
# *   Take the mean of the frisk column to find out what percentage of searches included a frisk.
# *   Calculate the frisk rate for each gender using a ``.groupby()``.

# %%
ri[ri["search_conducted"] == True]


# %%
ri['frisk'].mean()


# %%
ri.groupby('frisk')['driver_gender'].value_counts()


# %%



