# Simple gRPC Python App

This app implements [Simple Retry API](proto/simple_service/v1/simple_retry_api.proto) over gRPC and supports:

- Running a python server that serves [an implementation of the above](simple_grpc_py/simple_retry_api_impl.py)
- Running a python client with configured retries via channel options
- Running a python client with manual retries via channel options

[simple-grpc-rb](https://github.com/paigeruppel-upstart/simple-grpc-rb) implements the above in ruby and is meant to be paired with this for cross lang testing.

## Usage

### Install Dependencies
- Requires python = "^3.8" and Poetry 1.4.2
```shell
make install
```

### Re-Generate stubs from simple_retry_api.proto
```shell
make generate_proto_definitions
```

### Serve the API / run the Server

Port defaults to `7777` [PYTHON_SERVER_PORT](simple_grpc_py/constants.py)
`python simple_grpc_py/server.py` 

### Run a retry client against the above server

- Client configured with channel args / service_config:  
`python simple_grpc_py/configured_retry_client.py 7777`

Client with manual error handling
`python simple_grpc_py/manual_retry_client.py 7777`


### Running against Simple gRPC Ruby App  

(Assumes the ruby server is running on the default [RUBY_SERVER_PORT](simple_grpc_py/constants.py))

- Client configured with channel args / service_config:
`python simple_grpc_py/configured_retry_client.py 5555`

Client with manual error handling
`python simple_grpc_py/manual_retry_client.py 5555`
