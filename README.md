# Prefectお試し

Python製のワークフロー管理ツール
VPSでairflow立ち上げようにもメモリ不足で立ち上がらなかった経緯から他に無いか探してたら見つけたもの、まだ試してないもののこれなら多分問題なく行けそう。

この記事も参考になるかも
https://dev.classmethod.jp/articles/prefect-try/

## バージョン

- Prefect 2.8.6

## 最初にやる

`python_startup.sh`実行


## デプロイ
https://docs.prefect.io/tutorials/deployments/

以下は試しでRSSフィードのDiscord botを作成したのでそのデプロイ手順

1. `prefect deployment build ./discord_flow.py:discord -n rss_discord`
2. `discord-deployment.yaml`を開いて、parametersに`DISCORD_WEBHOOK_URL: {url}`を追加
3. `prefect deployment apply discord-deployment.yaml`
4. `prefect deployment run 'discord/rss_discord'`
5. `prefect agent start -q 'default'`

## スケジュール設定
https://docs.prefect.io/concepts/schedules/

GUI上でやるのが手軽。
`Interval`, `Cron`, `RRule`の3つから選べる

1. `Deployments` -> taskを選択
2. 画面右の`Schedule`の`Add`を選択
3. 設定し終わったら`Save`
4. 更新すると設定したスケジュール通りに実行待ちが作成されている