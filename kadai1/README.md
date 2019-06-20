## 解説-【基本課題】DockerコマンドでWelcome to nginxを表示させよう

### 解答例

```
docker run -p 8080:80 nginx:1.15-alpine
```

として、`http://127.0.0.1:8080` (DockerToolboxの場合は`http://192.168.99.100:8080`)でアクセスできます。 

![Welcome to nginx](https://github.com/anzairyo0127/docker_kadai/blob/master/image/nginxWelcome.png)

### 解説

`nginx:1.15-alpine`イメージは、`run`をすると80番ポートで`nginx`というソフトウェアを起動するコンテナを生成します。

Dockerfile:https://github.com/nginxinc/docker-nginx/blob/master/mainline/alpine/Dockerfile

ホストPCとコンテナの間にポートマッピングを施してあげれば、アクセスは可能になります。

そのための`-p`オプションが必要になります。`-p`の引数に`[ホストPCのポート番号]:[コンテナのポート番号]`を渡してあげましょう

つまづくポイントとしてはオプションの指定方法かもしれません。

失敗例
```
# オプションの位置がイメージ名より後に来ている。
docker run nginx:1.15-alpine -p 8080:80
```

これは`nginx:1.15-alpine`で作成するコンテナに「`-p 8080:80`というコマンドを実行しなさい」という命令になってしまいます。

基本的に、`docker run`を行うときは、オプションコマンドはイメージ名より手前にするようにしましょう。


## 解説-【応用課題】index.htmlを表示させましょう

### 解答例

```
docker run -p 8080:80 -v /home/kuzunoha/desktop/working/docker_kadai/kadai1:/usr/share/nginx/html  nginx:1.15-alpine 
```

`/home/kuzunoha/desktop/working/docker_kadai/kadai1`に関しては自分のディレクトリに置き換えてください。

あるいは

```
docker run -p 8080:80 -v ${PWD}:/usr/share/nginx/html nginx:1.15-alpine
```

![Hello Docker Volume](https://github.com/anzairyo0127/docker_kadai/blob/master/image/HelloDockerVolume.png)

### 解説

`nginx:1.15-alpine`のドキュメントルートは以下のパスになります。

```
/usr/share/nginx/html
```
この`html`ディレクトリ内にある`html`ファイルを読み込んで出力します。

うち、`index.html`がトップページになるようにデフォルトで設定されています。

`-v`コマンドはHintにも記載したとおり、絶対パスで指定してあげてください。

失敗例
```
# -vpとオプションを繋げている
docker run -pv 8080:80 ${PWD}:/usr/share/nginx/html nginx:1.15-alpine
```

基本的に引数を必要とするオプションコマンドについては、`-pv`といった繋げて表記する、ということはできません。

## 解説-【スペシャル課題】二つのNginxコンテナを起動させよう。

### 解答例

```
docker run -d -p 8080:80 nginx:1.15-alpine
docker run -d -p 9090:80 nginx:1.15-alpine
```

２つコマンドを打つだけですが、ホストPCのポート番号が重複しないようにしましょう。

失敗例
```
docker run -d -it -p 20:80 nginx:1.15-alpine
```

ウェルノウンポートという概念があります。コンピューターが特定のネットワーク通信を行う際にほぼ確定的に使用されるポート番号です。20番ポートに関しては`FTP`通信を行うためのポート番号となっています。

基本的にウェルノウンポートは使用しないようにしましょう。

https://ja.wikipedia.org/wiki/TCP%E3%82%84UDP%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%9D%E3%83%BC%E3%83%88%E7%95%AA%E5%8F%B7%E3%81%AE%E4%B8%80%E8%A6%A7

## 【おかたづけ】Dockerコンテナをストップし、削除しましょう。

### 片付け方一例

```
docker container ps
```

でコンテナネームやコンテナIDを確認後、

```
docker container stop コンテナネームorコンテナID
```

そうして停止したコンテナに対し

```
docker container rm コンテナネームorコンテナID
```

を行いましょう。
