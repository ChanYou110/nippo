# nippo
だるい日報PR作成が少しでも楽になればなと・・・（だるさ100→90くらいにはなる）

## やったこと
| 開始時間 | 終了時間 | 内容 | 詳細メモ |
| :-- | :-- | :-- | :-- |
| 12:00 | 12:30 | 休憩 | プルダックポックンミョン食べた |
| 18:00 | 18:30 | 日報作成 |  |

## 改善点/今後に向けて
-
-

↑こんな感じのができます。


# 使い方


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
$ python3 nippo.py
```
- 開始時刻と終了時刻は HH mm （例12:00→12 00）の形で入力

- 時刻入力ミスったらそこまでの内容でPR作成されます

- 終了時刻18:30の予定を入れたらそこまでの内容でPR作成されるようになってます

## 追記（2023/06/02）
Venturaはpython3が同梱されてたのでそれで実行できます

一応pythonの仮想環境インストール方法残しておきます。
## Pythonインストール
下記コマンドでpython入ってないよって言われた人はインストールしてください
```sh
python --version
```
pyenv（pythonのバージョン管理できるやつ）のインストール & 初期設定

エラー出るかもですが、何回か実行してると入ります（エラーはようわからん）
```sh
$ brew install pyenv
```
pyenv初期設定
```sh
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ source ~/.zshrc
```
pythonインストール & 適用
```sh
$ pyenv install 3.10.7
$ pyenv global 3.10.7
```
下記コマンドで`Python 3.10.7`と出ればOK
```sh
python --version
```