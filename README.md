# vertex_batch_predictions for Cloud run

Batch predictions are a way to efficiently send multiple multimodal prompt requests that are non-latency sensitive. Unlike online prediction, where you are limited to one input request at a time, you can send a large number of multimodal requests in a single batch request. A batch prediction workflow consists of determining your output location, adding your input requests (in JSON), and your responses asynchronously populate in your BigQuery storage output location.

This project configures a Cloud Run Service for use with batch predictions for gemini.

[Get batch predictions for Gemini ](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini)


# .env

    MODEL_ID=gemini-1.5-flash-001
    PROJECT_ID=[Cloud Project id]
    PROJECT_LOCATION=us-central1
    BQ_TABLE_ID=[Big Query table source]
    BQ_OUTPUT_DATASET=[Big query dataset]

# Big query input table

    CREATE TABLE `[BQ_PROJECT].[BQ_DATASET].[BQ_TABLE_NAME]`
    (
      request JSON
    );

# Input row.
 Each row in the input table will be one row request as so.

    {
      "contents": [
        {
          "role": "user",
          "parts": {
            "text": "Give me a recipe for banana bread."
          }
        }
      ],
      "system_instruction": {
        "parts": [
          {
            "text": "You are a chef."
          }
        ]
      },
      "generation_config": {
        "top_k": 5
      }
    }

# Note On email

If you want to use the mail_sender.py to send you an email when the job is complete. You must include a credentials.json 
file for an installed application.  

Then run mail_sender.py locally first to authorize the app that will give you a token.json.

then uncomment in main.py 

    send_status(f"Batch supporting Flask Status: {status}", str(result))


# Deploy on cloud run

This code was created using [Quickstart: Deploy a Python service to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)

You will need to init your gcp and then just run

    gcloud init
    gcloud run deploy


# Links

- [Get batch predictions for Gemini ](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini)

