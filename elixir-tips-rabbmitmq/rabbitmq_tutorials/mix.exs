defmodule RabbitmqTutorials.Mixfile do
  use Mix.Project

  def project do
    [app: :rabbitmq_tutorials,
     version: "0.1.0",
     elixir: "~> 1.3",
     build_embedded: Mix.env == :prod,
     start_permanent: Mix.env == :prod,
     deps: deps()]
  end

  def application do
    [applications: [:logger]]
  end

  defp deps do
    [
      {:amqp_client, git: "https://github.com/jbrisbin/amqp_client.git", override: true},
      {:amqp, "~> 0.1.4"},
    ]
  end
end
