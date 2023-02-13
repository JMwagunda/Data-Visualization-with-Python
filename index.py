import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("my_data.csv")
data_2007 = data[data['year'] ==2007]

df = pd.Dataframe(data)

#Function to plot the violin plots
def violinplots(df):
    sns.set_style('White grid')
    plt.figure(figsize=(10, 5))
    
    plt.subplot(131)
    sns.violinplot(x='lifeExp', data=df)
    plt.title('LIFE EXPECTANCY')
    
    plt.subplot(132)
    sns.violinplot(x='pop', data=df)
    plt.title('POPULATION')
    
    plt.subplot(133)
    sns.violinplot(x='gdpPercap', data=df)
    plt.title('GDP per Capita')
    
    plt.tight_layout()
    plt.show()
    
    #Streamlit Representation
    st.title("JUDD MARC ODOYO\nSCT211-0744/2021\nData Visualization with Violin Plots")
    violinplots(df)