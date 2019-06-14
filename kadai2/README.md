## 解説-【基本課題】Dockerfileを完成させましょう。

### 解答例

1. 使用する`Dockerfile`

```
FROM python:3.6.8-alpine
# Hint: Image生成時に右のコマンドを実行させましょう。 `pip install Flask==1.0.2`
RUN pip install Flask==1.0.2
# Hint: run.pyを/var/www内にコピーさせましょう。
COPY ./run.py /var/www/run.py
# Hint: WorkingDirectlyを/var/wwwに設定させましょう。
WORKDIR /var/www
# Hint: 環境変数「FLASK_ENV」に「development」という値を入れさせましょう。
ENV FLASK_ENV=development
# Hint: 環境変数「FLASK_APP」に「run.py」という値を入れさせましょう。
ENV FLASK_APP=run.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

2. その`Dockerfile`をbuildするコマンド

```
docker build . -t flask:1.0
```

3. その`DockerImage`を元にコンテナを立ち上げるコマンド

```
docker run -p 5000:5000 flask:1.0
```

![hello_world](https://github.com/anzairyo0127/docker_kadai/blob/master/image/flask_helloworld.png)

![hello_kuzunoha](https://github.com/anzairyo0127/docker_kadai/blob/master/image/flask_hello_kuzunoha.png)

### 解説

特に問題となる部分がないと思います。

```
# Hint: run.pyを/var/www内にコピーさせましょう。
COPY ./run.py /var/www/run.py
```

こちらでも良いです。

```
# Hint: run.pyを/var/www内にコピーさせましょう。
ADD https://raw.githubusercontent.com/anzairyo0127/docker_kadai/master/kadai2/kadai2-2/run.py /var/www/run.py
```

githubのコードを`ADD`でコピーする際は`rawファイル`のURLを指定してあげてください。

## 解説-【応用課題】DockerfileにARGSを持たせてフレキシブルなものにしよう。

### 解答例

1. 使用する`Dockerfile`

```
# 本来、FROMが一番上に来るように作るのがDockerfileの習わしです。
# しかし、そのFROM部分にARGを使う場合は、FROMより上部にないといけません。
ARG py_ver
ARG flask_env="development"
FROM python:${py_ver}-alpine
# Hint: Image生成時に右のコマンドを実行させましょう。 `pip install Flask==1.0.2`
RUN pip install Flask==1.0.2
# Hint: run.pyを/var/www内にコピーさせましょう。
ADD https://raw.githubusercontent.com/anzairyo0127/docker_kadai/master/kadai2/kadai2-2/run.py /var/www/run.py
# Hint: WorkingDirectlyを/var/wwwに設定させましょう。
WORKDIR /var/www
# Hint: 環境変数「FLASK_ENV」に「development」という値を入れさせましょう。
ENV FLASK_ENV=${flask_env}
# Hint: 環境変数「FLASK_APP」に「run.py」という値を入れさせましょう。
ENV FLASK_APP=run.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

2. その`Dockerfile`をbuildするコマンド

`docker build . --build-arg py_ver=3.7.2 --build-arg flask_env=production -t flask:2.0`

3. その`DockerImage`を元にコンテナを立ち上げるコマンド

`docker run -p 5000:5000 flask:2.0`

### 解説

`ARG`を使うことで変数を使うことが出来ます。

`docker build`時に`--build-arg`というオプションを追加してあげます。

複数の`ARG`がある場合、`--build-arg`も複数指定してあげます。

`FLASK_ENV`の値について、`production`か`development`のどちらかを与えてあげます。

`docker run`をするとログが出力されますが

```
 * Serving Flask app "run.py"
 * Environment: production <-ここが変化する。
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## 解説-【スペシャル課題】CharesetがUTF-8のMySQLイメージを作成しよう。

### 解答例

0. 準備する

以下の`mysql.cnf`というcnfファイルを作る

```
[mysql]
default-character-set=utf8
[mysqld]
character-set-server=utf8
[client]
default-character-set=utf8
```

1. 使用する`Dockerfile`

```
FROM mysql:5.7.26

COPY ./mysql.cnf /etc/mysql/my.cnf

RUN chmod 644 /etc/mysql/my.cnf
```

2. その`Dockerfile`をbuildするコマンド

`docker build . -t test_mysql:1.0`

3. その`DockerImage`を元にコンテナを立ち上げるコマンド

`docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret test_mysql:1.0`

### 解説

MySQLには`cnf`ファイルを与えることでその設定を読み込んで立ち上がることが出来ます。

その`cnf`ファイルをコンテナ内のディレクトリにコピー使っています。

`-e`コマンドは環境変数を代入できます。

`mysql:5.7.26`は環境変数`MYSQL_ROOT_PASSWORD`に何らかの値を入れないと立ち上がらないようになっています。

ベースイメージに`mysql:5.7.26`を使用していますので、環境変数が必要な部分に関しても変わりはありません。

Dockerfileに環境変数を代入しても良いでしょう。

立ち上がったコンテナへは`mysql-client`を使ってアクセスできます。

`mysql-client`では`mysql -h 127.0.0.1 -P 3306 -u root -p`といったコマンドになります。

`mysql-client`内で`show variables like '%char%';`と打ちましょう。

```
mysql> show variables like '%char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       | # ここがutf8
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       | # ここがutf8
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```

## 片付け方法-【おかたづけ】作ったものは削除しましょう。

`docker image rm IMAGE:TAG`とすれば、そのDockerイメージは削除できます。
