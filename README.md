# Statistical-Modelling-using-Python
Python for Data Science (Studi Independen Kampus Merdeka Batch 3 by Hacktiv8) | Period: 18 Aug - 31 Dec 2022 | Self-Paced Learning, Live Session, &amp; Project 

## Assignment 1: Analysis of Crime Data 2008-2016 in London
Dataset: [London Crime Data, 2008-2016](https://www.kaggle.com/datasets/jboysen/london-crime)
Crime in major metropolitan areas, such as London, occurs in distinct patterns from Jan 2008 - Dec 2016. This data covers the number of criminal reports by month, LSOA borough, and major/minor category.

Q: What was the crime rate like in London from 2008 to 2016?

A:
- The highest amount of criminal activity was observed in the years 2012 and 2016, while the lowest was seen in 2014.
- The category with the highest number of crimes is 'value=1' from 2008 to 2016. However, there is a decrease in the number of crimes per category in 2008-2009 and 2012-2014.
- The highest category of crime is indicated by the 'theft' and 'handling' categories.
- Based on the histogram visualization, the number of crime categories in London from 2008 to 2016 exhibits a heavy-tailed distribution with positive skewness.
- There is no significant trend in the amount of crime in London in 2012. Additionally, the lowest occurrences of crime were found in February and September, while the highest occurred in March.
- The distribution of crime counts by year shows a similar percentage to the lowest percentage of crimes occurring in 2010.
- The sector with the highest occurrence of crimes is the City of Westminster, followed by the City of London and Kensington and Chelsea.

## Assignment 2: Analysis of Property Sales in NYC
Dataset: [NYC Property Sales](https://www.kaggle.com/datasets/new-york-city/nyc-property-sales)
A year's worth of properties sold on the NYC real estate market. This dataset contains the location, address, type, sale price, and sale date of building units sold.

Q: How are the Property Sales in NYC?

A:
- The average total units, residential units, and commercial units sold in the New York City property market were 2.25, 2.02, and 0.19 respectively over the past 12 months since the data was published.
- The selling price of properties has a price range of 2,210,000,000 with a minimum selling price of 0. These sales are essentially inter-party deed transfers; for example, parents transfer ownership of their home to a child after relocating for retirement.
- The selling price values have a variance of 107,756,447,924,221.27 and a standard deviation of 10,380,580.32. This value is close to the mean of 1,147,900, indicating a small spread in property selling prices.
- Based on property selling prices and the total units sold, a correlation value of 0.1 is obtained. The correlation is positive but weak, indicating a relationship between the two variables, albeit a weak one.
- It can be observed that property selling price data in NYC follows a normally distributed curve with positive skewness. This means that the tail of the distribution is on the right side, indicating that most of the distribution is at lower values. In interpretation, a significant portion of the properties have selling prices below the average.
- The representative selling price of properties can be measured using the median value or the second quartile. Additionally, there is a significant difference in selling prices between properties with high and low values.

## Assignment 3: Prediction of Subscriptions by Clients Based on Classification Model
Dataset: [Bank Marketing Data Set](https://www.kaggle.com/datasets/tunguz/bank-marketing-data-set)
The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

Q: Do clients subscribe to the product?

A: The choice of algorithm is based on the objective of the analysis, which is to predict product subscriptions by clients. Because the response is either 'yes' or 'no,' or subscribe and do not subscribe, I used classification algorithms such as Logistic Regression, Decision Tree, Random Forest, SVM, Naive Bayes, and KNN. The Random Forest Algorithm was found to be the best algorithm for solving the problem in this dataset.

## Collaboration Project 1: Services Price Prediction Deployment using Linear Regression
Dataset: [Uber and Lyft Dataset Boston, MA]( https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma )

Conclusions:
1. From 57 existing attributes, 8 of the most influential attributes in services price predictions are taken, including source, destination, cab_type, name, short_summary, distance, surge_multiplier and the response is price variable.
2. The test method uses 3 models, namely linear regression, Ridge Regression, and Lasso Regression with accuracy values of 0.500870 all three and errors that are not much different

## Collaboration Project 2: Rain Next-Day Prediction Deployment using Logistic Regression & SVM
Dataset: Kaggle : [Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package/)

Conclusions:
1. From 23 existing attributes, 8 of the most influential attributes in Rain Next-Day Prediction are taken, including RainTomorrow, Location, Rainfall, WindGustSpeed, RainToday, Season, Average Temp, and Average Humidity.
2. The test method uses 2 models, namely Logistic Regression with an accuracy score 84.76%, MAE 15.23%, and MSE 15.23%. The second method is SVM (Support Vector Machine) with an accuracy score 83.12%, MAE 16.88%, and MSE 16.88%.
3. From the dataset used, it can be seen that the occurrence of no rain on RainTomorrow is more than the occurrence of rain. The percentage of no rain tomorrow if it rains today is 64.89% and if it does not rain today is 84.87%.

## Collaboration Project 3: Survival of Patients Prediction with Heart Failure using Ensemble Method
Dataset: [Heart Failure Prediction]( https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)

Conclusions:
1. At the age of 60 years the frequency of death from heart failure has the highest frequency.
2. over 60 years old for diabetics, anemia, and smokers have higher chances of getting heart failure.
3. In this dataset, model evaluation was carried out with 4 comparison models: Decision Tree, Random Forest, XGBoost, and Naive Bayes method.
4. The Random Forest model gets the highest accuracy for this dataset, at 93% so it is most appropriate for predicting patient safety from heart disease.

## Collaboration Project 4: Credit Card Clustering using Scikit-Learn
Dataset: [Credit Card Dataset for Clustering]( https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)

Conclusion: Based on the clustering that we have done on credit card user data, 3 groups of credit card users are divided based on their usage behavior, namely the Most Users, Quite a Lot of Users, and the Fewest Users. To position our business as an affordable option for local consumers, we plan to focus on middle-class consumers (Most Users and Quite a Lot of Users).






