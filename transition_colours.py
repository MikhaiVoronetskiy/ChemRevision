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
    "V 2+": "purple",
    "V 3+": "green",
    "VO 2+": "blue",
    "VO2 +": "yellow",
    "Cr 3+": "green",
    "Cr2O7 2-": "orange",
    "CrO4 2-": "yellow",
    "Cr2+": "blue",
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

got_it_wrong = {}
got_it_right = {}


def choose_complex_or_ion(count, previous_complex_or_ion, before_that):
    if len(got_it_wrong) != 0 and random.randint(0, 2) == 0:
        complex_or_ion = random.choice(list(got_it_wrong.keys()))
    else:
        complex_or_ion = random.choice(list(complexes_and_ions_colours.keys()))
    if complex_or_ion in got_it_right and got_it_right[complex_or_ion] > 2:
        complex_or_ion = choose_complex_or_ion(count + 1)
    if count > 15:
        print("You've done them all!")
        exit()
    if (complex_or_ion == previous_complex_or_ion or complex_or_ion == before_that) and count < 10:
        complex_or_ion = choose_complex_or_ion(count + 1, previous_complex_or_ion, before_that)
    return complex_or_ion

def main():
    user_input = input("P to play, S to stop")
    previous_complex_or_ion = ""
    before_that = ""
    complex_or_ion = ""
    while user_input != "S":
        before_that = previous_complex_or_ion
        previous_complex_or_ion = complex_or_ion
        complex_or_ion = choose_complex_or_ion(0, previous_complex_or_ion, before_that)
        print(complex_or_ion)
        user_input = input()
        if user_input == complexes_and_ions_colours[complex_or_ion]:
            print("Correct!")
            if complex_or_ion in got_it_wrong:
                got_it_wrong[complex_or_ion] -= 1
            if complex_or_ion not in got_it_wrong and complex_or_ion not in got_it_right:
                got_it_right[complex_or_ion] = 0
            if complex_or_ion in got_it_wrong and got_it_wrong[complex_or_ion] == 0:
                del got_it_wrong[complex_or_ion]
            if complex_or_ion in got_it_right:
                got_it_right[complex_or_ion] += 1
        else:
            got_it_wrong[complex_or_ion] = 2
            print("Incorrect! The answer is", complexes_and_ions_colours[complex_or_ion])

if __name__ == "__main__":
    main()