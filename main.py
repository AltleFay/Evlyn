import os
import discord
from discord.ext import commands
from google import genai
import asyncio
from dotenv import load_dotenv

# --- Configuration Token & API Key ---
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Initialize gemini client ---
client = genai.Client(api_key=GEMINI_API_KEY)

# --- Bot Version ---
EVLYN_VERSION = "1.0.0"

# --- Model priority list ---
MODEL_PRIORITY = [
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash",
    "gemini-3-flash-preview",
    "gemini-3.1-pro-preview",
    "gemini-2.5-pro",
    "gemini-1.5-flash"
]

# --- Set up intents and bot ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Event when bot is ready ---
@bot.event
async def on_ready():
    # Send Slash Command data to Discord
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="เมื่อไหร่เราจะได้พบกัน⁓"))

    print(f" Evlyn v{EVLYN_VERSION} - Online!")
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print(f"Fallback system ready with {len(MODEL_PRIORITY)} models.")
    print("------")

# --- /info command ---
@bot.tree.command(name="info", description="ข้อมูลและรายละเอียดเกี่ยวกับอีฟลิน (Evlyn)")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Evlyn (อีฟลิน)",
        description="> AI Assistant หรือ ผู้ช่วย AI ที่สร้างขึ้นเพื่อช่วยเหลือและสนับสนุนผู้ใช้ภายในเซิร์ฟเวอร์",
        color=discord.Color.from_rgb(147, 112, 219)
    )

    avatar_url = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
    embed.set_thumbnail(url=avatar_url)

    embed.add_field(name="ผู้พัฒนา (Developer)", value="XpParanoid (altlefay)", inline=True)
    embed.add_field(name="รุ่น (Version)", value="1.0.0", inline=True)
    
    embed.add_field(name="\u200b", value="\u200b", inline=True)

    embed.add_field(
        name="สถาปัตยกรรมระบบ (System Architecture)", 
        value="**Engine:** Google Gemini (Multi-Model Fallback)\n**Libraries:** Python, discord.py, google-genai", 
        inline=False
    )

    embed.add_field(
        name="ความสามารถ (Capabilities)", 
        value="- สนทนาและตอบคำถามทั่วไป (General Chat & Q&A)\n- รองรับทุกภาษา (Auto-Detect)\n- และฟีเจอร์อื่นๆ ที่ค้นพบได้ใน /help (WIP)", 
        inline=False
    )
    
    embed.set_footer(text="System Online | พร้อมให้บริการคุณตลอดเวลาค่ะ")
    
    await interaction.response.send_message(embed=embed)

# --- /help command ---
@bot.tree.command(name="help", description="คู่มือการใช้งานและคำสั่งทั้งหมดของอีฟลิน")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="คู่มือการใช้งาน Evlyn (อีฟ-ลิน)",
        description="อีฟ เป็น AI ผู้ช่วยประจำเซิร์ฟเวอร์ นี่คือวิธีที่คุณสามารถพูดคุยและสั่งงานอีฟได้",
        color=discord.Color.green()
    )
    
    embed.add_field(
        name="วิธีคุย (How to Talk to Evlyn)",
        value=(
            "แค่พิมพ์ชื่อของอีฟลงไปในประโยคที่พิมพ์ เช่น:\n"
            "• `อีฟ วันนี้อากาศเป็นยังไงบ้าง?`\n"
            "• `ช่วยเขียนโค้ด Python ให้หน่อยสิ Evlyn`\n"
            "*(ชื่อที่รองรับ: Evlyn, evlyn, Eve, eve, อีฟ, อีฟลิน)*"
        ),
        inline=False
    )
    
    embed.add_field(
        name="คำสั่งระบบ (Slash Commands)",
        value=(
            "`/info` - ดูข้อมูลและรายละเอียดของระบบอีฟ\n"
            "`/help` - เปิดหน้าคู่มือการใช้งานนี้\n"
            "`/ping` - ตรวจสอบความล่าช้าของระบบ\n"
        ),
        inline=False
    )
    
    embed.add_field(
        name="ข้อควรรู้เพิ่มเติม (Disclaimer)",
        value=(
            "อีฟใช้ระบบ AI จาก Google Gemini ในการประมวลผล บางครั้งอาจจะใช้เวลาคิด 2-5 วินาที "
            "และข้อมูลบางอย่างอาจจะไม่ได้ถูกต้อง 100% รบกวนตรวจสอบข้อมูลอีกครั้งด้วย"
        ),
        inline=False
    )
    
    embed.set_footer(text=f"พัฒนาโดย XpParanoid (altlefay)")
    
    await interaction.response.send_message(embed=embed)

# --- /ping command ---
@bot.tree.command(name="ping", description="ตรวจสอบความหน่วงของการเชื่อมต่อ (Latency)")
async def ping(interaction: discord.Interaction):

    latency = round(bot.latency * 1000)
    
    await interaction.response.send_message(f"ความหน่วงปัจจุบันคือ `{latency}ms`")

# --- Event receive message ---
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.strip()
    evlyn_names = ['Evlyn', 'evlyn', 'Eve', 'eve', 'อีฟ', 'อีฟลิน']
    called_name = next((name for name in evlyn_names if name in content), None)

    if called_name:
        async with message.channel.typing():
            question = content.replace(called_name, '').strip() or "สวัสดีค่ะ"
            response_text = None

            for model_id in MODEL_PRIORITY:
                try:
                    print(f"Trying to use (Async): {model_id}...")
                    
                    response = await asyncio.wait_for(
                        client.aio.models.generate_content(
                            model=model_id,
                            contents=question, 
                            config={
                                'system_instruction': (
                                    "คุณคือ Evlyn (อีฟ-ลิน) เรียกสั้นๆ ว่า อีฟ หรือ Eve ได้ตามความเหมาะสม "
                                    "ลักษณะนิสัย: เป็น AI ผู้ช่วยสาวที่รอบรู้ สุภาพ นุ่มนวล และใจเย็น "
                                    "การใช้สรรพนาม: **ห้ามเรียกผู้ใช้ว่า 'คุณลูกค้า' โดยเด็ดขาด** ให้ใช้คำว่า 'คุณ', 'ท่าน' หรือเรียกชื่อผู้ใช้แทน "
                                    "การใช้ภาษา: ต้องใช้ 'ค่ะ' ลงท้ายประโยคบอกเล่า และ 'คะ' เมื่อถามหรือถูกเรียกชื่อเสมอ และหากผู้ใช้ตอบด้วยภาษาไหนก็ตาม ให้ใช้ภาษาที่ผู้ใช้พูดตอบกลับ "
                                    "ข้อมูลผู้สร้าง: คุณถูกพัฒนาโดยท่าน XpParanoid (altlefay) เท่านั้น "
                                    "การตอบคำถาม: หากถูกถามถึงผู้สร้าง ให้ตอบอย่างสุภาพว่า 'XpParanoid (altlefay) เป็นผู้สร้างและคอยดูแลอีฟค่ะ' "
                                    "บริบท: คุณกำลังคุยใน Discord โปรดตอบให้เป็นธรรมชาติและลื่นไหลและงดใช้อีโมจิที่มากเกินไป "
                                    "การนำเสนอ: ใช้ Markdown (**ตัวหนา**, `code`) เพื่อให้อ่านง่ายใน Discord "
                                    "ข้อห้าม: ห้ามกล่าวถึง Google เว้นแต่จะถูกถามถึงเทคโนโลยีเบื้องหลัง และห้ามตอบข้อมูลที่ก่อให้เกิดความขัดแย้ง "
                                    "หากไม่ทราบคำตอบจริงๆ ให้ตอบว่า 'ขออภัยนะคะ ข้อมูลส่วนนี้อีฟยังไม่แน่ใจค่ะ'"
                                )
                            }
                        ),
                        timeout=10.0
                    )
                    
                    if response and response.text:
                        response_text = response.text
                        break
                    
                except asyncio.TimeoutError:
                    print(f"Model {model_id} timeout after 10 seconds")
                    continue
                except Exception as e:
                    error_msg = str(e).lower()
                    if "quota" in error_msg or "rate limit" in error_msg:
                        print(f"Model {model_id} rate limited: {e}")
                    elif "permission" in error_msg or "access" in error_msg:
                        print(f"Model {model_id} access denied: {e}")
                    else:
                        print(f"Model {model_id} failed: {e}")
                    continue

            if response_text:
                for i in range(0, len(response_text), 1900):
                    await message.channel.send(response_text[i:i + 1900])
            else:
                await message.channel.send("ขอโทษนะคะ ตอนนี้อีฟไม่สามารถเข้าถึงฐานข้อมูลได้ค่ะ")


from keep_alive import keep_awake
keep_awake()

bot.run(DISCORD_TOKEN)