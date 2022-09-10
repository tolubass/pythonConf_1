#All Questions
question1 = "q1. what is the name of Nigeria president?"\
       "\n(a) Fayose"\
       "\n(b) jonathan"\
       "\n(c) Buhari"\

question2 = "\nq2. what is the capital of lagos state?"\
       "\n(a) Ikeja"\
       "\n(b) Akure"\
       "\n(c) Sokoto"\

question3 = "\nq3. what is the name of governor elect of osun state?"\
       "\n(a) Davido"\
       "\n(b) Adeleke"\
       "\n(c) Tinubu"\

question_bank = {question1: "c",
          question2: "a",
          question3: "b"}
print("Welcome to current affairs Nigeria quetsions")
print("=" *25)
score=0
for key in question_bank:
    print(key)
user_input = input("Type your answer(a/b/c/d):")
if user_input == question_bank[key]:
    score += 1
print(f"\nYour Score is :{score} / {len(question_bank)}")

