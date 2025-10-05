from pyspark.sql.functions import *
from pyspark.sql.types import *
import datetime 

def add_audit_cols(df,filename):
    return(
        df.withColumn("batch_id",lit(filename)).withColumn("create_date",lit(current_date())).withColumn("create_user",lit('cpprod')).withColumn("update_date",lit(lit(None).cast('date'))).withColumn("update_user",lit(None).cast('string'))
    )