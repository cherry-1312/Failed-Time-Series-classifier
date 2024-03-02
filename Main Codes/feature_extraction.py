import json
import pandas as pd
import matplotlib.pyplot as plt
from tsfresh import extract_features, select_features
from tsfresh.utilities.dataframe_functions import impute
import multiprocessing


def process_data():
    with open('stock_prices_test.json', 'r') as json_file:
        data = json.load(json_file)

    #here we turn the code from a json file into a nice dataframe

    timestamps = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []
    stock_ids = []

    for stock_id, stock_data in data.items():
        for data_point in stock_data:
            timestamps.append(data_point[0])
            opens.append(data_point[1])
            highs.append(data_point[2])
            lows.append(data_point[3])
            closes.append(data_point[4])
            volumes.append(data_point[5])
            stock_ids.append(stock_id)

    df = pd.DataFrame({
        'StockID': stock_ids,
        'Timestamp': timestamps,
        'Open': opens,
        'High': highs,
        'Low': lows,
        'Close': closes,
        'Volume': volumes
    })

    df['id'] = df['StockID']  
    df['time'] = df['Timestamp']  

    df = df.drop(columns=['StockID', 'Timestamp']) 

    return df

if __name__ == '__main__':
   
    multiprocessing.freeze_support()

    data_frame = process_data()

    extracted_features = extract_features(data_frame, column_id='id', column_sort='time')

    extracted_features = extracted_features.reset_index()

    extracted_features.to_csv('extracted_features.csv', index=False)


#This snippet loops through the id's and graphs them

 grouped_data = df.groupby('StockID')

 for stock_id, stock_data in grouped_data:
     plt.figure(figsize=(10, 4))  # Set the figure size
     plt.plot(stock_data['Timestamp'], stock_data['Close'], label=stock_id)
     plt.title(f"Stock ID: {stock_id}")
     plt.xlabel("Timestamp")
     plt.ylabel("Closing Price")
     plt.legend()
     plt.grid()
     plt.show()

#below is a section of code used to check if there are duplicate
#id's in the json file


 seen_data = {}


duplicates = []

for key, value in data_dict.items():

   data_str = json.dumps(value)

   if data_str not in seen_data:
      seen_data[data_str] = key
   else:
      duplicates.append((key, seen_data[data_str]))


if duplicates:
   print("Duplicate data found. Here are the duplicate entries:")
   for duplicate_key, original_key in duplicates:
       print(f"Key: {duplicate_key}, Duplicate of: {original_key}")
else:
  print("No duplicate data found.")

print(f"Total duplicate entries: {len(duplicates)}")
