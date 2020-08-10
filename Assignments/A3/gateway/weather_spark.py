from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.regression import *
from pyspark.ml.feature import SQLTransformer, VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession, functions, types
import sys
import datetime
import numpy as np
import elevation_grid as eg
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+

spark = SparkSession.builder.appName('example code').getOrCreate()
assert spark.version >= '2.4'  # make sure we have Spark 2.4+
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

tmax_schema = types.StructType([
    types.StructField('station', types.StringType()),
    types.StructField('date', types.DateType()),
    types.StructField('latitude', types.FloatType()),
    types.StructField('longitude', types.FloatType()),
    types.StructField('elevation', types.FloatType()),
    types.StructField('tmax', types.FloatType()),
])

DATASET = '/courses/732/tmax-test'
MODEL = 'weather-model'
DATE = datetime.date(2020, 2, 1)


def change():
    data = spark.read.csv(DATASET, schema=tmax_schema)
    data.createOrReplaceTempView('d')
    y1 = spark.sql('select station,latitude,longitude,elevation,max(tmax) as tmax from d where year(date) between 2000 and 2017 group by station,latitude,longitude,elevation order by station')
    y1.createOrReplaceTempView('y1')
    y2 = spark.sql(
        'select station,max(tmax) as tmax from d where year(date) between 1900 and 1999 group by station order by station')
    y2.createOrReplaceTempView('y2')
    changes = spark.sql(
        'select y1.latitude,y1.longitude,y1.elevation,y2.tmax-y1.tmax as change from y1 inner join y2 on y1.station=y2.station order by y1.latitude,y1.longitude')
    changes.toPandas().to_csv('change.csv', index=False)

def predict():
    data = []
    for lat in list(np.arange(-90, 90, .5)):
        for lon in list(np.arange(-180, 180, .5)):
            elev = eg.get_elevation(lat, lon)
            tmp = ['STATION', DATE, float(lat), float(
                lon), float(elev), float(0)]
            data.append(tmp)
    df = spark.createDataFrame(data, tmax_schema)
    model = PipelineModel.load(MODEL)
    predictions = model.transform(df)
    predictions.toPandas().to_csv('prediction.csv', index=False)


def test():
    test_data = spark.read.csv(DATASET, schema=tmax_schema)
    model = PipelineModel.load(MODEL)
    errors = model.transform(test_data)
    errors.toPandas().to_csv('error.csv', index=False)


def main():
    change()
    predict()
    test()


if __name__ == '__main__':
    main()
