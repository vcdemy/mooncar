# Reflectance Sensor

## 設定

```python
from microbit import *

pin15.set_pull(pin15.NO_PULL)
pin16.set_pull(pin16.NO_PULL)
```

## 讀取訊號

```python
p15 = pin15.read_digital()
p16 = pin16.read_digital()
```

## TODO:

1. 寫一個程式防止小車跌出桌子。
2. 循跡小車。