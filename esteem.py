def main():
    print("This program is an implementation of the Rosenber")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    questions = ["1. I feel that I am a person of worth, at least on an equal plane with others.",
        "2. I feel that I have a number of good qualities.",
        "3. All in all, I am inclined to feel that I am a failure.",
        "4. I am able to do things as well as most other people.",
        "5. I feel I do not have much to be proud of.",
        "6. I take a positive attitude toward myself.",
        "7. On the whole, I am satisfied with myself.",
        "8. I wish I could have more respect for myself.",
        "9. I certainly feel useless at times.",
        "10. At times I think I am no good at all."]

    score = 0

    for i in range(len(questions)):
        print(questions[i])
        answer = input("Enter D, d, a, or A: ")
        if i == 0:
           score += GetPositiveScore(answer)
        elif i == 1:
            score += GetPositiveScore(answer)
        elif i == 2:
            score += GetNegativeScore(answer)
        elif i == 3:
            score += GetPositiveScore(answer)
        elif i == 4:
            score += GetNegativeScore(answer)
        elif i == 5:
            score += GetPositiveScore(answer)
        elif i == 6:
            score += GetPositiveScore(answer)
        elif i == 7:
            score += GetNegativeScore(answer)
        elif i == 8:
            score += GetNegativeScore(answer)
        elif i == 9:
            score += GetNegativeScore(answer)
        print()

    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def GetPositiveScore(choice):
    if choice == "D":
        score = 0
    elif choice == "d":
        score = 1
    elif choice == "a":
        score = 2
    elif choice == "A":
        score = 3
    
    return score

def GetNegativeScore(choice):
    if choice == "D":
        score = 3
    elif choice == "d":
        score = 2
    elif choice == "a":
        score = 1
    elif choice == "A":
        score = 0
    
    return score

main()