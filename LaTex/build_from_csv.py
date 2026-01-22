#!/usr/bin/env python3
import csv
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

TEX_FILE = Path("Achsenlast_verteilung.tex")
CSV_FILE = Path("names.csv")

# --- util: jobname sicuro per filesystem + TeX ---
def safe_jobname(s: str) -> str:
    s = s.strip()

    # normalizza (toglie accenti/umlaut -> ASCII)
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")

    # spazi e caratteri strani -> underscore
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)

    # evita jobname vuoto
    return s or "output"

def parse_float(cell: str) -> str:
    """
    Ritorna una stringa numerica adatta a \def\macro{...}
    Gestisce spazi e virgole decimali (se presenti).
    """
    if cell is None:
        return ""
    s = cell.strip()
    if not s:
        return ""
    # se qualcuno usa la virgola come decimale
    s = s.replace(",", ".")
    # rimuove cose tipo "+- 2.0", "55.6 und 2.9" -> prende il primo numero
    m = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", s)
    return m.group(0) if m else ""

def main():
    if not TEX_FILE.exists():
        print(f"Errore: file TeX non trovato: {TEX_FILE}")
        sys.exit(1)
    if not CSV_FILE.exists():
        print(f"Errore: file CSV non trovato: {CSV_FILE}")
        sys.exit(1)

    # Legge CSV "a virgole" con spazi dopo la virgola
    with CSV_FILE.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, skipinitialspace=True)

        # Controllo colonne minime
        needed = {"ObjektName", "Platte_Stärke", "h1"}
        missing = needed - set(reader.fieldnames or [])
        if missing:
            print("Errore: mancano colonne nel CSV:", ", ".join(sorted(missing)))
            print("Colonne trovate:", reader.fieldnames)
            sys.exit(1)

        ok = 0
        skipped = 0

        for i, row in enumerate(reader, start=2):  # 1=header, quindi dati da 2
            objekt = (row.get("ObjektName") or "").strip()
            if not objekt:
                skipped += 1
                print(f"[riga {i}] saltata: ObjektName vuoto")
                continue

            jobname = safe_jobname(objekt)
            dicke = parse_float(row.get("Platte_Stärke", ""))
            h = parse_float(row.get("h1", ""))

            if not dicke or not h:
                skipped += 1
                print(f"[riga {i}] saltata: valori mancanti (h1='{row.get('h1','')}', Platte_Stärke='{row.get('Platte_Stärke','')}')")
                continue

            # Comando pdflatex con macro definite prima dell'input
            tex_call = f"\\def\\h{{{h}}}\\def\\dicke{{{dicke}}}\\input{{{TEX_FILE.name}}}"

            cmd = [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-jobname={jobname}",
                tex_call,
            ]

            print(f"[riga {i}] -> {jobname}.pdf   (h={h}, dicke={dicke})")
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            if res.returncode != 0:
                print(f"ERRORE compilazione su riga {i} ({jobname}):")
                print(res.stdout)
                sys.exit(res.returncode)

            ok += 1

        print(f"\nFatto. PDF creati: {ok}. Righe saltate: {skipped}.")

if __name__ == "__main__":
    main()
