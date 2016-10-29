# Windows Virtual Machineをインストールする

OS Xを使っているとIEやEdgeが動作しないので動作確認できません。
しかしMicrosoftはWindowsが動作する仮想マシンのイメージ(以前はMordern.IEと呼ばれていた)を配布していますので、そちらを使うことで実機がなくても確認できます。
今回はVirtualbox用のイメージをダウンロードして使います。(Virtualboxはすでにインストール済みとします)

https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
![Windows仮想マシンイメージのダウンロードページ](https://github.com/TakesxiSximada/gist/blob/master/windows-virtual-machines/download-windows-vm.png)

1. 使いたいVirtual machineを選ぶ
2. 使用するプラットフォームを選ぶ
3. `Download .zip` ボタンを押す

するとzipファイルのダウンロードが始まります。サイズはまあまあ大きいです。

ダウンロードが完了したら7zコマンドで解凍します。

```
$ 7z e ~/Desktop/MSEdge.Win10_RS1.VirtualBox.zip
```

解凍するとovaファイルが作成されます。そのファイルを開いてVirtualboxにインポートします。
メモリサイズは1GB程度、その他はそのままの値で良さそうです。

このVMは90日で期限切れになってしまうので、起動する前にsnapshotを取っておきましょう。
![VirtualBoxのsnapshot](https://github.com/TakesxiSximada/gist/blob/master/windows-virtual-machines/virtualbox-snapshot.png)

VMを起動します。
![Windows VM](https://github.com/TakesxiSximada/gist/blob/master/windows-virtual-machines/windows-vm.png)
