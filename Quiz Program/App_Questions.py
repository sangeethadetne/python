from Question import Question

question_prompts = [
    "what is the color of the rose?\na.red\nb.blue\nc.violet\n\n",
    "what is the color of the sky?\na.red\nb.blue\nc.white\n\n",
    "what is the color of the tree?\na.green\nb.blue\nc.violet\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"), 
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got"+ str(score) + "/"  +str(len(questions))+ "correct")


run_test(questions)