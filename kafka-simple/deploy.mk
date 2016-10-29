.PHONY:
zookeeper:
	zkServer start

.PHONY:
kafka:
	kafka-server-start /usr/local/etc/kafka/server.properties
