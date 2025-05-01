import random 
from constants import *

def main():
    body_type = random.choice(gender)
    race = random.choice(races)
    Birth_signs = random.choice(Birth_sign)
    class_attribute = random.sample(class_attributes, 2)
    class_specializations = random.choice(class_specialization)
    major_skill = random.sample(major_skills, 7)

    print("Welcome to the Oblivion Character Generator!")
    print("Your new adventurer will be...")
    print(f"A {body_type} {race} born under {Birth_signs} star sign")
    print(f"Their class will have {class_attribute} as favored attributes and {class_specializations} as its specialization.")
    print(f"Your major skills will be {major_skill}")



if __name__ == "__main__":
    main()