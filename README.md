# Statistical-Modelling-using-Python
Python for Data Science (Studi Independen Kampus Merdeka Batch 3 by Hacktiv8) | Period : 18 Aug - 31 Dec 2022 | Self-Paced Learning, Live Session, &amp; Project 

## Assignment 1: Analisis Data Kriminalitas 2008-2016 di London
Dataset: [London Crime Data, 2008-2016](https://www.kaggle.com/datasets/jboysen/london-crime)
Crime in major metropolitan areas, such as London, occurs in distinct patterns from Jan 2008-Dec 2016. This data covers the number of criminal reports by month, LSOA borough, and major/minor category.
Q: Bagaimana Kriminalitas di London selama 2008-2016?
A:
- Jumlah kriminalitas tertinggi terlihat pada tahun 2012 dan 2016, sedangkan terendah terlihat pada tahun 2014
- Jumlah kategori kriminalitas yang paling banyak adalah value=1, dari tahun 2008 sampai 2016. Namun pada 2008-2009 dan 2012-2014 terdapat penurunan jumlah kriminalitas per kategori
- Kategori kriminalitas tertinggi ditunjukkan oleh kategori theft dan handling
- Berdasarkan visualisasi histogram, jumlah ketegori kriminalitas di London 2008-2016 menunjukkan heavy-tailed distribution dengan positif skewness 
- Tidak terdapat tren yang signifikan pada jumlah kriminalitas di London pada tahun 2012. Selain itu, jumlah kriminalitas yang paling jarang ditemukan pada bulan februari dan september serta yang tertinggi pada bulan Maret
- Jumlah kriminalitas berdasarkan tahun memiliki persentase yang similar dengan persentase kriminalitas terendah terjadi pada 2010
- Sektor yang paling banyak terjadi kriminalitas adalah sektor city of westminster, dilanjut city of london dan kensington and chelsea

## Assignment 2: Analisis Penjualan Properti di NYC
Dataset: [NYC Property Sales](https://www.kaggle.com/datasets/new-york-city/nyc-property-sales)
A year's worth of properties sold on the NYC real estate market. This dataset contains the location, address, type, sale price, and sale date of building units sold.
Q: Bagaimana Penjualan Properti di NYC
A:
- Rata-rata total unit, residensial unit, dan komersial unit yang terjual di pasar properti kota New York secara berturut-turut 2,25, 2,02, dan 0,19 selama periode 12 bulan terakhir sejak data di-publish
- Harga Jual properti memiliki range harga sebesar 2210000000 dengan minimum harga jual 0. Penjualan ini sebenarnya adalah transfer akta antar pihak: misalnya, orang tua mentransfer kepemilikan rumah mereka kepada seorang anak setelah pindah untuk pensiun.
- Nilai harga jual memiliki variance sebesar 107756447924221.27 dan standar deviasi sebesar 10380580.32. Nilai ini mendekati mean = 1147900, sehingga menunjukkan persebaran data harga jual properti yang kecil
- Berdasarkan harga jual properti dan total unit yang terjual, didapatkan nilai korelasi 0.1. Korelasi positif namun lemah, sehingga terdapat hubungan antara kedua variabel tersebut walaupun lemah
- Terlihat bahwa data harga jual properti di NYC berdistribusi normal dengan positively skewness. Sehingga, ekor distribusi berada di sebelah kanan dan menunjukkan sebagian besar distribusi berada di nilai rendah. Apabila diinterpretasikan, banyaknya properti yang memiliki harga jual di bawah rata-rata menjadi lebih dari 50%.
- Harga jual properti yang representatif dapat diukur dengan nilai median atau kuartil 2. Selain itu, gap harga jual properti mengalami perbedaan yang signifikan antara properti yang memiliki harga jual tinggi dan properti yang memiliki harga jual rendah

## Assignment 3: Prediksi Subscibe oleh Klien Berdasarkan Model Klasifikasi
Dataset: [Bank Marketing Data Set](https://www.kaggle.com/datasets/tunguz/bank-marketing-data-set)
The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.
Q: Apakah klien akan subscribe produk?
A: Penentuan algoritma didasarkan pada tujuan analisis, yaitu untuk melakukan prediksi subscribe produk oleh klien. Dikarenakan, response berupa 'yes' dan 'no' atau subscribe dan tidak subscribe maka saya menggunakan classification algorithm seperti Logistic Regression, Decision Tree, Random Forest, SVM, Naive Bayes, dan KNN classifier algorithm.

## Collaboration Project 1: Services Price Prediction Deployment using Linear Regression
Dataset: [Uber and Lyft Dataset Boston, MA]( https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma )
Objectives:
1. Get a good dataset with clear variables
2. Get complete and easy-to-understand informationTo understand the factors that influence the price of a cab 
3. Get a clear partition of data for modeling
4. Get a good linear regression model
5. To predict services prices based on influencing factors
Conclusions:
1. From 57 existing attributes, 8 of the most influential attributes in services price predictions are taken, including source, destination, cab_type, name, short_summary, distance, surge_multiplier and the response is price variable.
2. The test method uses 3 models, namely linear regression, Ridge Regression, and Lasso Regression with accuracy values of 0.500870 all three and errors that are not much different

## Collaboration Project 2: Rain Next-Day Prediction Deployment using Logistic Regression & SVM
Dataset: Kaggle : [Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package/)
Objectives:
1. Get a good dataset with clear variables
2. Get complete and easy-to-understand informationTo understand the dataset
3. Get a clear partition of data for modeling
4. Get a good logistic regression and support vector machine model
5. To predict next-day rain by training classification models on the target variable RainTomorrow
Conclusions:
1. From 23 existing attributes, 8 of the most influential attributes in Rain Next-Day Prediction are taken, including RainTomorrow, Location, Rainfall, WindGustSpeed, RainToday, Season, Average Temp, and Average Humidity.
2. The test method uses 2 models, namely Logistic Regression with accuracy score 84.76%, MAE 15.23%, MSE 15.23%. The second method is SVM (Support Vector Machine) with accuracy score 83.12%, MAE 16.88%, and MSE 16.88%.
3. From the dataset used, it can be seen that the occurrence of no rain on RainTomorrow is more than the occurrence of rain. Where the percentage of no rain tomorrow if it rains today is 64.89% and if it does not rain today is 84.87%.

## Collaboration Project 3: Survival of Patients Prediction with Heart Failure using Ensemble Method
Dataset: [Heart Failure Prediction]( https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)
Obectives:
1. Get a good dataset with clear variables
2. Get complete and easy-to-understand informationTo understand the dataset
3. Get a clear partition of data for modeling
4. Get a good Decision Tree, Random Forest, XG Boost, and Naive Bayes model
5. To predict survival of patients with heart failure by training classification models
Conclusions:
1. At the age of 60 years the frequency of death from heart failure has the highest frequency.
2. over 60 years old for diabetics, anemia, and smokers has a higher chances of getting a heart failure.
3. In this dataset, model evaluation was carried out with 4 comparison models, including: Decision Tree, Random Forest, XGBoost, and Naive Bayes method.
4. The Random Forest model gets the highest accuracy for this dataset, at 93% so it is most appropriate for predicting patient safety from heart disease.

## Collaboration Project 4: Credit Card Clustering using Scikit-Learn
Dataset: [Credit Card Dataset for Clustering]( https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)
Objectives:
1. Get a good dataset with clear variables
2. Get complete and easy-to-understand informationTo understand the dataset
3. Get a clear partition of data for modeling
4. Get a good K-Means and PCA Scikit-Learn model
5. To cluster credit card customer using Scikit-Learn
Conclusion: Based on the clustering that we have done on credit card user data, 3 groups of credit card users are divided based on their usage behavior, namely the Most Users, Quite a Lot of Users, and the Fewest Users. To position our business as an affordable option for local consumers, we plan to focus on middle-class consumers (Most Users and Quite a Lot of Users).






