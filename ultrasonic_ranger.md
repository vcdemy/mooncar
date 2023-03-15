# 超音波測距 (Ultrasonic Ranger)

假設trigger聲波的腳位在pin3，讀取echo的腳位在pin9。

## 發送聲波：

```python
pin3.write_digital(1)
pin3.write_digital(0)
```

## 計算聲波返回時間：

```python
import machine

# 計算回傳時間 (us)
micros = machine.time_pulse_us(pin9, 1)
```

## 音速公式 (m/s)：

```math
v = 331.6 + 0.6T
```
```math
T: 攝氏溫度
```

## TODO:

請寫一個程式計算障礙物距離！

