# load the basic librairies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
# load the data
train_df = pd.read_csv('C:\Users\ateek\Downloads\train.csv\train.csv')
test_df = pd.read_csv('C:\Users\ateek\Downloads\test.csv\test.csv')
sub = pd.read_csv('C:\Users\ateek\Downloads\sample_submission.csv\sample_submission.csv')