# neopixel使用說明

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

## 練習題

* 讓RGB LED不斷的循環置換顏色 (e.g., 全部亮紅燈，一秒後，全部亮綠燈，再一秒後全部亮藍燈。)
* 跑馬燈，依序顯示RGB LED，從第一顆亮到最後一顆。
* 全部的LED一起慢慢變亮，然後再慢慢變暗。
* 前面四顆閃紅燈、後面四顆閃藍燈 (警車效果)。
* 綠燈、黃燈、紅燈 (紅綠燈效果)。
* 按Button A逐步調亮RGB LED，按Button B逐步調暗RGB LED。

## 參考資料：

* [NeoPixel](https://microbit-micropython.readthedocs.io/en/v1.1.1/neopixel.html)
* [MicroBit MicroPython Documentation](https://microbit-micropython.readthedocs.io/en/v1.1.1/index.html)
