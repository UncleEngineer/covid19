# Covid19 Library by Uncle Engineer


สวัสดีจร้าาาา นี่ลุงวิศวกรเอง ไลบรารี่นี้ใช้สำหรับฝึกสร้างไลบรารี่เป็นของตัวเอง ความสามารถคือ

  - แสดงอัพเดตสถานการณ์ไวรัส COVID-19
  - อัพเดตทั้งโลกจากเว็บไซต์ https://www.worldometers.info/coronavirus/
  - อัดเดตของไทยจากเว็บไซต์กรมควบคุมโรค https://ddc.moph.go.th/viralpneumonia/ 


### วิธีติดตั้งแสนง่าย

ไปกดไลค์เพจลุงก่อนเลย [ลุงวิศวกร สอนคำนวณ](https://www.facebook.com/UncleEngineer)  ฮ่าาา ไม่บังคับ (กดไลค์เพจลุงหน่อยๆ 555)

เราจะติดตั้งผ่านเจ้า pip

```sh
pip install covid19uncle
```

ง่ายไหมล่ะ

วิธีใช้ก็ง่ายมาก
- เปิด Python แล้วพิพม์ตามนี้เลย

```sh
from covid19uncle import GlobalCovid19,ThaiCovid19

Example:

data = GlobalCovid19()
print(data['italy'])
print(data['italy']['total'])
print(data['italy']['new_cases'])
print(data['italy']['total_deaths'])
print(data['italy']['new_deaths'])
print(data['italy']['total_recoverd'])
print(data['italy']['active_cases'])
print(data['italy']['serious_critical'])
print(data['italy']['totalcase_per1million'])

print(data['header']) #show header
print(data['total'])  #show total
print(data['italy']['list']) #show list of Italy Information


thai = ThaiCovid19()

print('อัพเดต:', thai['อัพเดต'])
print('ผู้ป่วยสะสม', thai['ผู้ป่วยสะสม'])
print('ผู้ป่วยรายใหม่', thai['ผู้ป่วยรายใหม่'])
print('ผู้ป่วยรุนแรง', thai['ผู้ป่วยรุนแรง'])
print('ผู้ป่วยเสียชีวิต', thai['ผู้ป่วยเสียชีวิต'])
print('ผู้ป่วยกลับบ้านแล้ว', thai['ผู้ป่วยกลับบ้านแล้ว'])
print('ผู้ป่วยเฝ้าระวังสะสม', thai['ผู้ป่วยเฝ้าระวังสะสม'])
print('ผู้ป่วยเฝ้าระวังรายใหม่', thai['ผู้ป่วยเฝ้าระวังรายใหม่'])
print('รักษาพยาบาลอยู่รพ', thai['รักษาพยาบาลอยู่รพ.'])
print('รักษาพยาบาลกลับบ้าน', thai['รักษาพยาบาลกลับบ้าน'])
print('รักษาพยาบาลสังเกตอาการ', thai['รักษาพยาบาลสังเกตอาการ'])

print('ผู้เดินทางที่คัดกรองสะสมจากสนามบิน', thai['ผู้เดินทางที่คัดกรองสะสมจากสนามบิน'])
print('ผู้เดินทางที่คัดกรองสะสมจากท่าเรือ', thai['ผู้เดินทางที่คัดกรองสะสมจากท่าเรือ'])
print('ผู้เดินทางที่คัดกรองสะสมจากด่านพรมแดน', thai['ผู้เดินทางที่คัดกรองสะสมจากด่านพรมแดน'])
print('ผู้เดินทางที่คัดกรองสะสมจากสตม.แจ้งวัฒนะ', thai['ผู้เดินทางที่คัดกรองสะสมจากสตม.แจ้งวัฒนะ'])
print('อ้างอิง', thai['อ้างอิง'])


```

### Visit

แวะเข้าไปเยี่ยมชมกันได้ แหล่งกบดานเรามีสอนหลายวิชา

| เนื้อหา | ลิ้งค์ |
| ------ | ------ |
| ลุงมีวิชาอะไรบ้าง |http://uncle-engineer.com/ |
| อ่านบทความใน Medium  | https://medium.com/@UncleEngineer |
| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer |
| ------ | ------ |

### ติดตามตอนต่อไป...ในเพจ "ลุงวิศวกร สอนคำนวณ"
