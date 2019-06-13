## 【基本課題】DockerコマンドでWelcome to nginxを表示させよう

### 条件

1. `docker`コマンドを用いて以下の画像のように表示させよう。

1. `IPアドレス`部分または`port番号`部分は好きな値でも問題はありません。

1. `nginx:1.15-alpine`イメージを使用してください。

![Welcome to nginx](https://github.com/anzairyo0127/docker_kadai/blob/master/image/nginxWelcome.png)

### Hint

#### nginxイメージについて

`nginx:1.15-alpine`Imageは`80`ポートが解放されています。

## 【応用課題】index.htmlを表示させましょう

### 条件

1. `docker`コマンドを使って`Hello Docker Volume`と表示するHTMLページを表示させましょう。

1. `volume`オプションを使って`index.html`をコンテナに渡し、表示させてください。

1. `IPアドレス`部分または`port番号`部分は好きな値でも問題ありません。

1. `nginx:1.15-alpine`イメージを使用してください。

![Hello Docker Volume](https://github.com/anzairyo0127/docker_kadai/blob/master/image/HelloDockerVolume.png)

### Hint

#### index.htmlについて

使用する`index.html`はこの`kadai1`ディレクトリ内にあるものを使用してください。

#### volumeオプションについて

`docker`の`-v`オプションはホストPCのディレクトリとコンテナのディレクトリを共有できます。

```bash
-v ホストPCのマウント元の'絶対PATH':コンテナのマウント先の'絶対PATH'
```

#### nginxドキュメントルートについて

`nginx:1.15-alpine`イメージのデフォルトのドキュメントルートは下記のPATHです。

```
/usr/share/nginx/html
```

## 【スペシャル課題】二つのNginxコンテナを起動させよう。

### 条件

1. Dockerでnginxコンテナを２つ起動させましょう。

1. １つは基本課題のものを、もう１つは応用課題のものを起動させてください。

1. いずれもアクセス可能な状況であることが達成条件です。

### Hint

#### ポート番号が重複しないようにしましょう。

使用するポート番号が重複してしまうと起動することができません。

例)
```bash
docker: Error response from daemon: driver failed programming 
external connectivity on endpoint dazzling_bhaskara (CONTAINER_ID): 
Bind for 0.0.0.0:8080 failed: port is already allocated.
```

## 【おかたづけ】Dockerコンテナをストップし、削除しましょう。

### 条件

1. 3つの課題で作成したコンテナについて、全て停止しましょう。

1. 3つの課題で作成したコンテナについて、全て削除しましょう。

### Hint

#### Dockerコンテナの停止方法とDockerコンテナの削除方法について

いろんな方法がありますが、消えていればなんでも良いです。