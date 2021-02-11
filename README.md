# speech_rec_test
Google音声認識の結果をブラウザからWebSocketで送信してPythonで受信，またPythonから文字列を送りChromeで発話させるプログラム

## 準備
```
pip install websocket-server
```

## 実行
1. 認識結果の受信プログラムを起動：`python speech_recognition.py`
2. Google Chromeで[https://naka-tomo.github.io/speech_rec_test/](https://naka-tomo.github.io/speech_rec_test/)を開く
3. 「音声認識・合成開始」ボタンを押して，マイクの使用を許可する
4. pythonプログラムと接続できてないときは，ブラウザを更新して3.をもう一度実行
