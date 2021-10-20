# Log Finding

**Category:** Network
**Points:** 100

**Description:**
[LogFinding.zip](https://github.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/raw/main/LogFinding/LogFinding.zip)

โจทย์จะประมาณว่าให้หา username กับ password ที่สามารถล็อคอินผ่านเข้าสู่ระบบได้ โดย flag จะอยู่ในรูป username=ไอดี&password=รหัส

## write-up

![compare_file_signature.png](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/LogFinding/log.png)

จาก excel เราจะเห็นได้ว่าหลังจากเขาใส่ไอดี admin รหัส batman ก็ได้ตอบกลับเป็น index.php น่าจะแปลว่าเข้าได้จริงไหมครับเพราะข้างล่างก่อนหน้าไม่มีการตอบกลับเลยมีแต่การใส่รหัสไปเรื่อยๆ 
จะได้ว่า username=admin&password=batman เอาไป hash เป็น md5
(ถ้ากอปมาระหว่างจะผิดเหมือนผม555 เพราะมันเป็น passwd=batman อยู่ ทำให้ hash ที่ได้จะไม่ตรงกัน)

## NCSA{7341098813e23f5c064a869b1979d340}