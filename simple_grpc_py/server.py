import logging
import sys
from concurrent import futures

import grpc

from generated.simple_service.v1.simple_retry_api_pb2_grpc import add_SimpleRetryAPIServicer_to_server
import constants
from simple_retry_api_impl import SimpleRetryApiImpl

logger = logging.getLogger(__name__)

# run with python simple_grpc_py/server.py
#  optionally specify a port, otherwise defaults to constants.PYTHON_SERVER_PORT
def run():
    port = constants.PYTHON_SERVER_PORT
    if len(sys.argv) == 2:
        port = int(sys.argv[1])

    server: grpc.Server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    server.add_insecure_port("[::]:%s" % port)

    add_SimpleRetryAPIServicer_to_server(SimpleRetryApiImpl(), server)

    server.start()
    logger.info("Server started - listening on port %s", port)

    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    run()