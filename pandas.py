data.merge(data2, left_on='data_id', right_on="data2_id", how='right')

data.groupby(['UserId', 'SessionId'])['Event']

