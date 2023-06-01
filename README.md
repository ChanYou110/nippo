# nippo
だるい日報PR作成が少しでも楽になればなと・・・

# 使い方

## Pythonインストール
下記コマンドでpython入ってないよって言われた人はインストールしてください
```sh
python --version
```
pyenv（pythonのバージョン管理できるやつ）のインストール & 初期設定
```sh
$ brew install pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ source ~/.zshrc
```
pythonインストール & 適用
```sh
$ pyenv install 3.10.4
$ pyenv global 3.10.4
```
下記コマンドで`Python 3.10.4`と出ればOK
```sh
python --version
```

## nippo.pyの実行

リポジトリのクローン

HTTP
```sh
$ git clone https://github.com/ChanYou110/nippo.git
```
SSH
```sh
$ git clone git@github.com:ChanYou110/nippo.git
```
クローンしたリポジトリに移動
```sh
$ cd nippo
```
Pythonプログラムの実行
```sh
$ python nippo.py
```
