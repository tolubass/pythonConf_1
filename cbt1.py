from cbt import Questions

questions_quest = [
    "1.which of the following is an Animal?\n(a) Book\n(b) pen\n(c) goat\n\n",
    "2.how many states are in Nigeria?\n(a) 25\n(b) 36\n(c) 40\n\n",
    "3.who is the president of Nigeria?\n(a) Buhari\n(b) biden\n(c) fayose\n\n"
]

questions = [
    Questions(questions_quest[0], "C"),
    Questions(questions_quest[1], "b"),
    Questions(questions_quest[2], "a"),

]
def test(questions):
    score = 0
    for question in questions:
        answer = input(question.quest)
        if answer == question.answer:
            score = score + 1
    print("your score " + str(score) + "/" + str(len(questions)))

test(questions)