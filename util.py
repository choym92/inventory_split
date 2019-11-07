def bucket_avg(ts, bucket):
    '''
        ts: series with index
        bucket: ['30T', '60T', 'M', 'W'] etc.. read doc for .resample
    '''
    y = ts.resample(bucket).mean()
    return y

def bucket(ts, bucket, func = 'mean'):
    '''
        ts: series with index
        bucket: ['30T', '60T', 'M', 'W'] etc.. read doc for .resample
        func: default=mean; choices: ['mean', 'count', 'sum']
    '''
    if func == 'mean':
        y = ts.resample(bucket).mean()
    elif func == 'count':
        y = ts.resample(bucket).count()
    elif func == 'sum':
        y = ts.resample(bucket).sum()
    
    return y

