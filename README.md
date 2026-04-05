# 🤖 MiMo Chatbot

Xiaomi MiMo v2 Flash modeliyle çalışan sesli Türkçe chatbot.

## Kurulum

### 1. API Key ayarla
`main.py` dosyasını aç ve şu satırı düzenle:
```
API_KEY = "KEY_README"
```
OpenRouter'dan aldığın key'i yaz.

### 2. Çalıştır
```bash
bash run.sh
```
İlk çalıştırmada venv oluşturur ve paketleri yükler.

## Kullanım

| Komut | Açıklama |
|-------|----------|
| Herhangi bir şey yaz | MiMo cevap verir ve sesli okur |
| `ayar` | Ayarlar menüsünü açar |
| `q` | Çıkış |

## Ayarlar Menüsü

- **Ses aç/kapat** → MiMo'nun sesini açıp kapatır
- **Dil değiştir** → tr, en, de, fr
- **Max Token** → Cevap uzunluğu (256/512/1024)
- **Sohbeti sıfırla** → Hafızayı temizler

## Gereksinimler

- Python 3.8+
- İnternet bağlantısı
- OpenRouter API key

## Dosya Yapısı

```
aibot/
├── main.py          # Ana kod
├── requirements.txt # Paket listesi
├── run.sh           # Başlatma scripti
└── README.md        # Bu dosya
```
