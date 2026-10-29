# AWS S3 Event-Driven Automation Using Lambda

## Project Overview

This project demonstrates event-driven automation using Amazon S3 and AWS Lambda. When a file is uploaded to a configured S3 bucket, an S3 object creation event triggers a Lambda function. The function extracts the bucket name and uploaded file name and records the details in Amazon CloudWatch logs.

## Technologies Used

- Amazon Web Services (AWS)
- Amazon S3
- AWS Lambda
- Python
- Amazon CloudWatch
- IAM Execution Roles and S3 Event Notifications

## AWS Region

Asia Pacific (Mumbai) — `ap-south-1`

## Architecture

S3 File Upload → S3 Object Creation Event → AWS Lambda → Amazon CloudWatch Logs

## AWS Resources

| Resource | Name |
|---|---|
| S3 Bucket | `twinkle-lambda-event-bucket-2026` |
| Lambda Function | `S3FileUploadProcessor-TM` |
| Sample Input File | `sales.csv` |
| Region | `ap-south-1` |

## Implementation Steps

1. Created a dedicated S3 bucket for the project.
2. Created a Python-based AWS Lambda function.
3. Implemented code to extract the bucket name and uploaded file name from S3 event records.
4. Configured an S3 object creation trigger to invoke Lambda.
5. Uploaded a sample CSV file named `sales.csv`.
6. Examined the Lambda execution logs in Amazon CloudWatch to verify event processing.

## Lambda Functionality

The Lambda function processes S3 event records and prints the bucket name and object key to the execution logs. It returns a success response after processing the event records.

## Python Code

The Lambda implementation is available in `lambda_function.py`.

## Expected Output

When the configured S3 event triggers the function, the logs should contain information similar to:

```text
S3 Event Received!
Bucket name: twinkle-lambda-event-bucket-2026
Uploaded file: sales.csv
```

## Key Learnings

- Understanding event-driven architecture.
- Configuring S3 event notifications.
- Developing and deploying Python Lambda functions.
- Understanding Lambda execution roles and CloudWatch logs.
- Testing automated cloud workflows.

## Project Documentation

The accompanying PDF report contains the project overview, implementation explanations, screenshots, and verification steps.

**Report:** `Twinkle_Meska_S3_Lambda_Report.pdf`

## Author

Twinkle Meska

B.Tech Computer Science — Software Engineering

GitHub: [TwinkleMes](https://github.com/TwinkleMes)
