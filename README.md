# ROS

# ロボットシステム学
## robsys2020 課題2 
## 課題2 <内容>
- <内容>
  - 一人でもあっち向いてホイを遊べる
- <アピールポイント>
  - 相手が煽ってこないため, 精神を安定した状態であっち向いてホイの練習ができる
  
## <実行環境>
Raspberry Pi及びubuntu(desktop,serverとはない)が必要
次の環境では動作を確認
|||
|:---|---:|
|機種|Raspberry Pi Model 4|
|ROS|ROS melodic|
|OS|ubuntu mate 20.04|

## <動作手順>
- gitcloneする

```bash:build
$git clone https://github.com/saitoCIT/ROS.git
```

- 端末1でroscoreを立ち上げる

```bash:move
$roscore
```

- 端末2, 端末3をscriptsに移動する
```bash:move
$cd mypkg/scripts
```
- 端末2で以下のコマンドを実行

```bash:move
$rosrun mypkg user.py
```

- 端末3で以下のコマンドを実行
```bash:move
$rosrun mypkg enemy.py
```
端末2で0~3までの数字を入力し, 方向を決定  
端末3で結果が表示される
