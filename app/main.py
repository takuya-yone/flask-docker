from fastapi import FastAPI
import os
import json
app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello,World"}

@app.get("/health")
async def health():
    return {"message": "Status OK!!"}

@app.get("/env")
async def env():
    return dict(os.environ)

@app.get("/pod")
async def pod():
    K8S_NODE_NAME = os.environ.get('K8S_NODE_NAME')
    K8S_POD_NAME = os.environ.get('K8S_POD_NAME')
    K8S_POD_NAMESPACE = os.environ.get('K8S_POD_NAMESPACE')
    K8S_POD_IP = os.environ.get('K8S_POD_IP')
    return {
        'K8S_NODE_NAME': K8S_NODE_NAME,
        'K8S_POD_NAME': K8S_POD_NAME,
        'K8S_POD_NAMESPACE': K8S_POD_NAMESPACE,
        'K8S_POD_IP': K8S_POD_IP}
