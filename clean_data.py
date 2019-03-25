from pandas import DataFrame, read_csv
from matplotlib.pyplot import rcParams, title, xlabel, show
from tqdm import tqdm

def derive_nth_day_feature(df, feature, N):  
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = f'{feature}_{N}'
    df[col_name] = nth_prior_measurements

df = read_csv('data/training_data.csv', sep=',', header=0, index_col='date')
feats = list(df.columns)
df = df.sort_index(ascending=True)

days = [1, 2, 3, 4, 5, 6, 7, 365, 366, 367, 368, 369, 370, 380]

for feat in tqdm(feats):
    for N in days:
        derive_nth_day_feature(df, feat, N)

# to_remove = [feat
#             for feat in feats
#             if feat not in ['mean_temp', 'min_temp', 'max_temp', 'precip_probability']]
# to_keep = [c for c in df.columns if c not in to_remove]
# df = df[to_keep]

# Transpose because lots of columns
# distibution = df.describe().T
# IQR = distibution['75%'] - distibution['25%']
# distibution['outliers'] = (distibution['min']<(distibution['25%']-(3*IQR)))|(distibution['max']>(distibution['75%']+3*IQR))
# print(distibution.ix[distibution.outliers,])

# Below is to define a positive skew on the precip intensity
# rcParams['figure.figsize'] = [14, 8]  
# df.precip_intensity_1.hist()  
# title('Distribution of precip_intensity_1')  
# xlabel('precip_intensity_1')
# show()

df.dropna()
print(df)
df.to_csv('data/clean_training_data_year.csv', sep=',')