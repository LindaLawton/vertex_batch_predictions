import os
from flask import Flask
import os

from mail_sender import send_status
from vertex_batch import create_batch_prediction_job

app = Flask(__name__)


@app.route("/")
def create_job():
    result, status = create_batch_prediction_job()
    # Uncomment to send email if you have authorized it first.
    # send_status(f"Batch supporting Flask Status: {status}", str(result))
    return f"Job Status {str(result)}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))