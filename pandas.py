data.merge(data2, left_on='data_id', right_on="data2_id", how='right')

data.groupby(['UserId', 'SessionId'])['Event']

usales = defaultdict()
for index in range(sales.shape[0]):
    usales.setdefault(sales['UserId'][index], sales['timestamp'][index])
	
	
error_data[error_data['id']==i]['report'].iloc[0] 

pd.DataFrame.from_dict(dict(usales), orient='index')	