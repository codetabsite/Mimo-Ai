import requests
from gtts import gTTS
import pygame
import os
import tempfile

API_KEY = "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"
MODEL = "nvidia/nemotron-nano-12b-v2-vl:free"
conversation = []

pygame.mixer.init()

ayarlar = {
    "ses": True,
    "dil": "tr",
    "max_token": 512
}

def konuş(metin):
    if not ayarlar["ses"]:
        return
    try:
        tts = gTTS(text=metin, lang=ayarlar["dil"])
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            tmp = f.name
        tts.save(tmp)
        pygame.mixer.music.load(tmp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        os.remove(tmp)
    except Exception as e:
        print(f"Ses hatası: {e}")

def sor_mimo(user_input):
    conversation.append({"role": "user", "content": user_input})
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "MiMo Chatbot"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "Sen Türkçe konuşan yardımcı bir asistansın. Kısa ve net cevaplar ver."}
                ] + conversation,
                "max_tokens": ayarlar["max_token"]
            },
            timeout=30
        )
        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
            conversation.append({"role": "assistant", "content": reply})
            return reply
        else:
            hata = data.get("error", {}).get("message", str(data))
            print(f"API Hatası: {hata}")
            conversation.pop()
            return None

    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        conversation.pop()
        return None

def ayar_menusu():
    while True:
        print("\n╔══════════════════════╗")
        print("║      ⚙️  AYARLAR      ║")
        print("╠══════════════════════╣")
        print(f"║ 1. Ses: {'✅ Açık  ' if ayarlar['ses'] else '❌ Kapalı'}       ║")
        print(f"║ 2. Dil: {ayarlar['dil']}              ║")
        print(f"║ 3. Max Token: {ayarlar['max_token']}      ║")
        print("║ 4. Sohbeti Sıfırla   ║")
        print("║ 0. Geri              ║")
        print("╚══════════════════════╝")

        seçim = input("Seçim: ").strip()

        if seçim == "1":
            ayarlar["ses"] = not ayarlar["ses"]
            print("Ses", "açıldı ✅" if ayarlar["ses"] else "kapatıldı ❌")
        elif seçim == "2":
            print("Dil seç: tr / en / de / fr")
            yeni = input("Dil: ").strip()
            if yeni in ["tr", "en", "de", "fr"]:
                ayarlar["dil"] = yeni
                print(f"Dil {yeni} oldu.")
            else:
                print("Geçersiz dil.")
        elif seçim == "3":
            yeni = input("Token (256/512/1024): ").strip()
            if yeni.isdigit():
                ayarlar["max_token"] = int(yeni)
                print(f"Max token {yeni} oldu.")
        elif seçim == "4":
            conversation.clear()
            print("Sohbet sıfırlandı ✅")
        elif seçim == "0":
            break

print("=== MiMo Chatbot ===")
print("'ayar' → Ayarlar")
print("'q'    → Çıkış")
print("=" * 20)

while True:
    try:
        user_input = input("\nSen: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "q":
            print("Güle güle!")
            break
        if user_input.lower() == "ayar":
            ayar_menusu()
            continue

        print("⏳ Düşünüyor...")
        cevap = sor_mimo(user_input)
        if cevap:
            print(f"\nMiMo: {cevap}")
            konuş(cevap)

    except KeyboardInterrupt:
        print("\nGüle güle!")
        break
