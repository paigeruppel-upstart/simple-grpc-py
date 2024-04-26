import json
import logging
import sys
import uuid

import grpc

import constants
from generated.simple_service.v1.simple_retry_api_pb2 import RetriableActionRequest, RespondWith
from generated.simple_service.v1.simple_retry_api_pb2_grpc import SimpleRetryAPIStub

logger = logging.getLogger(__name__)

# run with `python manual_retry_client.py`
#   optionally specify a port, otherwise will default constants.PYTHON_SERVER_PORT
def main() -> None:
    port = constants.PYTHON_SERVER_PORT
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    logger.info("Connecting to the server at '%s:%s'", "localhost", port)

    service_config_json = json.dumps(
        {
            "methodConfig": [
                {
                    "name": [
                        {"service": ""}
                    ],
                    "retryPolicy": {
                        "maxAttempts": 5,
                        "initialBackoff": "0.1s",
                        "maxBackoff": "1s",
                        "backoffMultiplier": 2,
                        "retryableStatusCodes": ["FAILED_PRECONDITION", "ABORTED"],
                    },
                }
            ]
        }
    )
    # NOTE: the retry feature will be enabled by default >=v1.40.0
    # options.append(("grpc.enable_retries", 1))
    options = [("grpc.service_config", service_config_json)]

    target = f"localhost:{port}"
    channel = grpc.insecure_channel(target, options=options)

    with channel as channel:
        request_id = f"{uuid.uuid4()}"
        respond_with = [RespondWith(status_code=9), RespondWith(status_code=10)]
        request = RetriableActionRequest(request_id= request_id, respond_with=respond_with)
        stub = SimpleRetryAPIStub(channel)
        response = stub.RetriableAction(request)
        print(f"Configured client received: {response}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    main()
