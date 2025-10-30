# Drug Dosage Calculator & Unit Converter

A Python program that helps healthcare professionals calculate drug dosages and convert between units (mcg, mg, g).  
The program includes a unit converter and a dosage calculator to determine the volume to administer.

## Overview
This project provides a console-based tool that:
- Converts medication doses between **micrograms (mcg), milligrams (mg), and grams (g)**.
- Calculates the volume of medication to give based on **desired dose**, **on-hand concentration**, and **volume available**.
- Provides accurate, easy-to-read results for clinical use or educational purposes.

## Features
- Unit conversion between **mcg, mg, and g**.  
- Drug dosage calculation with volume to administer.  
- Simple command-line interface — no external libraries required.  
- Interactive input prompts with clear instructions.

## Formulas Used

**Unit Conversion (to mg first):**  
- From g: `amount_mg = amount * 1000`  
- From mg: `amount_mg = amount`  
- From mcg: `amount_mg = amount / 1000`  

Then convert from mg to target unit:  
- To g: `amount_g = amount_mg / 1000`  
- To mg: `amount_mg = amount_mg`  
- To mcg: `amount_mcg = amount_mg * 1000`  

**Dosage Calculation:**  
```
Volume to Give (mL) = (Desired Dose / On-Hand Dose) * Volume on Hand
```

## Example Output

**Unit Converter:**
```
Medication Unit Converter (mcg ↔ mg ↔ g)
Enter the dose amount: 500
Convert from (g/mg/mcg): mg
Convert to (g/mg/mcg): g

500 mg = 0.5000 g
```

**Drug Dosage Calculator:**
```
Drug Dosage Calculator
Make sure both doses are in the same unit (e.g., mg or g).

Enter desired dose: 250
Enter on-hand dose: 500
Enter volume on hand (mL): 10

→ Give 5.00 mL
```

## How to Run
1. Make sure you have **Python 3.6+** installed.  
2. Download or clone this repository.  
3. Open your terminal or command prompt.  
4. Navigate to the project folder.  
5. Run the script:  
   ```bash
   python data/drug_dosage_calculator.py
   ```

## Project File
The main Python script is included in the `data` folder of this repository:  
[data/drug_dosage_calculator.py](data/drug_dosage_calculator.py)

## Skills Demonstrated
- Python programming fundamentals  
- Functions and error handling  
- Unit conversion logic  
- Drug dosage calculations  
- User experience (UX) through clear console prompts  

## Author
**Sofia Strisch**  
Toronto, Canada  
Registered Nurse | Data & Health Analytics Enthusiast
