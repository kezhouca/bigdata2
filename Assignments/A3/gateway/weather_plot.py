import elevation_grid as eg
import numpy as np
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pyspark.sql import SparkSession, functions, types
from pyspark.ml import PipelineModel
spark = SparkSession.builder.appName('tmax model tester').getOrCreate()

tmax_schema = types.StructType([
    types.StructField('station', types.StringType()),
    types.StructField('date', types.DateType()),
    types.StructField('latitude', types.FloatType()),
    types.StructField('longitude', types.FloatType()),
    types.StructField('elevation', types.FloatType()),
    types.StructField('tmax', types.FloatType()),
])

model = PipelineModel.load('weather-model')


def get_temp(lat, lon, elev):
    day = datetime.date(2020, 2, 1)
    df = spark.createDataFrame(
        [('STATION', day, float(lat), float(lon), float(elev), 1.1)], tmax_schema)
    predictions = model.transform(df)
    result = predictions.select("prediction").collect()
    temp = result[0]['prediction']
    return temp


def get_temps(latlonelevs):
    return [get_temp(lat, lon, elev) for lat, lon, elev in latlonelevs]


fig = plt.figure(num=None, figsize=(16, 10))
m = Basemap(projection='cyl', resolution='c', lat_0=0, lon_0=0)
m.drawcoastlines()
lats, lons = np.meshgrid(np.arange(-90, 90, .5), np.arange(-180, 180, .5))
elevs = [eg.get_elevations(np.array([lat, lon]).T)
         for lat, lon in zip(lats, lons)]
temps = [get_temps(np.array([lat, lon, elev]).T)
         for lat, lon, elev in zip(lats, lons, elevs)]
print(temps)
cs = m.pcolormesh(lons, lats, temps, cmap='jet')
m.colorbar(cs)
plt.title("Eckert IV Projection")
plt.savefig('2a.png')