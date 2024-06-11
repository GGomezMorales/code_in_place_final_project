import random
import numpy as np

def initialize_game(difficulty):
    return {"level": 1, "score": 0, "difficulty": difficulty}

def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard\n")
    difficulty = input("Enter the number corresponding to the difficulty level: ")
    if difficulty not in ["1", "2", "3"]:
        print("Invalid input. Please select a valid difficulty level.\n")
        return select_difficulty()
    else :
        return int(difficulty)

def generate_problem(level, difficulty):
    if level == 1:
        return generate_basic_problem(difficulty)
    elif level == 2:
        return generate_basic_problem(difficulty)
    elif level == 3:
        return generate_basic_problem(difficulty)
    elif level == 4:
        return generate_calculus_problem(difficulty)
    elif level == 5:
        return generate_linear_algebra_problem(difficulty)
    else:
        return random.choice([generate_calculus_problem(difficulty), generate_linear_algebra_problem(difficulty)])

def generate_basic_problem(difficulty):
    if difficulty == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == 2:
        a, b = random.randint(10, 50), random.randint(10, 50)
    elif difficulty == 3:
        a, b = random.randint(50, 100), random.randint(50, 100)
        
    operation = random.choice(["addition", "subtraction", "multiplication", "modulus"])
    if operation == "addition":
        return f"{a} + {b}", a + b
    elif operation == "subtraction":
        return f"{a} - {b}", a - b
    elif operation == "multiplication":
        return f"{a} * {b}", a * b
    elif operation == "modulus":
        return f"{a} mod {b}", a % b

def generate_linear_algebra_problem(difficulty):
    if difficulty == 1:
        size = 2
    elif difficulty == 2:
        size = 3
    elif difficulty == 3:
        size = 4

    problem_type = random.choice(["matrix_multiplication", "determinant"])
    if problem_type == "matrix_multiplication":
        A = np.random.randint(0, 10, size=(size, size))
        B = np.random.randint(0, 10, size=(size, size))
        problem = f"Multiply matrices A and B, where A and B are:\n{A}\n\n{B}\nrespectively."
        solution = np.dot(A, B)
        return problem, solution
    elif problem_type == "determinant":
        A = np.random.randint(0, 10, size=(size, size))
        problem = f"Calculate the determinant of matrix A, where A is:\n{A}"
        solution = int(np.round(np.linalg.det(A)))
        return problem, solution

def generate_calculus_problem(difficulty):
    if difficulty == 1:
        problem_type = random.choice(["derivative_basic"])
    elif difficulty == 2:
        problem_type = random.choice(["derivative_basic", "integral_basic"])
    elif difficulty == 3:
        problem_type = random.choice(["derivative_complex", "integral_complex"])
    
    if problem_type == "derivative_basic":
        coeff = random.randint(-10, 10)
        power = random.randint(2, 4)
        problem = f"Calculate the derivative of {coeff}*x^{power}"
        solution = f"{coeff * power}*x^{power - 1}"
        return problem, solution
    elif problem_type == "integral_basic":
        coeff = random.randint(-10, 10)
        power = random.randint(1, 3)
        problem = f"Calculate the integral of {coeff}*x^{power}"
        solution = f"{round((coeff / (power + 1)), 1)}*x^{power + 1}"
        return problem, solution
    elif problem_type == "derivative_complex":
        coeff1, coeff2 = random.randint(-10, 10), random.randint(-10, 10)
        power1, power2 = random.randint(-8, 8), random.randint(-8, 8)
        operation = random.choice(["sum", "modulus"])
        problem = f"Calculate the {operation} of coefficients associated with 'x' terms in the derivative of {coeff1}*x^{power1} + {coeff2}*x^{power2}"
        if operation == "sum":
            solution = {coeff1 * power1} + {coeff2 * power2}
        elif operation == "modulus":
            solution = {coeff1 * power1} % {coeff2 * power2}
        return problem, solution
    elif problem_type == "integral_complex":
        coeff1, coeff2 = random.randint(-10, 10), random.randint(-10, 10)
        power1, power2 = random.randint(-8, 8), random.randint(-8, 8)
        operation = random.choice(["sum", "product"])
        problem = f"Calculate the {operation} of coefficients associated with 'x' terms in the integral of {coeff1}*x^{power1} + {coeff2}*x^{power2}"
        if operation == "sum":
            solution = round((round(coeff1 / (power1 + 1), 1) + round(coeff2 / (power2 + 1), 1)), 1)
        elif operation == "product":
            solution = round((round(coeff1 / (power1 + 1), 1) * round(coeff2 / (power2 + 1), 1)), 1)
        return problem, solution

def check_answer(answer, correct_answer):
    if str(answer) == str(correct_answer):
        return True
    else:
        return False

def update_level(game_state):
    game_state["level"] += 1

def play_again(game_state):
    while True:
        play_again = input("Do you want to continue playing? (yes/no): ")
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            print(f"Thanks for playing! Your final score is {game_state['score']}.")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def start_game():
    print("Welcome to the Math Adventure Game! Let's get started.\n")
    difficulty = select_difficulty()
    game_state = initialize_game(difficulty)

    while True:
        problem, correct_answer = generate_problem(game_state["level"], game_state["difficulty"])
        print(f"Solve this problem: {problem}")
        answer = input("Your answer: ")

        if check_answer(answer, correct_answer):
            print("Correct answer! You have earned 10 points")
            game_state["score"] += 10
            update_level(game_state)
        else:
            print("Sorry, that's incorrect. The correct answer is:", correct_answer)
        print(f"You are now on level {game_state['level']} with a score of {game_state['score']}\n")

        if not play_again(game_state):
            break

if __name__ == "__main__":
    start_game()
