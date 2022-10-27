[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
# Release Note
* **update 22.10.27** version 0.0.0  
신규 지원: L298N 모터 드라이버, I2C RTC, I2C LCD, 초음파 센서 [**지원 부품 더보기**](#step-3-stepmaker-패키지-지원-부품)

* **update 22.10.28** version 0.0.1  
신규 지원: Pico 내장 온도 센서, Pico 내장 LED [**지원 부품 더보기**](#step-3-stepmaker-패키지-지원-부품)

<br/>

# Stepmaker 패키지는 무엇인가요?
파이썬을 잘 몰라도, 누구나 손쉽게 라즈베리파이 피코를 다룰 수 있도록 도와주는 패키지입니다.

<br/>

# Stepmaker 패키지 사용 방법
## Step 1. Thonny에서 Stepmakerkit 패키지 다운로드 
**Stepmaker 패키지**는 **Rpi Pico(라즈베리파이 피코)** 와 호환됩니다.  

<br/>

## Step 2. Rpi Pico에 업로드 되었는지 확인
**Rpi Pico** 내부에 **_/lib_** 폴더가 생성 되었다면, 정상적으로 업로드가 완료된것입니다.

<br/>

## Step 3. Stepmaker 패키지 지원 부품
```python
#아래 지원 목록을 확인하여 필요한 모듈만 불러오는 것을 권장합니다.
from stepmaker import *
```
**현재 지원 중**
- L298N 모터 드라이버 `Module Name: driver`
- I2C RTC `Module Name: rtc`
- I2C LCD `Module Name: lcd`
- 초음파 센서 `Module Name: ultrasound`
- Pico 내장 온도 센서 `Module Name: pico`
- Pico 내장 LED `Module Name: pico`

<br/>

**현재 개발 중**
- 피에조 부저 (수동형)
- 로터리 엔코더

추후 더 많은 부품을 지원할 수 있도록 노력하겠습니다.  
만약 추가를 원하시는 부품이 있을 경우 아래 이메일 주소로 관련 내용을 보내주세요.  
<dev@takeup.cc>

<br/>

## Step 4. Stepmaker 패키지 부품별 적용 방법
* **L298N 모터 드라이버 사용하기**  
현재 아래와 같은 4가지의 기능이 있습니다.
```python
#장치를 지정한 파워로 즉시 켜기
device_name.on(100) #0 ~ 100 사이로 조절 가능

#장치를 즉시 끄기
device_name.off()

#장치를 지정한 파워로 천천히 켜기 (페이드 인 효과)
device_name.slow_on(100) #0 ~ 100 사이로 조절 가능

#장치를 천천히 끄기 (페이드 아웃 효과)
device_name.slow_off()
```  
<br/>

이를 응용한 예제 코드는 아래와 같습니다.  
자세한 사용 방법은 **[예제]** 를 참고해주세요.  

```python
#[예제 1] 장치를 지정한 파워로 즉시 켜기
from stepmaker import driver

device_name = driver.Pin(11, 12, 13) #In1, In2, PWM1
device_name.on(100) #0 ~ 100 사이로 조절 가능
```

```python
#[예제 2] 장치를 즉시 끄기
from stepmaker import driver

device_name = driver.Pin(11, 12, 13) #In1, In2, PWM1
device_name.off()
```

```python
#[예제 3] 장치를 지정한 파워로 천천히 켜기 (페이드 인 효과)
from stepmaker import driver

device_name = driver.Pin(11, 12, 13) #In1, In2, PWM1
device_name.slow_on(100) #0 ~ 100 사이로 조절 가능
```

```python
#[예제 4] 장치를 천천히 끄기 (페이드 아웃 효과)
from stepmaker import driver

device_name = driver.Pin(11, 12, 13) #In1, In2, PWM1
device_name.slow_off()
```

<br/>

* **I2C 주소 찾기**
```python
#[예제 1] I2C 주소를 찾아 터미널에 출력하기
from stepmaker import addr

i2c_num = 0
sda = 16
scl = 17

addr = addr.Find(i2c_num, sda, scl) #i2c번호, sda, scl
print(addr)
```

<br/>

* **I2C LCD 사용하기**
```python
#[기능] 자주 사용하는 명령어
device_name.clear() #LCD 초기화
device_name.move_to(0, 0) #LCD 커서 이동
device_name.putstr("text") #LCD 텍스트 출력
device_name.backlight_on() #LCD 백라이트 켜기
device_name.backlight_off() #LCD 백라이트 끄기

```

```python
#[예제 1] LCD에 글자(hello) 출력하기
from stepmaker import lcd, addr

lcd_i2c_num = 0
lcd_sda = 16
lcd_scl = 17

lcd_addr = addr.Find(lcd_i2c_num, lcd_sda, lcd_scl) #i2c번호, sda, scl
lcd = lcd.I2cPin(lcd_i2c_num, lcd_addr, lcd_sda, lcd_scl) #i2c번호, i2c주소, sda, scl

lcd.move_to(0,0)
lcd.putstr("hello")
```

```python
#[예제 2] LCD에 "hello"출력 후 5초 뒤에 "world"출력하기
from stepmaker import lcd, addr
import utime

lcd_i2c_num = 0
lcd_sda = 16
lcd_scl = 17

lcd_addr = addr.Find(lcd_i2c_num, lcd_sda, lcd_scl) #i2c번호, sda, scl
lcd = lcd.I2cPin(lcd_i2c_num, lcd_addr, lcd_sda, lcd_scl) #i2c번호, i2c주소, sda, scl

lcd.move_to(0,0)
lcd.putstr("hello")
utime.sleep(5)
lcd.clear()
lcd.putstr("world")
```

<br/>

* **I2C RTC 사용하기**
```python
#[예제 1] RTC 연결하여 현재 시각 설정하기
from stepmaker import rtc, addr

rtc_i2c_num = 1
rtc_sda = 14
rtc_scl = 15

rtc_addr = addr.Find(rtc_i2c_num, rtc_sda, rtc_scl) #i2c번호, sda, scl
rtc = rtc.I2cPin(rtc_i2c_num, rtc_addr, rtc_sda, rtc_scl) #i2c번호, i2c주소, sda, scl

rtc.set()
```

```python
#[예제 2] RTC 현재 시각 불러와 터미널에 출력하기
from stepmaker import rtc, addr

rtc_i2c_num = 1
rtc_sda = 14
rtc_scl = 15

rtc_addr = addr.Find(rtc_i2c_num, rtc_sda, rtc_scl) #i2c번호, sda, scl
rtc = rtc.I2cPin(rtc_i2c_num, rtc_addr, rtc_sda, rtc_scl) #i2c번호, i2c주소, sda, scl

print(rtc.datetime())
```
<br/>

* **초음파센서 사용하기**
```python
#[에제 1] 초음파 센서로 측정한 거리를 터미널에 5초 간격으로 터미널에 출력하기
from stepmaker import ultrasound
import utime

ultrasound = ultrasound.Pin(echo, trig) #echo, trig
print(ultrasound.measure())
```

<br/>

* **Pico 내장 온도 센서 사용하기**
```python
#[예제 1] Pico 내장 온도 센서로 측정한 값을 1초 간격으로 터미널에 출력하기
from stepmaker import pico
import utime

built_in_temp = pico.Temp()
print(built_in_temp.measure())
utime.sleep(1)

```

<br/>

* **Pico 내장 LED 사용하기**
```python
#[예제 1] Pico 내장 LED 켜기
from stepmaker import pico

built_in_led = pico.Led()
built_in_led.on()
```

```python
#[예제 2] Pico 내장 LED 끄기
from stepmaker import pico

built_in_led = pico.Led()
built_in_led.off()
```

```python
#[예제 3] Pico 내장 LED 1초 간격으로 10번 점멸하기
from stepmaker import pico
import utime

built_in_led = pico.Led()

for i in range(10):
    built_in_led.on()
    utime.sleep(1)
    built_in_led.off()
    utime.sleep(1)
```