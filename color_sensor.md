

```python
# Imports go at the top
from microbit import *
i2c.init()

sensor = i2c.scan()

# senser[0] 的值會是 41

i2c.write(41, bytes([0x81, 0xfc]))
i2c.write(41, bytes([0x80, 0x03]))

while True:
    # 打開補光燈
    pin11.set_pull(pin11.PULL_DOWN)
    sleep(1000)
    
    i2c.write(41, bytes([178]))
    i2c.write(41, bytes([179]))
    i2c.write(41, bytes([182]), True)
    R = int.from_bytes(i2c.read(41, 2), 'big')
    R = int(R/65536*255)
    i2c.write(41, bytes([184]), True)
    G = int.from_bytes(i2c.read(41, 2), 'big')
    G = int(G/65536*255)
    i2c.write(41, bytes([186]), True)
    B = int.from_bytes(i2c.read(41, 2), 'big')
    B = int(B/65536*255)
    
    print("[R, G, B]:", [R, G, B])
    
    sleep(1000)
    
    # 關閉補光燈
    pin11.set_pull(pin11.PULL_UP)

    sleep(1000)
```
