## DockerコマンドでWelcome to nginxを表示させよう。

`docker`コマンドを用いて以下の画像のように表示させること。

`http://127.0.0.1:8080`または`http://192.168.99.100:8080`にアクセスすると表示されるようにすること。

`IPアドレス`部分または`port番号`部分は好きな値でも問題はない。

`nginx:1.15-apline`イメージを使用すること。

![Welcome to nginx](https://github.com/anzairyo0127/docker_kadai/blob/master/image/nginxWelcome.png)

## Hint

### nginxイメージについて

`nginx:1.15`Imageは`80`ポートが解放されています。

## 【応用】index.htmlを表示させて見よう

`docker`コマンドを使って`Hello Docker Volume`と表示するHTMLを表示させること。

`volume`オプションを使って`index.html`をコンテナに渡し表示させること。

`http://127.0.0.1:8080`または`http://192.168.99.100:8080`にアクセスすると表示されるようにすること。

`IPアドレス`部分または`port番号`部分は好きな値でも問題はない。

`nginx:1.15-apline`イメージを使用すること。

![Hello Docker Volume](https://github.com/anzairyo0127/docker_kadai/blob/master/image/HelloDockerVolume.png)

### hint

`docker`の`-v`オプションはホストPCとコンテナ


```bash
-v ホストPCのマウント元の'絶対PATH':コンテナのマウント先の'絶対PATH'
```
