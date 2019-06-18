## 解説-【基本課題1】DockerComposeを完成させましょう

### 解答例

1. `docker-compose.yml`の完成形

```
version: '3'
services:
  nginx:
    image: nginx:1.15-alpine
    ports:
     - "8080:80"
```

1. `docker-compose`を起動させるコマンド

`docker-compose up`


### 解説

`ports`の記述が必要となります。

ウェブブラウザ`http://127.0.0.1:8080`でアクセス可能です。


## 解説-【応用問題】RedisとFlaskを接続させたdocker-compose.ymlを完成させてください

### 解答例

1. `docker-compose.yml`の完成形

```
version: '3'
services:
  app:
    build: .
    environment:
     - REDIS_ADDRESS=redis
     - REDIS_PORT=6379
    ports:
     - "5000:5000"
    volumes:
     - "./app:/var/app"

  redis:
    image: redis:5.0.5-alpine
```

1. `docker-compose`を起動させるコマンド

`docker-compose up`

### 解説

#### Dockerネットワークとコンテナ間の接続

コンテナからコンテナにアクセスをするには、Dockerネットワークの設定が必要ですが、DockerComposeは自動でそこを設定してくれます。

`DockerCompose`で生成されるサービス間ネットワーク内は、サービス名で名前解決されています。`redis`サービスは`redis`というホストネームをもっています。環境変数`REDIS_ADDRESS`に`redis`を入れればアクセスできます。

#### volumeを使ったディレクトリの共有

`volumes`という記述を用いてappサービス内にホストPCのディレクトリをマウントできます。

ただ、volumesでマウントを行った際、マウント先のディレクトリの内容はなくなります。

```
ホストPCのディレクトリ
A, B
マウント前のコンテナのディレクトリ
C, D
ホストPCとマウント後のコンテナのディレクトリ
A, B
```
