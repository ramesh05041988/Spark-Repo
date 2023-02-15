from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("First pyspark program").getOrCreate()
df = spark.read.format("csv").option("header","true").load("file:///C://BigData-1//Files//test.csv")
df.show()