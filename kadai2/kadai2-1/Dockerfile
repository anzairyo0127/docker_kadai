FROM python:3.6.8-alpine
# Hint: Image生成時に右のコマンドを実行させましょう。 `pip install Flask==1.0.2`
RUN pip install Flask==1.0.2
# Hint: run.pyを/var/www内にコピーさせましょう。
ADD https://raw.githubusercontent.com/anzairyo0127/docker_kadai/master/kadai2/kadai2-2/run.py /var/www/run.py
# Hint: WorkingDirectlyを/var/wwwに設定させましょう。
WORKDIR /var/www
# Hint: 環境変数「FLASK_ENV」に「development」という値を入れさせましょう。
ENV FLASK_ENV=development
# Hint: 環境変数「FLASK_APP」に「run.py」という値を入れさせましょう。
ENV FLASK_APP=run.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
