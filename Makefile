#* Installation
.PHONY: install
install:
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n

#* Regenerate _pb.py from definitions under proto
.PHONY: generate_proto_definitions
generate_proto_definitions:
	rm -rf simple_grpc_py/generated
	mkdir -p simple_grpc_py/generated
	python -m grpc_tools.protoc -I proto \
		--python_out=simple_grpc_py/generated \
		--grpc_python_out=simple_grpc_py/generated \
		--mypy_out=simple_grpc_py/generated \
		./proto/simple_service/v1/simple_retry_api.proto
	# https://github.com/cpcloud/protoletariat#motivation
	protol \
	--create-package \
	--in-place \
	--python-out simple_grpc_py/generated \
	protoc --proto-path=proto simple_service/v1/simple_retry_api.proto