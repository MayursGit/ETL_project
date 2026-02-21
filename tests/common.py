from pyspark.sql.functions import col, regexp_replace

# Remove additional spaces in a column (e.g., name)
def remove_extra_spaces(df, column_name):
    df_transformed = df.withColumn(
        column_name,
        regexp_replace(col(column_name), "\\s+", " ")
    )
    return df_transformed


# Filter Senior Citizens (age >= 60)
def filter_senior_citizen(df, column_name):
    df_filtered = df.filter(col(column_name) >= 60)
    return df_filtered

def add_column_with_constant_value(df, new_column_name, value):
    from pyspark.sql.functions import lit
    df_with_new_column = df.withColumn(new_column_name, lit(value))
    return df_with_new_column