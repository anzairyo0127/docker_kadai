## DockerコマンドでWelcome to nginxを表示させよう。

`docker`コマンドを用いて以下の画像のように表示させること。

`http://127.0.0.1:8080`または`http://192.168.99.100:8080`にアクセスすると表示されるようにすること。

`IPアドレス`部分または`port番号`部分は好きな値でも問題はない。

`nginx:1.15-alpine`イメージを使用すること。

![Welcome to nginx](https://github.com/anzairyo0127/docker_kadai/blob/master/image/nginxWelcome.png)

## Hint

### nginxイメージについて

`nginx:1.15-alpine`Imageは`80`ポートが解放されています。

## 【応用】index.htmlを表示させて見よう

`docker`コマンドを使って`Hello Docker Volume`と表示するHTMLを表示させること。

`volume`オプションを使って`index.html`をコンテナに渡し表示させること。

`http://127.0.0.1:8080`または`http://192.168.99.100:8080`にアクセスすると表示されるようにすること。

`IPアドレス`部分または`port番号`部分は好きな値でも問題はない。

`nginx:1.15-alpine`イメージを使用すること。

![Hello Docker Volume](https://github.com/anzairyo0127/docker_kadai/blob/master/image/HelloDockerVolume.png)

## Hint

### index.htmlについて

使用する`index.html`はこの`kadai1`ディレクトリ内にあるものを使用してください。

### volumeオプションについて

`docker`の`-v`オプションはホストPCのディレクトリとコンテナのディレクトリを共有できます。

```bash
-v ホストPCのマウント元の'絶対PATH':コンテナのマウント先の'絶対PATH'
```

### nginxイメージについて

`nginx:1.15-alpine`イメージのデフォルトのドキュメントルートは下記のPATHです。

```
/usr/share/nginx/html
```

