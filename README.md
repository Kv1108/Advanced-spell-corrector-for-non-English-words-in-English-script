🪄 Auto Spell Correction for Non-English Words (Roman Script)
🔤 Intelligent Spell Corrector for Hindi & Gujarati Words Written in English Script

This project implements an advanced spell correction system designed specifically for non-English languages (like Hindi & Gujarati) written in Roman/English script.
It automatically detects and corrects misspelled words using a combination of:

Edit Distance (Levenshtein algorithm)

Phonetic similarity mapping

Multi-factor scoring system

📘 Project Overview

People often type Hindi or Gujarati words in English letters — for example:

aum → aam  
rajuu → raju  
bhavn → bhavan


Such transliterated spellings vary across users and regions.
This project corrects those spellings by comparing them to a reference dictionary of valid words.

⚙️ Features

✅ Supports phonetic correction (sound-alike words)
✅ Handles case-insensitive matches (e.g., “RAM” → “Ram”)
✅ Corrects character substitutions (e.g., ‘0’ ↔ ‘o’, ‘5’ ↔ ‘s’)
✅ Detects and fixes missing, extra, or swapped characters
✅ Supports combined multiple errors (like typos + phonetic variations)
✅ Provides detailed correction statistics (accuracy, time, performance)

🧩 How It Works
🔹 Step 1: Input Data

reference.txt → A list of correct words (dictionary)

errors.txt → A list of incorrect words (to be corrected)

Example:

reference.txt

ram
raju
aam
bhavan
shanti
mantra


errors.txt

rajuu
aum
bhavn
shanty

🔹 Step 2: Processing Flow

Load the dictionary of correct words (reference.txt)

Read all misspelled words (errors.txt)

For each word:

Check if it exists in dictionary (case-insensitive)

Generate edit-distance and phonetic variations

Filter valid candidates

Score each candidate using:

score = edit_dist + phon_dist*0.7 + len_diff*0.3 + case_bonus


Select the lowest-scoring (best) candidate

Save results in corrected_output.txt

Print correction accuracy statistics

🔹 Step 3: Output Data

corrected_output.txt

Error                          Corrected
============================================================
rajuu                          raju
aum                            aam
bhavn                          bhavan
shanty                         shanti

🧮 Algorithm Highlights
Component	Description
Edit Distance	Calculates how many edits (insert/delete/replace) are needed to correct a word.
Phonetic Map	Maps similar-sounding characters (e.g., c-k-q, s-z, a-e-o-u).
Character Similarity Map	Handles visually similar characters (0-o, 1-l, 5-s).
Scoring Formula	Combines edit, phonetic, and length similarity for best accuracy.
📊 Example Statistics (Console Output)
============================================================
SPELL CORRECTION STATISTICS
============================================================
Total words processed: 100
Time taken: 0.42 seconds
Words per second: 238.1

Correction Breakdown:
  Exact matches: 15 (15.0%)
  Case corrected: 10 (10.0%)
  Edit distance 1: 45 (45.0%)
  Edit distance 2: 20 (20.0%)
  Phonetic match: 5 (5.0%)
  No match found: 5 (5.0%)

Accuracy: 95.00%
============================================================

🧠 Data Source Information

The reference data (reference.txt) contains a curated list of verified Hindi and Gujarati words written in English (Roman) script.

It can be:

Manually compiled using common words, names, and terms.

Collected from open datasets such as:

Indic NLP Library

Open Multilingual WordNet

Expanded easily by adding new words to the file.

Example entry snippet:

krishna
vishnu
raju
bhavan
om
shanti

🧰 Setup and Usage
🪜 Requirements

Python 3.7+

A text editor (VS Code, Sublime, etc.)

No external libraries required — everything uses Python’s standard library.

▶️ How to Run

Place all files in the same folder:

spell_corrector.py
reference.txt
errors.txt


Run the script:

python spell_corrector.py


Output will be generated as:

corrected_output.txt
``` bash
📦 File Structure
📁 AutoSpellCorrector/
│
├── spell_corrector.py         # Main Python code
├── reference.txt              # Dictionary of correct words
├── errors.txt                 # Words to correct
├── corrected_output.txt       # Output file (auto-generated)
└── README.md                  # Documentation (this file)
```
🔍 Example Command-Line Run
> python spell_corrector.py
Loading errors from errors.txt...
Correcting 100 words...
Progress: 100/100 words processed...
Writing results to corrected_output.txt...

============================================================
SPELL CORRECTION STATISTICS
============================================================
Correction Breakdown:
  Exact matches: 261 (2.6%)
  Case corrected: 2381 (23.8%)
  Edit distance 1: 5105 (51.0%)
  Edit distance 2: 1914 (19.1%)
  Phonetic match: 42 (0.4%)
  No match found: 297 (3.0%)

Accuracy: 97.03%

📈 Future Improvements

Add ML-based scoring (learn weights automatically)

Add context-aware correction (using n-grams)

Integrate with Flask/Streamlit for web interface

Support multiple Indian languages dynamically

👨‍💻 Author
Krishna Viradiya


🪶 License

This project is open-source under the MIT License.
You are free to use, modify, and distribute it with proper attribution.
