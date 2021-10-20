# Key

**Category:** Crypto
**Points:** 100

**Description:**
[key.zip](https://github.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/raw/main/Key/key.zip)

## write-up

เริ่มมาเราจะได้ไฟล์ key.zip ที่มีรูปภาพ key.jpg อยู่ข้างในแต่ต้องใช้รหัสผ่านเพื่อแตกไฟล์ออกมา ทำการใช้ john the ripper crack ออกมา เริ่มโดยการใช้ zip2john ดึง hash ออกมาแล้วให้ john crack hash นั้นด้วยใช้ wordlist rockyou.txt

เราก็จะได้ password เป็น qqaazzwwssxx1

แต่รูปดันเปิดไม่ได้นี่สิ นึกว่าจะเสร็จแล้วนะเนี่ยยย แปลว่า format ไฟล์น่าจะผิดอยู่ผิด ทำการเปิดไฟล์ขึ้นมาใหม่แต่เปิดด้วย hex editor อะไรก็ได้ ของผมใช้ HxD

![compare_file_signature.png](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/Key/compare_file_signature.png)

เปิดขึ้นมาแล้วตอนแรกก็งงๆผิดตรงไหน ที่ไหนได้ file signature ผิดอยู่เทียบกันจากรูปด้านบนโดยด้านซ้าย wiki file signatures ขวา hxd ของ key.jpg ผิดอยู่ 4 bytes

![on_edited.png](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/Key/on_edited.png)

แก้แล้วก็จะได้ตำตอบแบบในรูปเลยย เย่

## NCSA{4d4098d64e163d2726959455d04fd7c}