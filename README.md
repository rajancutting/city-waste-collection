## Overview
The terrorist attacks on 9/11 permanently changed the world. How people travel, how buildings are built, 
and how the intelligence community operates are some of the most visible changes to our society in response 
to the attacks. What most people do not know is that 9/11 also drastically changed recycling in New York City. 
In the middle of 2002, the mayor at the time, Michael Bloomberg, announced that his administration was getting rid of residential 
metal glass and plastic (MGP) collection due to the strain 9/11 had caused to the city budget. It was estimated that the city 
could save $40 million dollars a year by dumping waste into landfills as opposed to recycling them. 

In 2004, the mayor reversed his decision and the city once again moved on track to embrace recycling. He then 
later said that NYC would lead the nation in moving towards sustainable waste management by doubling recycling 
rates by 2017. The current mayor, Bill de Blasio, is even more ambitious and has stated that by 2030 NYC will 
divert 90% of its waste from landfills. The city is nowhere near that goal. 

<p align="center">
  <img src="https://github.com/rajancutting/city-waste-collection/blob/master/visuals/nyc_breakdown.png">
</p>

The recycling efforts in the city have only improved modestly since 2005. The purpose of this project is to take 
a closer look at the city’s recycling program and examine its varying success throughout the city.

## Motivation
One of my first jobs was in my college's recycling center and that experience exposed me to the complexity and importance of waste management. 
There is a clear disconnect between a person throwing something out and understanding where that thing ends up. People do 
not understand the process of recycling or how much trash we create daily. 

In NYC recycling has been treated as an inconvenience instead of an environmental responsibility. NYC prides itself on being a 
progressive leader for the nation on many issues, but particularly for environmentalism and building a sustainable future. 
The recycling data suggests otherwise, though.

I started this project to further my passion for sustainable recycling and to help people understand that NYC has a lot of 
work to do to build a more robust recycling program. 

## Dataset
NYC Open Data is reported by NYC agencies and other partners. The data for this project is monthly tonnage collection by district 
by the sanitation department (DSNY). The data starts from  1991 and is updated each month with the latest monthly data. 
I chose to focus on the data from 2005 through 2019 to focus the scope on the time since former mayor Bloomberg revitalized recycling. 
The data is broken down by the five boroughs and the different districts within the boroughs. Each borough has a different number of districts.
Manhattan has 11; the Bronx has 12; Brooklyn has 18; Queens has 14; and Staten Island has 3.

## Results 
The five boroughs for the most part are all following somewhat identical trends. The trash called in Manhattan in 2019 made up about 
76% of all the collection, which is the lowest rate across the boroughs. The Bronx has the highest rate of trash collection with trash 
making up 83.7% of all the collection. Manhattan has the most successful paper recycling program with paper collections in 2019 making 
up 13.6% of all waste collected. However as shown in the graph below, the paper collection in Manhattan has fallen throughout the years 
and has now plateaued.

<p align="center">
  <img src="https://github.com/rajancutting/city-waste-collection/blob/master/visuals/Manhattan/Paper_Manhattan.png">
</p>

There is clear divergence within the districts of a borough. Different districts are recycling differently and producing more waste than others. 
This is important data because it can help inform more targeted strategies to increase the rates within a borough. The districts that are recycling 
more paper are generally the districts with better MGP collection. This could give insights into solutions and offer an explanation for the current discrepancy.

<p align="center">
  <img src="https://github.com/rajancutting/city-waste-collection/blob/master/visuals/Brooklyn/districts/Brooklyn_paper_divergance.png">
 </p>
<p align="center">
  <img src="https://github.com/rajancutting/city-waste-collection/blob/master/visuals/Brooklyn/districts/Brooklyn_MGP_divergance.png">
</p>

When mayor Bloomberg announced in 2002 that MGP collection was going to be suspended, he kept the paper collection program because it generated revenue for the city. 
However over the years MGP collection has outpaced the paper collection program. The MGP program in Queens accounted for 10.3% of the total collections. 
The growth of Queen’s MGP program is a direct contrast to Manhattan’s stagnating paper program.  

<p align="center">
  <img src="https://github.com/rajancutting/city-waste-collection/blob/master/visuals/Queens/MGP_Queens.png">
</p>

MGP collection has outpaced paper collection since 2005 and it is the main driver of NYC’s moderate recycling improvements. Part of the explanation could be that MGP 
is a broader category so naturally makes up more of household consumption. Nevertheless it is a piece of good news from the city government and offers a path to further 
increase recycling rates. The challenge going forward is to continue that growth and stimulate recycling in the lagging districts. That is the only way the city will reach 
its goal by 2030.

## Next Steps
<h4> Compost Program </h4>Diverting food waste from landfills could be one of the most efficient ways of driving down the NYC trash collection rate. The city has 
started a composting program and that is something to work into the analysis. It wasn’t included in this version because it is not in all districts within the boroughs. 
Furthermore it is not in all of the zip codes within a district, so even though the data is reported on a district level, it does not paint a clear picture. The more 
interesting thing to consider is which districts are receiving prioritization and how the correlation between the existence of a composting program and recycling rates.
<h4> District Demographics </h4>It is important to understand who lives in the different districts and how that changes recycling rates. One of the challenges to the 
city’s efforts is that there is not adequate recycling in the public housing system. So if a district has more public housing, it might be reasonable to expect it to have 
lower rates. Another thing to consider is how often collection is made in the different districts.
<h4> Funding Issues </h4>The data shows clear trends for recycling surges and declines. Budget reports can provide context to these trends.
<h4> Capture vs. Diversion </h4>The data reported is only the collection data and says nothing of how much of the recycling actually was recycled and how much was sent to 
landfills. This is important because it is a clear function of public awareness and education. How much of the collection actually gets recycled depends on how much New Yorkers 
understand about recycling, and how good they are at it.
