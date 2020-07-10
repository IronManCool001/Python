print("If you think you know all about Computer.Take this quiz \n")
total_q = 5
score =0

ans = input("Yes/No")
if ans =="Yes" or ans.lower() == "yes":
    print("1. What is the most easiest programming language \n")
    ans = input("Enter your answer here: \n")
    if ans == "python" or ans.lower() == "python":
        score += 1
        print("Correct! \n")
        print(f"Current Score: {score}")
    else:
        score -= 1
        print("2. Incorrect \n")
        print(f"Current Score: {score}")
    

    print("Is java object-oriented \n")
    ans = input("Yes/No")
    if ans == "Yes" or ans.lower() == "yes":
        score += 1
        print("Correct \n")
        print(f"Current Score: {score}")
    else:
        score -= 1
        print("Incorrect \n")
        print(f"Current Score: {score}")

    print("3. Is html a programming language? \n")
    ans = input("Yes/No")
    if ans == "No" or ans.lower() == "no":
        score += 1
        print("Correct \n")
        print(f"Current Score: {score}")
    else:
        score -= 1
        print("Incorrect \n")
        print(f"Current Score: {score}")

    print("4. Which is better 1080ti or 2080 [graphics card] \n")
    ans = input("Enter your answer here: \n")
    if ans =="2080" or ans.lower() =="2080":
        score += 1
        print("Correct \n ")
        print(f"Current Score: {score}  \n")
    else:
        score -= 1
        print("Incorrect \n")
        print(f"Current Score: {score}\n")

    print("5. Is Machine Learning and Deep Learning same ?\n")
    ans = input("Yes or No")
    if ans =="No" or ans.lower() == "no":
        score += 1
        print("Correct \n")
        print(f"Current Score: {score}\n")
    else:
        score -= 1
        print("Incorrect")
        print(f"Current Score: {score}")

    p = score / 5 * 100
    print(f"Percentage: {p}")
    if p >= 50:
        print("Pass")
    elif p < 50:
        print("You Failed")

else:
    print("Exiting")
    exit()
