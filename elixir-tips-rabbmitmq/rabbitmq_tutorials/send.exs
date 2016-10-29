{:ok, connection} = AMQP.Connection.open
{:ok, channel} = AMQP.Channel.open connection
AMQP.Queue.declare(channel, "hello")
status = AMQP.Basic.publish(channel, "", "hello", "Hello World!")
IO.puts status
AMQP.Connection.close connection
