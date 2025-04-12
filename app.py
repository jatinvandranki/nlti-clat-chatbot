from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)

# Step 1: Knowledge base
faq = {
    "What is the syllabus for CLAT 2025?": "CLAT 2025 includes English, GK, Legal Reasoning, Logical Reasoning, and Quantitative Techniques.",
    "How many questions are there in the English section?": "The English section typically has 28-32 questions.",
    "Give me last year’s cut-off for NLSIU Bangalore.": "In 2024, NLSIU Bangalore had a cut-off around 120-125 marks.",
    "Is there negative marking in CLAT?": "Yes, 0.25 marks are deducted for each wrong answer.",
    "How many total questions are in the CLAT exam?": "There are 150 questions in the CLAT UG exam."
}

# Step 2: NLP Matching Logic
def get_closest_answer(user_question, faq):
    questions = list(faq.keys())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions + [user_question])
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    best_match_index = similarity.argmax()
    return faq[questions[best_match_index]]

# Route to handle input/output
@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["query"]
        answer = get_closest_answer(user_input, faq)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
