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

## 解説-【スペシャル課題】dotenvを使おう

### 解答例

1. `docker-compose.yml`の完成形

```
version: '3'
services:
  login_app:
    image: python:3.6.8-alpine
    environment:
      - LOGIN_NAME=${login_name}
      - PASSWORD=${password}
    volumes:
      - ./app/:/var/app
    command: ["python", "/var/app/login.py"]
```


2. `.env`の完成形

```
# login password
login_name=honda
password=vFr8+rr
```

3. `.env.example`の完成形

```
# login password
login_name=example_username
password=example_password
```

### 解説

#### .envについて

`.env`は作成済みですので、それから特別変更を加える必要はありません。

問題は`.env`で宣言された変数を`docker-compose.yml`でどのように展開するか、というところになります。

`docker-compose.yml`内では`${変数名}`とすれば変数を展開することが出来ます。

```
# docker-compose.ymlの一部
    environment:
      - LOGIN_NAME=${login_name}
```

`docker-compose up`として`DockerCompose`が実施されるとまず`${login_name}`が展開されます。

そして`${login_name}`が`honda`という値に変化します。

それから、`login_app`サービス内の環境変数`LOGIN_NAME`に`honda`が代入されます。

その後はPythonプログラムが環境変数`LOGIN_NAME`を読み込み、それを使用してログインを行います。

#### .env.exampleについて

`.env`にはログインをする情報を記載しておく必要があります。この情報はセンシティブなものになります。

`うっかり`でバージョン管理ソフトで記録されてしまうと、Log情報からデータをサルベージされてしまいます。

そういったミスも許容できるよう`.env`そのものをバージョン管理ソフトで記録しないという運用方法が考えられました。

そのため、gitをcloneした際、ローカルで`.env`を作成する必要があるわけですが、その`.env`を簡単に作れるように`.env.example`を作成する運用が考えられました。

もちろん、`.env.example`には`例`を入れるだけにとどめてください。

必要なセンシティブな情報は別の方法で確認を取りましょう。
