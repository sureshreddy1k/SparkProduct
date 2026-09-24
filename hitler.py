print("=====🔴🔴🔴🔴🔴== CELL 1 =======")

data = [
    (1, "Sai",   "Python",     30000, "ACTIVE"),
    (2, "Raj",   "Python",     32000, "ACTIVE"),
    (3, "John",  "Java",       28000, "ACTIVE"),
    (4, "Rita",  "Python",     31000, "ACTIVE"),
    (5, "Sam",   "Java",       29000, "ACTIVE"),
    (6, "Kiran", "Databricks", 33000, "ACTIVE"),
    (7, "Anu",   "Python",     27000, "ACTIVE"),
    (8, "Ram",   "Spark",      34000, "ACTIVE"),
    (9, "Priya", "Spark",      30000, "ACTIVE"),
    (10,"Vijay", "Databricks", 35000, "ACTIVE")
]

df = spark.createDataFrame(
    data,
    ["student_id", "name", "course", "fee", "status"]
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("students")

print("INITIAL DATA")
display(spark.table("students").orderBy("student_id"))