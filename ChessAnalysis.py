#!/usr/bin/env python
# coding: utf-8

# ### Description of columns
# - id: The internal Lichess game id
# - rated: If the game was played with rating points on the line
# - created_at and last_move_at: The start and end times, respectively, of the game
# - turns: The number of turns before the game ended
# - victory_status: How the win was achieved; notable ones for our purposes include "mate" (the loser was placed in checkmate), "resign" (the loser resigned), "outoftime" (the loser ran out of - time to make their moves; often referred to as "flagging") and "draw" (users agreed to a draw).
# - winner: The winner, by color of pieces (or "draw" if the game was drawn)
# - increment code: The amount of time the users played with.It's an amount of time added to the clock after each move is made. In format x + y, x refers to the number of minutes players start with, and y refers to the number of seconds they gain every time they make a move. Common formats include 1 + 0 ("bullet"), 3 + 0 or 5 + 0 ("blitz"), and 10 + something ("rapid")
# - hite/black id: The lichess username of the white/black player
# - white/black rating: The lichess ELO of the white/black player
# - moves: A complete list of moves played in the game, given in algebraic notation) (see here for a more detailed explanation)
# - opening_eco: A standardized short code for openings; see list of ecos
# - opening_name: The common referrent for the opening name; Openings are referred to by both a general opening name and a variation name after (e.g. Italian Game: Schilling-Kostic Gambit means the Schilling-Kostic Gambit variation of the Italian Game.)
# - opening_ply: The number of moves considered to be played in the opening.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('games.csv')
df.head() 


# ### Checking data types

# In[2]:


df.info()


# ### Removing unnecessary columns
# * There are a lot of columns that we are not going to use in any manner and there are some columns that we will add in later sections which will help us in categorizing and visualizing data. So, we can safely drop those unnecessary columns. After dropping those columns, we are left with

# In[7]:


df = df.drop(['id','created_at', 'last_move_at'], axis = 1)
df.info()


# * We convert Object data type to Categorical data type

# In[8]:


df['victory_status'] = df['victory_status'].astype('category')
df['winner'] = df['winner'].astype('category')
df['increment_code'] = df['increment_code'].astype('category')
df['white_id'] = df['white_id'].astype('category')
df['black_id'] = df['black_id'].astype('category')
df['moves'] = df['moves'].astype('category')
df['opening_eco'] = df['opening_eco'].astype('category')
df['opening_name'] = df['opening_name'].astype('category')


df.info()


# #### Data Distribution
# * We should check the statistical summary of each column to gain insight into the distribution of data in each column. Statistical measurements can tell you any mathematical problems you may have, such as overly significant values and large deviations.
# * It returns results for numeric variables only, not for text data. If we want to see them too, we can add the 'include='all' parameter to the method to see all the variables together, or the 'include=['O']' parameter to see only the text variables.

# In[9]:


#df.describe(include='O')
#df.describe(include='all')
df.describe()


# In[10]:


#showing all the unique values in a column.
unique_counts = df.from_records([(col, df[col].nunique()) for col in df.columns],
                                columns = ['Columns_Name','Num_Unique']).sort_values(by=['Num_Unique'])
print(unique_counts)


# - This table highlights a couple of items that will help determine which values should be categorical.

# ### Check the null values¶
# If there are missing values in the Dataset before doing any statistical analysis, we need to handle those missing values.
# - MCAR(Missing completely at random): These values do not depend on any other features.
# - MAR(Missing at random): These values may be dependent on some other features.
# - MNAR(Missing not at random): Missing values depend on the unobserved data.

# In[11]:


# Checking the missing values
df.isnull().sum() 
#df.isnull().sum().sort_values(ascending=False) >> Finding the number of missing data in df and sorting in descending order


# ### Exploratory Analysis & Data Visualization

# ### Q1. How frequently has each victory status?

# In[12]:


# Let's calculate the percentage of each job status category.
df.victory_status.value_counts(normalize=True)

#plot the bar graph of percentage victory_status categories
df.victory_status.value_counts(normalize=True).plot.barh()
plt.show()


# - mate the loser was placed in checkmate
# - resign the loser resigned
# - outoftime the loser ran out of - time to make their moves; often referred to as "flagging"
# - draw users agreed to a draw.

# ### Q2. How frequently has each color won a match?

# In[21]:


white_winner, black_winner, draw_winner = df['winner'].value_counts()


# In[23]:


total_winner = df['winner'].value_counts().sum()
print(total_winner)


# In[25]:


white_win_percent = (white_winner/total_winner)*100
black_win_percent = (black_winner/total_winner)*100
draw_win_percent = (draw_winner/total_winner)*100


# In[27]:



print(f"White has won { round(white_win_percent, 2) } percent of all matches")
print(f"Black has won { round(black_win_percent, 2) } percent of all matches")
print(f"There have been { round(draw_win_percent, 2) } percent draws in all matches")


# In[13]:


#Winner column distribution
df.winner.value_counts(normalize=True)
df.winner.value_counts(normalize=True).plot.barh()
plt.show()


# 
# ### Q3. How many rated games were played?

# In[28]:


print('The number of rated games were {}.'.format(df[df.rated ==True].shape[0]))


# In[29]:


w_rate = df["white_rating"].tolist()
b_rate = df["black_rating"].tolist()
w_rate.extend(b_rate) #Python Concatenating Lists extend()
mean_rating, max_rating, min_rating, std_rating = round(np.mean(w_rate), 2), max(w_rate), min(w_rate), round(np.std(w_rate), 2)

print("Mean Rating :", mean_rating)
print("Max Rating :", max_rating)
print("Min Rating :", min_rating)
print("Std Rating :", std_rating)

plt.hist(w_rate, histtype="bar", rwidth=1, color="black")
plt.title("Distribution of Player Rating")
plt.xlabel("Player ratings")
plt.ylabel("Number of players")
plt.xticks(range(700, 3100, 300))
plt.show()


# ### Q4. What is the most preferred opening name?¶
# 

# In[43]:


df['opening_name'].value_counts()


# In[71]:


most_choice = df['opening_name'].value_counts().head(10)


# In[78]:


#chess opening names are too long so we will shorten them
def shorten_names(opening):
    if ':' in opening:
        opening = opening.split(':')[0]
    while '|' in opening:
        opening = opening.split('|')[0]
    if '#' in opening:
        opening = opening.split('#')[0]
    if 'Accepted' in opening:
        opening = opening.replace('Accepted', '')
    if 'Declined' in opening:
        opening = opening.replace('Declined', '')
    if 'Refused' in opening:
        opening = opening.replace('Refused', '')
    return opening.strip()
df['opening_name_s'] = df.opening_name.apply(shorten_names)


# In[79]:


plt.subplots(figsize=(20,8))
plt.title("Distribution of Openings")
counts1 = df['opening_name_s'].value_counts()
Data1 = df.loc[df['opening_name_s'].isin(counts1.index[counts1>600])]
sns.countplot(Data1.main_openings)
plt.xlabel('Openings Name')
plt.ylabel('Number of Games')


# #### opening_ply: The number of moves considered to be played in the opening

# In[38]:


highest_opening_play = df['opening_ply'].sort_values(ascending=False).max()
print(highest_opening_play)


# In[37]:


highest_opening_count = df[df['opening_ply']==highest_opening_play]['opening_ply'].value_counts().max()
print(highest_opening_count)


# In[35]:


print(f"{highest_opening_play} is maximum number of moves in an opening move. There are {highest_opening_count} opening plays with {highest_opening_play} moves.")


# In[ ]:




