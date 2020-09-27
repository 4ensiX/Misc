# my docker cheat sheet


## Dockerの操作
`docker run -it --name <name> <image>`で初回起動とbash表示。イメージをDLしていない場合は、`docker pull <image>`でイメージ取得。`<name>`は任意で。
例えば[minideb](https://hub.docker.com/r/bitnami/minideb)利用の場合。
```
$ docker pull bitnami/minideb
$ docker run -it --name test-minideb bitnami/minideb
#何故か -it が無いと上手くいかないときがある。初回起動時しか色々設定するオプションが無い。
#bashからexitするとコンテナも終了する
```
コンテナ停止は、`docker stop <name>`
例
```
$ docker stop test-minideb
```
コンテナの起動は、`docker start <name>`
例
```
$ docker start test-minideb
```
起動中のコンテナにbashで接続するには、`docker exec -i <name> bash`
例
```
$ docker exec -it test-minideb bash
(exitで抜けられる)
```
コンテナの確認は`docker ps -a`
コンテナの削除は`docker rm <name>` or`docker rm <CONTAINER ID>` 
イメージの削除は`docker rmi <image>` or `docker rmi <IMAGE ID>`

コンテナが起動しているか確認　`docker ps`
今ローカルに持ってるイメージの確認　`docker images`

#### http://docs.docker.jp/v1.9/engine/reference/commandline/index.html

## Dockerfile
Dockerfile に必要な設定を書き込みイメージをビルドする。
`<命令 > 引数`
Dockerfile内の命令一部
- *FROM* Docker hub からベースイメージ選択
- *ENV* コンテナ内の環境変数の設定
- *EXPOSE* 公開ポートの設定
- *RUN* コマンドの実行
- *COPY* ローカルファイルのコピー
- *CMD* 一度しか実行されないコマンドの指定。構築時には実行されず、起動時にイメージ内で実行される。

#### http://docs.docker.jp/v1.9/engine/reference/builder.html
#### http://docs.docker.jp/v1.9/engine/articles/dockerfile_best-practice.html


## 参考
[Docker ドキュメント日本語化プロジェクト — Docker-docs-ja 1.9.0b ドキュメント](http://docs.docker.jp/v1.9/index.html)

