# 本来、FROMが一番上に来るように作るのがDockerfileの習わしです。
# しかし、そのFROM部分にARGを使う場合は、FROMより上部にないといけません。

FROM python:3.6.8-alpine
# Hint: Image生成時に右のコマンドを実行させましょう。 `pip install Flask==1.0.2`

# Hint: run.pyを/var/www内にコピーさせましょう。

# Hint: WorkingDirectlyを/var/wwwに設定させましょう。

# Hint: 環境変数「FLASK_ENV」に「development」という値を入れさせましょう。

# Hint: 環境変数「FLASK_APP」に「run.py」という値を入れさせましょう。

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
