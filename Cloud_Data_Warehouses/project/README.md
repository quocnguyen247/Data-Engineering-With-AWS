# Project: Cloud Data Warehouse

## Project Description:

This project involves building a data warehouse and ETL pipeline to analyze song play data from Sparkify, a fictional music streaming service. The data warehouse is built on Amazon Redshift, and the ETL process loads data from S3 to the warehouse, transforming it into a star schema for analytical queries.

## Purpose of the Database:

The purpose of this database is to provide Sparkify with insights into user behavior and song popularity. This information can be used to:

- **Improve user experience**: By understanding user preferences, Sparkify can recommend relevant songs and features.
- **Optimize marketing campaigns**: Targeting users based on their listening habits can increase the effectiveness of marketing efforts.
- **Identify trends in music consumption**: Understanding song popularity can inform content acquisition and playlist curation strategies.


## Database Schema Design:
The database utilizes a star schema with a fact table (songplays) and several dimension tables. The dimension tables are designed to store descriptive data about users, songs, artists, and time, while the fact table captures the actual song play events.
# Dimension Tables:
- **users**: Stores information about each user, including user ID, first and last name, gender, level, and registration date.
- **songs**: Stores information about each song, including song ID, title, artist ID, year, duration, and genre.
- **artists**: Stores information about each artist, including artist ID, name, location, latitude, and longitude.
- **time**: Stores information about the timestamp of each song play event, including hour, day, week, month, year, and weekday.

## Fact Table:

- **songplays**: Stores information about each song play event, including song play ID, start time, user ID, level, song ID, artist ID, session ID, location, and user agent.


### Justification for Schema Design:
The star schema design is chosen for its efficiency in querying large datasets. The fact table contains the core information about song plays, while the dimension tables provide detailed context for each event. This structure enables fast retrieval of data for specific analyses without needing to join multiple large tables.

## ETL Pipeline:

### The ETL pipeline consists of two stages:
1. **Loading data from S3 to staging tables**: Data from S3 is loaded into staging tables on Redshift using COPY commands. Staging tables are temporary tables that hold raw data before it is transformed.
2. **Transforming data from staging tables to analytical tables**: Data from staging tables is then transformed and inserted into the final analytical tables. This includes selecting relevant columns, joining data from staging tables, and applying necessary data types.

### Justification for ETL Pipeline:

This pipeline is designed for scalability and efficiency:
- **Scalability**: The use of staging tables allows for incremental data loading and avoids the need to rewrite the entire database with each update.
- **Efficiency**: The use of COPY commands for loading data from S3 ensures fast and efficient data transfer.


## Additional Notes:
- The *sql_queries.py* file contains all the SQL statements required for creating the tables and running the ETL process.
- The *create_tables.py* file contains the logic for connecting to the Redshift database and creating the tables.
- The *etl.py* file contains the logic for the ETL process, loading data from S3 to staging tables and transforming data into analytical tables.
- The *dwh.cfg* file contains the credentials for accessing the Redshift database and S3 bucket.