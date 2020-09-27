# Dockerのイメージの 作成 wordpress
接続するとwordpress の初回設定だけで済むイメージのビルド
- ベースイメージは docker hub の ubuntu
- apache2,php7.4,mariadb,supervisor を導入
- Docker では systemd が利用できないので、その代わりのサービス管理として supervisor を利用する。
Dockerイメージのビルド
```
$ docker build -t <image_name> .
# dockerfile がカレントディレクトリにある場合
```

