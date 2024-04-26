"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(simple_service/v1/simple_retry_api.proto\x12\x11simple_service.v1"b\n\x16RetriableActionRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x124\n\x0crespond_with\x18\x02 \x03(\x0b2\x1e.simple_service.v1.RespondWith"F\n\x17RetriableActionResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x17\n\x0fnumber_attempts\x18\x02 \x01(\x05""\n\x0bRespondWith\x12\x13\n\x0bstatus_code\x18\x01 \x01(\r2|\n\x0eSimpleRetryAPI\x12j\n\x0fRetriableAction\x12).simple_service.v1.RetriableActionRequest\x1a*.simple_service.v1.RetriableActionResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_service.v1.simple_retry_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_RETRIABLEACTIONREQUEST']._serialized_start = 63
    _globals['_RETRIABLEACTIONREQUEST']._serialized_end = 161
    _globals['_RETRIABLEACTIONRESPONSE']._serialized_start = 163
    _globals['_RETRIABLEACTIONRESPONSE']._serialized_end = 233
    _globals['_RESPONDWITH']._serialized_start = 235
    _globals['_RESPONDWITH']._serialized_end = 269
    _globals['_SIMPLERETRYAPI']._serialized_start = 271
    _globals['_SIMPLERETRYAPI']._serialized_end = 395