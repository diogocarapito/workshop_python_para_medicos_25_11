def gfr_cki(age=30, creatinine=0.9, sex="Mulher"):

    # Formula GFR KPI
    # 142 × (Scr/A)B × 0.9938age × (1.012 if Mulher)

    # Validações de entrada
    if creatinine <= 0 or creatinine is None or creatinine > 20:
        raise ValueError("Creatinina deve ser um valor entre 0 e 20 mg/dL.")

    if sex not in ["Mulher", "Homem"]:
        raise ValueError("Sexo inválido. Deve ser 'Mulher' ou 'Homem'.")

    if age < 0 or age is None or age > 120:
        raise ValueError("Idade deve ser um valor entre 0 e 120.")

    # Constantes
    base_factor = 142
    age_factor = 0.9938
    sex_factor = 1.012 if sex == "Mulher" else 1

    # Coeficientes baseados no sexo e níveis de creatinina
    coeficients = {
        "Mulher": {
            "Scr ≤0.7": {"A": 0.7, "B": -0.241},
            "Scr >0.7": {"A": 0.7, "B": -1.2},
        },
        "Homem": {
            "Scr ≤0.9": {"A": 0.9, "B": -0.302},
            "Scr >0.9": {"A": 0.9, "B": -1.2},
        },
    }

    # Default assignment for src
    src = None

    if sex == "Mulher":
        if creatinine <= 0.7:
            src = "Scr ≤0.7"
        else:
            src = "Scr >0.7"
    elif sex == "Homem":
        if creatinine <= 0.9:
            src = "Scr ≤0.9"
        else:
            src = "Scr >0.9"
    else:
        raise ValueError("Invalid sex value. Must be 'Mulher' or 'Homem'.")

    # Cálculo do GFR
    gfr = (
        base_factor
        * (creatinine / coeficients[sex][src]["A"]) ** coeficients[sex][src]["B"]
        * age_factor**age
        * sex_factor
    )

    # Arredondar o resultado para 1 casa decimal
    gfr = round(gfr, 1)

    return gfr


if __name__ == "__main__":

    # Valores iniciais
    age = 30
    creatinine = 0.9
    sex = "Mulher"

    # Cálculo do GFR CKI
    gfr = gfr_cki(age, creatinine, sex)

    # print dos resultados
    print(
        f"""
Calculating GFR CKI with the following parameters:
Age: {age}
Creatinine: {creatinine}
Sex: {sex}
---
GFR CKI: {gfr} mL/min/1.73m²
"""
    )
