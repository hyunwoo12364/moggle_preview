import pandas as pd
train = pd.read_csv('train.csv')
train
test = pd.read_csv('test.csv')
submission = pd.read_csv('sample_submission.csv')
submission.head()
submission.to_csv('submission.csv', index=False)
