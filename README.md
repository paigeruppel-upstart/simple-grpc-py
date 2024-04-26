# Simple gRPC Python App

This app implements [Simple Retry API](proto/simple_service/v1/simple_retry_api.proto) over gRPC and supports:

- Running a python server that serves [an implementation of the above](simple_grpc_py/simple_retry_api_impl.py)
- Running a python client with configured retries via channel options
- Running a python client with manual retries via channel options

This repo implements the above in ruby and is meant to be paired with this for cross lang testing.

## Re-Generate stubs from simple_retry_api.proto
`make regen-proto`

## Serve the API / run the Server

`python simple_grpc_py/server.py` - defaults to port 7777 (defined in constants.py/PYTHON_SERVER_PORT = "7777")

## Run a retry client against the above server

Client configured with channel args / service_config:
`python simple_grpc_py/configured_retry_client.py` - defaults to port 7777 (defined in constants.py/PYTHON_SERVER_PORT = "7777")

Client with manual error handling
`python simple_grpc_py/manual_retry_client.py 7777`


## Running against Simple gRPC Ruby App

Client configured with channel args / service_config:
`python simple_grpc_py/configured_retry_client.py 5555`

Client with manual error handling
`python simple_grpc_py/manual_retry_client.py` - defaults to port 5555 (defined in constants.py/RUBY_SERVER_PORT = "5555")

