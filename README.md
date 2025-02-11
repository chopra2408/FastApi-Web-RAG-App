# AI-Powered Web Scraper & Query System

## 🚀 Overview
This project is an **AI-powered web scraper and query system** that processes web pages, extracts text, and allows users to ask questions based on the extracted content. The system leverages **FastAPI** for the backend, **FAISS** for vector storage, and **Groq's Llama 3.2 model** for AI-powered responses.

## ✨ Features
- 🌐 **Scrape Web Pages** – Extracts text from any given URL.
- 🔍 **AI-Powered Search** – Queries processed content using Llama 3.2.
- ⚡ **Fast & Efficient** – Uses FAISS for quick similarity search.
- 🎨 **Modern UI** – Dark-themed, responsive, and interactive frontend.
- 🚀 **Asynchronous Processing** – Ensures smooth user experience.

## 🛠️ Tech Stack
### **Backend**
- **FastAPI** – Handles API requests.
- **BeautifulSoup** – Scrapes web content.
- **LangChain & FAISS** – Splits and stores extracted content.
- **Groq API** – Provides AI-powered responses.

### **Frontend**
- **HTML, CSS, JavaScript** – Built for an interactive experience.
- **Dark Theme UI** – Modern, user-friendly design.
- **Responsive Layout** – Works on all devices.

## 📂 Project Structure
```
📦 ai-web-scraper
├── backend
│   ├── main.py  # FastAPI server
│   ├── utils.py  # Helper functions
│   ├── requirements.txt  # Dependencies
│
├── frontend
│   ├── index.html  # UI layout
│   ├── styles.css  # Styling (dark mode)
│   ├── script.js  # Client-side logic
│
├── README.md  # Project documentation
├── .env  # API keys and secrets
```

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-web-scraper.git
cd ai-web-scraper
```

### 2️⃣ Backend Setup
#### **Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```
#### **Set Up Environment Variables**
Create a `.env` file in the `backend` folder and add:
```
GROQ_API_KEY=your_groq_api_key_here
```
#### **Run FastAPI Server**
```bash
uvicorn main:app --reload
```

### 3️⃣ Frontend Setup
Simply open `frontend/index.html` in a browser or serve it with a local server:
```bash
cd frontend
python -m http.server 8000
```
Then, visit `http://localhost:8000`.

## 🎯 Usage Guide
### **Processing a Web Page**
1. Enter a **valid URL** in the input box.
2. Click **"Process"** to extract text from the webpage.
3. The system will store and index the content for queries.

### **Querying AI**
1. Type your **question** in the query box.
2. Click **"Get Answer"** to retrieve an AI-generated response.
3. View results in the response section.

## 🛠️ API Endpoints
### **1️⃣ Process URL**
```http
POST /process_url
```
#### Request Body:
```json
{
  "url": "https://example.com"
}
```
#### Response:
```json
{
  "message": "URL processed successfully"
}
```

### **2️⃣ Query System**
```http
POST /query
```
#### Request Body:
```json
{
  "prompt": "What is this article about?"
}
```
#### Response:
```json
{
  "answer": "The article discusses AI-powered web scraping...",
  "response_time": 0.82
}
```

## 📌 Future Improvements
- 📌 **Support for Multiple Pages** – Allow users to process multiple URLs.
- 📌 **Authentication** – Secure API with user authentication.
- 📌 **Django Migration** – Move backend to Django for better scalability.

