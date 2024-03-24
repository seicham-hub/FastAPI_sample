# FastAPI Sample Application

シンプルなチャットサービスアプリです。   
※ 作成途中です。

主な技術的特徴  
- graphqlを用いたクライアント間のデータ送受信
- pub/sub機能
- FastAPIの非同期プロセスにrabbitMQ(メッセージブローカー)の受信プロセスを埋め込み
- JWTによる認証、認可


# 仮想マシンとして起動しよう
このサービスはDockerを仮想マシンとして使用しています。


- vscode上で拡張機能の「Dev containers」をインストール
- Dockerを起動
- プロジェクトをクローンした後に左下の「><」を押して「reopen in container」を選択


これでDockerコンテナ内で開発する準備は完了です。
必要なツール、vscodeの拡張機能を含めてコンテナ内に入っているので、同じ環境で開発ができます。



# サービスの起動方法
/var/www/sample_project/main.pyファイルを開いてF5を押してください。
もしくはpythonで直接ファイルを実行してもよいです。

