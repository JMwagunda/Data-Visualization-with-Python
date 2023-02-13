import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("VIOLIN PLOT FOR LIFE EXPECTANCY,POPULATION AND GDPPERCAP WITH STREAMLIT")
st.subheader('JUDD MARC WAGUNDA')
st.subheader('SCT211-0744/2021')
st.subheader('ICS 2207 ASSIGNMENT II')

#Read data from my_data csv file
data = pd.read_csv("my_data.csv")

#Retrieve GDPPERCAP data for the year column of 2007 
data_2007 = data[data['year']==2007]

# Violin plot of the retrieved data
fig, ax = plt.subplots()
sns.violinplot(data=data_2007,x='gdpPercap',ax=ax)
plt.title("GDP Data Representation  for 2007\n", fontweight='bold')
ax.set_xlabel("GDP", fontweight='bold')
ax.set_ylabel("Values", fontweight='bold')

# Render the matplotlib fig in the Streamlit app
st.pyplot(fig)

#Retrieve POPULATION data for the year column of 2007 
data_pop = data[data['year'] == 2007][['pop']]

# Violin plot of the POPULATION data
fig2 , ax2 = plt.subplots()
sns.violinplot(data=data_pop,x= 'pop', ax=ax2)
ax2.set_xlabel("POPULATION", fontweight='bold')
ax2.set_ylabel("Values", fontweight='bold')

# Render the matplotlib fig in the Streamlit app
st.pyplot(fig2)

#Retrieve LIFE EXPECTANCY data for the year column of 2007 
data_exp = data[data['year'] == 2007][['lifeExp']]

# Violin plot of the LIFE EXPECTANCY data
fig3 , ax3 = plt.subplots()
sns.violinplot(data=data_exp,x='lifeExp', ax=ax3)
ax3.set_xlabel("LIFE EXPECTANCY", fontweight='bold')
ax3.set_ylabel("Values", fontweight='bold')

# Render the matplotlib fig in the Streamlit app
st.pyplot(fig3)