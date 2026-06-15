
print("WELCOME TO THE QUIZ MAKER")

quiz = []


def add_question():
    question = input("Enter the question: ")

    options = []
    for i in range(4):
        option = input(f"Enter option {i+1}: ")
        options.append(option)

    answer = input("Enter the correct answer: ")

    new_question = {
        "question": question,
        "options": options,
        "answer": answer
    }

    quiz.append(new_question)

    print("Question added successfully!")


def view_questions():
    if len(quiz) == 0:
        print("No questions found")
    else:
        for index, q in enumerate(quiz, start=1):
            print(f"\n{index}) {q['question']}")

            for index, option in enumerate(q["options"], start=1):
                print(f"   {index}. {option}")


def delete_question():
    if len(quiz) == 0:
        print("No questions found")
        return

    view_questions()

    index = int(input("Enter question number to delete: "))

    if 1 <= index <= len(quiz):
        deleted = quiz.pop(index - 1)
        print("Deleted:", deleted["question"])
    else:
        print("Invalid question number")


def play_quiz():
    if len(quiz) == 0:
        print("No questions found")
        return

    score = 0

    for q in quiz:

        print("\n" + q["question"])

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Enter your answer: ")

        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"])

    print(f"\nYour score: {score}/{len(quiz)}")

def update_question():
        
        if len(quiz)==0:
            print("no updation is done")
        else:
            
            for index, q in enumerate(quiz, start=1):
             print (f"\n{index}) {q['question']}")
            index=int(input("enter the question number you want to update"))


             

            if 1<= index <= len(quiz):
                 question=input("enter your new question you wnat to update")
                 options=[]

                 for i in range(4):
                     
                    
                      option=input("enter the option you want to edit")
                      options.append(option)
                      ans=input("enter you correct answer")

                      quiz[index-1]["question"]=question
                      quiz[index-1]["options"]=options
                      quiz[index-1]["answer"]=ans
                      print(quiz)
                      print("updated done")


                    

                     

            


        
        





while True:

    choice = input(
        "\nChoose [a]dd, [v]iew, [d]elete, [p]lay or [q]uiz or [u]pdate:- "
    ).lower()

    if choice == "a":
        add_question()

    elif choice == "v":
        view_questions()

    elif choice == "d":
        delete_question()

    elif choice == "p":
        play_quiz()

    elif choice == "u":
        update_question()

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")


             
             

    



      

    
        





      

   

