import os
import speech_recognition as sr
import openai
from dotenv import load_dotenv


load_dotenv("config.env")
openai.api_key= os.getenv("API_KEY")

stt = sr.Recognizer()

with sr.Microphone() as source:
    print("لطفا صحبت کنید...")
    stt.adjust_for_ambient_noise(source)
    stt.pause_threshold =0.5
    audio = stt.listen(source, timeout=5, phrase_time_limit=10)

try:
    query = stt.recognize_google(audio, language='fa-IR')
    print("شما گفتید:", query)
except sr.WaitTimeoutError:
    print("زمان انتظار تمام شد. لطفا دوباره تلاش کنید.")
except sr.UnknownValueError:
    print("متوجه نشدم، لطفا واضح‌تر صحبت کنید.")
except sr.RequestError as e:
    print(f"مشکل در ارتباط با سرویس تشخیص صدا: {e}")

soal = query

response = openai.chat.completions.create(
    model="gpt-4o-mini",
messages=[
        {"role": "user", "content": soal}
    ],
max_tokens=1024,
temperature=0.5,
n=1,
)
Answer = response.choices[0].message.content
print(Answer, "ChatGPT:")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(Answer)