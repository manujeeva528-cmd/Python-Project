def run_quiz():
    questions=[
         {"question": "What is the capital of France?", 
          "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"], 
          "answer": "C"},

         {"question": "What is the largest planet in our solar system?", 
          "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B"},

         {"question": "Who wrote 'Romeo and Juliet'?",
           "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
             "answer": "B"},

             {"question": "What is the chemical symbol for water?",
              "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
              "answer": "B"}
    ]
    score=0
    for index,q in enumerate(questions):  
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer=input("Your answer (A/B/C/D): ").strip().upper()
        if answer==q["answer"]:
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"Quiz Over! Your total score is {score} out of {len(questions)}.")

run_quiz()