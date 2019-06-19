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

`volumes`という記述を用いてappサービス内のディレクトリ`/var/app`に`./app`ディレクトリをマウントしましょう

## 【スペシャル課題】dotenvを使おう

### 条件

1. `kadai3-3`ディレクトリ内にある`docker-compose.yml`を完成さましょう。

1. DockerComposeのversionは3とします。

1. 今回はPythonプログラムを使って、とあるシステムにログインしたいと思っています。

1. とあるシステムにログインをするにはログインネームとパスワードが必要です。

1. 作成済みのPythonプログラムは環境変数`LOGIN_NAME`を取得してログインネームとします。

1. また環境変数`PASSWORD`を取得してパスワードとします。

1. サービス内の環境変数`LOGIN_NAME`に`honda`、環境変数`PASSWORD`に`vFr8+rr`という値を代入したいと思っています。

1. ただし、直接`docker-compose.yml`にログインネームとパスワードを記載し、バージョン管理ソフトで共有するのは危険です。

1. DockerComposeには`.env`という`docker-compose.yml`内で使用できる変数を作成してくれる機能が存在します。

1. `.env`は`docker-compose.yml`内で使用できる環境変数を代入できますがサービス内には直接代入しません。

1. `.env`を使って環境変数`LOGIN_NAME`と環境変数`PASSWORD`に値を代入してください。

1. `docker-compose up`として起動した時に以下のようなログ`OK! Login Succeeded!`を出力させてください。

1. また、`.env`を共有できないよう`.gitignore`にする予定です。

1. `.env`の書き方を参考に出来る`.env.example`を作成してください。

1. `.env.example`は直接、ログインに必要な値を記述しないでください。

```
[kuzunoha@:11:08:57:~/docker_kadai/kadai3/kadai3-3]$docker-compose up
Creating kadai3-3_login_app_1 ... done
Attaching to kadai3-3_login_app_1
login_app_1  | INFO : 2019-06-19 02:10:08,672 : LoginName="honda" ; Password="vFr8+rr"
login_app_1  | INFO : 2019-06-19 02:10:08,672 : Cheking Username & Password .....
login_app_1  | INFO : 2019-06-19 02:10:09,673 : OK! Login Succeeded!
kadai3-3_login_app_1 exited with code 0
```

上記条件のとき

1. `docker-compose.yml`の完成形

1. `.env`の完成形

1. `.env.example`の完成形


それぞれを解答としてください。

### Hint

#### 環境変数を代入する記述

`environment`という記述を用いてappサービスに環境変数を代入しましょう。

#### ログインに失敗するときのログ

`docker-compose up`としたときにログインに失敗した場合のログは以下のようになります。

`ERROR! Failed to login.`

```
[kuzunoha@:11:10:10:~/docker_kadai/kadai3/kadai3-3]$docker-compose up
Recreating kadai3-3_login_app_1 ... done
Attaching to kadai3-3_login_app_1
login_app_1  | INFO : 2019-06-19 02:27:48,212 : LoginName="hogehoge" ; Password="piyopioyo"
login_app_1  | INFO : 2019-06-19 02:27:48,212 : Cheking Username & Password .....
login_app_1  | ERROR : 2019-06-19 02:27:49,213 : ERROR! Failed to login.
kadai3-3_login_app_1 exited with code 0
```

#### .env.exampleについて

`.env`は直接ログインに掛かる情報が記載されていても`.gitignore`に記載される予定ですので、github等で共有される問題はありません。

しかし、今回のDockerComposeは`.env`が無いと動かないような仕組みとなっています。

また`.env`の記述は`変数名=値`というもので、そもそも`変数名`がわからないと記述のしようがないというものとなっています。

そのため`.env.example`という`例となるファイル`を作成し、`変数名=例の値`と記載しておくことで、`他の人`がすぐに扱えるような状態にしたいと思っています。

もちろん、`.env.example`に直接ログインに掛かる情報が記載されていてはいけません。
