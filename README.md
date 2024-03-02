# Time-Series-classifier
A messy attempted time series classifier written in Python. The main steps of this project include:

-1: Scrape financial stock data off of morningstar's Spanish website. This was limited to 60 test stocks.
-2: Extract time series features from the 60 test stocks using tsfresh.
-3: Clean the extracted features data.
-4: Cluster the features with KMeans from SKlearn and principal component analysis. 
