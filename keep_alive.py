from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Evlyn is awake and running!"

def run():
    # บังคับให้รันบนพอร์ต 8080 ซึ่งเป็นพอร์ตมาตรฐานที่ Render มองหา
    app.run(host='0.0.0.0', port=8080)

def keep_awake():
    # แยกการทำงานของเว็บออกไปอีกเส้นทาง (Thread) เพื่อไม่ให้บอท Discord ค้าง
    t = Thread(target=run)
    t.start()