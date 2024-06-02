# Cloud Data Warehouses

This file contains notes on data warehouses, including their purpose, architecture, and implementation in cloud environments.

## Business Need for Data Warehouses

    - **Analytical vs. Operational Processes**:

        - **Operational**: Real-time transactions, system efficiency.

        - **Analytical**: Insights from historical data, trends, and patterns.

    - **OLTP vs. OLAP**:

        - **OLTP (Online Transaction Processing)**: Real-time, normalized databases, fast transactions.

        - **OLAP (Online Analytical Processing)**: Historical, aggregated data, complex queries.

    - **Data Warehouses**: Bridge OLTP and OLAP, provide a platform for analyzing historical data.

## Data Warehouse Architecture

    - **ETL Process (Extract, Transform, Load)**:

        - **Extraction**: Pulling data from source systems.

        - **Transformation**: Cleaning, integrating, and preparing data.

        - **Loading**: Storing data in the warehouse.

    - **Kimball's Bus Architecture**: Dimensional modeling approach, emphasizing a shared dimensional data model.

## Dimensional Modeling and ETL

    - **Star Schema**:

        - **Fact Table**: Stores quantitative event data (e.g., sales, song plays).

        - **Dimension Tables**: Store descriptive context information (e.g., customers, products, time).

    - **Benefits of Star Schema**:

        - **Easier for business users to understand.**

        - **Faster query performance.**

    - **ETL Implementation**: Extracting, transforming, and loading data into a star schema.

## OLAP Cubes

    - **OLAP Cubes**: Multidimensional representations of data in a star schema.

    - **Cube Operations**: Flexible data analysis.

        - **Roll-up**: Aggregating data to higher levels.

        - **Drill-down**: Expanding data to lower levels.

        - **Slice** : Selecting a subset based on a specific dimension value.

        - **Dice**: Selecting a sub-cube based on multiple dimension values.

## Data Warehousing in the Cloud

    - **Cloud Benefits**: Scalability, flexibility, cost optimization.

    - **Shift from ETL to ELT**: Transformation on the destination server (data warehouse).

    - **Cloud Managed Databases**:

        - **SQL Databases**: Managed relational databases (e.g., SQL Server, PostgreSQL).

        - **NoSQL Databases**: Managed services for various NoSQL database types.

    - **Cloud ETL Pipeline Services**: Tools for building and managing data pipelines.

    - **Cloud Data Warehouse Solutions**: Azure Synapse, Amazon Redshift, GCP BigQuery.

## AWS Data Warehouse Technologies

    - **Amazon Redshift**: MPP database optimized for analytical workloads.

        - **Key Concepts**: Leader Node, Compute Nodes, Slices, Distribution Styles, Sorting Key.

    - **AWS S3**: Object storage for data ingestion and backup.

    - **AWS RDS**: Managed relational database service (e.g., PostgreSQL).

    - **Boto3 SDK**: Python library for interacting with AWS services.

## Implementing a Data Warehouse on AWS (Sparkify Project)

    - **Project Goal**: Building an ETL pipeline for Sparkify's music streaming data.

    - **Steps**:

        - **Create AWS Resources**: IAM role, security group, Redshift cluster, S3 bucket, RDS instance.

        - **ETL Process**: Extract, stage, and transform data into dimensional tables.

            - **Use COPY Command**: Efficiently load data from S3 to Redshift.

            - **Optimize Table Design**: Choose appropriate distribution and sorting keys.
