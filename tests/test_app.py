from common import add_column_with_constant_value, remove_extra_spaces,filter_senior_citizen
def test_single_space(spark_session):
    sample_data = [
        {"name": "John  D.", "age": 30},
        {"name": "Alice   G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve  A.", "age": 28}
    ]

    # Create Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the transformation function
    transformed_df = remove_extra_spaces(original_df, "name")

    expected_data = [
        {"name": "John D.", "age": 30},
        {"name": "Alice G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve A.", "age": 28}
    ]

    expected_df = spark_session.createDataFrame(expected_data)

    # Assertion
    assert transformed_df.collect() == expected_df.collect()

def test_row_count(spark_session):
    sample_data = [
        {"name": "John  D.", "age": 30},
        {"name": "Alice   G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve  A.", "age": 28}
    ]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the transformation function
    transformed_df = remove_extra_spaces(original_df, "name")

    expected_data = [
        {"name": "John D.", "age": 30},
        {"name": "Alice G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve A.", "age": 28}
    ]

    expected_df = spark_session.createDataFrame(expected_data)

    # Optional debug print
    print(expected_df.count())

    # Assertion: row count should remain same
    assert transformed_df.count() == expected_df.count()
def test_senior_citizen_count(spark_session):
    sample_data = [
        {"name": "John D.", "age": 60},
        {"name": "Alice G.", "age": 25},
        {"name": "Bob T.", "age": 65},
        {"name": "Eve A.", "age": 28}
    ]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the filter function
    filtered_df = filter_senior_citizen(original_df, "age")

    expected_data = [
        {"name": "John D.", "age": 60},
        {"name": "Bob T.", "age": 65}
    ]

    expected_df = spark_session.createDataFrame(expected_data)

    # Optional debug print
    print(expected_df.count())

    # Assertion: senior citizen count should match
    assert filtered_df.count() == expected_df.count()


def test_add_column_with_constant_value(spark_session):
    sample_data = [
        {"name": "John D.", "age": 60},
        {"name": "Alice G.", "age": 25}
    ]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the function to add a new column with a constant value
    new_column_name = "country"
    constant_value = "USA"
    transformed_df = add_column_with_constant_value(original_df, new_column_name, constant_value)

    expected_data = [
        {"name": "John D.", "age": 60, "country": "USA"},
        {"name": "Alice G.", "age": 25, "country": "USA"}
    ]

    expected_df = spark_session.createDataFrame(expected_data)

    # Assertion
    # assert transformed_df.collect() == expected_df.collect()
    cols = ["name", "age", "country"]

    assert (
        transformed_df.select(cols).collect()
    == expected_df.select(cols).collect()
    )

def test_add_column_with_constant_value_row_count(spark_session):
    sample_data = [
        {"name": "John D.", "age": 60},
        {"name": "Alice G.", "age": 25}
    ]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the function to add a new column with a constant value
    new_column_name = "country"
    constant_value = "USA"
    transformed_df = add_column_with_constant_value(original_df, new_column_name, constant_value)

    expected_data = [
        {"name": "John D.", "age": 60, "country": "USA"},
        {"name": "Alice G.", "age": 25, "country": "USA"}
    ]

    expected_df = spark_session.createDataFrame(expected_data)

    # Assertion: row count should remain same
    assert transformed_df.count() == expected_df.count()