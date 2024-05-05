import random



complexes_and_ions_colours = {
    "[Cu(H2O)6]2+": "pale blue solution",
    "[Cu(H2O)4(OH)2]": "blue precipitate",
    "[Cu(NH3)4(H2O)2]2+": "deep blue solution",
    "[CuCl4]2-": "yellow solution",
    "[Fe(H2O)6]2+": "pale green solution",
    "[Fe(H2O)6]3+": "yellow-brown solution",
    "[Fe(H2O)4(OH)2]": "green precipitate",
    "[Fe(H2O)3(OH)3]": "brown precipitate",
    "[Co(H2O)6]2+": "pink solution",
    "[Co(H2O)4(OH)2]": "blue precipitate",
    "[Co(NH3)6]2+": "pale yellow solution",
    "[CoCl4]2-": "blue solution",
    "[Mn(H2O)6]2+": "pale pink solution",
    "[Mn(H2O)4(OH)2]": "pale brown precipitate",
    "V 2+      V(||)": "purple",
    "V 3+      V(|||)": "green",
    "VO 2+     V(|V)": "blue",
    "VO2 +     V(V)": "yellow",
    "Cr 3+": "green",
    "Cr2O7 2-": "orange",
    "CrO4 2-": "yellow",
    "Cr 2+": "blue",
    "[Cr(NH3)6]3+": "violet or purple solution",
    "[Cr(H2O)6]3+": "green solution",
    "[Cr(H2O)3(OH)3]": "green precipitate",
    "[Cr(H2O)2(OH)4]-": "green solution",
    "[Cr(OH)6]3-": "green solution",
    "[Ni(H2O)6]2+": "green solution",
    "[Ni(H2O)4(OH)2]": "green precipitate",
    "[Ni(NH3)6]2+": "blue solution",
    "[Zn(H2O)6]2+": "colourless solution",
    "[Zn(H2O)4(OH)2]": "white precipitate",
    "[Zn(H2O)2(OH)4]2-": "colourless solution",
    "[Zn(NH3)4]2+": "colourless solution",
    }


vanadium = {
    "V 2+      V(||)": "purple",
    "V 3+      V(|||)": "green",
    "VO 2+     V(|V)": "blue",
    "VO2 +     V(V)": "yellow",
}

nickel = {
    "[Ni(H2O)6]2+": "green solution",
    "[Ni(H2O)4(OH)2]": "green precipitate",
    "[Ni(NH3)6]2+": "blue solution"
}

chrome = {
    "Cr 3+": "green",
    "Cr2O7 2-": "orange",
    "CrO4 2-": "yellow",
    "Cr 2+": "blue",
    "[Cr(NH3)6]3+": "violet or purple solution",
    "[Cr(H2O)6]3+": "green solution",
    "[Cr(H2O)3(OH)3]": "green precipitate",
    "[Cr(H2O)2(OH)4]-": "green solution",
    "[Cr(OH)6]3-": "green solution",
}

cobalt = {
    "[Co(H2O)6]2+": "pink solution",
    "[Co(H2O)4(OH)2]": "blue precipitate",
    "[Co(NH3)6]2+": "pale yellow solution",
    "[CoCl4]2-": "blue solution",
}


copper = {
    "[Cu(H2O)6]2+": "pale blue solution",
    "[Cu(H2O)4(OH)2]": "blue precipitate",
    "[Cu(NH3)4(H2O)2]2+": "deep blue solution",
    "[CuCl4]2-": "yellow solution",
}

current_test = {**complexes_and_ions_colours}


got_it_right = {}


def choose_ion(previous):
    if len(current_test) == 0:
        print("You have completed the game!")
        quit()
    elif len(current_test) == 1:
        return list(current_test.keys())[0]
    else:
        ion = random.choice(list(current_test.keys()))
        if ion == previous:
            return choose_ion(previous)
        return ion


def main():
    previous = ""
    won = False
    print("Welcome to the transition metal colour game!")
    while not won:
        print("\n \n ")
        complex = choose_ion(previous)
        previous = complex
        answer = input(f"{complex}\n")
        if answer == current_test[complex]:
            print("Correct!")
            if complex in got_it_right:
                got_it_right[complex] += 1
                if got_it_right[complex] == 2:
                    del current_test[complex]
            else:
                got_it_right[complex] = 1
        else:
            print(f"Incorrect! The answer is {current_test[complex]}")
            if complex in got_it_right:
                got_it_right[complex] -= 1


if __name__ == "__main__":
    main()