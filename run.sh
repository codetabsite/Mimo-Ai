#!/bin/bash

cd "$(dirname "$0")"

# venv yoksa oluştur
if [ ! -d "venv" ]; then
    echo "⚙️  Sanal ortam oluşturuluyor..."
    python3 -m venv venv
fi

# venv aktif et
source venv/bin/activate

# paketleri kontrol et
echo "📦 Paketler kontrol ediliyor..."
pip install -q -r requirements.txt

# çalıştır
echo "🚀 MiMo başlatılıyor..."
python main.py
