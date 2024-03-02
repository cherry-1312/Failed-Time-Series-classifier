import pandas as pd

#The code below removes NaN values and any values that may be too 
#large so the features aren't skewed. For future reference, normalise dataset.

df_features = pd.read_csv('extracted_features.csv')

columns_with_nan = df_features.columns[df_features.isna().any()].tolist()
print(f"Columns with NaN: {columns_with_nan}")

nan_counts = df_features[columns_with_nan].isna().sum()
print("NaN counts per column:")
print(nan_counts)

df_features[columns_with_nan] = df_features[columns_with_nan].fillna(0)

print(f"Number of samples before replacing NaN: {len(df_features)}")

df_features.to_csv('extracted_features_no_nan.csv', index=False)

print(f"Number of samples after replacing NaN: {len(df_features)}")

df_features = pd.read_csv('extracted_features_no_nan.csv')

stock_ids = df_features['index']

df_features = df_features.drop(columns=['index'])
df_features = df_features.apply(pd.to_numeric, errors='coerce')

max_values = df_features.max(numeric_only=True)

threshold = 100

columns_above_threshold = max_values[max_values > threshold].index

df_features_filtered = df_features.drop(columns=columns_above_threshold)

df_features_filtered = pd.concat([stock_ids, df_features_filtered], axis=1)

df_features_filtered.to_csv('extracted_features_filtered.csv', index=False)
