#Part2 a
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('change.csv')
lons = np.array(df.longitude).tolist()
lats = np.array(df.latitude).tolist()
changes = np.array(df.change).tolist()
fig = plt.figure(num=None, figsize=(18, 12))
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.drawmapboundary(fill_color='darkgrey')
# m.fillcontinents(color='#cc9966', lake_color='#99ffff')
x, y = m(lons, lats)
scatter=plt.scatter(x, y, 10, marker='o', c=changes, cmap='jet')
# handles, labels = scatter.legend_elements(prop="change", alpha=0.6)
# plt.legend(handles, labels, loc="upper right", title="Sizes")
m.colorbar(scatter)
plt.title('NOAA Global Temperature Change: 20th-21st Century',fontsize=16)
plt.show()

#Part2 b1
import elevation_grid as eg
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap

DATE = datetime.date(2020, 2, 1)
df_prediction=pd.read_csv('prediction.csv')
def get_temp(x):
    x_index=int((x.longitude-(-180))*2)
    y_index=int((x.latitude-(-90))*2)
    temps[x_index][y_index]=x.prediction

fig = plt.figure(num=None, figsize=(16, 10))
m = Basemap(projection='cyl', resolution='c', lat_0=0, lon_0=0)
m.drawcoastlines()
lats, lons = np.meshgrid(np.arange(-90, 90, .5), np.arange(-180, 180, .5))
elevs = [eg.get_elevations(np.array([lat, lon]).T) for lat, lon in zip(lats, lons)]
temps = [[0 for i in range(360)] for j in range(720)]
df_prediction.apply(get_temp,axis=1)
cs = m.pcolormesh(lons, lats, temps, cmap='jet')
m.colorbar(cs)
plt.title('Global Temperature Prediction on 2020-2-1',fontsize=16)
plt.show()

#Part2 b2
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('error.csv')
lons = np.array(df.longitude).tolist()
lats = np.array(df.latitude).tolist()
errors = np.array(df.prediction-df.tmax).tolist()
fig = plt.figure(num=None, figsize=(18, 12))
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.drawmapboundary(fill_color='darkgrey')
x, y = m(lons, lats)
scatter=plt.scatter(x, y, 10, marker='o', c=errors, cmap='jet')
m.colorbar(scatter)
plt.title('Global Temperature Model Regression Error',fontsize=16)
plt.show()