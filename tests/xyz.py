import pytest
import pyspark
from pyspark.sql import SparkSession
spark =SparkSession.builder.appName("Spark Unit Test").master("local[*]").getOrCreate()


sample_data = [
        {"name": "John  D.", "age": 30},
        {"name": "Alice   G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve  A.", "age": 28}
    ]
original_df = spark.createDataFrame(sample_data)
original_df.show()
spark.stop()