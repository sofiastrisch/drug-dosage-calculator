def convert_dose(amount, from_unit, to_unit):
    """Convert between mcg, mg, and g."""
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()


    if from_unit == "g":
        amount_mg = amount * 1000
    elif from_unit == "mg":
        amount_mg = amount
    elif from_unit == "mcg":
        amount_mg = amount / 1000
    else:
        raise ValueError("Invalid unit. Use g, mg, or mcg.")


    if to_unit == "g":
        return amount_mg / 1000
    elif to_unit == "mg":
        return amount_mg
    elif to_unit == "mcg":
        return amount_mg * 1000
    else:
        raise ValueError("Invalid unit. Use g, mg, or mcg.")


def main():
    print("Medication Unit Converter (mcg ↔ mg ↔ g)")
    print("------------------------------------------")

    amount = float(input("Enter the dose amount: "))
    from_unit = input("Convert from (g/mg/mcg): ")
    to_unit = input("Convert to (g/mg/mcg): ")

    result = convert_dose(amount, from_unit, to_unit)
    print(f"\n {amount} {from_unit} = {result:.4f} {to_unit}")


main()

print()
print()



print("Drug Dosage Calculator")
print("--------------------------")
print("Make sure both doses are in the same unit (e.g., mg or g).")

desired_dose = float(input("Enter desired dose: "))
on_hand_dose = float(input("Enter on-hand dose: "))
volume_on_hand = float(input("Enter volume on hand (mL): "))

volume_to_give = (desired_dose / on_hand_dose) * volume_on_hand

print(f"\n→ Give {volume_to_give:.2f} mL")
