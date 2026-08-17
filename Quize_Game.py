import os,json,random,time
from datetime import datetime

RESET="\033[0m";BOLD="\033[1m";DIM="\033[2m"
RED="\033[91m";GREEN="\033[92m";YELLOW="\033[93m"
BLUE="\033[94m";CYAN="\033[96m"
CLEAR="\033[2J\033[H"
DATA_FILE="quiz_data.json"

QUESTIONS=[
{"c":"Python","d":"Easy","q":"Which keyword defines a function in Python?","o":{"A":"function","B":"def","C":"define","D":"func"},"a":"B"},
{"c":"Python","d":"Easy","q":"Which symbol is used for comments in Python?","o":{"A":"//","B":"#","C":"/*","D":"--"},"a":"B"},
{"c":"Python","d":"Easy","q":"Which data type represents True or False?","o":{"A":"int","B":"str","C":"bool","D":"float"},"a":"C"},
{"c":"Python","d":"Easy","q":"Which function displays output?","o":{"A":"input()","B":"display()","C":"print()","D":"output()"},"a":"C"},
{"c":"Python","d":"Medium","q":"Which method adds an element to the end of a list?","o":{"A":"add()","B":"insert()","C":"append()","D":"push()"},"a":"C"},
{"c":"Python","d":"Medium","q":"What is len('Python')?","o":{"A":"5","B":"6","C":"7","D":"8"},"a":"B"},
{"c":"Python","d":"Medium","q":"Which data structure stores key-value pairs?","o":{"A":"List","B":"Tuple","C":"Dictionary","D":"Set"},"a":"C"},
{"c":"Python","d":"Hard","q":"Which keyword creates an anonymous function?","o":{"A":"anonymous","B":"lambda","C":"function","D":"inline"},"a":"B"},

{"c":"Java","d":"Easy","q":"Which keyword creates a class in Java?","o":{"A":"class","B":"Class","C":"object","D":"create"},"a":"A"},
{"c":"Java","d":"Easy","q":"What is the entry point of a Java program?","o":{"A":"start()","B":"run()","C":"main()","D":"execute()"},"a":"C"},
{"c":"Java","d":"Medium","q":"Which keyword is used for inheritance?","o":{"A":"inherit","B":"extends","C":"inherits","D":"super"},"a":"B"},
{"c":"Java","d":"Medium","q":"Which concept allows the same method to behave differently?","o":{"A":"Encapsulation","B":"Polymorphism","C":"Compilation","D":"Abstraction"},"a":"B"},
{"c":"Java","d":"Hard","q":"Which keyword implements an interface?","o":{"A":"extends","B":"inherits","C":"implements","D":"interface"},"a":"C"},

{"c":"SQL","d":"Easy","q":"Which SQL command retrieves data?","o":{"A":"GET","B":"SELECT","C":"FETCH","D":"READ"},"a":"B"},
{"c":"SQL","d":"Easy","q":"Which clause filters rows?","o":{"A":"FILTER","B":"WHERE","C":"HAVING","D":"CHECK"},"a":"B"},
{"c":"SQL","d":"Easy","q":"Which function counts rows?","o":{"A":"COUNT()","B":"NUMBER()","C":"ROWS()","D":"TOTAL()"},"a":"A"},
{"c":"SQL","d":"Medium","q":"Which JOIN returns only matching rows?","o":{"A":"LEFT JOIN","B":"RIGHT JOIN","C":"INNER JOIN","D":"FULL JOIN"},"a":"C"},
{"c":"SQL","d":"Medium","q":"Which function calculates an average?","o":{"A":"MEAN()","B":"AVG()","C":"AVERAGE()","D":"MID()"},"a":"B"},
{"c":"SQL","d":"Hard","q":"Which clause filters grouped results?","o":{"A":"WHERE","B":"HAVING","C":"GROUP","D":"FILTER"},"a":"B"},

{"c":"Data Science","d":"Easy","q":"Which Python library is used for data manipulation?","o":{"A":"Pandas","B":"Flask","C":"Django","D":"Tkinter"},"a":"A"},
{"c":"Data Science","d":"Easy","q":"Which library is used for numerical computing?","o":{"A":"NumPy","B":"Flask","C":"Requests","D":"Tkinter"},"a":"A"},
{"c":"Data Science","d":"Easy","q":"What does EDA stand for?","o":{"A":"Easy Data Analysis","B":"Exploratory Data Analysis","C":"External Data Algorithm","D":"Experimental Data Application"},"a":"B"},
{"c":"Data Science","d":"Medium","q":"Which metric is commonly used for classification?","o":{"A":"Accuracy","B":"RMSE","C":"MSE","D":"MAE"},"a":"A"},
{"c":"Data Science","d":"Medium","q":"Which algorithm is commonly used for binary classification?","o":{"A":"Linear Regression","B":"Logistic Regression","C":"K-Means","D":"PCA"},"a":"B"},
{"c":"Data Science","d":"Hard","q":"Which metric is commonly used for regression error?","o":{"A":"Accuracy","B":"Precision","C":"RMSE","D":"Recall"},"a":"C"},

{"c":"Computer Science","d":"Easy","q":"What does CPU stand for?","o":{"A":"Central Processing Unit","B":"Computer Processing Unit","C":"Central Program Unit","D":"Computer Program Utility"},"a":"A"},
{"c":"Computer Science","d":"Easy","q":"Which one is an operating system?","o":{"A":"Python","B":"Linux","C":"MySQL","D":"HTML"},"a":"B"},
{"c":"Computer Science","d":"Medium","q":"Which data structure follows FIFO?","o":{"A":"Stack","B":"Queue","C":"Tree","D":"Graph"},"a":"B"},
{"c":"Computer Science","d":"Medium","q":"Which data structure follows LIFO?","o":{"A":"Queue","B":"Stack","C":"Tree","D":"Graph"},"a":"B"},
{"c":"Computer Science","d":"Hard","q":"Which search algorithm has O(log n) complexity on sorted data?","o":{"A":"Linear Search","B":"Binary Search","C":"Bubble Sort","D":"DFS"},"a":"B"},

{"c":"General Knowledge","d":"Easy","q":"What is the capital of India?","o":{"A":"Mumbai","B":"New Delhi","C":"Kolkata","D":"Hyderabad"},"a":"B"},
{"c":"General Knowledge","d":"Easy","q":"Which planet is known as the Red Planet?","o":{"A":"Earth","B":"Venus","C":"Mars","D":"Jupiter"},"a":"C"},
{"c":"General Knowledge","d":"Medium","q":"How many continents are there?","o":{"A":"5","B":"6","C":"7","D":"8"},"a":"C"},
{"c":"General Knowledge","d":"Medium","q":"Which is the largest ocean?","o":{"A":"Atlantic Ocean","B":"Indian Ocean","C":"Arctic Ocean","D":"Pacific Ocean"},"a":"D"},
{"c":"General Knowledge","d":"Hard","q":"Which is the largest planet in our Solar System?","o":{"A":"Earth","B":"Saturn","C":"Jupiter","D":"Neptune"},"a":"C"}
]

def clear():
    print(CLEAR,end="")

def pause():
    input(f"\n{DIM}Press ENTER to continue...{RESET}")

def title(x):
    print(f"\n{CYAN}{BOLD}{'═'*68}\n{x.center(68)}\n{'═'*68}{RESET}")

def section(x):
    print(f"\n{BLUE}{BOLD}▸ {x}{RESET}\n{BLUE}{'─'*68}{RESET}")

def error(x):
    print(f"{RED}✗ {x}{RESET}")

def success(x):
    print(f"{GREEN}✓ {x}{RESET}")

def number(prompt,low,high):
    while True:
        try:
            n=int(input(prompt))
            if low<=n<=high:
                return n
        except:
            pass
        error(f"Enter a number from {low} to {high}.")

def default_player():
    return {
        "games":0,
        "total":0,
        "best":0,
        "correct":0,
        "wrong":0,
        "skip":0,
        "streak":0
    }

def normalize_player(p):
    return {
        "games":p.get("games",p.get("games_played",0)),
        "total":p.get("total",p.get("total_score",0)),
        "best":p.get("best",p.get("best_score",0)),
        "correct":p.get("correct",p.get("correct_answers",0)),
        "wrong":p.get("wrong",p.get("wrong_answers",0)),
        "skip":p.get("skip",p.get("skipped",p.get("skipped_questions",0))),
        "streak":p.get("streak",p.get("best_streak",0))
    }

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"players":{},"games":[]}

    try:
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            d=json.load(f)

        d.setdefault("players",{})
        d.setdefault("games",{} if isinstance(d.get("games"),dict) else [])

        for name,p in d["players"].items():
            d["players"][name]=normalize_player(p)

        return d

    except:
        return {"players":{},"games":[]}

def save_data(d):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(d,f,indent=4)

def login(d):
    clear()
    title("PLAYER LOGIN")

    name=input("Enter your name: ").strip()

    while not name:
        error("Name cannot be empty.")
        name=input("Enter your name: ").strip()

    if name not in d["players"]:
        d["players"][name]=default_player()
        save_data(d)
        success(f"Profile created for {name}!")
    else:
        d["players"][name]=normalize_player(d["players"][name])
        save_data(d)
        success(f"Welcome back, {name}!")

    time.sleep(1)
    return name

def choose_category():
    categories=sorted(set(q["c"] for q in QUESTIONS))

    clear()
    title("SELECT CATEGORY")

    print("0. All Categories")

    for i,c in enumerate(categories,1):
        print(f"{i}. {c}")

    n=number("Choose: ",0,len(categories))
    return "All" if n==0 else categories[n-1]

def choose_difficulty():
    clear()
    title("SELECT DIFFICULTY")

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed")

    return ["","Easy","Medium","Hard","Mixed"][number("Choose: ",1,4)]

def choose_mode():
    clear()
    title("SELECT GAME MODE")

    print("1. Classic")
    print("2. Timed")
    print("3. Survival")
    print("4. Practice")

    return ["","Classic","Timed","Survival","Practice"][number("Choose: ",1,4)]

def points(d):
    return {"Easy":10,"Medium":20,"Hard":30}[d]

def play_quiz(name,d):
    category=choose_category()
    difficulty=choose_difficulty()
    mode=choose_mode()

    questions=[
        q for q in QUESTIONS
        if (category=="All" or q["c"]==category)
        and (difficulty=="Mixed" or q["d"]==difficulty)
    ]

    random.shuffle(questions)
    questions=questions[:10]

    if not questions:
        error("No questions available.")
        pause()
        return

    score=correct=wrong=skipped=streak=best_streak=0
    lives=3
    review=[]

    for i,q in enumerate(questions,1):
        clear()
        title(f"QUESTION {i}/{len(questions)}")

        print(f"{q['c']} | {q['d']} | Mode: {mode}")

        if mode=="Survival":
            print(f"❤️ Lives: {lives}")

        print(f"\n{BOLD}{q['q']}{RESET}\n")

        for k,v in q["o"].items():
            print(f"{YELLOW}{k}.{RESET} {v}")

        print("\nH = 50/50")
        print("S = Skip")
        print("Q = Quit")

        fifty=False
        start=time.time()

        while True:
            if mode=="Timed" and time.time()-start>=15:
                answer="Time Up"
                result="wrong"
                error("Time's up!")
                break

            answer=input("\nYour answer: ").strip().upper()

            if answer=="Q":
                return

            if answer=="S":
                skipped+=1
                streak=0
                result="skip"
                break

            if answer=="H" and not fifty:
                wrongs=[k for k in q["o"] if k!=q["a"]]

                for k in random.sample(wrongs,2):
                    q["o"][k]=""

                fifty=True

                clear()
                title(f"QUESTION {i}/{len(questions)}")
                print(f"\n{BOLD}{q['q']}{RESET}\n")

                for k,v in q["o"].items():
                    if v:
                        print(f"{YELLOW}{k}.{RESET} {v}")

                continue

            if answer in q["o"]:
                result="correct" if answer==q["a"] else "wrong"
                break

            error("Choose A, B, C or D.")

        if result=="skip":
            review.append((q["q"],"Skipped",q["a"],"SKIPPED"))
            continue

        if result=="correct":
            correct+=1
            streak+=1
            best_streak=max(best_streak,streak)

            earned=points(q["d"])

            if streak>=3:
                earned+=10

            score+=earned
            success(f"Correct! +{earned} points")

            review.append((q["q"],answer,q["a"],"CORRECT"))

        else:
            wrong+=1
            streak=0

            if mode!="Practice":
                score=max(0,score-points(q["d"])//2)

            lives-=1

            error(f"Wrong! Correct answer: {q['a']}")

            review.append((q["q"],answer,q["a"],"WRONG"))

            if mode=="Survival" and lives<=0:
                error("GAME OVER!")
                break

        time.sleep(1)

    max_score=sum(points(q["d"]) for q in questions)
    percentage=score/max_score*100 if max_score else 0

    grade=(
        "A+" if percentage>=90 else
        "A" if percentage>=80 else
        "B" if percentage>=70 else
        "C" if percentage>=60 else
        "D" if percentage>=50 else
        "F"
    )

    player=d["players"][name]

    player["games"]+=1
    player["total"]+=score
    player["best"]=max(player["best"],score)
    player["correct"]+=correct
    player["wrong"]+=wrong
    player["skip"]+=skipped
    player["streak"]=max(player["streak"],best_streak)

    d["games"].append({
        "player":name,
        "category":category,
        "difficulty":difficulty,
        "mode":mode,
        "score":score,
        "max":max_score,
        "percent":round(percentage,2),
        "grade":grade,
        "correct":correct,
        "wrong":wrong,
        "skip":skipped,
        "streak":best_streak,
        "date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_data(d)

    clear()
    title("QUIZ COMPLETE")

    print(
        f"Player      : {name}\n"
        f"Category    : {category}\n"
        f"Difficulty  : {difficulty}\n"
        f"Mode        : {mode}"
    )

    section("RESULT")

    print(
        f"Score       : {score}/{max_score}\n"
        f"Percentage  : {percentage:.2f}%\n"
        f"Grade       : {grade}\n"
        f"Correct     : {correct}\n"
        f"Wrong       : {wrong}\n"
        f"Skipped     : {skipped}\n"
        f"Best Streak : {best_streak}"
    )

    section("PLAYER TOTAL")

    print(
        f"Games Played : {player['games']}\n"
        f"Total Score  : {player['total']}\n"
        f"Best Score   : {player['best']}\n"
        f"Avg Score    : {player['total']/player['games']:.2f}"
    )

    success("Game saved successfully!")

    if input("\nReview answers? (Y/N): ").strip().upper()=="Y":
        clear()
        title("ANSWER REVIEW")

        for i,(q,y,a,r) in enumerate(review,1):
            print(
                f"\n{i}. {q}\n"
                f"Your Answer : {y}\n"
                f"Correct     : {a}\n"
                f"Result      : {r}"
            )

    pause()

def profile(name,d):
    clear()
    title("PLAYER PROFILE")

    p=normalize_player(d["players"][name])
    d["players"][name]=p

    attempts=p["correct"]+p["wrong"]

    accuracy=p["correct"]/attempts*100 if attempts else 0
    average=p["total"]/p["games"] if p["games"] else 0

    print(f"👤 Player: {BOLD}{name}{RESET}")

    section("STATISTICS")

    print(
        f"Games Played      : {p['games']}\n"
        f"Total Score       : {p['total']}\n"
        f"Average Score     : {average:.2f}\n"
        f"Best Score        : {p['best']}\n"
        f"Correct Answers   : {p['correct']}\n"
        f"Wrong Answers     : {p['wrong']}\n"
        f"Skipped Questions : {p['skip']}\n"
        f"Best Streak       : {p['streak']}\n"
        f"Overall Accuracy  : {accuracy:.2f}%"
    )

    save_data(d)
    pause()

def leaderboard(d):
    clear()
    title("LEADERBOARD")

    players=[]

    for name,p in d["players"].items():
        p=normalize_player(p)

        if p["games"]>0:
            attempts=p["correct"]+p["wrong"]
            accuracy=p["correct"]/attempts*100 if attempts else 0

            players.append({
                "name":name,
                "games":p["games"],
                "score":p["total"],
                "accuracy":accuracy,
                "best":p["best"]
            })

    players.sort(
        key=lambda x:x["score"],
        reverse=True
    )

    if not players:
        print("No games played yet.")
        pause()
        return

    print(
        f"{'Rank':<6}"
        f"{'Player':<20}"
        f"{'Games':<9}"
        f"{'Total Score':<15}"
        f"{'Accuracy':<10}"
    )

    print("─"*68)

    for rank,p in enumerate(players[:10],1):
        print(
            f"{rank:<6}"
            f"{p['name'][:19]:<20}"
            f"{p['games']:<9}"
            f"{p['score']:<15}"
            f"{p['accuracy']:.2f}%"
        )

    pause()

def history(name,d):
    clear()
    title("GAME HISTORY")

    games=[
        g for g in d["games"]
        if g.get("player")==name
    ]

    if not games:
        print("No games played yet.")
        pause()
        return

    for i,g in enumerate(games[::-1][:10],1):
        percent=g.get(
            "percent",
            g.get("percentage",0)
        )

        maximum=g.get(
            "max",
            g.get("max_score",0)
        )

        print(
            f"\n{i}. {g.get('date','Unknown')} | "
            f"{g.get('category','Unknown')} | "
            f"{g.get('mode','Classic')}"
        )

        print(
            f"   Score: {g.get('score',0)}/{maximum} | "
            f"{percent}% | "
            f"Grade: {g.get('grade','-')}"
        )

    pause()

def how_to_play():
    clear()
    title("HOW TO PLAY")

    print(
"""🎯 OBJECTIVE

Answer questions correctly and achieve the highest score.

📊 SCORING

Easy   = 10 points
Medium = 20 points
Hard   = 30 points
3+ streak = +10 bonus

🎮 GAME MODES

Classic  = Standard quiz
Timed    = 15 seconds per question
Survival = 3 lives
Practice = No negative marking

💡 LIFELINES

H = Remove two wrong answers
S = Skip a question
Q = Quit the quiz

🏆 LEADERBOARD

Your total score is accumulated across
ALL games you play.

Example:
Game 1 = 100
Game 2 = 150
Game 3 = 120
Game 4 = 180

Total = 550

💾 DATA

All profiles, scores and game history
are saved automatically."""
    )

    pause()

def main_menu(name,d):
    while True:
        clear()

        print(
            f"{CYAN}{BOLD}"
            f"{'═'*68}\n"
            f"{'QUIZMASTER'.center(68)}\n"
            f"{'═'*68}{RESET}"
        )

        print(
            f"\nWelcome back, "
            f"{GREEN}{BOLD}{name}{RESET} 👋\n"
        )

        print(
            "1. 🎮  Start Quiz\n"
            "2. 🏆  Leaderboard\n"
            "3. 👤  My Profile\n"
            "4. 📜  Game History\n"
            "5. 📖  How to Play\n"
            "6. 🚪  Exit"
        )

        choice=number(
            "\nChoose an option: ",
            1,
            6
        )

        if choice==1:
            play_quiz(name,d)
        elif choice==2:
            leaderboard(d)
        elif choice==3:
            profile(name,d)
        elif choice==4:
            history(name,d)
        elif choice==5:
            how_to_play()
        else:
            clear()
            print(
                f"\n{GREEN}{BOLD}"
                "Thank you for playing QUIZMASTER! 👋"
                f"{RESET}\n"
            )
            break

def main():
    d=load_data()

    clear()

    print(
f"""
{CYAN}{BOLD}
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                         🧠 QUIZMASTER                              ║
║                                                                    ║
║                    Professional Quiz Game                          ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
{RESET}
"""
    )

    name=login(d)
    main_menu(name,d)

if __name__=="__main__":
    main()