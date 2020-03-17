from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
mySurvey = AnonymousSurvey(question)
mySurvey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    mySurvey.save_response(response)

print("\n Thank you for your participation!\n")
mySurvey.show_results()

