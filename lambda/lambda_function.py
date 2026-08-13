import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):
    rec = event["Records"][0]["s3"]

    key = rec["object"]["key"]
    bucket = rec["bucket"]["name"]

    if not key.endswith(".csv"):
        return {"skipped": key}

    run = glue.start_job_run(
        JobName="csv_to_json_job",
        Arguments={
            "--input_key": key,
            "--src_bucket": bucket
        }
    )

    print("started glue run", run["JobRunId"])

    return {
        "jobRunId": run["JobRunId"]
    }
