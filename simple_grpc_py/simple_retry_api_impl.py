import logging
from typing import Optional

import grpc

from generated.simple_service.v1.simple_retry_api_pb2_grpc import SimpleRetryAPI
from generated.simple_service.v1.simple_retry_api_pb2 import RetriableActionRequest, RetriableActionResponse

logger = logging.getLogger(__name__)

class SimpleRetryApiImpl(SimpleRetryAPI):
    def __init__(self):
        self.attempt_map = {}

    def RetriableAction(self, request: RetriableActionRequest, context: Optional[grpc.ServicerContext], **kwargs) -> RetriableActionResponse:
        logger.info("PYTHON SERVICE IMPL****************************************")
        request_id = request.request_id
        respond_with_index = self.get_attempts_for(request_id)

        attempt_number = respond_with_index + 1
        logger.info(f"received request:\n** request_id: {request_id}\n** attempt number: {attempt_number}")

        if respond_with_index < len(request.respond_with):
            response = request.respond_with[respond_with_index]
            status_code = response.status_code
            logger.info(f"responding with {status_code}")
            respond_with_status = [x for x in grpc.StatusCode if x.value[0] == status_code][0]
            if context:
                context.abort(respond_with_status, "responding as instructed")

        logger.info("no respond_with found for attempt number  - returning successful response")
        # successful response
        return RetriableActionResponse(request_id=request_id, number_attempts=attempt_number)

    def get_attempts_for(self, request_id):
        attempt_idx = self.attempt_map.get(request_id, 0)
        self.attempt_map[request_id] = attempt_idx + 1
        return attempt_idx

