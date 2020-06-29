import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from datetime import datetime as dt
import numpy as np

data = "DSNY_Monthly_Tonnage_Data.csv"
DF = pd.read_csv(data)


def date_convert(string):

    return dt.strptime(string,"%Y / %m")

DF['MONTH'] = DF['MONTH'].apply(date_convert)
DF.sort_values(by="MONTH",inplace=True)


class Borough:

    def __init__(self,id):
        self.id = id
        self.data = DF[DF.BOROUGH_ID == id]
        self.boro_name = self.data['BOROUGH'].to_list()[0]

    def year_result(self,year,data,data_col):
        #
        # This function returns the amount of collection by year for the specificed column.
        # args:
        #    -> year is an integer
        #    -> data is a specific df
        #    -> data_col is the string name of the column

        new = data[(data['MONTH'] >= '{}-01-01'.format(year)) & (data['MONTH'] < '{}-01-01'.format(year+1))]
        d = new[data_col].to_list()
        return sum(d)

    def ratio(self,year,data):
        #
        # This function returns the total amount collected from the major categories.
        # Major categoris are Trash, Paper, and MGP (Metal Glass Paper).
        # args:
        #    -> year is an integer
        #    -> data is a specific df
        #

        all = ['REFUSETONSCOLLECTED','PAPERTONSCOLLECTED','MGPTONSCOLLECTED']
        waste = self.year_result(year,data,all[0])
        paper = self.year_result(year,data,all[1])
        plastic = self.year_result(year,data,all[2])
        total = waste+paper+plastic
        return {'total':total,'waste':waste,'paper':paper,'MGP':plastic}


    def list_dist(self):
        # Returns a list of the districts in the borough
        dist = self.data['COMMUNITYDISTRICT'].to_list()
        uni = set(dist)
        return list(uni)

    def list_compost(self,year):
        #
        # This function returns a list of the districts in a boro that are
        # composting
        end_year = self.data[self.data.MONTH == '{}-12-01'.format(year)]
        comp = end_year[end_year.RESORGANICSTONS > 0]
        dist_list = comp['COMMUNITYDISTRICT'].tolist()
        return dist_list

    def list_nocompost(self,year):
        #
        # Function returns the list of districts that are not composting
        all = self.list_dist()
        compost = self.list_compost(year)
        none = np.setdiff1d(all,comp)
        return none

    def no_compost(self,year):
        #
        # Functions returns the number of districts not composting
        return len(self.list_dist()) - len(self.list_compost(year))

    def num_compost(self,year):
        #
        # Returns the number of districts that are composting
        return len(self.list_compost(year))

    def pie_chart(self,year,data):
        #
        # This function creates a pie graph for the waste distrubution of the boro
        # given the year
        obj = self.ratio(year,data)
        labels = 'Trash', 'Paper', 'MGP'
        sizes = [obj['waste']/obj['total'],obj['paper']/obj['total'],obj['plastic']/obj['total']]
        explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title('{} breakdown in {}'.format(self.boro_name,year), fontweight='bold')
        #fig1.suptitle('{} breakdown in {}'.format(self.boro_name,year), fontweight='bold', y=.85)
        #plt.savefig('visuals/{}/{}_ratio.png'.format(self.boro_name.replace(" ",""),self.boro_name.replace(" ","")))
        plt.show()
        return None
    def draw_graph(self,start,end,data,data_col):
        #
        # This function graphs the amount collected from the year start to end
        years = []
        coll = []
        year = start
        while year < end+1:
            years.append(year)
            sum = self.year_result(year,data,data_col)
            coll.append(sum)
            year += 1
        scaled = [y *.001 for y in coll]
        plt.plot(years,scaled)
        plt.ylabel('Tons in thousands')
        plt.xlabel('Year')
        plt.xticks(years,rotation=45)
        plt.xlim(start,end)
        plt.legend()
        plt.subplots_adjust(left=0.12, bottom=0.17, right=0.90, top=0.88, wspace=0.20, hspace=0.20)
        boro = data['BOROUGH'].to_list()[0]
        if data_col == "REFUSETONSCOLLECTED":
            name = "Trash"
        if data_col == "PAPERTONSCOLLECTED":
            name = "Paper"
        if data_col == "MGPTONSCOLLECTED":
            name = "MGP"

        place = self.boro_name
        try:
            dist = self.dist_id
            plt.title("{} D{} {} collection by tons from {} to {}".format(place,dist,name,start,end))
        except:
            dist = ""
            plt.title("{} {} collection by tons from {} to {}".format(place,name,start,end))
        #plt.savefig('visuals/{}/{}_{}.png'.format(place.replace(' ',''),name.replace(" ",""),place))
        plt.show()

class District(Borough):

    def __init__(self,id,dist_id):
        self.dist_id = dist_id
        super().__init__(id)
        self.df = self.data[self.data.COMMUNITYDISTRICT == self.dist_id]
    def do_compost(self,year):
        #
        # Boolean function whether or not the district composts

        end_year = self.df[self.df.MONTH == '{}-12-01'.format(year)]
        comp = end_year['RESORGANICSTONS'].tolist()
        return sum(i>0 for i in comp) > 0


class NYC:

    def __init__(self):
        self.mh = Borough(1)
        self.bx = Borough(2)
        self.bk = Borough(3)
        self.qu = Borough(4)
        self.si = Borough(5)
        self.boros = [self.mh,self.bx,self.bk,self.qu,self.si]

    def city_totals(self,year):
        #
        # Takes the ratio function from Borough class and gets the results for
        # the whole city.
        total = 0
        waste = 0
        paper = 0
        plastic = 0

        for boro in self.boros:
            obj = boro.ratio(year,boro.data)
            waste += obj['waste']
            paper += obj['paper']
            plastic += obj['MGP']
            total += obj['total']
        return {'total':total,'waste':waste,'paper':paper,'plastic':plastic}
    def city_pie(self,start,end):
        #
        # Makes a pie chart comparing breakdown from start year to end year
        obj = self.city_totals(start)
        obj2 = self.city_totals(end)
        labels = 'Trash', 'Paper', 'MGP'
        sizes1 = [obj['waste']/obj['total'],obj['paper']/obj['total'],obj['plastic']/obj['total']]
        sizes2 = [obj2['waste']/obj2['total'],obj2['paper']/obj2['total'],obj2['plastic']/obj2['total']]
        explode = (0, .1, .1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, axarr = plt.subplots(1,2)
        ax1 = axarr[0]
        ax1.pie(sizes1, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        ax2 = axarr[1]
        ax2.pie(sizes2, shadow=True, startangle=90, autopct='%1.1f%%')
        ax2.axis('equal')

        lgd1 = ax1.legend(labels, loc='lower center')
        lgd2 = ax2.legend(labels, loc='lower center')

        ax1.set_title('{}'.format(start), y=0.8)
        ax2.set_title('{}'.format(end), y=0.8)
        fig1.suptitle('NYC waste management breakdown by year', fontweight='bold', y=0.85)
        plt.savefig('visuals/nyc_breakdown.png')
        plt.show()

    def boro_plots(self,year):
        #
        # Plot each boro
        data_col = ['paper' ,'waste', 'MGP']
        for boro in self.boros:
            for col in data_col:
                self.plot_div(2019,boro,col)
        return None
    def boro_ratio(self,year):
        #
        # Make the piechart for each boro
        for boro in self.boros:
            boro.pie_chart(year,boro.data)

    def div_dist(self,year,boro,data):
        #
        #This function returns a df of the rates per district
        obj = boro.ratio(year,boro.data)
        paper_stat = obj[data]/obj['total']

        all_dist = boro.list_dist()

        name = []
        amount = []
        for dist in all_dist:
            dist_obj = District(boro.id,dist)
            dist_data = dist_obj.ratio(year,dist_obj.df)
            name.append("District {}".format(dist_obj.dist_id))
            amount.append(dist_data[data]/dist_data['total'])

        df = pd.DataFrame({'name':name,'value':amount})
        return df

    def plot_div(self,year,boro,data):
        #
        # This function plots the divergence per district
        # Args:
        #   -> data is either 'paper' 'MGP' or 'waste'
        boro_obj= boro.ratio(2019,boro.data)
        boro_value = boro_obj[data]/boro_obj['total']
        df = self.div_dist(year,boro,data)
        x = df.loc[:, ['value']]

        df['values_z'] = df.value - boro_value
        df['colors'] = ['red' if x < 0 else 'green' for x in df['values_z']]

        df.sort_values('values_z', inplace=True)
        df.reset_index(inplace=True)

        plt.figure(figsize=(10,6), dpi= 80)
        plt.hlines(y=df.index, xmin=0, xmax=df.values_z, color=df.colors, alpha=0.4, linewidth=5)

        plt.gca().set(ylabel='District', xlabel='Divergence from a {} rate'.format(round(boro_value,4)))
        plt.yticks(df.index, df.name, fontsize=12)
        plt.title('{} {} collection divergence by district'.format(boro.boro_name,data), fontdict={'size':20})
        plt.grid(linestyle='--', alpha=0.5)
        plt.savefig('visuals/{}/districts/{}_{}_divergance.png'.format(boro.boro_name.replace(" ",""),boro.boro_name.replace(" ",""),data))
        plt.show()
nyc = NYC()
plots = nyc.boro_plots(2019)
