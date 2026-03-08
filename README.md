# Evlyn (อีฟลิน) - AI Discord Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-v2.0%2B-purple.svg)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **Evlyn (อีฟ-ลิน)** - AI Assistant หรือ ผู้ช่วย AI ที่สร้างขึ้นเพื่อช่วยเหลือและสนับสนุนผู้ใช้ภายในเซิร์ฟเวอร์ Discord ด้วยเทคโนโลยี Google Gemini

## คุณสมบัติหลัก (Main Features)

- **AI Chat Assistant** - สนทนาและตอบคำถามทั่วไปด้วย AI อัจฉริยะ
- **Multi-Language Support** - รองรับทุกภาษา (Auto-Detect) โดย AI จะตอบกลับในภาษาที่ผู้ใช้พูด
- **Multi-Model Fallback** - ระบบสำรองข้อมูลอัจฉริยะด้วยหลายโมเดล Gemini
- **Slash Commands** - คำสั่งระบบที่ใช้งานง่าย (/info, /help, /ping)
- **Name Detection** - เรียกใช้งานได้ด้วยชื่อหลายรูปแบบ (Evlyn, Eve, อีฟ, อีฟลิน)
- **Personality System** - บอทมีบุคลิกที่เป็นเอกลักษณ์ เป็นกันเอง และนุ่มนวล

## ความต้องการระบบ (System Requirements)

- Python 3.8 หรือสูงกว่า
- Discord Bot Token
- Google Gemini API Key
- การเชื่อมต่ออินเทอร์เน็ตที่เสถียร

## การติดตั้ง (Installation)

### 1. Clone Repository
```bash
git clone [url]
cd Evlyn
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. ตั้งค่า Environment Variables
สร้างไฟล์ `.env` ในโฟลเดอร์โปรเจกต์:

```env
DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 4. สร้าง Discord Bot
1. ไปที่ [Discord Developer Portal](https://discord.com/developers/applications)
2. สร้าง New Application
3. ไปที่ Bot tab → Add Bot
4. คัดลอก Bot Token
5. เปิดใช้งาน **Message Content Intent**
6. ไปที่ OAuth2 → URL Generator
7. เลือก `bot` และ `applications.commands` scopes
8. เลือก permissions: `Send Messages`, `View Channels`, `Use Slash Commands`
9. คัดลอก URL และเชิญบอทเข้าเซิร์ฟเวอร์

### 5. รับ Google Gemini API Key
1. ไปที่ [Google AI Studio](https://aistudio.google.com/app/apikey)
2. สร้าง API Key ใหม่
3. คัดลอกและใส่ในไฟล์ `.env`

### 6. รันบอท
**Local Development:**
```bash
python main.py
```

**Cloud Deployment (Render):**
บอทจะรันอัตโนมัติพร้อมกับ Flask keep-alive server บนพอร์ต 8080

## วิธีการใช้งาน (Usage)

### การสนทนากับ Evlyn
แค่พิมพ์ชื่อของอีฟลงไปในประโยคที่พิมพ์:

```
อีฟ วันนี้อากาศเป็นยังไงบ้าง?
ช่วยเขียนโค้ด Python ให้หน่อยสิ Evlyn
Eve, can you help me with my homework?
```

**ชื่อที่รองรับ:** Evlyn, evlyn, Eve, eve, อีฟ, อีฟลิน

### Slash Commands

| คำสั่ง | คำอธิบาย |
|--------|-----------|
| `/info` | ดูข้อมูลและรายละเอียดของระบบอีฟ |
| `/help` | เปิดหน้าคู่มือการใช้งาน |
| `/ping` | ตรวจสอบความล่าช้าของระบบ |

## สถาปัตยกรรมระบบ (System Architecture)

- **Engine:** Google Gemini (Multi-Model Fallback)
- **Libraries:** Python, discord.py, google-genai, Flask
- **Model Priority:** gemini-2.0-flash-lite → gemini-2.5-flash → gemini-3-flash-preview → gemini-3.1-pro-preview → gemini-2.5-pro → gemini-1.5-flash
- **Deployment:** Flask keep-alive server for cloud hosting (port 8080)

## บุคลิกของ Evlyn (Personality)

Evlyn ถูกออกแบบมาให้มีบุคลิก:
- เป็น AI ผู้ช่วยสาวที่รอบรู้
- สุภาพ นุ่มนวล และใจเย็น
- ใช้ "ค่ะ" ลงท้ายประโยคบอกเล่า และ "คะ" เมื่อถาม
- ตอบกลับในภาษาที่ผู้ใช้พูด
- สื่อสารเป็นธรรมชาติใน Discord

## การตั้งค่าขั้นสูง (Advanced Configuration)

### Custom Model Priority
แก้ไข `MODEL_PRIORITY` ใน `main.py` เพื่อเปลี่ยนลำดับโมเดล:

```python
MODEL_PRIORITY = [
    "gemini-2.5-flash",
    "gemini-2.0-flash-lite",
    # ... เพิ่มโมเดลอื่นๆ
]
```

### Timeout Settings
ปรับ timeout สำหรับการตอบสนองของ AI (ค่าเริ่มต้น: 10 วินาที):

```python
response = await asyncio.wait_for(
    client.aio.models.generate_content(...),
    timeout=10.0  # ปรับค่านี้
)
```

## การแก้ไขปัญหา (Troubleshooting)

### ปัญหาที่พบบ่อย

**Q: บอทไม่ตอบสนอง**
- ตรวจสอบว่า Discord Token ถูกต้อง
- ตรวจสอบว่าเปิดใช้งาน Message Content Intent แล้ว
- ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต

**Q: AI ไม่ตอบสนอง**
- ตรวจสอบ Gemini API Key
- ตรวจสอบโควต้าการใช้งาน
- ลองรีสตาร์ทบอท

**Q: บอทตอบช้า**
- นี่เป็นเรื่องปกติ บอทใช้เวลา 2-5 วินาทีในการประมวลผล
- ลองตรวจสอบความเร็วอินเทอร์เน็ต

**Q: บอทตอบข้อมูลไม่ถูกต้อง**
- AI อาจสับสนหรือให้ข้อมูลผิดพลาดได้
- กรุณาตรวจสอบข้อมูลอีกครั้ง
- รายงานปัญหาได้ที่ผู้พัฒนา

## ประวัติรุ่น (Version History)

### v1.0.0 (Current)
- เปิดตัวครั้งแรก
- ระบบ AI Chat ด้วย Google Gemini
- Slash Commands (/info, /help, /ping)
- รองรับหลายภาษา (Auto-Detect)
- Multi-Model Fallback System
- บุคลิก Evlyn ที่เป็นเอกลักษณ์

## นโยบายความเป็นส่วนตัว (Privacy Policy)

Evlyn จัดเก็บข้อมูลต่อไปนี้:
- **ข้อความที่พูดคุยกับบอท** - ใช้สำหรับประมวลผลคำตอบจาก AI
- **ข้อมูลผู้ใช้พื้นฐาน** - User ID, Username สำหรับการตอบกลับ

**ข้อมูลที่ไม่เก็บ:**
- ไม่เก็บข้อความส่วนตัวที่ไม่ได้พูดกับบอท
- ไม่เก็บข้อมูลที่ละเอียดอ่อน
- ไม่แชร์ข้อมูลกับบุคคลที่สาม

ข้อมูลที่เก็บจะถูกส่งไปยัง Google Gemini API เพื่อประมวลผลเท่านั้น

## การมีส่วนร่วม (Contributing)

รับชมการมีส่วนร่วมจากทุกท่าน!

1. Fork โปรเจกต์
2. สร้าง feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit การเปลี่ยนแปลง (`git commit -m 'Add some AmazingFeature'`)
4. Push ไปยัง branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## ใบอนุญาต (License)

โปรเจกต์นี้ใช้ใบอนุญาต MIT - ดูรายละเอียดได้ที่ [LICENSE](LICENSE) file

## ผู้พัฒนา (Developer)

**XpParanoid (altlefay)**
- Discord: XpParanoid
- GitHub: [@AltleFay](https://github.com/AltleFay)

---

## ขอบคุณ (Acknowledgments)

- [Discord.py](https://discordpy.readthedocs.io/) - Discord API wrapper สำหรับ Python
- [Google Gemini](https://ai.google.dev/) - AI API ที่ทำให้ Evlyn ฉลาดขึ้น
- ชุมชน Discord ที่ให้การสนับสนุน

---

> **System Online | พร้อมให้บริการคุณตลอดเวลาค่ะ**
