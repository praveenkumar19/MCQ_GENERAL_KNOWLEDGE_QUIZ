quiz = [ 
    {"question": "1. What is the capital of India?", "options": ["1. Mumbai", "2. Delhi", "3. Kolkata", "4. Chennai"], "answer": "2"},
    {"question": "2. Which language is used for web development?", "options": ["1. Python", "2. Java", "3. JavaScript", "4. All of these"], "answer": "4"},
    {"question": "3. What is 5 + 7?", "options": ["1. 10", "2. 11", "3. 12", "4. 13"], "answer": "3"},
    {"question": "4. Who is known as the Father of Computers?", "options": ["1. Charles Babbage", "2. Alan Turing", "3. Tim Berners-Lee", "4. Bill Gates"], "answer": "1"},
    {"question": "5. Which company developed Python?", "options": ["1. Microsoft", "2. Sun Microsystems", "3. Google", "4. None of these"], "answer": "4"},
    {"question": "6. Which of these is a Python data type?", "options": ["1. String", "2. Integer", "3. List", "4. All of these"], "answer": "4"},
    {"question": "7. What does CPU stand for?", "options": ["1. Central Process Unit", "2. Central Processing Unit", "3. Control Processing Unit", "4. Central Peripheral Unit"], "answer": "2"},
    {"question": "8. HTML stands for?", "options": ["1. Hyper Text Markup Language", "2. Hyperlinks and Text Markup Language", "3. Home Tool Markup Language", "4. Hyperlinking Text Marking Language"], "answer": "1"},
    {"question": "9. Which of these is a loop in Python?", "options": ["1. for", "2. while", "3. do-while", "4. Both 1 and 2"], "answer": "4"},
    {"question": "10. What is the output of print(2**3)?", "options": ["1. 6", "2. 8", "3. 9", "4. 5"], "answer": "2"}
]

score = 0
for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_ans = input("Enter the correct option number: ")
    while user_ans not in ['1', '2', '3', '4']:
        print("Invalid input! Enter 1, 2, 3, or 4.")
        user_ans = input("Enter the correct option number: ")
    
    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_option = q["options"][int(q["answer"]) - 1]
        print(f"Wrong! Correct answer is: {correct_option}")

print(f"\nQuiz completed! Your final score is: {score}/{len(quiz)}")
