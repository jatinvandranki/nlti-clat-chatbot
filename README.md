# nlti-clat-chatbot
Submission for NLTI Internship AI/ML Task
# NLTI Internship Assignment – Task 2

## 📌 Task: Legal Exam Query Chatbot

This project is a basic NLP-powered chatbot created to help CLAT aspirants by answering frequently asked questions related to the exam. It's a prototype designed to demonstrate how automation can make mentorship and support more scalable.

### 🧠 Sample Questions It Can Answer:
- “What is the syllabus for CLAT 2025?”
- “How many questions are there in the English section?”
- “Give me last year’s cut-off for NLSIU Bangalore.”

### 🛠️ Tools & Techniques Used:
- Python (with NLTK and Flask)
- Rule-based NLP matching (keywords and sentence patterns)
- Simple local knowledge base stored in a Python dictionary
- Web interface using Flask

### ✅ What the Chatbot Does:
- Accepts a user’s input (a query)
- Searches a small knowledge base for relevant answers
- Displays a response back to the user in a friendly way

---

## 📈 How It Works (Step-by-Step):

1. A mini knowledge base was created manually with CLAT-related FAQs and their answers.
2. The chatbot tokenizes and processes user input to look for key topics.
3. Based on keyword matching or phrase detection, it responds with a suitable answer.
4. Flask is used to host a simple web interface where users can type their queries.

---

## 📁 Files You’ll Find in This Project:
- `chatbot.py`: The backend logic for the chatbot (Flask app)
- `templates/index.html`: Simple HTML form to interact with the chatbot
- `requirements.txt`: Libraries required to run the app
- `README.md`: Overview of the project and setup guide

---

## 🚀 Ideas for Improvement:
- Add a feedback loop to refine answers based on user thumbs up/down
- Expand the knowledge base dynamically or load from external files
- Fine-tune a small LLM (e.g., DistilBERT) on CLAT FAQs for smarter answers

---

## 🙌 About Me:
Hi, I’m Jatin — a Computer Science student passionate about AI/ML and eager to create real-world solutions. This chatbot was built as part of my application for the NLTI internship to support law aspirants with quick, accurate answers.

