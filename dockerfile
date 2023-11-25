# alpine OSのPython3.12のimage取得
FROM python:3.12-alpine

# 実行ディレクトリ
WORKDIR /usr/src/app

# ホストOSのrequirements.txtファイルを実行ディレクトリにコピー
COPY requirements.txt ./

# pip (pythonライブラリ)のバージョンアップ
RUN /usr/local/bin/python -m pip install --upgrade pip

# requirements.txtに書かれているpythonのライブラリをpipを使ってインストール
RUN pip install -r requirements.txt


# 以下Docker コマンド

# 1. docker ビルド
#     $ docker build ./ -t ptbse_img
 

# 2. docker コンポーネント実行
#     $  docker run -itd -p 127.0.0.1:8000:8000 -v ${pwd}:/usr/src/app --name ptbse_com ptbse_img

# 3. Django server 起動
#     $ docker exec -it ptbse_com sh
#          python3 manage.py runserver 0.0.0.0:8000
#     $ docker exec django_com python3 manage.py runserver 0.0.0.0:8000

# 6. ブラウザ確認
#     http://localhost:8000


# ディレクトリ構成
# project
#    ┣ Dockerfile
#    ┣ requirements.txt
#    ┣ manage.py    →
#    ┣ db.sqllite3  →
#    ┣ tripsearch   → プロジェクト

