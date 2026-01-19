import os

from vertexai import agent_engines
import vertexai
from .agent import root_agent

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "gapps-elmo-sandbox")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "europe-west1")
STAGING_BUCKET = os.environ.get(
    "GOOGLE_STAGING_BUCKET", "gs://elmo-test-bucket")

# Initialize the Vertex AI SDK
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

app = agent_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)


remote_app = agent_engines.create(
    agent_engine=app,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]",
        "hubspot-api-client",
        "fastmcp",
        "uvicorn",
        "python-dotenv"
    ],
    extra_packages=[
        ".assistant_agent/.env",  # a single file
        "./mcp-severa",  # a directory
    ]
)

print(f"Deployment finished!")
print(f"Resource Name: {remote_app.resource_name}")
