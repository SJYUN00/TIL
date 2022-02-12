# how to use pyspark

## pyspark course
- link : https://www.youtube.com/watch?v=_C8kWso4ne4
  
## multiple ways of reading csv files

To read Data set...

1. first one needs Checking Schema
``spark.read.optiion('header','true').csv('test1.csv')``
not with .show() at the end of code

2. using this option can skip Checking Schema
``df_pyspark=spark.read.csv('test.csv', header=True, inferSchema=True)``
``df_pyspark.show()``

## Check the schema(columns)

``df_pyspark.printSchema()``

will be

root 
|-- Name: string (nullable = true)
|-- age: integer (nullable = true)
|-- Experience: integer (nullable = true)

## type of df_pyspark

``type(df_pyspark)``
will be pyspark.sql.dataframe.DataFrame

### how to see dftypes

``df_pyspark.dtypes``

## How to get column name, head

``df_pyspark.columns``
``df_pyspark.head()``

## How to select column

``df_pyspark.select('Name')``

will be 

DataFrame[Nmae: string]

``df_pyspark.select('Name').show()``

will be

in Dial Column. 

type of this will be pyspark.sql.df.DF. not pandas DF.

### selecting multiple columns

``df_pyspark.select(['Name','Experience']).show()``

will be

in Dial showing Name, Experince columns.

NEXT
z