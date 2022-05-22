'''
str, list, dict, array, series
axis=0 or index -> apply to each column
axis=1 or column -> apply to each row
''' 
# Import & Export 
    other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
    df = pd.read_csv(other_path, header=None)
    headers = ['','','']
    df.columns = headers
    path = "/content/drive/MyDrive/Python101/IBM_DataAnalystCourse/automobile.csv"
    df.to_csv(path)
# Browse the dataset
    df.head(): including column header and the cotent of each row
    df.info()
    print(df.columns)
    df.shape: size of the dadtaframe
    df.describe(include='all')
    df['col'].unique()
    df_counts = df['col'].value_counts().to_frame()
    df.count(axis = 0)
# Descriptive Statistics
    df.describe() / df[''].describe()
    df.value_counts(): frequencies of unique rows
    df.mean() / df[''].mean() / df.mean(axis=1) / df.apply(np.mean)
    df.sum(0, skipna=False): exclude missing data
    df.cumsum(axis=0), df.cumsum(axis=1) / df.apply(np.cumsum)
    z_score: (df - df.mean()) / df.std()
    z_score.std()
# Indexing/Slicing
    - index a column: df['a']
    - select rows by index: df[0:3] ## 0,1,2 = 3 columns in total
    - loc (inclusive): use labels
        - select row by label: df.loc['a'] # by index
        - list of labels: df.loc[['a','c']] # a, b, c 
        - single entry for row and column: df.loc['a','one']
        - slice with labels for rows + column: df.loc['a':'b','one':'two']
    - iloc (not inclusive): use indices
        - entire row by index: df.iloc[[2]] df.iloc[[0,1]] # 3rd row, 0&1 rows
        - just the rows: df.iloc[:2] # 0-1 row = 2 tows in total
        - both axises: df.iloc[0,1] # row 0 + column 1
    - filter  
        - select rows containg 'str': df.filter(like='str', axis=0)
# Filter by Value
    - filter rows by using logical operators on col: df[df.col > 1]
        a = details[details.Place == "Delhi"]
        len(a)
    - multiple filters: df[(df.col > 0.5) & (df.col2 == 1)] # &:and, |:or
        b = details[ (details.Place == "Delhi") | (details.Name == "Ankita") ]
        len(b)
# Data Transformation
    - datetime: df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True) 
    - apply function along an axis: df.apply(np.sum/mean/std, axis = 0/1)
    - change dtype: df.astype('')
    - combine & join:
    df.add(df2, fill_value=0): replace NaN from df with 0 and add to df2
    df1.combine_first(df2): combine two DataFrame objects where missing values in one DataFrame are conditionally filled
# Data Cleansing
    - delete missing values: df.dropna()
    - fill missing values: df['col'].fillna(38.5, inplace=True) / df1=df.replace('?',np.NaN)
    - drop duplicates: df.drop_duplicates(inplace=True)
    - df.rename(columns={'old':'new', 'old':'new'})
    - reindex: df.reindex(index=["c", "f", "b"], columns=["three", "two", "one"])
    - df.drop(columns=['col','col'], inplace = True) 
    - convert index column to a data column: df.reset_index()
    - sorting: df.sort_values('col', ascending=False)
# Data Aggregation
    - merge: merged = pd.merge(df1, df2, on='Name', how='inner')
    - groupby 
        - df1 = df.groupby(['col1'])['col2'].count().reset_index()
        - df1 = df.groupby(['col1', 'col2'], as_index=False).mean().reset_index() # sql style
    - convert to pivot table:
        table = pd.pivot_table(df, values='D', index=['A', 'B'],
                        columns=['C'], aggfunc=np.sum)
        table
        C        large  small
        A   B
        bar one    4.0    5.0
            two    7.0    6.0
        foo one    4.0    1.0
            two    NaN    6.0
    - concat: pd.concat([df1,df2])
# Count with conditions
    - unique: 
        count = df['ShopID'].value_counts().to_frame() / len(count)
        df.value_counts(df['is_preferred'] == 1)
    - how many with condition/s
        len( df[ (df['col1'] == 2) & (df['col2'] =='abc') ] )
        OR 
        count = df.apply(lambda x: True 
            if x['col']==2 & x['col2']=='abc' 
            else False], axis = 1)
        len(count[count=True].index)
        len(count(count=False).index)
# Data analysis
    ## Visualisation
        - boxplot: sns.boxplot(x='',y='',data=df)
        - scatter plot 
            x=df[''] y=df['']
            plt.scatter(x,y)
            plt.title()
            plt.xlabel()
            plt.ylabel()
    ## Correlation 
        - sns.regplot(x='',y='',data-=df)
        plt.ylmi(0,)
        - pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  
    ## Normalisation
        - simple feature: df[] / df[].max()
        - min max: (df[] - df[].min()) / (df.max()-df.min())
        - z_score: (df - df.mean()) / df[].std() -- -3< z <3