## 【基本課題1】DockerComposeを完成させましょう。

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

## 【基本課題2】MySQLサービスを作成しましょう。

1. `kadai3-1`ディレクトリ内にある`docker-compose.yml`を完成さましょう。

1. DockerComposeのversionは3とします。

1. mysqlサービスが途中まで作成されています。

1. nginxサービスにポートマッピングの設定を記載してください。

1. 環境変数`MYSQL_ROOT_PASSWORD`に好きな値を入れてください。

1. mysqlクライアントでアクセスできるようにしてください。

上記の条件のとき

1. `docker-compose.yml`の完成形

1. `docker-compose`を起動させるコマンド

それぞれを解答としてください。

