import random
import textwrap
import time
import csv
from datetime import datetime

# -----------------------------
# Trivia Quiz Game (Expanded Version)
# -----------------------------
# Each category now includes 5 questions.
# You can select up to 5 per category.
# -----------------------------

CHOICE_LABELS = ["A", "B", "C", "D"]

QUESTION_BANK = [
    # -----------------------------
    # GEOGRAPHY (5)
    # -----------------------------
    {
        "question": "What is the capital of France?",
        "choices": ["Madrid", "Paris", "Rome", "Berlin"],
        "answer_index": 1,
        "category": "Geography",
    },
    {
        "question": "Which ocean is the largest by area?",
        "choices": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer_index": 2,
        "category": "Geography",
    },
    {
        "question": "How many continents are there?",
        "choices": ["5", "6", "7", "8"],
        "answer_index": 2,
        "category": "Geography",
    },
    {
        "question": "Which river flows through Egypt?",
        "choices": ["Amazon", "Danube", "Nile", "Mississippi"],
        "answer_index": 2,
        "category": "Geography",
    },
    {
        "question": "Mount Everest lies in which mountain range?",
        "choices": ["Andes", "Himalayas", "Alps", "Rockies"],
        "answer_index": 1,
        "category": "Geography",
    },

    # -----------------------------
    # SCIENCE (5)
    # -----------------------------
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer_index": 1,
        "category": "Science",
    },
    {
        "question": "The chemical symbol 'Na' stands for which element?",
        "choices": ["Nitrogen", "Sodium", "Neon", "Nickel"],
        "answer_index": 1,
        "category": "Science",
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "choices": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
        "answer_index": 1,
        "category": "Science",
    },
    {
        "question": "What part of the human body controls balance?",
        "choices": ["Heart", "Inner ear", "Lungs", "Brain"],
        "answer_index": 1,
        "category": "Science",
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "choices": ["Mercury", "Iron", "Silver", "Lead"],
        "answer_index": 0,
        "category": "Science",
    },

    # -----------------------------
    # LITERATURE (5)
    # -----------------------------
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "answer_index": 0,
        "category": "Literature",
    },
    {
        "question": "Who wrote 'Pride and Prejudice'?",
        "choices": ["Emily Brontë", "Jane Austen", "Louisa May Alcott", "George Eliot"],
        "answer_index": 1,
        "category": "Literature",
    },
    {
        "question": "Which novel features the character 'Huckleberry Finn'?",
        "choices": ["Moby Dick", "The Adventures of Huckleberry Finn", "Treasure Island", "Oliver Twist"],
        "answer_index": 1,
        "category": "Literature",
    },
    {
        "question": "Who wrote the poem 'The Raven'?",
        "choices": ["Edgar Allan Poe", "Robert Frost", "Walt Whitman", "T.S. Eliot"],
        "answer_index": 0,
        "category": "Literature",
    },
    {
        "question": "In George Orwell’s 'Animal Farm', what type of animal is Boxer?",
        "choices": ["Horse", "Pig", "Dog", "Sheep"],
        "answer_index": 0,
        "category": "Literature",
    },

    # -----------------------------
    # MATH (5)
    # -----------------------------
    {
        "question": "What is 7 × 8?",
        "choices": ["54", "56", "64", "58"],
        "answer_index": 1,
        "category": "Math",
    },
    {
        "question": "What is the square root of 81?",
        "choices": ["8", "9", "10", "11"],
        "answer_index": 1,
        "category": "Math",
    },
    {
        "question": "What is 12 divided by 3?",
        "choices": ["4", "5", "6", "3"],
        "answer_index": 0,
        "category": "Math",
    },
    {
        "question": "What is the perimeter of a square with side 5?",
        "choices": ["10", "15", "20", "25"],
        "answer_index": 2,
        "category": "Math",
    },
    {
        "question": "What is 15% of 200?",
        "choices": ["25", "30", "35", "40"],
        "answer_index": 1,
        "category": "Math",
    },

    # -----------------------------
    # CULTURE (5)
    # -----------------------------
    {
        "question": "Which language is primarily spoken in Brazil?",
        "choices": ["Portuguese", "Spanish", "French", "English"],
        "answer_index": 0,
        "category": "Culture",
    },
    {
        "question": "Which country is famous for the traditional dance 'Flamenco'?",
        "choices": ["Spain", "Italy", "Argentina", "Portugal"],
        "answer_index": 0,
        "category": "Culture",
    },
    {
        "question": "Sushi is a traditional food of which country?",
        "choices": ["China", "Japan", "Thailand", "Korea"],
        "answer_index": 1,
        "category": "Culture",
    },
    {
        "question": "Diwali is a festival celebrated in which country?",
        "choices": ["India", "China", "Turkey", "Egypt"],
        "answer_index": 0,
        "category": "Culture",
    },
    {
        "question": "The Eiffel Tower is located in which city?",
        "choices": ["Rome", "Paris", "London", "Berlin"],
        "answer_index": 1,
        "category": "Culture",
    },

    # -----------------------------
    # TECH (5)
    # -----------------------------
    {
        "question": "In computing, what does 'CPU' stand for?",
        "choices": ["Central Processing Unit", "Computer Power Unit", "Central Program Utility", "Core Power Unit"],
        "answer_index": 0,
        "category": "Tech",
    },
    {
        "question": "Which year did the first iPhone release?",
        "choices": ["2005", "2007", "2009", "2011"],
        "answer_index": 1,
        "category": "Tech",
    },
    {
        "question": "What does 'HTML' stand for?",
        "choices": ["Hyper Text Markup Language", "Hyperlink and Text Management Language", "High Transfer Machine Language", "Hyper Terminal Machine Link"],
        "answer_index": 0,
        "category": "Tech",
    },
    {
        "question": "Who founded Microsoft?",
        "choices": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"],
        "answer_index": 1,
        "category": "Tech",
    },
    {
        "question": "What does USB stand for?",
        "choices": ["Universal Serial Bus", "Unique System Base", "Unified Software Bridge", "Universal Signal Band"],
        "answer_index": 0,
        "category": "Tech",
    },
]


# -----------------------------
# Helper functions
# -----------------------------
def wrap(text: str, width: int = 70) -> str:
    return "\n".join(textwrap.wrap(text, width=width))


def prompt_int(message: str, default: int | None = None, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(f"{message} ").strip()
        if not raw and default is not None:
            return default
        if raw.isdigit():
            value = int(raw)
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
        print("Please enter a valid number.")


def choose_category(questions: list[dict]) -> str | None:
    categories = sorted({q.get("category", "General") for q in questions})
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"  {i}. {cat}")
    print("  0. All categories")

    idx = prompt_int("Choose a category number (0 for All):", default=0, min_value=0, max_value=len(categories))
    if idx == 0:
        return None
    return categories[idx - 1]


def save_score(name: str, score: int, total: int, duration: float):
    with open("scores.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), name, score, total, f"{duration:.1f}s"])


def ask_question(q: dict, qnum: int, total: int) -> bool:
    print("\n" + "-" * 60)
    print(f"Question {qnum}/{total}")
    print(wrap(q["question"]))

    indices = list(range(len(q["choices"])))
    random.shuffle(indices)
    shuffled = [q["choices"][i] for i in indices]
    correct_label = CHOICE_LABELS[indices.index(q["answer_index"])]

    for label, choice in zip(CHOICE_LABELS, shuffled):
        print(f"  {label}. {choice}")

    while True:
        ans = input("Your answer (A/B/C/D or Q to quit): ").strip().upper()
        if ans == "Q":
            raise KeyboardInterrupt
        if ans in CHOICE_LABELS[:len(shuffled)]:
            is_correct = ans == correct_label
            if is_correct:
                print("✅ Correct!")
            else:
                correct_text = shuffled[CHOICE_LABELS.index(correct_label)]
                print(f"❌ Incorrect. Correct answer: {correct_label}. {correct_text}")
            return is_correct
        print("Please enter A, B, C, or D (or Q to quit).")


# -----------------------------
# Main quiz logic
# -----------------------------
def run_quiz(questions: list[dict]):
    print("\nWelcome to the Trivia Quiz!")
    selected_category = choose_category(questions)

    if selected_category:
        pool = [q for q in questions if q["category"] == selected_category]
    else:
        pool = questions[:]

    random.shuffle(pool)
    total_questions = prompt_int(
        "How many questions would you like? (default: 5):",
        default=5,
        min_value=1,
        max_value=len(pool)
    )
    pool = pool[:total_questions]

    name = input("\nEnter your name: ").strip() or "Player"
    score = 0
    wrong = []
    start_time = time.time()

    try:
        for i, q in enumerate(pool, start=1):
            if ask_question(q, i, total_questions):
                score += 1
            else:
                wrong.append(q)
    except KeyboardInterrupt:
        print("\nYou quit the quiz early.")

    duration = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"Your score: {score}/{len(pool)} ({(score/len(pool))*100:.0f}%)")
    print(f"⏱ Time taken: {duration:.1f} seconds")

    save_score(name, score, len(pool), duration)

    if wrong:
        print("\nYou missed these:")
        for q in wrong:
            print(f"❌ {q['question']}")
            print(f"   ✔ {q['choices'][q['answer_index']]}")

    print("\n✅ Score saved to scores.csv")
    print("Thanks for playing!\n")


if __name__ == "__main__":
    run_quiz(QUESTION_BANK)
