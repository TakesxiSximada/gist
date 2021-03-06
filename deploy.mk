.DEFAULT_GOAL_NAME := help


.PHONY: help
help:
	@# display usage

	@unmake $(MAKEFILE_LIST)

.PHONY: install
install:
	@# install tool chain

	bundle install --path vendor

.PHONY: sync
sync:
	@# install tool chain

	python bin/gist-sync.py *

.PHONY: list
list:
	@# list gists

	head -n 1 $$(ls */README.md)
