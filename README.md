<div align="center">

# 🤖 Gemini Terminal Assistant
### 🌍 Bilingual CLI Chatbot & Automation Tool

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Google GenAI](https://img.shields.io/badge/Google%20GenAI%20SDK-Latest-orange?logo=google)
![Gemini 3.1 Flash-Lite](https://img.shields.io/badge/Model-Gemini%203.1%20Flash--Lite-4E75F8)
![License](https://img.shields.io/badge/License-MIT-green)

<p align="center">
  <b>Python ve resmi <code>google-genai</code> SDK mimarisiyle geliştirilmiş, oturum boyunca bağlam geçmişini koruyan iki dilli komut satırı asistanı.</b>
</p>

</div>

---

## 🇹🇷 Türkçe Hızlı Başlangıç

### 📊 Adım Adım Kurulum Çizelgesi

| No | İşlem | Komut / Açıklama |
| :---: | :--- | :--- |
| **1** | **Repoyu Klonlama** | `git clone [https://github.com/canseker812-ops/gemini-terminal-assistant.git](https://github.com/canseker812-ops/gemini-terminal-assistant.git)`<br>`cd gemini-terminal-assistant` |
| **2** | **Kütüphaneleri Yükleme** | `pip install -r requirements.txt` |
| **3** | **API Anahtarı Alma** | [Google AI Studio](https://aistudio.google.com) üzerinden ücretsiz anahtar oluşturun. |
| **4** | **Anahtarı Tanımlama** | **PowerShell:** `$env:GEMINI_API_KEY="ANAHTARINIZ"`<br>**Linux/macOS:** `export GEMINI_API_KEY="ANAHTARINIZ"` |
| **5** | **Uygulamayı Çalıştırma** | `python src/main.py` |

<br>

### 💻 Komut Satırı Kullanımı

Terminalinizde sırasıyla çalıştıracağınız kod blokları:

```powershell
# 1. Ortam değişkenini belirleyin
$env:GEMINI_API_KEY="AIzaSy...ANAHTARINIZ"

# 2. Asistanı başlatın
python src/main.py
```

> 💡 **İpucu:** Çıkış yapmak için sohbete `q`, `exit` veya `cikis` yazmanız yeterlidir.

---

## 🇬🇧 English Documentation

### 📊 Step-by-Step Execution Plan

| Step | Action | Command / Details |
| :---: | :--- | :--- |
| **1** | **Clone Repo** | `git clone [https://github.com/canseker812-ops/gemini-terminal-assistant.git](https://github.com/canseker812-ops/gemini-terminal-assistant.git)`<br>`cd gemini-terminal-assistant` |
| **2** | **Install Deps** | `pip install -r requirements.txt` |
| **3** | **Get API Key** | Create an API key at [Google AI Studio](https://aistudio.google.com). |
| **4** | **Set Environment** | **PowerShell:** `$env:GEMINI_API_KEY="YOUR_API_KEY"`<br>**Linux/macOS:** `export GEMINI_API_KEY="YOUR_API_KEY"` |
| **5** | **Run Project** | `python src/main.py` |

<br>

### 💻 Terminal Execution

```bash
# 1. Export key (macOS/Linux)
export GEMINI_API_KEY="YOUR_API_KEY"

# 2. Launch assistant
python src/main.py
```

---

## 📁 Proje Dosya Düzeni (Project Architecture)

```text
gemini-terminal-assistant/
├── .gitignore          # Git dışı tutulacak dosyalar
├── requirements.txt    # Bağımlılık paketleri
├── metin.txt           # Test amaçlı veri metni
├── README.md           # Proje vitrini ve rehberi
└── src/
    └── main.py         # Asistan döngüsü ve API çağrıları
```
