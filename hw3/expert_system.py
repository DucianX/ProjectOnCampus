
def is_yes_useranswer(prompt):
    while True:
        user_answer = input(prompt)
        if user_answer == "Yes":
            return True
        if user_answer == "No":
            return False
        else:
            print("Please input 'Yes' or 'No'.")
            continue


def headache():
    if is_yes_useranswer("headache? "):
        if is_yes_useranswer("pain when bending your head...?"):
            print("possibilities include menigitis.")
        elif is_yes_useranswer("vomiting or diarrhea? "):
            print("possibilities include digestive tract infection.")
        else:
            aching_bone_joint2()
    else:
        aching_bone_joint2()
        

def aching_bone_joint2():
        if is_yes_useranswer("aching bones or joints? "):
            print("viral infection")
        elif is_yes_useranswer("rash? "):
            print("insufficient info")
        elif is_yes_useranswer("sore throat? "):
            print("throat infection")
        elif is_yes_useranswer("back pain just above the wwaist with chills and fever? "):
            print("kidney infection")
        elif is_yes_useranswer("pain urinating or more often? "):
            print("urinary tract infection")
        elif is_yes_useranswer("Spent the day in the sun or in hot conditions? "):
            print("sunstroke or heat exhaustion")
        else:
            print("insufficient information")
      
            
def main():
    if is_yes_useranswer("Cough? "):
        if is_yes_useranswer("Short of breath or wheezing or coughing up phlegm? "):
            print("pneumonia or infection of airways.")
        elif is_yes_useranswer("headache? "):
            print("viral infection")
        else:
            aching_bone_joint2()
    else:
        headache()

main()


