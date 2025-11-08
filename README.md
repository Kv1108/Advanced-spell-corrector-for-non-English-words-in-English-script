# 🪄 Auto Spell Correction for Non-English Words (Roman Script)
# 🔤 Intelligent Spell Corrector for Hindi & Gujarati Words Written in English Script
---
This project is an advanced spell correction system that automatically detects and corrects misspelled Hindi or Gujarati words written in English (Roman) script.

It combines:

🧮 Edit Distance (Levenshtein Algorithm)

🔊 Phonetic Similarity Mapping

🧠 Multi-Factor Scoring System

to deliver over 97% accuracy on a dataset of 10,000 words.
---
📘 Overview

Many users type Hindi or Gujarati words in English (e.g., aum, rajuu, bhavn).
The spell corrector takes such words and automatically converts them into their correct form using a custom-built dictionary.

Example:
aum   → aam  
rajuu → raju  
bhavn → bhavan

⚙️ Features

✅ Handles phonetic and spelling variations
✅ Fixes case mismatches (e.g., RAM → Ram)
✅ Corrects missing, swapped, or repeated letters
✅ Detects sound-alike errors (aum → aam)
✅ Supports visual similarity corrections (0-o, 1-l, 5-s)
✅ Provides detailed accuracy & performance statistics

🧩 System Workflow
reference.txt  →  spell_corrector.py  →  errors.txt  →  corrected_output.txt

🔹 Step-by-Step Flow

Load dictionary (reference.txt) — Contains valid words (Hindi/Gujarati in Roman script)

Load input words (errors.txt) — Contains words to be corrected

Compare & Generate Variations — Edit distance and phonetic variations are created

Score & Rank Candidates — Using a weighted formula:

score = edit_dist + phon_dist*0.7 + len_diff*0.3 + case_bonus


Select Best Correction — Lowest scoring candidate is chosen

Write Results — Saved to corrected_output.txt

Display Stats — Accuracy, timing, and performance summary shown on console

🧾 Example Data
reference.txt
ram
raju
aam
bhavan
shanti
mantra
krishna
vishnu

errors.txt
rajuu
aum
bhavn
shanty

corrected_output.txt
Error                          Corrected
============================================================
rajuu                          raju
aum                            aam
bhavn                          bhavan
shanty                         shanti
```bash
📊 Real Execution Report
C:\Users\Krishna\Desktop\Interview> python spell_corrector.py
Loading errors from errors.txt...
Correcting 10000 words...
Progress: 1000/10000 words processed...
Progress: 2000/10000 words processed...
Progress: 3000/10000 words processed...
Progress: 4000/10000 words processed...
Progress: 5000/10000 words processed...
Progress: 6000/10000 words processed...
Progress: 7000/10000 words processed...
Progress: 8000/10000 words processed...
Progress: 9000/10000 words processed...
Progress: 10000/10000 words processed...
Writing results to corrected_output.txt...

============================================================
SPELL CORRECTION STATISTICS
============================================================
Total words processed: 10000
Time taken: 254.31 seconds
Words per second: 39.32

Correction Breakdown:
  Exact matches: 261 (2.6%)
  Case corrected: 2381 (23.8%)
  Edit distance 1: 5105 (51.0%)
  Edit distance 2: 1914 (19.1%)
  Phonetic match: 42 (0.4%)
  No match found: 297 (3.0%)

Accuracy: 97.03%
============================================================

Correction complete! Results saved to corrected_output.txt
```
🧮 Algorithm Components
Component	Description
🧾 Edit Distance	Measures how many insert/delete/replace operations are needed to transform one word into another.
🔊 Phonetic Map	Groups similar-sounding characters (c-k-q, s-z, a-e-o-u).
👁️ Character Similarity Map	Handles visually similar letters (0-o, 1-l, 5-s).
🧠 Weighted Scoring System	Combines all metrics for best correction accuracy.
🧩 Multi-Level Matching	Uses Edit Distance 1 → Phonetic → Edit Distance 2 → Hybrid approach.
🧠 Data Source Information

The reference data (reference.txt) consists of verified Hindi and Gujarati words written in English (Roman) script.

📚 Sources:

Indic NLP Library

Open Multilingual WordNet

Manually curated list of common words, names, and cultural terms.

🧰 Setup and Usage
🪜 Requirements
```bash
Python ≥ 3.7

No external dependencies (uses only built-in Python libraries)

▶️ Run the Project
# 1️⃣ Clone or copy project folder
cd "C:\Users\Krishna\Desktop\Interview"

# 2️⃣ Ensure files exist
# ├── spell_corrector.py
# ├── reference.txt
# ├── errors.txt

# 3️⃣ Run the script
python spell_corrector.py

# 4️⃣ Output file will be generated
# corrected_output.txt

📁 Project Structure
📦 AutoSpellCorrector
│
├── spell_corrector.py          # Main algorithm
├── reference.txt               # Dictionary of correct words
├── errors.txt                  # Misspelled input words
├── corrected_output.txt        # Generated output (auto)
└── README.md                   # Documentation (this file)
```
---
📈 Performance Summary
Metric	Value
Words processed	10,000
Execution time	254.31 seconds
Words per second	39.32
Overall Accuracy	🟩 97.03%
Main correction type	Edit Distance 1 (51%)
💡 Future Enhancements

✨ Add machine learning–based scoring (learn weights automatically)
✨ Integrate Flask/Streamlit web interface for user interaction
✨ Expand to other Indian languages (Marathi, Tamil, Bengali, etc.)
✨ Add context-aware correction using N-grams or embeddings

👨‍💻 Author
Krishna Viradiya

🪶 License

This project is licensed under the MIT License —
you are free to use, modify, and distribute it with attribution.
