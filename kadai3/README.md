## 【基本課題1】DockerComposeを完成させましょう

### 条件

1. `kadai3-1`ディレクトリ内にある`docker-compose.yml`を完成さましょう。

1. DockerComposeのversionは3とします。

1. nginxサービスが途中まで作成されています。

1. nginxサービスにポートマッピングの設定を記載してください。

1. `docker-compose`コマンドを使ってnginxサービスを立ち上げてください。

1. ウェブブラウザからWelcome画面を表示できるようにしましょう。

上記の条件のとき

1. `docker-compose.yml`の完成形

1. `docker-compose`を起動させるコマンド

それぞれを解答としてください。

### Hint

#### サービスという単位

`DockerCompose`ではサービスという単位をもっています。

今回の`docker-compose.yml`では、下記がサービスの１単位になります。

```
  nginx:
    image: nginx:1.15-alpine
```
サービスはコンテナに様々なオプションをつけて起動するものと思ってください。

## 【応用問題】RedisとFlaskを接続させたdocker-compose.ymlを完成させてください

1. `kadai3-3`ディレクトリ内にある`docker-compose.yml`を完成さましょう。

1. DockerComposeのversionは3とします。

1. appサービスに環境変数`REDIS_ADDRESS`にRedisサービスへアクセスするアドレスやホストネームを代入してください。

1. appサービスに環境変数`REDIS_PORT`にRedisサービスへアクセスするポート番号を代入してください。

1. appサービスは`app.py`を使ってflaskを起動しています。

1. appサービスの`/var/app`ディレクトリを`/kadai3-3/app`とマウントしてください。

1. appサービスの5000番ポートをポートマッピングしてください。

1. `docker-compose`コマンドを使ってappサービス, redisサービスを立ち上げてください。

1. ウェブブラウザから`This is Test Message!`画面を表示できるようにしましょう。

上記の条件のとき

1. `docker-compose.yml`の完成形

1. `docker-compose`を起動させるコマンド

それぞれを解答としてください。

### Hint

#### 環境変数を代入する記述

`environment`という記述を用いてappサービスに環境変数を代入しましょう。

#### Dockerネットワーク

`DockerCompose`はDockerネットワークが自動で生成される`kadai3-2_default`ネットワークがあり、appコンテナとredisコンテナがそのネットワーク内でアクセスすることが可能です。

今回はホストPCからサービス(あるいはコンテナ)にアクセスするのではなく、サービスからサービスにアクセスするようになっています。

`DockerCompose`で生成されるサービス間ネットワーク内は、サービス名で名前解決されています。上記を思慮した上で環境変数`REDIS_ADDRESS`に値を代入しましょう。

#### volumeを使用する

`volume`という記述を用いてappサービス内に./appディレクトリをマウントしましょう
