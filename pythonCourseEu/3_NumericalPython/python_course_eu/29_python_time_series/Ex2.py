from datetime import datetime, timedelta as delta
import random
import pandas as pd
import numpy as np

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

#Create data ranges
splitter('Create data ranges')
index = pd.date_range('24/12/2012', '01/03/2013')
print(index)
