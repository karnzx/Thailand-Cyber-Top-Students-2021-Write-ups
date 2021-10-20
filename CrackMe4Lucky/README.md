# CrackMe4Lucky

**Category:** forensics
**Points:** 100

**Description:**
[CrackMe4Lucky.zip](https://github.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/raw/main/CrackMe4Lucky/CrackMe4Lucky.zip)
## write-up

เปิด CrackMe4Lucky.zip จะเห็นได้ว่ามีไฟล์แปลกชื่อ CrackMe4Lu.cky พอเอาออกมาเซ็คดูด้วย `$ file` CrackMe4Lu.cky  จะได้ว่ามันเป็นไฟล์ .zip นี่นา เปลี่ยนไฟล์ extension เป็น Crackme4Lucky_2.zip ก็จะเปิดได้ แต่! แตกไฟล์ไม่ได้ ไฟล์ถูกเข้ารหัสอีกแล้ววว โอเคไม่เป็นไรเพราะเรามี john the ripper ใช้วิธีเดิมเลย

```
$ zip2john CrackMe4Lucky_2.zip > hash
$ john -w=/usr/share/wordlists/rockyou.txt hash
```

ได้รหัสผ่านคือ admin แตกไฟล์ได้

![file(exe)](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/file(exe).png)

จะได้ไฟล์มาตัวหนึ่งที่เปิดไม่ได้ หรือว่ามันไม่ใช่ .exe ? ลองใช้ $ file เหมือนเดิม

![checkfile(exe)](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/check%20file%20(exe).png)

นั้นไง PNG นี่นา เปลี่ยนจาก .exe เป็น .png ก็จะได้

![POPCAT](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/popcat.png)

น้องแมววว ที่กำลังเป็นกระแสเลย POPCAT ถึงตรงนี้คือติดอยู่นานเลยครับ จนในที่สุดลองเปิดด้วย hex editor มันมีไฟล์ exe ซ่อนอยู่ ทำการตัดต้องแต่ตำแหน่งที่ 2A4494 ถึง 2BF493 มาสร้างเป็นไฟล์ใหม่ .exe ผมต้องชื่อว่า inner.exe

พอเปิดขึ้นมาจะได้ตามลำดับดังนี้

![hello](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/hello.png)

![programe](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/programe.png)

ถึงตอนนี่ก็งงกว่าเดิมใช้เวลาอยู่นานเลยกดไปกดมาไม่ได้ซะที คำใบ้ก็ไม่เก็ตซักนิด5555 ไปต่อไม่ถูกแต่ก็ได้มาว่าถ้าลองเอาไปเปิดใน Notepad จะเห็นส่วนนี้

![on notepad](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/notepad.png)

แล้วลองเปิดด้วย radare2 (ใช้คำสั่ง izz)

![on notepad](https://raw.githubusercontent.com/karnzx/Thailand-Cyber-Top-Students-2021-Write-ups/main/CrackMe4Lucky/rad2.png)

## NCSA{83d2ed77ed059051484c964c0aabada9}