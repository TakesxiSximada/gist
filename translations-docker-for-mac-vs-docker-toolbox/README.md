# [翻訳] Docker for Mac vs. Docker Toolbox

https://docs.docker.com/docker-for-mac/docker-toolbox/ の翻訳です。

## Docker for Mac vs. Docker Toolbox

```
If you already have an installation of Docker Toolbox, please read these topics first to learn how Docker for Mac and Docker Toolbox differ, and how they can coexist.
```

既にDocker Toolboxのインストールをインストール済みであれば、Docker for MacとDocker Toolboxの違いと、それらの共存方法を学ぶために、最初にこれらのトピックを読んでください。

### The Docker Toolbox environment

```
Docker Toolbox installs docker, docker-compose and docker-machine in /usr/local/bin on your Mac. It also installs VirtualBox. At installation time, Toolbox uses docker-machine to provision a VirtualBox VM called default, running the boot2docker Linux distribution, with Docker Engine with certificates located on your Mac at $HOME/.docker/machine/machines/default.
```

Docker ToolboxはMacの/usr/local/bin内にdockerとdocker-composeとdocekr-machineをインストールします。またVirtualBoxもインストールします。
インストール時に、Toolboxはdocker-machineを使い、Docker Engineと証明書を$HOME/.docker/machine/machines/default配下に準備するとともに、defaultという名前でVirtualBox VMを準備し、boot2docker Linuxディストリビューションを実行します。

```
Before you use docker or docker-compose on your Mac, you typically use the command eval $(docker-machine env default) to set environment variables so that docker or docker-compose know how to talk to Docker Engine running on VirtualBox.

This setup is shown in the following diagram.
```

お使いのMac上でdockerまたはdocker-composeを使う前に、一般的には`eval $(docker-machine env default)` コマンドを使い、環境変数を設定します。その後はdockerまたはdocker-composeはVirtualBox上で実行中のDocker Engineとやりとりする方法を提供します。

この設定は、次の図に示されています。

------

ここまでで力尽きてしまった。


### The Docker for Mac environment

Docker for Mac is a Mac native application, that you install in /Applications. At installation time, it creates symlinks in /usr/local/bin for docker and docker-compose, to the version of the commands inside the Mac application bundle, in /Applications/Docker.app/Contents/Resources/bin.

Here are some key points to know about Docker for Mac before you get started:

- Docker for Mac does not use VirtualBox, but rather HyperKit, a lightweight macOS virtualization solution built on top of Hypervisor.framework in macOS 10.10 Yosemite and higher.
- Installing Docker for Mac does not affect machines you created with Docker Machine. The install offers to copy containers and images from your local default machine (if one exists) to the new Docker for Mac HyperKit VM. If chosen, content from default is copied to the new Docker for Mac HyperKit VM, and your original default machine is kept as is.
- The Docker for Mac application does not use docker-machine to provision that VM; but rather creates and manages it directly.
- At installation time, Docker for Mac provisions an HyperKit VM based on Alpine Linux, running Docker Engine. It exposes the docker API on a socket in /var/tmp/docker.sock. Since this is the default location where docker will look if no environment variables are set, you can start using docker and docker-compose without setting any environment variables.

This setup is shown in the following diagram.

With Docker for Mac, you get only one VM, and you don’t manage it. It is managed by the Docker for Mac application, which includes autoupdate to update the client and server versions of Docker.

If you need several VMs and want to manage the version of the Docker client or server you are using, you can continue to use docker-machine, on the same machine, as described in Docker Toolbox and Docker for Mac coexistence.

### Setting up to run Docker for Mac

1. Check whether Toolbox DOCKER environment variables are set:

   ```
   $ env | grep DOCKER
   DOCKER_HOST=tcp://192.168.99.100:2376
   DOCKER_MACHINE_NAME=default
   DOCKER_TLS_VERIFY=1
   DOCKER_CERT_PATH=/Users/victoriabialas/.docker/machine/machines/default
   ```

   If this command returns no output, you are ready to use Docker for Mac.
   If it returns output (as shown in the example), you need to unset the DOCKER environment variables to make the client talk to the Docker for Mac Engine (next step).

2. Run the unset command on the following DOCKER environment variables to unset them in the current shell.
