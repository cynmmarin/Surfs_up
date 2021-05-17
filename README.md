# **Surfs Up Analysis**

## Overview of Project 
We will be performing a weather analysis to determine precipitation patterns in Oahu, an island in Hawaii. We will be using the data gathered by W. Avy, to help us determine if investing in a Surf Shop in a lucrative investment. The lack of understanding of temperature trends caused W. Avy to close his shop when he first opened it. In order to avoid those same mistakes and will be using his SQLite database, where he has stored the weather data. 


## Results
For the purpose of this analysis, we will focus on the trends from the month of June and December from 2010 to 2017. Picking months that are so apart from each other can give us an idea of the extreme weather that occurs at two points in the year. However, focusing all our resources to only two months can give us contradicting information and not be enough to make a vast assessment of the situation. Here are the results we obtained from each month. 

### Statistics for June
In the month of June, we find that Oahu’s has an average weather of 74.94, low 64 and high 85 degrees. The following conclusions can be made:
- The average temperature of ~75 degrees, is warm and it may be conducive to have a steady consumer base. 
- The low of 64 degrees can be a bit worry some. It seems this is not true beach weather, and the low can scare a few surfers away. 
- The high of 85 can be good for business. But with the low being 64 and our lack of understanding of wind factors. June is not giving us significant trust that this is a good venture.

![summary_statistic_june]( https://github.com/cynmmarin/Surfs_up/blob/9393528188ca034af1fb90884e1898ddf0369b95/Resources/summary_statistics_june.png)

### Statistics for December
In the month of December, we find that Oahu’s has an average weather of 71.04, low 56 and high 83 degrees. The following conclusions can be made:
- The average temperature of ~71 degrees, is slightly below that of June. This may indicate that this island may have a steady weather throughout the year. However, we would need to analyze more months to know if this assumption is true.
- The low of 56, is troubling given that it’s over 10 degrees colder than in June and are not conducive temperatures for surfing.
- The high of 83, is just slightly lower than that of June. However, a temperature of 83 is not enough to have a surf shop succeed if we are unaware of the impact of wind trends.

![summary_statistic_december](https://github.com/cynmmarin/Surfs_up/blob/9393528188ca034af1fb90884e1898ddf0369b95/Resources/summary_statistic_december.png)

### Summary
The analysis as it stands does not contain enough data to properly determine if a Surf Shop would thrive. Limiting the evaluation to only the month of June and December leaves a lot of unknowns. Such as, are these the warmest months of the year? Are they the coldest? What happens between those months? If we are hoping to open a Surf Shop, temperature in not the only factor to keep in mind, we want to examine the data for wind factors too. This also depends on if we want the shop to be open year-round or only a few months out of the year.

An option to help us determine if this is a worthwhile investment, is to do additional queries. One option is to analyze the wind patterns in Oahu for the month of June and December. A second option is seeing if the data available to us has information of ocean currents. If the data to complete these two queries are not available to us, and we want to continue working with our initial database. Then, it would be recommended we analyze the months of May, July, November and January to give us a broader picture of the weather patterns. As the analysis stands, it would be highly recommended the Surf Shop does not open until these queries have been run.
