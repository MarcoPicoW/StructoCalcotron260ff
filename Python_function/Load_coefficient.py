import pandas as pd

Load_coefficient = pd.DataFrame([
    # Ständige Einwirkungen
    ["Ständige Einwirkungen", "ungünstig wirkend", "γG,sup", 1.10, 1.35, 1.00],
    ["", "günstig wirkend", "γG,inf", 0.90, 0.80, 1.00],

    # Veränderliche Einwirkungen
    ["Veränderliche Einwirkungen", "im Allgemeinen", "γQ", 1.50, 1.50, 1.30],
    ["Veränderliche Einwirkungen", "Strassenverkehrslasten", "γQ", 1.50, 1.50, 1.30],
    ["Veränderliche Einwirkungen", "Bahnverkehrslasten (LM 1,2,4 bis 7)", "γQ", 1.45, 1.45, 1.25],
    ["Veränderliche Einwirkungen", "Bahnverkehrslasten (LM 3)", "γQ", 1.45, 1.20, 1.25],

    # Einwirkungen aus dem Baugrund
    ["Erdaulasten", "ungünstig wirkend", "γG,sup", 1.10, 1.35, 1.00],
    ["", "günstig wirkend", "γG,inf", 0.90, 0.80, 1.00],

    ["Erddruck", "ungünstig wirkend", "γG,Q,sup", 1.35, 1.35, 1.00],
    ["", "günstig wirkend", "γG,Q,inf", 0.80, 0.70, 1.00],

    ["Wasserdruck", "ungünstig wirkend", "γG,Q,sup", 1.05, 1.20, 1.00],
    ["", "günstig wirkend", "γG,Q,inf", 0.95, 0.90, 1.00],
],
columns=["Einwirkung", "Wirkungsart", "γF", "Typ 1", "Typ 2", "Typ 3"]
)

print(Load_coefficient)


