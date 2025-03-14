# 🎶 **TransArt - Tamil Audio Transcription, Translation & Art Generation**

---

## 🌟 **Project Overview**
TransArt is a cutting-edge application that seamlessly integrates advanced AI models to perform Tamil audio transcription, English translation, image generation, and text generation. Powered by Groq API and Hugging Face's Stable Diffusion model, this app transforms audio content into creative outputs with ease.

---

## 🚀 **Key Features**
✅ Tamil Audio to Text Transcription (Whisper Large v3)
✅ Tamil Text to English Translation
✅ English Text to Image Generation (Stable Diffusion 2)
✅ English Text Generation (AI-Powered Creative Writing)

---

## 🛠️ **Tech Stack**
| Component           | Technology         |
|-----------------|--------------------|
| Language           | Python                |
| UI Framework    | Gradio                |
| API Integration | Groq API              |
| Image Generation | Hugging Face API |
| Image Handling | Pillow                  |

---

## 📂 **File Structure**
```
TransArt-App/
│
├── app.py                  # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignore unnecessary files
```

---

## 🌐 **Installation Guide**

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/madhan96p/TransArt-HF.git
```

### 2️⃣ Navigate to the project directory:
```bash
cd TransArt-HF
```

### 3️⃣ Create a virtual environment (optional but recommended):
```bash
python -m venv transart-env
source transart-env/bin/activate  # For Linux/Mac
transart-env\Scripts\activate     # For Windows
```

### 4️⃣ Install the dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔑 **API Keys Configuration**
Create a `.env` file and add the following keys:
```env
GROQ_API_KEY=your_groq_api_key
HF_API_KEY=your_hugging_face_api_key
```

---

## 🎯 **How to Run the App**
```bash
python app.py
```
Access the Gradio interface via the link provided in the terminal.

---

## 🎨 **Workflow**
1️⃣ Upload Tamil audio.
2️⃣ Get Tamil transcription.
3️⃣ Translate to English.
4️⃣ Generate an image or text based on the translation.

---

## ✅ **Example Output**
| Input                 | Output                |
|-----------------|---------------------|
| Tamil Audio 🎵 | "என் பெயர் பிரகதீஷ்" |
| Translated Text 📜 | "My name is Pragadeesh" |
| Generated Image 🖼️ | 🎨 Artistic visual |
| Generated Text 📝 | "A creative story begins..." |

---

## 🛡️ **Error Handling**
- Handles API errors and invalid inputs
- Displays user-friendly error messages

---

## 🤝 **Contributions**
We welcome contributions! Feel free to fork and raise pull requests.

---

## 📬 **Contact**
📧 **Email:** pragadeesh.s96@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/praga1482](https://linkedin.com/in/praga1482)  
💻 **GitHub:** [github.com/madhan96p](https://github.com/madhan96p)

