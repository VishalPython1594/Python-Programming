
'''

Quiz Application: 
Create a quiz with multiple-choice questions and keep track of the user's score. Display feedback based on their answers.


You can also take to next level by working on below :
 - Shuffle Questions: Use the random library to randomize the order of questions.
 - Track Number of Attempts: Allow multiple attempts per question and track the total number of attempts.
'''


questions = [
    ("What is the capital of France?", "A. Paris", "B. London", "C. Rome", "A"),
    ("What is the largest planet in our solar system?", "A. Earth", "B. Jupiter", "C. Mars", "B"),
    ("What is the chemical symbol for water?", "A. H2O", "B. CO2", "C. NaCl", "A"),
    ("What is the highest mountain in the world?", "A. Mount Everest", "B. K2", "C. Kilimanjaro", "A"),
    ("What is the name of the current president of the United States?", "A. Joe Biden", "B. Donald Trump", "C. Barack Obama", "A"),
    ("What is the smallest country in the world?", "A. Vatican City", "B. Monaco", "C. Nauru", "A"),
    ("What is the fastest land animal?", "A. Cheetah", "B. Lion", "C. Pronghorn antelope", "A"),
    ("What is the largest ocean in the world?", "A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "A"),
    ("What is the most abundant element in the Earth's atmosphere?", "A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "A"),
    ("What is the name of the first person to walk on the moon?", "A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "A")
]


score = 0
total_questions = len(questions)

for question, option1, option2, option3, correct_answer in questions:
    print(question)
    print(option1)
    print(option2)
    print(option3)

    user_answer = input("Enter your answer (A, B, or C): ")

    if user_answer.upper() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", correct_answer)

print("\nYour final score is", score, "out of", total_questions)
