import datetime
import pandas as pd
import numpy as np
from itertools import cycle, islice
import seaborn as sns
import matplotlib.pyplot as plt
import time
import re



from scipy import stats
from collections import Counter
from datetime import datetime

class NetflixTitlesInfo:

    df = pd.read_csv('datasets/20210401_dl_netflix_titles.csv',header=0,engine='python')

    def dataset_basics(self):

        print(type(self.df))
        print(self.df.info())
        print(self.head())
        print(self.shape)
        print(self.describe())


    def movies_tv_shows(self):
        '''Count how many movies and how many TV shows '''

        labels = self.df['type'].unique()
        show_sizes = self.df['type'].value_counts()

        #Plot Basic Pie Chart
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(show_sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


        #Basic Bar Graph
        x = np.arange(len(labels))# the label locations
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots()
        ax.bar(x - width / 1, show_sizes, width, label='Show Types')
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Number of Shows')
        ax.set_title('Types of shows')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        fig.tight_layout()

        #Show Graphs
        plt.show()

    def unique_directors(self):
        '''Show the Most popular Directors'''

        #print(self.df.info())

        rows = self.df['director'].count()
        directors = self.df['director'].unique()
        num_shows_directed = self.df['director'].value_counts()

        #Top 20 Directors on Netflicks And Movies Directed
        top_20_dirs = num_shows_directed.head(20)
        print(top_20_dirs)

        #Number of movies directed by unique directors
        movies_dir = num_shows_directed.value_counts().sort_values(ascending=False)

        print(movies_dir)

    def most_popular_categories(self):
        '''Find the unique categories and popular they are on the Channel'''

        listed_in = self.df['listed_in']

        categories = []
        for element in range(len(listed_in)):
            for item in listed_in[element].split(','):
                categories.append(item.strip())

        #created a new Dataframe
        df_cat = DataFrame(categories,columns=['show types'])
        num_categories = len( df_cat['show types'].unique())
        labels = df_cat['show types'].unique()
        #Create the Pie Chart
        fig1, ax1 = plt.subplots()
        ax1.pie(df_cat['show types'].value_counts(), labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Categories
        categories = df_cat['show types'].unique()


        # Show Graphs
        #plt.show()

        return categories

    def pattern_description_category(self):
        '''Match the categories with Descriptions'''
        # Categories
        categories = self.most_popular_categories()
        descriptions = []
        tv_genre_description = []
        counter = 0

        while counter < len(self.df['listed_in']):
            for genre in categories:

                if re.findall(genre, self.df['listed_in'].loc[counter]):

                    items = [genre + ", " + self.df['description'].loc[counter]]

                    tv_genre_description.append(items)


            counter += 1

        return tv_genre_description

    def frequency_words_description(self):


        #Top 100 words more the 4 letters
        top_100 = Counter(" ".join(self.df['description']).split()).most_common(100)

        frequency = []
        labels = []

        for i in top_100:
            if len(i[0]) > 4:
                labels.append(i[0])
                frequency.append(i[1])

        all_words = Counter(" ".join(self.df['description']).split()).most_common()

        for i in all_words :
            if len(i[0]) > 4:
                labels.append(i[0])
                frequency.append(i[1])

        #Points to graph
        xpoints = np.array(labels)
        ypoints = np.array(frequency)

    def time_to_date_added(self):

        self.df['date_added_format'] = pd.to_datetime(self.df['date_added'])
        self.df['date_released'] = pd.to_datetime(self.df['release_year'].astype(str)).values
        self.df['time_to_netflix'] = self.df['date_added_format'].dt.year - self.df['date_released'].dt.year

        average_time_to_netflix = self.df['time_to_netflix'].mean()
        years_to_launch_on_netflix = self.df['time_to_netflix']
        when_added = self.df['date_added_format'] #datetime
        date_released = self.df['date_released'] #datetime
        unique_years = pd.DatetimeIndex(self.df['date_released']).year

        xpoints = years_to_launch_on_netflix
        ypoints = unique_years

        # plt.scatter(xpoints, ypoints, alpha=0.3)
        # plt.grid()
        # plt.ylabel("Year launched")
        # plt.xlabel("Number of years before added to Netflix from release date")
        # plt.show()



    def seaborn_graph(self):

        self.df['date_added_format'] = pd.to_datetime(self.df['date_added'])
        self.df['date_released'] = pd.to_datetime(self.df['release_year'].astype(str)).values
        self.df['time_to_netflix'] = self.df['date_added_format'].dt.year - self.df['date_released'].dt.year

        #Create a visualization
        ##  1
        #sns.distplot(self.df['date_added_format'], bins=80)

        sns.jointplot(x='date_added_format', y='time_to_netflix', height=7, kind="kde", ratio=5, space=0,  data=self.df)




        plt.show()







        #print(type(self.df['time_df']))










if __name__ =="__main__":
    nf = NetflixTitlesInfo()
    nf.seaborn_graph()





