# AWS Glue ETL Pipeline with Amazon S3

## Project Overview

This project demonstrates an end-to-end Extract, Transform, and Load (ETL) pipeline using Amazon S3 and AWS Glue. Employee data is stored as a CSV file in Amazon S3, discovered using an AWS Glue Crawler, transformed using an AWS Glue visual ETL job, and written to S3 in Parquet format.

## Architecture

```text
Employee CSV Dataset
        |
        v
Amazon S3 - raw/
        |
        v
AWS Glue Crawler
        |
        v
AWS Glue Data Catalog
        |
        v
AWS Glue Visual ETL Job
        |
        v
Drop Fields Transformation
(Remove city column)
        |
        v
Amazon S3 - curated/
(Parquet format with Snappy compression)
```

## Technologies Used

- Amazon S3
- AWS Glue
- AWS Glue Data Catalog
- AWS Glue Crawler
- AWS Glue Studio
- Python / PySpark
- CSV and Parquet

## AWS Region

Asia Pacific (Mumbai) — `ap-south-1`

## S3 Bucket Structure

```text
twinkle-glue-etl-project-2026/
├── raw/
│   └── employees.csv
└── curated/
    └── Transformed Parquet output
```

## Implementation Steps

1. Created a dedicated Amazon S3 bucket for the ETL project.
2. Created `raw/` and `curated/` folders to organize input and output data.
3. Uploaded the employee dataset in CSV format to the `raw/` folder.
4. Created an AWS Glue Data Catalog database named `twinkle_glue_etl_db`.
5. Configured an AWS Glue Crawler to discover the CSV schema and create table metadata.
6. Created a visual ETL job named `twinkle-employees-etl-job`.
7. Configured a Drop Fields transformation to remove the `city` column.
8. Configured the Amazon S3 target to write the transformed dataset in Parquet format.
9. Verified that a Parquet output file was generated in the `curated/` folder.

## Dataset

The sample dataset contains these columns:

- `employee_id`
- `name`
- `department`
- `salary`
- `city`

The transformation removes `city` and retains the other employee fields.

## Output

The transformed dataset is stored in the S3 `curated/` folder in Parquet format using Snappy compression.

## Key Learnings

- Organizing raw and curated data in Amazon S3.
- Using AWS Glue Crawlers for automatic schema discovery.
- Managing table metadata through the AWS Glue Data Catalog.
- Building visual ETL pipelines with AWS Glue Studio.
- Transforming employee data and removing unwanted columns.
- Writing processed data in Parquet format.

## Project Documentation

The accompanying PDF report contains screenshots and explanations of the setup, crawler, transformation, and output verification.

**Report:** `Twinkle_Meska_AWS_Glue_ETL_Pipeline.pdf`

## Author

**Twinkle Meska**

- GitHub: [TwinkleMes](https://github.com/TwinkleMes)
- LinkedIn: [Twinkle Meska](https://www.linkedin.com/in/twinkle-meska-aa254338a/)
