import json
import logging
import sys
import uuid

import grpc

import constants
from generated.simple_service.v1.simple_retry_api_pb2 import RetriableActionRequest, RespondWith
from generated.simple_service.v1.simple_retry_api_pb2_grpc import SimpleRetryAPIStub

logger = logging.getLogger(__name__)


# run with python simple_grpc_py/manual_retry_client.py
#   optionally specify a port, otherwise will default constants.RUBY_SERVER_PORT
def main() -> None:
    port = constants.RUBY_SERVER_PORT
    if len(sys.argv) == 2:
        port = int(sys.argv[1])

    logger.info("Connecting to the server at '%s:%s'", "localhost", port)
    target = f"localhost:{port}"

    with grpc.insecure_channel(target) as channel:
        request_id = f"{uuid.uuid4()}"
        logger.info(f"Sending request with request_id {request_id}")

        # instruct the service to respond first with 9, then with 10, and on the third attempt succeed
        respond_with = [RespondWith(status_code=9), RespondWith(status_code=10)]
        request = RetriableActionRequest(request_id=request_id, respond_with=respond_with)
        stub = SimpleRetryAPIStub(channel)

        attempts = 0
        while attempts <= len(respond_with):
            logger.info(f"Attempt number: {attempts + 1}")
            try:
                attempts += 1
                response = stub.RetriableAction(request)
                logger.info(f"Manual retry client received: {response}")
            except grpc.RpcError as e:
                logger.error("RECEIVED ERROR FROM SERVER: %s", e.code())
                continue


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    main()
