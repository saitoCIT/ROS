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
$echo 1 > /dev/myled0
```
と入力すると, GPIO[25, 24]に接続されたLEDが点灯する  
このとき, ブレッドボードの2の位と1の位が点灯するため, このブレッドボードは3を表示していることがわかる

```bash:move
$echo 2 > /dev/myled0
```
と入力すると, GPIO[25]に接続されたLEDが点灯する  
このとき, ブレッドボードの1の位が点灯するため, このブレッドボードは1を表示していることがわかる

- デバイスドライバの削除
```bash:delate device driver
$sudo rmmod myled
```

## <共同作成者との共通点/相違点>
- 共通点  
LEDを点灯させる部分をfor文で回す

- 相違点  
LEDのON/OFFで2進数表現し, ON/OFFの書き込みの部分で円周率に対応させた

# 参考資料
https://github.com/ryuichiueda/robosys_device_drivers
