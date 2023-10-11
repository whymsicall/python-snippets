# File: kinetic_energy.py
# Description: Kinetic energy
# Assignment Name and Number: #14 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    print("Kinetic energy of object: ", kineticEnergy())



def kineticEnergy():
    m = int(input("Enter value for mass: "))
    v = int(input("Enter value for velocity: "))

    energy = (1 / 2) * m * (v ** 2)
    return energy

if __name__ == "__main__":
    main()
