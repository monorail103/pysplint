# オセロ
ミニマックス法を用いたオセロのAIです。

## ファイル構成
- cpu.py: ゲームのメインファイルです。
- view.py: ゲームのビューを表示するファイルです。資料の画像を作るために作成しました。

## 初期設定
1. Python の仮想環境を作成します。3.8.5で動作確認済みです。
2. `pip install -r requirements.txt` を実行して、仮想環境にライブラリをインストールします。
3. cpu.pyを実行します。

## オセロの仕組み
「ミニマックス法」と「アルファベータ枝刈り」を組み合わせたものを使用しています。
