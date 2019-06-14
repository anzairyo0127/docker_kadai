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
