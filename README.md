# 🧱 StructoCalcotron260ff — README (dumb draft)

> 🧠 The *totally serious* structural analysis tool that definitely won’t crash your building. Reads CSVs 📊, pretends to follow SIA 260 ff. 📘, and spits out a LaTeX report with TikZ doodles 🎨.

## ⚙️ What it (kinda) does

* **Input:** Throw a CSV full of “structure data” at it. Hope it makes sense 🤷‍♂️.
* **Compute:** Apply highly scientific formulas inspired (ish) by SIA 260 ff. 🧮.
* **Output:** Auto-generates a LaTeX report that looks official enough to fool your boss 📄.
* **Visuals:** Uses TikZ to draw majestic stick figures pretending to be structures 🏗️.

## 🪄 The grand plan

Because everything serious starts dumb:

### 🧩 Part 1 — Tiny smart-ish functions

Little helpers that do one thing (and sometimes the right thing):

* 📂 **CSV parsing** — turns your chaos into a dictionary of confusion.
* 🧱 **Materials** — steel, concrete, hopes, dreams.
* 📐 **Geometry** — compute inertia, area, or your existential dread.
* 💨 **Loads** — apply gravity (or blame it for everything).
* 🔢 **Combinations** — multiply by scary Greek letters (γ, ψ, whatever feels right).
* 💥 **Checks** — N, M, V, maybe sanity.
* 🖋️ **Formatter** — makes numbers look like they mean something.

### 🔧 Part 2 — The Big Merge

Glue all the baby functions together into something that *almost* works:

* 🧾 Read CSV → validate (ish) → calculate → collect results.
* 🧠 Keep a log of assumptions (a.k.a. excuses).
* ⚙️ Config file for your custom set of errors.

### 📚 Part 3 — The Report Factory

* 🪶 One **LaTeX template** to rule them all.
* 📄 Generates a beautiful `.tex` file full of questionable results.
* 🏢 Optional logo for the illusion of professionalism.
* ☠️ Compiles a PDF if your system doesn’t rebel first.

### 🎨 Part 4 — TikZ Magic

* 🧱 Draw beams, arrows, and triangles like a structural caveman.
* 📈 Load diagrams that look cooler than they are accurate.
* 😭 Support reactions that react emotionally.
* 🎯 Uses TikZ because nothing says pain like debugging coordinates.

## 🗂️ CSV Format (good luck)

* **Project:** name, location, version of your despair.
* **Materials:** `id, type (steel/concrete/wood/plasticine), grade`.
* **Elements:** `id, type, material_id, geometry, length`.
* **Loads:** `element_id, case, type, value`.

## 🚀 Future ideas (that may or may not happen)

* 🧮 Add real calculations (eventually).
* 🧰 More materials, fewer mistakes.
* 🇨🇭 Reports in multiple languages (Swiss German optional).
* 📊 Fancy plots no one asked for.

## 🧗 Example workflow

1. 📝 Create a CSV.
2. ⚙️ Run `run_calculation(csv, config)`.
3. 📄 Watch it generate a PDF that *looks* credible.
4. 😎 Present it. Smile confidently.

## 📘 Notes on SIA usage

We respect SIA 260 ff. — just not enough to quote it here. The constants are configurable so you can blame someone else.

---

**🤖 StructoCalcotron260ff:** making structures safe-ish since 2025 💥.
