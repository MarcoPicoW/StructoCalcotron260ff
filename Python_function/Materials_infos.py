# Glossary: Mittlere Raumlasten von Baustoffen (kN/m³)
# Quelle: SIA / Bauingenieurwesen Tabelle 28

raumlasten = {
    "Metalle": {
        "Aluminium": 27,
        "Baustahl": 78.5,
    },
    "Beton": {
        "unbewehrt": 24,
        "bewehrt": 25,
        "Leichtbeton (im Einzelfall zu bestimmen)": None,  # Wert individuell bestimmen
    },
    "Holz": {
        "Nadelhölzer, allgemein": 5,
        "Laubhölzer, allgemein": 7.5,
        "verleimte Nadelhölzer": 5,
        "Spanplatten": 8,
    },
    "Natursteinmauerwerk": {
        "Bruchstein (Kalkstein)": 24,
        "Granit": 27,
        "Basalt": 30,
        "Molasse-Sandstein": 24,
    },
    "Mörtelüberzüge": {
        "Kalkmörtel": 19,
        "Zementmörtel": 22,
        "Gipsmörtel": 12,
        "Wandverputz aussen": 18,
        "Wandverputz innen": 14,
    },
    "Mauerwerk, unverputzt": {
        "Backsteine, voll": 18,
        "Backsteine, gelocht": 13,
        "Backsteine, schalldämmend": 17,
        "Sichtbacksteine, gelocht": 15,
        "Zementsteine, voll": 22,
        "Zementsteine, gelocht": 18,
        "Zementsteine, schalldämmend": 20,
        "Kalksandsteine, voll": 20,
        "Kalksandsteine, gelocht": 18,
        "Gasbetonsteine, normale Qualität": 6,
        "Gasbetonsteine, hochwertig": 7,
        "Glasbausteine, voll": 25,
        "Glasbausteine, hohl": 14,
        "Zelltonplatten": 12,
        "Gipsplatten": 12,
    },
    "Bodenbeläge": {
        "Keramikplatten": 20,
        "Natursteine": 30,
        "Holzparkett, geklebt": 8,
        "Linoleum": 15,
    },
    "Bituminöse Beläge": {
        "Gussasphalt": 24,
        "Bituminöser Belag (HMT)": 24,
    },
}

# Glossary: Mittlere Flächenlasten von Bedachungen und Verkleidungen (kN/m²)
# Quelle: SIA / Bauingenieurwesen Tabelle 29

flaechenlasten = {
    "Bedachungen und Verkleidungen": {
        "Faserzement": 0.18,
        "Profilbleche, Höhe 80 mm, Dicke 0.8 mm": 0.12,
        "Stahlblech": 0.12,
        "Aluminiumblech": 0.04,
        "Faserzementschieferdach (Einfachdeckung)": 0.23,
        "Faserzementschieferdach (Doppeldeckung)": 0.30,
        "Tondachziegel inkl. Lattung (Biberschwanz, Doppeldeckung)": 0.75,
        "Tondachziegel inkl. Lattung (Pfannenziegel)": 0.47,
        "Betonziegeldach inkl. Lattung (Flachziegel)": 0.55,
        "Betonziegeldach inkl. Lattung (Pfannenziegel)": 0.48,
    },
    "Unterdächer": {
        "Schindelunterzug": 0.10,
        "Hartfaserplatten": 0.05,
        "Faserzementplatten": 0.12,
        "Holzschalung, 24 mm inkl. eine Lage Bitumenpappe oder Kunststofffolie": 0.14,
    },
    "Verglasung inkl. Rahmenkonstruktion": {
        "Normalglas, 5 mm": 0.25,
        "Armiertes Glas, 6 mm": 0.35,
        "Feinkiesauflage, pro 10 mm Dicke": 0.20,
    },
    "Zusätzliche Materialien": {
        "Bitumenpappe, pro Lage": 0.02,
        "Kunststofffolie": 0.02,
        "Mörtelüberzüge": 0.02,
    },
}

# Table 30 — Raumlasten (kN/m³)
raumlast_Erdauflasten_Gleischotter_Lagergüter = {
    "Erdauflasten und Gleisschotter": {
        "Sand": 15.0,
        "Kiessand, gemischt": 20.0,
        "Schotter, gebrochen": 18.0,
        "Erde, trocken": 16.0,
        "Erde, nass": 21.0,
        "Bauschutt (im Mittel)": 14.0,
    },
    "Brennstoffe": {
        "Steinkohle": 9.0,
        "Briketts, geschüttet": 9.0,
        "Briketts, gestapelt": 13.5,
        "Koks, geschüttet": 5.0,
    },
    "Holz in Scheitern": {
        "Nadelholz, trocken": 4.4,
        "Nadelholz, nass": 6.5,
        "Laubholz, trocken": 7.0,
        "Laubholz, nass": 10.0,
        "Holzspäne, geschüttet": 1.5,
        "Holzspäne, gut gepresst": 2.5,
    },
    "Bindemittel": {
        "Hydraulischer Kalk": 12.0,
        "Zement im Silo": 16.0,
        "Zement in Säcken": 12.0,
        "Zementklinker, geschüttet": 17.0,
    },
    "Flüssige Stoffe": {
        "Benzin": 7.3,
        "Petrol-, Diesel- und Heizöl": 8.5,
        "Steinkohleteer, Bitumen": 12.0,
        "Mineralschmieröl": 9.2,
        "Pflanzenöl": 9.5,
    },
    "Papier": {
        "Bücher auf Gestellen": 6.0,
        "Papier, geschichtet": 11.0,
        "Papier, in Rollen": 15.0,
    },
    "Futtermittel": {
        "Getreide, geschüttet": 7.5,
        "Kartoffeln, Zuckerrüben": 7.0,
        "Heu und Stroh, geschüttet": 1.5,
        "Grünfutter, geschüttet": 3.5,
    },
    "Stallmist": {
        "Stallmist, verrottet": 9.5,
    },
    "Nahrungsmittel": {
        "Mehl, geschüttet": 6.0,
        "Zucker, geschüttet": 9.5,
        "Salz, geschüttet": 12.0,
        "Salz, in Säcken": 10.0,
    },
}

# Table 30 — Schüttwinkel (°)
# Single value -> float; range -> (min, max); not given -> None
schuettwinkel_Erdauflasten_Gleischotter_Lagergüter = {
    "Erdauflasten und Gleisschotter": {
        "Sand": 35.0,
        "Kiessand, gemischt": 27.0,
        "Schotter, gebrochen": 35.0,
        "Erde, trocken": (40.0, 45.0),
        "Erde, nass": (20.0, 25.0),
        "Bauschutt (im Mittel)": (30.0, 35.0),
    },
    "Brennstoffe": {
        "Steinkohle": 35.0,
        "Briketts, geschüttet": 30.0,
        "Briketts, gestapelt": None,
        "Koks, geschüttet": None,
    },
    "Holz in Scheitern": {
        "Nadelholz, trocken": 45.0,
        "Nadelholz, nass": 45.0,
        "Laubholz, trocken": 45.0,
        "Laubholz, nass": 45.0,
        "Holzspäne, geschüttet": 25.0,
        "Holzspäne, gut gepresst": 45.0,
    },
    "Bindemittel": {
        "Hydraulischer Kalk": 25.0,
        "Zement im Silo": 30.0,
        "Zement in Säcken": None,
        "Zementklinker, geschüttet": 30.0,
    },
    "Flüssige Stoffe": {
        "Benzin": None,
        "Petrol-, Diesel- und Heizöl": None,
        "Steinkohleteer, Bitumen": None,
        "Mineralschmieröl": None,
        "Pflanzenöl": None,
    },
    "Papier": {
        "Bücher auf Gestellen": None,
        "Papier, geschichtet": None,
        "Papier, in Rollen": None,
    },
    "Futtermittel": {
        "Getreide, geschüttet": 30.0,
        "Kartoffeln, Zuckerrüben": 30.0,
        "Heu und Stroh, geschüttet": None,
        "Grünfutter, geschüttet": None,
    },
    "Stallmist": {
        "Stallmist, verrottet": None,
    },
    "Nahrungsmittel": {
        "Mehl, geschüttet": 35.0,
        "Zucker, geschüttet": 35.0,
        "Salz, geschüttet": 40.0,
        "Salz, in Säcken": None,
    },
}
