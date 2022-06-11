import sys
import os
import pandas as pd
import quandl
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')
data = quandl.Dataset('WIKI/'+sys.argv[1]).data().to_pandas()
plt.plot_date(x=data.index, y=data['Adj. Close'],  fmt="r-")
plt.show()
plt.savefig('results/ticker.png',format='png')
plt.close()