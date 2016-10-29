.DEFAULT_GOAL_NAME := help

.PHONY: help
help:
	@unmake $(MAKEFILE_LIST)

.PHONY: server
server:
	echo "Admin site url: http://127.0.0.1:15672"
	rabbitmq-server

.PHONY: publish
publish:
	python producer.py

.PHONY: consume
consume:
	python consumer.py
