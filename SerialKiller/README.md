# Serial Killer

**Category:** Crypto
**Points:** 100

**Description:**
```
Hhpnivraosgt5MzNw
jNieegoeecweteOzQ
Y5MDTZarnddCytoTW
kM2YWEhokasemiohv
iaN3Z2UziditYcypu
hcslTMjU4MsinuoiZ
poeafiQzQ5YXiaglu
ahhdrnldXZxM20scC
sotaeiNuaaskYGI=t
```
## write-up

จากคำใบนักฆ่าปี 1960 แถมยังมีรหัสลับอีกก็ลองเอาไปหา คิดว่าน่าจะเป็น Zodiac Killer แน่ๆเลย แต่คือการเข้ารหัสมันเป็นเหมือนภาพวาด ลองพยายามทำความเข้าใจแล้วแต่ไม่เก็ตเลย555 จนเพื่อนบอกว่ามันถอดรหัสโดยการมองเป็นแนวเฉียงนี่นาคือ ลง 1 ขวา 3 จะได้

```
-------------------------------------------------------------
H
    i
        T
            h
                i
                    s
                        i
                            s
                               t
=> Hi This is t
-------------------------------------------------------------
```
เห้ยได้เหรอเนี่ยยย ทำไปเรื่อยๆ จะได้คำยาวๆ ออกมาเป็น
Hi This is the Zodiac speaking Congratulations You have deciphered my Zodiac Cipher Now you can use this flag to validate
TkNTQXs5OWM3MzZkMzY2ZjQxYzQ5Y2U5MGNjMWU4Y2IwNDEzMX0=%
ถอดรหัสบรรทัดสุดท้ายด้วย base64 ก็จะได้

## NCSA{99c736d366f41c49ce90cc1e8cb04131}