from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace, col, concat_ws

spark = SparkSession.builder \
    .appName("CleanHondaPartsData") \
    .config("spark.jars.packages",
            "com.crealytics:spark-excel_2.12:3.6.2,"
            "org.mongodb.spark:mongo-spark-connector_2.12:10.1.1") \
    .config("spark.mongodb.write.connection.uri", "mongodb://localhost:27017/honda_parts.cleaned_parts") \
    .getOrCreate()


excel_path = r"C:\Users\Admin\Downloads\testparts\honda_1-5\ALL HONDA PARTS 700K(1).xlsx"

df = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(excel_path)

split_url = split(col("Original_URL"), "/")

df_extracted = df.withColumn("Maker", split_url.getItem(4)) \
    .withColumn("Model_raw", split_url.getItem(5)) \
    .withColumn("Frame1_raw", split_url.getItem(6)) \
    .withColumn("Frame2_raw", split_url.getItem(7)) \
    .withColumn("Parts_Group_raw", split_url.getItem(8)) \
    .withColumn("Full_Description", concat_ws(" ", col("Description"), col("Description1")))

clean_suffix = "-[a-z]*\\d+$"

df_cleaned = df_extracted \
    .withColumn("Model", regexp_replace(col("Model_raw"), clean_suffix, "")) \
    .withColumn("Frame1", regexp_replace(col("Frame1_raw"), clean_suffix, "")) \
    .withColumn("Frame2", regexp_replace(col("Frame2_raw"), clean_suffix, "")) \
    .withColumn("Parts_Group", regexp_replace(col("Parts_Group_raw"), clean_suffix, "")) \
    .drop("Model_raw", "Frame1_raw", "Frame2_raw", "Parts_Group_raw")

final_df = df_cleaned.select(
    "Original_URL",
    "Full_Description",
    "OEM_Part_",
    "Price",
    "Field",
    "Maker",
    "Model",
    "Frame1",
    "Frame2",
    "Parts_Group"
)

final_df.write \
    .format("mongodb") \
    .mode("append") \
    .option("uri", "mongodb://localhost:27017/honda_parts.cleaned_parts") \
    .save()

print("✅ Data written to MongoDB")
