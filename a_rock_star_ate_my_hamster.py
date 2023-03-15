import random
import os
import json

class Musician:
    def __init__(self, name, talent, cost):
        self.name = name
        self.talent = talent
        self.cost = cost


musicians = [
    Musician("Mick Jail", 8, 500),
    Musician("Wacky Jacko", 7, 400),
    Musician("Tina Turnoff", 6, 300),
]


def hire_musician(budget, hired_musicians):
    print("Available musicians:")
    for i, musician in enumerate(musicians):
        print(f"{i + 1}. {musician.name} - Talent: {musician.talent}, Cost: {musician.cost}")
    
    choice = int(input("Enter the number of the musician you want to hire: "))
    musician = musicians[choice - 1]
    
    if budget - musician.cost < 0:
        print("You don't have enough budget to hire this musician.")
    else:
        budget -= musician.cost
        hired_musicians.append(musician)
        print(f"{musician.name} has been hired!")
    
    return budget


def organize_gig(hired_musicians):
    if not hired_musicians:
        print("You need to hire musicians before organizing a gig.")
        return 0

    avg_talent = sum(musician.talent for musician in hired_musicians) / len(hired_musicians)
    revenue = int(avg_talent * 100 * random.uniform(0.5, 1.5))
    print(f"The gig was a success! You earned {revenue}.")
    return revenue


def record_album(hired_musicians):
    if not hired_musicians:
        print("You need to hire musicians before recording an album.")
        return 0

    avg_talent = sum(musician.talent for musician in hired_musicians) / len(hired_musicians)
    revenue = int(avg_talent * 200 * random.uniform(0.5, 1.5))
    print(f"The album was a hit! You earned {revenue}.")
    return revenue


def publicity_stunt():
    cost = random.randint(100, 500)
    revenue = int(cost * random.uniform(0.5, 3))
    print(f"The publicity stunt cost {cost}, but you earned {revenue} from the increased exposure.")
    return revenue - cost


def bad_publicity():
    reasons = [
        "Your lead singer accidentally set fire to a hotel room while attempting a magic trick.",
        "Your bassist was caught on camera stealing a famous musician's guitar.",
        "A viral video showed your drummer insulting a group of fans during a concert.",
        "Your guitarist got into a fistfight with a paparazzo while leaving a club.",
        "A tabloid published a story claiming your band's music causes hallucinations.",
        "Your lead singer was caught on camera eating a live insect during a TV interview.",
        "A leaked recording revealed your band badmouthing a popular charity organization.",
        "Your bassist was arrested for streaking during a live television broadcast.",
        "A video went viral showing your drummer destroying a hotel room with a sledgehammer.",
        "Your guitarist was caught on camera vandalizing a famous monument while on tour."
    ]
    return reasons


    reason = random.choice(reasons)
    cost = random.randint(100, 1000)
    print(f"Bad publicity! {reason} You lost {cost} due to the negative attention.")
    return cost


def main():
    budget = 1000
    hired_musicians = []
    weeks_remaining = 52

    while weeks_remaining > 0:
        print(f"\nWeeks remaining: {weeks_remaining}")
        print("Your options:")
        print("1. Hire a musician")
        print("2. Organize a gig")
        print("3. Record an album")
        print("4. Do a publicity stunt")
        print("5. Check your band")
        print("6. Quit")

        action = int(input("Choose an action: "))

        if action == 1:
            budget = hire_musician(budget, hired_musicians)
        elif action == 2:
            budget += organize_gig(hired_musicians)
        elif action == 3:
            budget += record_album(hired_musicians)
        elif action == 4:
            budget += publicity_stunt()
        elif action == 5:
            print("Your band members:")
            for musician in hired_musicians:
                print(musician.name)
            print(f"Remaining budget: {budget}")
        elif action == 6:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        weeks_remaining -= 2

        if random.random() < 0.2:
            budget -= bad_publicity()

    print("Game over!")
    print(f"Your final score: {budget}")
    save_high_score(budget)


def save_high_score(score):
    high_scores_file = "high_scores.json"
    if os.path.exists(high_scores_file):
        with open(high_scores_file, "r") as f:
            high_scores = json.load(f)
    else:
        high_scores = []

    high_scores.append(score)
    high_scores.sort(reverse=True)
    high_scores = high_scores[:10]

    with open(high_scores_file, "w") as f:
        json.dump(high_scores, f)


if __name__ == "__main__":
    main()

