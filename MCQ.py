

question1="Q1. what is the name of the president of Nigeria?"\
            "\n(a)senator adeleke"\
          "\n(b)muhamadu buhari"\
          "\n(c)Ayodele Fayose"

question2="Q2. what is the capital of the Germany?"\
          "\n(a)Berlin"\
          "\n(b)Amstadarm"\
          "\n(c)Lublin"

question3="Q3. whic of the following is a wild animal?"\
          "\n(a)tiger"\
          "\n(b)goat"\
          "\n(c)hen"

question_bank = {question1: "b",
                 question2: "a",
                 question3: "a"}

print("welcome to MCQ")
print("Current affairs questions")
print("="*25)
score=0
for key in question_bank:
    print(key)
    user_input = input("Type your answer(a/b/c/d):")
    if user_input==question_bank[key]:
        score+=1
print(f"\nYou Score:{score} out of {len(question_bank)}")

