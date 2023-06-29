from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, LongType, StringType, DoubleType

spark = SparkSession.builder.appName("ISS-TRACK").getOrCreate()

schema = StructType([
    StructField("message", StringType(), True),
    StructField("iss_position", StructType([
        StructField("latitude", StringType(), True),
        StructField("longitude", StringType(), True)
    ]), True),
    StructField("timestamp", LongType(), True),
])

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "my-topic") \
  .option("startingOffsets", "latest") \
  .load() \
  .selectExpr("CAST(value AS STRING)") \
  .select(from_json("value", schema).alias("data")) \
  .select("data.*")

df = df.withColumn("latitude", col("iss_position.latitude"))

df = df.withColumn("longitude", col("iss_position.longitude"))

df = df.drop("iss_position")

df = df.filter(col("message") == "success")

csv_query = df \
    .writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("checkpointLocation", "/mnt/c/users/admin/desktop/winlinux/bde/checkpoint") \
    .option("path", "/mnt/c/users/admin/desktop/winlinux/bde/output") \
    .option("header", "true") \
    .start()

console_query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

csv_query.awaitTermination()

console_query.awaitTermination()
