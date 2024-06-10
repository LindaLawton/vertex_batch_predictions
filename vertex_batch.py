import os
import time
import vertexai
from vertexai.preview.batch_prediction import BatchPredictionJob
from dotenv import load_dotenv

load_dotenv()


def create_batch_prediction_job():
    try:
        vertexai.init(project=os.getenv("PROJECT_ID"), location=os.getenv("PROJECT_LOCATION"))

        job = BatchPredictionJob.submit(
            source_model=os.getenv("MODEL_ID"),  # source_model
            input_dataset=f"bq://{os.getenv("BQ_TABLE_ID")}",  # input_dataset
            output_uri_prefix=f"bq://{os.getenv("BQ_OUTPUT_DATASET")}"  # Optional, output_uri_prefix
        )

        # Check job status
        print(f"Job resource name: {job.resource_name}")
        print(f"Model resource name with the job: {job.model_name}")
        print(f"Job state: {job.state.name}")

        # Refresh the job until complete
        while not job.has_ended:
            time.sleep(5)
            job.refresh()

        # Check if the job succeeds
        if job.has_succeeded:
            print("Job succeeded!")
            return "Job succeeded!", True
        else:
            print(f"Job failed: {job.error}")
            return f"Job failed: {job.error}", False

        # Check the location of the output
        print(f"Job output location: {job.output_location}")

        # List all the GenAI batch prediction jobs under the project
        for bpj in BatchPredictionJob.list():
            print(f"Job ID: '{bpj.name}', Job state: {bpj.state.name}, Job model: {bpj.model_name}")
    except Exception as err:
        return err, False


if __name__ == "__main__":
    create_batch_prediction_job()
