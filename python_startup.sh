# dockerを使用しないpython開発環境構築用シェルスクリプト

# 手順
# 1. このスクリプトを開発するディレクトリ直下に置く
# 2. 欲しいパッケージを`pip3 install flake8 autopep8`の末尾以降に書く
# 3. ターミナルで`./python_startup.sh`を実行
# 4. 以下を`settings.json`にコピペ
#   "python.linting.pylintEnabled": false,
#   "python.linting.enabled": true,
#   "python.linting.flake8Enabled": true,
#   "python.linting.lintOnSave": true,
#   "python.formatting.provider": "autopep8",
#   "python.linting.flake8Args": ["--ignore=E501"],
#   "[python]": {
#     "editor.formatOnType": true,
#     "editor.formatOnSave": true,
#   },

python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install flake8 autopep8 prefect==2.8.6 feedparser