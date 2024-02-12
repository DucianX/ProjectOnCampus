def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #TODO: Fill in the rest of the necessary code here
    max_HR = 208 - 0.7 * age
    HR_res = max_HR - restHR
    print(
        "Your heart rate reserve is: " + str(round(HR_res, 2)) + "bpm\n"
        "Here is a breakdown of your training zones:\n"
        "Zone 1: " + str(round(0.5 * HR_res + restHR, 2)) + " to " 
        + str(round(0.6 * HR_res + restHR - 0.01, 2)) + "\n"
        "Zone 2: " + str(round(0.6 * HR_res + restHR, 2)) + " to " 
        + str(round(0.7 * HR_res + restHR - 0.01, 2)) + "\n"
        "Zone 3: " + str(round(0.7 * HR_res + restHR, 2)) + " to " 
        + str(round(0.8 * HR_res + restHR - 0.01, 2)) + "\n"
        "Zone 4: " + str(round(0.8 * HR_res + restHR, 2)) + " to " 
        + str(round(0.9 * HR_res + restHR - 0.01, 2)) + "\n"
        "Zone 5: " + str(round(0.9 * HR_res + restHR, 2)) + " to " 
        + str(round(HR_res + restHR - 0.01, 2)) + "\n"
          )
    


    print("=======================================")

main()