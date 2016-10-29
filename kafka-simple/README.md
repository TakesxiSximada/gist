# [kafka] Apache KafkaをOSX上で起動する

## インストール

```
n############################## 100.0%
==> Pouring zookeeper-3.4.8.yosemite.bottle.tar.gz
==> Caveats
To have launchd start zookeeper now and restart at login:
brew services start zookeeper
Or, if you don't want/need a background service you can just run:
zkServer start
==> Summary
🍺  /usr/local/$ brew install kafka
```

zookeeperもinstallされます。


## zookeeperの起動

```
$ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper ... STARTED
```

## kafkaの起動

homebrewでkafkaをインストールすると/usr/local/etc/kafka/server.propertiesに設定ファイルが作られます。
そのままこの設定ファイルを使い起動してみます。


```
$ kafka-server-start /usr/local/etc/kafka/server.properties
[2016-10-29 20:28:58,215] INFO KafkaConfig values:
        advertised.host.name = null
        metric.reporters = []
        quota.producer.default = 9223372036854775807
        offsets.topic.num.partitions = 50
        log.flush.interval.messages = 9223372036854775807
        auto.create.topics.enable = true
        controller.socket.timeout.ms = 30000
        log.flush.interval.ms = null
        principal.builder.class = class org.apache.kafka.common.security.auth.DefaultPrincipalBuilder
        replica.socket.receive.buffer.bytes = 65536
        min.insync.replicas = 1
        replica.fetch.wait.max.ms = 500
        num.recovery.threads.per.data.dir = 1
        ssl.keystore.type = JKS
        sasl.mechanism.inter.broker.protocol = GSSAPI
        default.replication.factor = 1
        ssl.truststore.password = null
        log.preallocate = false
        sasl.kerberos.principal.to.local.rules = [DEFAULT]
        fetch.purgatory.purge.interval.requests = 1000
        ssl.endpoint.identification.algorithm = null
        replica.socket.timeout.ms = 30000
        message.max.bytes = 1000012
        num.io.threads = 8
        offsets.commit.required.acks = -1
        log.flush.offset.checkpoint.interval.ms = 60000
        delete.topic.enable = false
        quota.window.size.seconds = 1
        ssl.truststore.type = JKS
        offsets.commit.timeout.ms = 5000
        quota.window.num = 11
        zookeeper.connect = localhost:2181
        authorizer.class.name =
        num.replica.fetchers = 1
        log.retention.ms = null
        log.roll.jitter.hours = 0
        log.cleaner.enable = true
        offsets.load.buffer.size = 5242880
        log.cleaner.delete.retention.ms = 86400000
        ssl.client.auth = none
        controlled.shutdown.max.retries = 3
        queued.max.requests = 500
        offsets.topic.replication.factor = 3
        log.cleaner.threads = 1
        sasl.kerberos.service.name = null
        sasl.kerberos.ticket.renew.jitter = 0.05
        socket.request.max.bytes = 104857600
        ssl.trustmanager.algorithm = PKIX
        zookeeper.session.timeout.ms = 6000
        log.retention.bytes = -1
        log.message.timestamp.type = CreateTime
        sasl.kerberos.min.time.before.relogin = 60000
        zookeeper.set.acl = false
        connections.max.idle.ms = 600000
        offsets.retention.minutes = 1440
        replica.fetch.backoff.ms = 1000
        inter.broker.protocol.version = 0.10.0-IV1
        log.retention.hours = 168
        num.partitions = 1
        broker.id.generation.enable = true
        listeners = null
        ssl.provider = null
        ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
        log.roll.ms = null
        log.flush.scheduler.interval.ms = 9223372036854775807
        ssl.cipher.suites = null
        log.index.size.max.bytes = 10485760
        ssl.keymanager.algorithm = SunX509
        security.inter.broker.protocol = PLAINTEXT
        replica.fetch.max.bytes = 1048576
        advertised.port = null
        log.cleaner.dedupe.buffer.size = 134217728
        replica.high.watermark.checkpoint.interval.ms = 5000
        log.cleaner.io.buffer.size = 524288
        sasl.kerberos.ticket.renew.window.factor = 0.8
        zookeeper.connection.timeout.ms = 6000
        controlled.shutdown.retry.backoff.ms = 5000
        log.roll.hours = 168
        log.cleanup.policy = delete
        host.name =
        log.roll.jitter.ms = null
        max.connections.per.ip = 2147483647
        offsets.topic.segment.bytes = 104857600
        background.threads = 10
        quota.consumer.default = 9223372036854775807
        request.timeout.ms = 30000
        log.message.format.version = 0.10.0-IV1
        log.index.interval.bytes = 4096
        log.dir = /tmp/kafka-logs
        log.segment.bytes = 1073741824
        log.cleaner.backoff.ms = 15000
        offset.metadata.max.bytes = 4096
        ssl.truststore.location = null
        group.max.session.timeout.ms = 300000
        ssl.keystore.password = null
        zookeeper.sync.time.ms = 2000
        port = 9092
        log.retention.minutes = null
        log.segment.delete.delay.ms = 60000
        log.dirs = /usr/local/var/lib/kafka-logs
        controlled.shutdown.enable = true
        compression.type = producer
        max.connections.per.ip.overrides =
        log.message.timestamp.difference.max.ms = 9223372036854775807
        sasl.kerberos.kinit.cmd = /usr/bin/kinit
        log.cleaner.io.max.bytes.per.second = 1.7976931348623157E308
        auto.leader.rebalance.enable = true
        leader.imbalance.check.interval.seconds = 300
        log.cleaner.min.cleanable.ratio = 0.5
        replica.lag.time.max.ms = 10000
        num.network.threads = 3
        ssl.key.password = null
        reserved.broker.max.id = 1000
        metrics.num.samples = 2
        socket.send.buffer.bytes = 102400
        ssl.protocol = TLS
        socket.receive.buffer.bytes = 102400
        ssl.keystore.location = null
        replica.fetch.min.bytes = 1
        broker.rack = null
        unclean.leader.election.enable = true
        sasl.enabled.mechanisms = [GSSAPI]
        group.min.session.timeout.ms = 6000
        log.cleaner.io.buffer.load.factor = 0.9
        offsets.retention.check.interval.ms = 600000
        producer.purgatory.purge.interval.requests = 1000
        metrics.sample.window.ms = 30000
        broker.id = 0
        offsets.topic.compression.codec = 0
        log.retention.check.interval.ms = 300000
        advertised.listeners = null
        leader.imbalance.per.broker.percentage = 10
 (kafka.server.KafkaConfig)
[2016-10-29 20:28:58,278] INFO starting (kafka.server.KafkaServer)
[2016-10-29 20:28:58,285] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2016-10-29 20:28:58,299] INFO Starting ZkClient event thread. (org.I0Itec.zkclient.ZkEventThread)
[2016-10-29 20:28:58,337] INFO Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,337] INFO Client environment:host.name=10.27.16.113 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,337] INFO Client environment:java.version=1.8.0_45 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,337] INFO Client environment:java.vendor=Oracle Corporation (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,338] INFO Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,338] INFO Client environment:java.class.path=:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/aopalliance-repackaged-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/argparse4j-0.5.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-api-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-file-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-json-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-runtime-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/guava-18.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-api-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-locator-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-utils-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-annotations-2.6.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-core-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-databind-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-base-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-json-provider-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-module-jaxb-annotations-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javassist-3.18.2-GA.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.annotation-api-1.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.servlet-api-3.1.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.ws.rs-api-2.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-client-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-common-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-core-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-guava-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-media-jaxb-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-server-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-continuation-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-http-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-io-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-security-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-server-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlet-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlets-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-util-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jopt-simple-4.9.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-clients-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-log4j-appender-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-examples-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-tools-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-test-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/log4j-1.2.17.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/lz4-1.3.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/metrics-core-2.2.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/osgi-resource-locator-1.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/reflections-0.9.10.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/rocksdbjni-4.8.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-library-2.11.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-parser-combinators_2.11-1.0.4.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-api-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-log4j12-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/snappy-java-1.1.2.6.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/validation-api-1.1.0.Final.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zkclient-0.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zookeeper-3.4.6.jar (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,340] INFO Client environment:java.io.tmpdir=/var/folders/hx/xp4thw0x7rj15r_2w57_wvfh0000gn/T/ (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,340] INFO Client environment:java.compiler=<NA> (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,341] INFO Client environment:os.name=Mac OS X (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,341] INFO Client environment:os.arch=x86_64 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,341] INFO Client environment:os.version=10.10.5 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,343] INFO Initiating client connection, connectString=localhost:2181 sessionTimeout=6000 watcher=org.I0Itec.zkclient.ZkClient@35047d03 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:28:58,361] INFO Waiting for keeper state SyncConnected (org.I0Itec.zkclient.ZkClient)
[2016-10-29 20:28:58,363] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:28:58,441] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:28:58,547] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:28:58,548] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:28:59,652] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:28:59,652] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:28:59,758] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:28:59,759] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:00,866] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:00,867] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:00,968] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:00,969] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:02,072] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:02,072] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:02,173] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:02,174] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:03,279] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:03,280] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:03,381] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:03,382] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
[2016-10-29 20:29:04,365] INFO Terminate ZkClient event thread. (org.I0Itec.zkclient.ZkEventThread)
[2016-10-29 20:29:04,491] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:04,600] INFO Session: 0x0 closed (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:29:04,600] INFO EventThread shut down (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:29:04,602] FATAL Fatal error during KafkaServer startup. Prepare to shutdown (kafka.server.KafkaServer)
org.I0Itec.zkclient.exception.ZkTimeoutException: Unable to connect to zookeeper server within timeout: 6000
        at org.I0Itec.zkclient.ZkClient.connect(ZkClient.java:1232)
        at org.I0Itec.zkclient.ZkClient.<init>(ZkClient.java:156)
        at org.I0Itec.zkclient.ZkClient.<init>(ZkClient.java:130)
        at kafka.utils.ZkUtils$.createZkClientAndConnection(ZkUtils.scala:75)
        at kafka.utils.ZkUtils$.apply(ZkUtils.scala:57)
        at kafka.server.KafkaServer.initZk(KafkaServer.scala:294)
        at kafka.server.KafkaServer.startup(KafkaServer.scala:180)
        at kafka.server.KafkaServerStartable.startup(KafkaServerStartable.scala:37)
        at kafka.Kafka$.main(Kafka.scala:67)
        at kafka.Kafka.main(Kafka.scala)
[2016-10-29 20:29:04,603] INFO shutting down (kafka.server.KafkaServer)
[2016-10-29 20:29:04,610] INFO shut down completed (kafka.server.KafkaServer)
[2016-10-29 20:29:04,610] FATAL Fatal error during KafkaServerStartable startup. Prepare to shutdown (kafka.server.KafkaServerStartable)
org.I0Itec.zkclient.exception.ZkTimeoutException: Unable to connect to zookeeper server within timeout: 6000
        at org.I0Itec.zkclient.ZkClient.connect(ZkClient.java:1232)
        at org.I0Itec.zkclient.ZkClient.<init>(ZkClient.java:156)
        at org.I0Itec.zkclient.ZkClient.<init>(ZkClient.java:130)
        at kafka.utils.ZkUtils$.createZkClientAndConnection(ZkUtils.scala:75)
        at kafka.utils.ZkUtils$.apply(ZkUtils.scala:57)
        at kafka.server.KafkaServer.initZk(KafkaServer.scala:294)
        at kafka.server.KafkaServer.startup(KafkaServer.scala:180)
        at kafka.server.KafkaServerStartable.startup(KafkaServerStartable.scala:37)
        at kafka.Kafka$.main(Kafka.scala:67)
        at kafka.Kafka.main(Kafka.scala)
[2016-10-29 20:29:04,611] INFO shutting down (kafka.server.KafkaServer)

```

停止してしまいました。うーん。


最初のWARNINGは次のメッセージのようです。

```
[2016-10-29 20:28:58,441] WARN Session 0x0 for server null, unexpected error, closing socket connection and attempting reconnect (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:717)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:361)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1081)
```

どうやらzookeeperに繋げないようです。

```
$ zkServer status
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Error contacting service. It is probably not running.
```

どうやらzookeeperが起動していないようです。zookeeperのログを確認します。

```
$ cat /usr/local/var/log/zookeeper/zookeeper.log
$
```

何も出ていません。`zkServer start-foreground`でデーモン化しないようにして実行します。

```
$ zkServer start-foreground
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg

```

うーん、実行できているみたいです。
プロセスを確認してみます。

```
$ ps -ef | grep zoo
  501  3640  3639   0  8:38PM ttys003    0:00.81 /Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/bin/java -Dzookeeper.log.dir=. -Dzookeeper.root.logger=INFO,CONSOLE -cp /usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../build/classes:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../build/lib/*.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/slf4j-log4j12-1.6.1.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/slf4j-api-1.6.1.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/netty-3.7.0.Final.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/log4j-1.2.16.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/jline-0.9.94.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../zookeeper-3.4.8.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../src/java/lib/*.jar:/usr/local/etc/zookeeper: -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/local/etc/zookeeper/zoo.cfg
  501  3917  3686   0  8:40PM ttys004    0:00.00 grep --color zoo
```

起動していますね。この状態でkafkaを起動してみます。

```
$ kafka-server-start /usr/local/etc/kafka/server.properties
[2016-10-29 20:42:00,392] INFO KafkaConfig values:
        advertised.host.name = null
        metric.reporters = []
        quota.producer.default = 9223372036854775807
        offsets.topic.num.partitions = 50
        log.flush.interval.messages = 9223372036854775807
        auto.create.topics.enable = true
        controller.socket.timeout.ms = 30000
        log.flush.interval.ms = null
        principal.builder.class = class org.apache.kafka.common.security.auth.DefaultPrincipalBuilder
        replica.socket.receive.buffer.bytes = 65536
        min.insync.replicas = 1
        replica.fetch.wait.max.ms = 500
        num.recovery.threads.per.data.dir = 1
        ssl.keystore.type = JKS
        sasl.mechanism.inter.broker.protocol = GSSAPI
        default.replication.factor = 1
        ssl.truststore.password = null
        log.preallocate = false
        sasl.kerberos.principal.to.local.rules = [DEFAULT]
        fetch.purgatory.purge.interval.requests = 1000
        ssl.endpoint.identification.algorithm = null
        replica.socket.timeout.ms = 30000
        message.max.bytes = 1000012
        num.io.threads = 8
        offsets.commit.required.acks = -1
        log.flush.offset.checkpoint.interval.ms = 60000
        delete.topic.enable = false
        quota.window.size.seconds = 1
        ssl.truststore.type = JKS
        offsets.commit.timeout.ms = 5000
        quota.window.num = 11
        zookeeper.connect = localhost:2181
        authorizer.class.name =
        num.replica.fetchers = 1
        log.retention.ms = null
        log.roll.jitter.hours = 0
        log.cleaner.enable = true
        offsets.load.buffer.size = 5242880
        log.cleaner.delete.retention.ms = 86400000
        ssl.client.auth = none
        controlled.shutdown.max.retries = 3
        queued.max.requests = 500
        offsets.topic.replication.factor = 3
        log.cleaner.threads = 1
        sasl.kerberos.service.name = null
        sasl.kerberos.ticket.renew.jitter = 0.05
        socket.request.max.bytes = 104857600
        ssl.trustmanager.algorithm = PKIX
        zookeeper.session.timeout.ms = 6000
        log.retention.bytes = -1
        log.message.timestamp.type = CreateTime
        sasl.kerberos.min.time.before.relogin = 60000
        zookeeper.set.acl = false
        connections.max.idle.ms = 600000
        offsets.retention.minutes = 1440
        replica.fetch.backoff.ms = 1000
        inter.broker.protocol.version = 0.10.0-IV1
        log.retention.hours = 168
        num.partitions = 1
        broker.id.generation.enable = true
        listeners = null
        ssl.provider = null
        ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
        log.roll.ms = null
        log.flush.scheduler.interval.ms = 9223372036854775807
        ssl.cipher.suites = null
        log.index.size.max.bytes = 10485760
        ssl.keymanager.algorithm = SunX509
        security.inter.broker.protocol = PLAINTEXT
        replica.fetch.max.bytes = 1048576
        advertised.port = null
        log.cleaner.dedupe.buffer.size = 134217728
        replica.high.watermark.checkpoint.interval.ms = 5000
        log.cleaner.io.buffer.size = 524288
        sasl.kerberos.ticket.renew.window.factor = 0.8
        zookeeper.connection.timeout.ms = 6000
        controlled.shutdown.retry.backoff.ms = 5000
        log.roll.hours = 168
        log.cleanup.policy = delete
        host.name =
        log.roll.jitter.ms = null
        max.connections.per.ip = 2147483647
        offsets.topic.segment.bytes = 104857600
        background.threads = 10
        quota.consumer.default = 9223372036854775807
        request.timeout.ms = 30000
        log.message.format.version = 0.10.0-IV1
        log.index.interval.bytes = 4096
        log.dir = /tmp/kafka-logs
        log.segment.bytes = 1073741824
        log.cleaner.backoff.ms = 15000
        offset.metadata.max.bytes = 4096
        ssl.truststore.location = null
        group.max.session.timeout.ms = 300000
        ssl.keystore.password = null
        zookeeper.sync.time.ms = 2000
        port = 9092
        log.retention.minutes = null
        log.segment.delete.delay.ms = 60000
        log.dirs = /usr/local/var/lib/kafka-logs
        controlled.shutdown.enable = true
        compression.type = producer
        max.connections.per.ip.overrides =
        log.message.timestamp.difference.max.ms = 9223372036854775807
        sasl.kerberos.kinit.cmd = /usr/bin/kinit
        log.cleaner.io.max.bytes.per.second = 1.7976931348623157E308
        auto.leader.rebalance.enable = true
        leader.imbalance.check.interval.seconds = 300
        log.cleaner.min.cleanable.ratio = 0.5
        replica.lag.time.max.ms = 10000
        num.network.threads = 3
        ssl.key.password = null
        reserved.broker.max.id = 1000
        metrics.num.samples = 2
        socket.send.buffer.bytes = 102400
        ssl.protocol = TLS
        socket.receive.buffer.bytes = 102400
        ssl.keystore.location = null
        replica.fetch.min.bytes = 1
        broker.rack = null
        unclean.leader.election.enable = true
        sasl.enabled.mechanisms = [GSSAPI]
        group.min.session.timeout.ms = 6000
        log.cleaner.io.buffer.load.factor = 0.9
        offsets.retention.check.interval.ms = 600000
        producer.purgatory.purge.interval.requests = 1000
        metrics.sample.window.ms = 30000
        broker.id = 0
        offsets.topic.compression.codec = 0
        log.retention.check.interval.ms = 300000
        advertised.listeners = null
        leader.imbalance.per.broker.percentage = 10
 (kafka.server.KafkaConfig)
[2016-10-29 20:42:00,482] INFO starting (kafka.server.KafkaServer)
[2016-10-29 20:42:00,492] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2016-10-29 20:42:00,504] INFO Starting ZkClient event thread. (org.I0Itec.zkclient.ZkEventThread)
[2016-10-29 20:42:00,532] INFO Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,532] INFO Client environment:host.name=10.27.16.113 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,532] INFO Client environment:java.version=1.8.0_45 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,532] INFO Client environment:java.vendor=Oracle Corporation (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,532] INFO Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,533] INFO Client environment:java.class.path=:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/aopalliance-repackaged-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/argparse4j-0.5.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-api-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-file-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-json-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-runtime-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/guava-18.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-api-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-locator-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-utils-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-annotations-2.6.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-core-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-databind-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-base-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-json-provider-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-module-jaxb-annotations-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javassist-3.18.2-GA.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.annotation-api-1.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.servlet-api-3.1.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.ws.rs-api-2.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-client-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-common-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-core-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-guava-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-media-jaxb-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-server-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-continuation-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-http-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-io-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-security-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-server-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlet-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlets-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-util-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jopt-simple-4.9.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-clients-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-log4j-appender-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-examples-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-tools-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-test-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/log4j-1.2.17.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/lz4-1.3.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/metrics-core-2.2.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/osgi-resource-locator-1.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/reflections-0.9.10.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/rocksdbjni-4.8.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-library-2.11.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-parser-combinators_2.11-1.0.4.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-api-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-log4j12-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/snappy-java-1.1.2.6.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/validation-api-1.1.0.Final.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zkclient-0.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zookeeper-3.4.6.jar (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,536] INFO Client environment:java.io.tmpdir=/var/folders/hx/xp4thw0x7rj15r_2w57_wvfh0000gn/T/ (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,536] INFO Client environment:java.compiler=<NA> (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,536] INFO Client environment:os.name=Mac OS X (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,536] INFO Client environment:os.arch=x86_64 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,536] INFO Client environment:os.version=10.10.5 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,537] INFO Initiating client connection, connectString=localhost:2181 sessionTimeout=6000 watcher=org.I0Itec.zkclient.ZkClient@35047d03 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 20:42:00,555] INFO Waiting for keeper state SyncConnected (org.I0Itec.zkclient.ZkClient)
[2016-10-29 20:42:00,558] INFO Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:42:00,634] INFO Socket connection established to localhost/127.0.0.1:2181, initiating session (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:42:01,098] INFO Session establishment complete on server localhost/127.0.0.1:2181, sessionid = 0x158103bfadf0000, negotiated timeout = 6000 (org.apache.zookeeper.ClientCnxn)
[2016-10-29 20:42:01,100] INFO zookeeper state changed (SyncConnected) (org.I0Itec.zkclient.ZkClient)
[2016-10-29 20:42:01,441] INFO Log directory '/usr/local/var/lib/kafka-logs' not found, creating it. (kafka.log.LogManager)
[2016-10-29 20:42:01,696] INFO Loading logs. (kafka.log.LogManager)
[2016-10-29 20:42:01,729] INFO Logs loading complete. (kafka.log.LogManager)
[2016-10-29 20:42:01,952] INFO Starting log cleanup with a period of 300000 ms. (kafka.log.LogManager)
[2016-10-29 20:42:01,956] INFO Starting log flusher with a default period of 9223372036854775807 ms. (kafka.log.LogManager)
[2016-10-29 20:42:01,962] WARN No meta.properties file under dir /usr/local/var/lib/kafka-logs/meta.properties (kafka.server.BrokerMetadataCheckpoint)
[2016-10-29 20:42:02,238] INFO Awaiting socket connections on 0.0.0.0:9092. (kafka.network.Acceptor)
[2016-10-29 20:42:02,259] INFO [Socket Server on Broker 0], Started 1 acceptor threads (kafka.network.SocketServer)
[2016-10-29 20:42:02,356] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 20:42:02,358] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 20:42:02,574] INFO Creating /controller (is it secure? false) (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 20:42:02,599] INFO Result of znode creation is: OK (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 20:42:02,600] INFO 0 successfully elected as leader (kafka.server.ZookeeperLeaderElector)
[2016-10-29 20:42:02,812] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 20:42:02,813] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 20:42:02,885] INFO [GroupCoordinator 0]: Starting up. (kafka.coordinator.GroupCoordinator)
[2016-10-29 20:42:02,886] INFO [GroupCoordinator 0]: Startup complete. (kafka.coordinator.GroupCoordinator)
[2016-10-29 20:42:02,999] INFO [Group Metadata Manager on Broker 0]: Removed 0 expired offsets in 124 milliseconds. (kafka.coordinator.GroupMetadataManager)
[2016-10-29 20:42:03,044] INFO [ThrottledRequestReaper-Produce], Starting  (kafka.server.ClientQuotaManager$ThrottledRequestReaper)
[2016-10-29 20:42:03,047] INFO [ThrottledRequestReaper-Fetch], Starting  (kafka.server.ClientQuotaManager$ThrottledRequestReaper)
[2016-10-29 20:42:03,100] INFO Will not load MX4J, mx4j-tools.jar is not in the classpath (kafka.utils.Mx4jLoader$)
[2016-10-29 20:42:03,158] INFO Creating /brokers/ids/0 (is it secure? false) (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 20:42:03,163] INFO Result of znode creation is: OK (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 20:42:03,169] INFO Registered broker 0 at path /brokers/ids/0 with addresses: PLAINTEXT -> EndPoint(10.27.16.113,9092,PLAINTEXT) (kafka.utils.ZkUtils)
[2016-10-29 20:42:03,181] WARN No meta.properties file under dir /usr/local/var/lib/kafka-logs/meta.properties (kafka.server.BrokerMetadataCheckpoint)
[2016-10-29 20:42:03,266] INFO New leader is 0 (kafka.server.ZookeeperLeaderElector$LeaderChangeListener)
[2016-10-29 20:42:03,379] INFO Kafka version : 0.10.0.1 (org.apache.kafka.common.utils.AppInfoParser)
[2016-10-29 20:42:03,379] INFO Kafka commitId : a7a17cdec9eaa6c5 (org.apache.kafka.common.utils.AppInfoParser)
[2016-10-29 20:42:03,381] INFO [Kafka Server 0], started (kafka.server.KafkaServer)

```

起動しました。やはりzookeeperの問題のようです。zookeeperが起動しない理由を調査します。
zookeeperはstart-foregroundでは起動したのにstartでは起動しませんでした。

zookeeerの起動スクリプトを確認します。

```
$ cat /usr/local/bin/zkServer
#!/usr/bin/env bash
. "/usr/local/etc/zookeeper/defaults"
cd "/usr/local/Cellar/zookeeper/3.4.8/libexec/bin"
./zkServer.sh "$@"
```

zookeeperのversionは3.4.8のようです。zookeeperはhomebrewでインストールしています。複数インストールされておかしな状況になってないか確認します。

```
$ ls /usr/local/Cellar/zookeeper/
3.4.8
$
```

うーん、一個だけですね。

```
 $ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper ... STARTED
(py3.5.2) $ ps -ef | grep zook
  501  5915     1   0  9:06PM ttys006    0:01.07 /Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/bin/java -Dzookeeper.log.dir=. -Dzookeeper.root.logger=INFO,CONSOLE -cp /usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../build/classes:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../build/lib/*.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/slf4j-log4j12-1.6.1.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/slf4j-api-1.6.1.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/netty-3.7.0.Final.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/log4j-1.2.16.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../lib/jline-0.9.94.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../zookeeper-3.4.8.jar:/usr/local/Cellar/zookeeper/3.4.8/libexec/bin/../src/java/lib/*.jar:/usr/local/etc/zookeeper: -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/local/etc/zookeeper/zoo.cfg
  501  5923  4759   0  9:06PM ttys006    0:00.00 grep --color zook

```

あれ、何かわからないけど起動してしまいました。やったことといえばターミナルを起動しなおしたぐらいです。
では気を取り直してkafkaを再度起動します。

```
$ kafka-server-start /usr/local/etc/kafka/server.properties
[2016-10-29 21:09:33,224] INFO KafkaConfig values:
	advertised.host.name = null
	metric.reporters = []
	quota.producer.default = 9223372036854775807
	offsets.topic.num.partitions = 50
	log.flush.interval.messages = 9223372036854775807
	auto.create.topics.enable = true
	controller.socket.timeout.ms = 30000
	log.flush.interval.ms = null
	principal.builder.class = class org.apache.kafka.common.security.auth.DefaultPrincipalBuilder
	replica.socket.receive.buffer.bytes = 65536
	min.insync.replicas = 1
	replica.fetch.wait.max.ms = 500
	num.recovery.threads.per.data.dir = 1
	ssl.keystore.type = JKS
	sasl.mechanism.inter.broker.protocol = GSSAPI
	default.replication.factor = 1
	ssl.truststore.password = null
	log.preallocate = false
	sasl.kerberos.principal.to.local.rules = [DEFAULT]
	fetch.purgatory.purge.interval.requests = 1000
	ssl.endpoint.identification.algorithm = null
	replica.socket.timeout.ms = 30000
	message.max.bytes = 1000012
	num.io.threads = 8
	offsets.commit.required.acks = -1
	log.flush.offset.checkpoint.interval.ms = 60000
	delete.topic.enable = false
	quota.window.size.seconds = 1
	ssl.truststore.type = JKS
	offsets.commit.timeout.ms = 5000
	quota.window.num = 11
	zookeeper.connect = localhost:2181
	authorizer.class.name =
	num.replica.fetchers = 1
	log.retention.ms = null
	log.roll.jitter.hours = 0
	log.cleaner.enable = true
	offsets.load.buffer.size = 5242880
	log.cleaner.delete.retention.ms = 86400000
	ssl.client.auth = none
	controlled.shutdown.max.retries = 3
	queued.max.requests = 500
	offsets.topic.replication.factor = 3
	log.cleaner.threads = 1
	sasl.kerberos.service.name = null
	sasl.kerberos.ticket.renew.jitter = 0.05
	socket.request.max.bytes = 104857600
	ssl.trustmanager.algorithm = PKIX
	zookeeper.session.timeout.ms = 6000
	log.retention.bytes = -1
	log.message.timestamp.type = CreateTime
	sasl.kerberos.min.time.before.relogin = 60000
	zookeeper.set.acl = false
	connections.max.idle.ms = 600000
	offsets.retention.minutes = 1440
	replica.fetch.backoff.ms = 1000
	inter.broker.protocol.version = 0.10.0-IV1
	log.retention.hours = 168
	num.partitions = 1
	broker.id.generation.enable = true
	listeners = null
	ssl.provider = null
	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
	log.roll.ms = null
	log.flush.scheduler.interval.ms = 9223372036854775807
	ssl.cipher.suites = null
	log.index.size.max.bytes = 10485760
	ssl.keymanager.algorithm = SunX509
	security.inter.broker.protocol = PLAINTEXT
	replica.fetch.max.bytes = 1048576
	advertised.port = null
	log.cleaner.dedupe.buffer.size = 134217728
	replica.high.watermark.checkpoint.interval.ms = 5000
	log.cleaner.io.buffer.size = 524288
	sasl.kerberos.ticket.renew.window.factor = 0.8
	zookeeper.connection.timeout.ms = 6000
	controlled.shutdown.retry.backoff.ms = 5000
	log.roll.hours = 168
	log.cleanup.policy = delete
	host.name =
	log.roll.jitter.ms = null
	max.connections.per.ip = 2147483647
	offsets.topic.segment.bytes = 104857600
	background.threads = 10
	quota.consumer.default = 9223372036854775807
	request.timeout.ms = 30000
	log.message.format.version = 0.10.0-IV1
	log.index.interval.bytes = 4096
	log.dir = /tmp/kafka-logs
	log.segment.bytes = 1073741824
	log.cleaner.backoff.ms = 15000
	offset.metadata.max.bytes = 4096
	ssl.truststore.location = null
	group.max.session.timeout.ms = 300000
	ssl.keystore.password = null
	zookeeper.sync.time.ms = 2000
	port = 9092
	log.retention.minutes = null
	log.segment.delete.delay.ms = 60000
	log.dirs = /usr/local/var/lib/kafka-logs
	controlled.shutdown.enable = true
	compression.type = producer
	max.connections.per.ip.overrides =
	log.message.timestamp.difference.max.ms = 9223372036854775807
	sasl.kerberos.kinit.cmd = /usr/bin/kinit
	log.cleaner.io.max.bytes.per.second = 1.7976931348623157E308
	auto.leader.rebalance.enable = true
	leader.imbalance.check.interval.seconds = 300
	log.cleaner.min.cleanable.ratio = 0.5
	replica.lag.time.max.ms = 10000
	num.network.threads = 3
	ssl.key.password = null
	reserved.broker.max.id = 1000
	metrics.num.samples = 2
	socket.send.buffer.bytes = 102400
	ssl.protocol = TLS
	socket.receive.buffer.bytes = 102400
	ssl.keystore.location = null
	replica.fetch.min.bytes = 1
	broker.rack = null
	unclean.leader.election.enable = true
	sasl.enabled.mechanisms = [GSSAPI]
	group.min.session.timeout.ms = 6000
	log.cleaner.io.buffer.load.factor = 0.9
	offsets.retention.check.interval.ms = 600000
	producer.purgatory.purge.interval.requests = 1000
	metrics.sample.window.ms = 30000
	broker.id = 0
	offsets.topic.compression.codec = 0
	log.retention.check.interval.ms = 300000
	advertised.listeners = null
	leader.imbalance.per.broker.percentage = 10
 (kafka.server.KafkaConfig)
[2016-10-29 21:09:35,045] INFO starting (kafka.server.KafkaServer)
[2016-10-29 21:09:35,366] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2016-10-29 21:09:35,819] INFO Starting ZkClient event thread. (org.I0Itec.zkclient.ZkEventThread)
[2016-10-29 21:09:35,947] INFO Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,947] INFO Client environment:host.name=10.27.16.113 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,947] INFO Client environment:java.version=1.8.0_45 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:java.vendor=Oracle Corporation (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:java.home=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:java.class.path=:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/aopalliance-repackaged-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/argparse4j-0.5.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-api-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-file-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-json-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/connect-runtime-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/guava-18.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-api-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-locator-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/hk2-utils-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-annotations-2.6.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-core-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-databind-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-base-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-jaxrs-json-provider-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jackson-module-jaxb-annotations-2.6.3.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javassist-3.18.2-GA.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.annotation-api-1.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.inject-2.4.0-b34.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.servlet-api-3.1.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/javax.ws.rs-api-2.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-client-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-common-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-container-servlet-core-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-guava-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-media-jaxb-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jersey-server-2.22.2.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-continuation-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-http-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-io-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-security-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-server-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlet-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-servlets-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jetty-util-9.2.15.v20160210.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/jopt-simple-4.9.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-clients-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-log4j-appender-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-streams-examples-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka-tools-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1-test-sources.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/kafka_2.11-0.10.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/log4j-1.2.17.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/lz4-1.3.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/metrics-core-2.2.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/osgi-resource-locator-1.0.1.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/reflections-0.9.10.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/rocksdbjni-4.8.0.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-library-2.11.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/scala-parser-combinators_2.11-1.0.4.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-api-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/slf4j-log4j12-1.7.21.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/snappy-java-1.1.2.6.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/validation-api-1.1.0.Final.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zkclient-0.8.jar:/usr/local/Cellar/kafka/0.10.0.1/libexec/bin/../libs/zookeeper-3.4.6.jar (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:java.io.tmpdir=/var/folders/hx/xp4thw0x7rj15r_2w57_wvfh0000gn/T/ (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:java.compiler=<NA> (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:os.name=Mac OS X (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:os.arch=x86_64 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,948] INFO Client environment:os.version=10.10.5 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:35,950] INFO Initiating client connection, connectString=localhost:2181 sessionTimeout=6000 watcher=org.I0Itec.zkclient.ZkClient@35047d03 (org.apache.zookeeper.ZooKeeper)
[2016-10-29 21:09:36,099] INFO Waiting for keeper state SyncConnected (org.I0Itec.zkclient.ZkClient)
[2016-10-29 21:09:36,144] INFO Opening socket connection to server localhost/0:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknown error) (org.apache.zookeeper.ClientCnxn)
[2016-10-29 21:09:37,153] INFO Socket connection established to localhost/0:0:0:0:0:0:0:1:2181, initiating session (org.apache.zookeeper.ClientCnxn)
[2016-10-29 21:09:37,413] INFO Session establishment complete on server localhost/0:0:0:0:0:0:0:1:2181, sessionid = 0x1581055d24a0000, negotiated timeout = 6000 (org.apache.zookeeper.ClientCnxn)
[2016-10-29 21:09:37,416] INFO zookeeper state changed (SyncConnected) (org.I0Itec.zkclient.ZkClient)
[2016-10-29 21:09:38,900] INFO Loading logs. (kafka.log.LogManager)
[2016-10-29 21:09:39,065] INFO Logs loading complete. (kafka.log.LogManager)
[2016-10-29 21:09:39,845] INFO Starting log cleanup with a period of 300000 ms. (kafka.log.LogManager)
[2016-10-29 21:09:39,932] INFO Starting log flusher with a default period of 9223372036854775807 ms. (kafka.log.LogManager)
[2016-10-29 21:09:40,847] INFO Awaiting socket connections on 0.0.0.0:9092. (kafka.network.Acceptor)
[2016-10-29 21:09:40,864] INFO [Socket Server on Broker 0], Started 1 acceptor threads (kafka.network.SocketServer)
[2016-10-29 21:09:41,470] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 21:09:41,471] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 21:09:42,492] INFO Creating /controller (is it secure? false) (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 21:09:42,562] INFO Result of znode creation is: OK (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 21:09:42,563] INFO 0 successfully elected as leader (kafka.server.ZookeeperLeaderElector)
[2016-10-29 21:09:43,234] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 21:09:43,236] INFO [ExpirationReaper-0], Starting  (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2016-10-29 21:09:43,465] INFO [GroupCoordinator 0]: Starting up. (kafka.coordinator.GroupCoordinator)
[2016-10-29 21:09:43,466] INFO [GroupCoordinator 0]: Startup complete. (kafka.coordinator.GroupCoordinator)
[2016-10-29 21:09:43,731] INFO [Group Metadata Manager on Broker 0]: Removed 0 expired offsets in 319 milliseconds. (kafka.coordinator.GroupMetadataManager)
[2016-10-29 21:09:43,777] INFO [ThrottledRequestReaper-Produce], Starting  (kafka.server.ClientQuotaManager$ThrottledRequestReaper)
[2016-10-29 21:09:43,778] INFO [ThrottledRequestReaper-Fetch], Starting  (kafka.server.ClientQuotaManager$ThrottledRequestReaper)
[2016-10-29 21:09:43,845] INFO Will not load MX4J, mx4j-tools.jar is not in the classpath (kafka.utils.Mx4jLoader$)
[2016-10-29 21:09:43,998] INFO Creating /brokers/ids/0 (is it secure? false) (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 21:09:44,084] INFO Result of znode creation is: OK (kafka.utils.ZKCheckedEphemeral)
[2016-10-29 21:09:44,100] INFO Registered broker 0 at path /brokers/ids/0 with addresses: PLAINTEXT -> EndPoint(10.27.16.113,9092,PLAINTEXT) (kafka.utils.ZkUtils)
[2016-10-29 21:09:44,534] INFO Kafka version : 0.10.0.1 (org.apache.kafka.common.utils.AppInfoParser)
[2016-10-29 21:09:44,534] INFO Kafka commitId : a7a17cdec9eaa6c5 (org.apache.kafka.common.utils.AppInfoParser)
[2016-10-29 21:09:44,536] INFO [Kafka Server 0], started (kafka.server.KafkaServer)
[2016-10-29 21:09:44,559] INFO New leader is 0 (kafka.server.ZookeeperLeaderElector$LeaderChangeListener)

```
起動しました。
