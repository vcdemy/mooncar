# neopixel

## 載入 neopixel

```python
import neopixel
```

## 初始化neopixel

```python
np = neopixel.NeoPixel(pin0, 8)
```

## 一次設定所有的pixel成最亮的紅色。
```python
np.fill((255, 0, 0))
```

## 更新pixel的數值
```python
np.show()
```

## 設定索引值為n的pixel成紅色。

```python
np[n] = (255, 0, 0)
```

參考資料：

* [NeoPixel](https://microbit-micropython.readthedocs.io/en/v1.1.1/neopixel.html)
* [MicroBit MicroPython Documentation](https://microbit-micropython.readthedocs.io/en/v1.1.1/index.html)
