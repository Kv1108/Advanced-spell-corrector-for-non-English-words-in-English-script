#!/usr/bin/env python3
"""
Generate Test Data for Spell Correction

Creates:
- reference.txt: ~5000 correct non-English words in English script
- errors.txt: ~10000+ misspelled versions with various error types
"""

import random
import string


class TestDataGenerator:
    """Generate test data for spell correction."""
    
    def __init__(self):
        self.base_words = [
            "Aam", "Ram", "Sita", "Krishna", "Radha", "Gita", "Bharat", "Delhi",
            "Mumbai", "Pune", "Ahmedabad", "Surat", "Vadodara", "Rajkot",
            "Roti", "Daal", "Chawal", "Sabzi", "Paneer", "Ghee", "Lassi", "Chai",
            "Samosa", "Pakora", "Jalebi", "Gulab", "Jamun", "Barfi", "Ladoo",
            "Kheer", "Halwa", "Puri", "Paratha", "Naan", "Kulcha", "Bhatura",
            "Dhokla", "Khandvi", "Thepla", "Fafda", "Khakhra", "Undhiyu", "Handvo",
            "Mata", "Pita", "Bhai", "Behen", "Dada", "Dadi", "Nana", "Nani",
            "Chacha", "Chachi", "Mama", "Mami", "Bua", "Mausa", "Beta", "Beti",
            "Pati", "Patni", "Sasur", "Saas", "Devar", "Jeth", "Nanad",
            "Aana", "Jaana", "Khana", "Peena", "Sona", "Uthna", "Baithna", "Khada",
            "Chalana", "Bolna", "Sunna", "Dekhna", "Samajhna", "Padhna", "Likhna",
            "Karna", "Hona", "Lena", "Dena", "Milna", "Aana", "Rona", "Hasna",
            "Kitab", "Kalam", "Kagaz", "Kursi", "Mez", "Darwaza", "Khidki",
            "Ghar", "Kamra", "Rasoi", "Bathroom", "Chhat", "Deewar", "Zameen",
            "Pankha", "Batti", "Pani", "Bartan", "Chulha", "Bistar", "Takiya",
            "Laal", "Neela", "Peela", "Hara", "Safed", "Kala", "Gulabi", "Bhura",
            "Narangi", "Baingani", "Sunehra", "Chandi",
            "Ek", "Do", "Teen", "Char", "Paanch", "Chhe", "Saat", "Aath",
            "Nau", "Das", "Gyarah", "Barah", "Terah", "Chaudah", "Pandrah",
            "Solah", "Satrah", "Atharah", "Unnis", "Bees", "Pachas", "Sau",
            "Namaste", "Namaskar", "Pranam", "Dhanyavaad", "Shukriya", "Alvida",
            "Khush", "Dukh", "Pyaar", "Nafrat", "Dost", "Dushman",
            "Kemcho", "Majama", "Aavjo", "Sahebji", "Benjo",
            "Suraj", "Chand", "Tara", "Aasman", "Badal", "Barish", "Hawa",
            "Pani", "Aag", "Mitti", "Patthar", "Ped", "Phool", "Phal",
            "Patta", "Jad", "Barf", "Dhuan", "Bijli", "Toofan",
            "Kutta", "Billi", "Gaay", "Bhains", "Ghoda", "Hathi", "Sher",
            "Chidiya", "Machli", "Saanp", "Bandar", "Bakri", "Murgi",
            "Bheda", "Unt", "Khargosh", "Gilhari", "Mor", "Kauwa", "Tota",
            "Subah", "Dopahar", "Shaam", "Raat", "Kal", "Aaj", "Parso",
            "Hafta", "Mahina", "Saal", "Din", "Ghanta", "Minute", "Pal",
            "Sir", "Aankh", "Naak", "Kaan", "Munh", "Haath", "Pair",
            "Ungli", "Peeth", "Pet", "Dil", "Dimag", "Gala", "Dant",
            "Baal", "Chehara", "Kandha", "Ghutna", "Kalaai",
            "Khushi", "Gham", "Gussa", "Dar", "Shanti", "Asha", "Vishwas",
            "Prem", "Krodh", "Santosh", "Daya", "Mamta",
            "Mandir", "Masjid", "Gurudwara", "School", "Hospital", "Bazaar",
            "Station", "Airport", "Park", "Jungle", "Parvat", "Nadi", "Samudra",
            "Kapde", "Kurta", "Pajama", "Saree", "Dhoti", "Dupatta", "Chunni",
            "Joote", "Chappal", "Topi", "Chaniyo", "Choli", "Kediyu",
            "Accha", "Bura", "Bada", "Chota", "Naya", "Purana", "Garam", "Thanda",
            "Meetha", "Namkeen", "Kadwa", "Khatta", "Teekha", "Sookha", "Geela",
            "Saaf", "Ganda", "Sundar", "Badsurat", "Ameer", "Gareeb",
            "Taza", "Basi", "Pakka", "Kachha", "Mota", "Patla", "Lamba", "Chhota",
            "Rajesh", "Suresh", "Mahesh", "Ganesh", "Ramesh", "Dinesh", "Naresh",
            "Yogesh", "Jignesh", "Hitesh", "Paresh", "Bhavesh", "Kalpesh",
            "Priya", "Pooja", "Anjali", "Sneha", "Kavita", "Sunita", "Geeta",
            "Meena", "Seema", "Reema", "Neha", "Rekha", "Asha", "Usha",
            "Divya", "Riya", "Nisha", "Komal", "Payal", "Hetal", "Kinjal",
            "Dikra", "Dikri", "Bapa", "Bapu", "Ben", "Vahala", "Jamva",
            "Pivanu", "Bethanu", "Ubhanu", "Chalvu", "Aavvu", "Javvu",
            "Ghanu", "Thodu", "Motu", "Patlu", "Lambu", "Nanhu",
        ]
        self._expand_word_list()
    
    def _expand_word_list(self):
        """Expand the word list to reach ~5000 words."""
        syllables = [
            "Ka", "Kha", "Ga", "Gha", "Cha", "Chha", "Ja", "Jha",
            "Ta", "Tha", "Da", "Dha", "Na", "Pa", "Pha", "Ba", "Bha",
            "Ma", "Ya", "Ra", "La", "Va", "Sha", "Sa", "Ha",
            "Ki", "Khi", "Gi", "Chi", "Ji", "Ti", "Di", "Ni", "Pi", "Bi", "Mi",
            "Ku", "Khu", "Gu", "Chu", "Ju", "Tu", "Du", "Nu", "Pu", "Bu", "Mu",
            "Ke", "Ge", "Je", "Te", "De", "Ne", "Pe", "Be", "Me",
            "Ko", "Kho", "Go", "Cho", "Jo", "To", "Do", "No", "Po", "Bo", "Mo",
            "Ri", "Li", "Vi", "Shi", "Si", "Hi",
            "Ru", "Lu", "Vu", "Shu", "Su", "Hu",
            "Re", "Le", "Ve", "She", "Se", "He",
            "Ro", "Lo", "Vo", "Sho", "So", "Ho",
        ]
        
        for i in range(2000):
            word = random.choice(syllables) + random.choice(syllables).lower()
            if word not in self.base_words and len(word) >= 3:
                self.base_words.append(word)
        
        for i in range(1500):
            word = (random.choice(syllables) + 
                   random.choice(syllables).lower() + 
                   random.choice(syllables).lower())
            if word not in self.base_words and len(word) >= 4:
                self.base_words.append(word)
        
        for i in range(500):
            word = (random.choice(syllables) + 
                   random.choice(syllables).lower() + 
                   random.choice(syllables).lower() + 
                   random.choice(syllables).lower())
            if word not in self.base_words and len(word) >= 5:
                self.base_words.append(word)
    
    def generate_case_error(self, word: str) -> str:
        """Generate case-related errors."""
        error_type = random.choice(['upper', 'lower', 'random'])
        
        if error_type == 'upper':
            return word.upper()
        elif error_type == 'lower':
            return word.lower()
        else:
            return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in word)
    
    def generate_phonetic_error(self, word: str) -> str:
        """Generate phonetic errors (sound-alike substitutions)."""
        phonetic_map = {
            'a': ['aa', 'e', 'u', 'o'],
            'e': ['a', 'i', 'ee'],
            'i': ['e', 'ee', 'y'],
            'o': ['a', 'u', 'au'],
            'u': ['oo', 'a', 'o'],
            'b': ['p', 'v'],
            'p': ['b', 'f'],
            'v': ['b', 'w'],
            'w': ['v'],
            'f': ['ph', 'v'],
            'c': ['k', 's', 'ch'],
            'k': ['c', 'q', 'kh'],
            'q': ['k', 'c'],
            's': ['z', 'sh', 'c'],
            'z': ['s', 'j'],
            'd': ['t', 'dh'],
            't': ['d', 'th'],
            'g': ['j', 'gh'],
            'j': ['g', 'z'],
            'm': ['n'],
            'n': ['m', 'nn'],
            'r': ['l'],
            'l': ['r'],
        }
        
        word_list = list(word.lower())
        if len(word_list) == 0:
            return word
        
        num_changes = random.randint(1, min(2, len(word_list)))
        positions = random.sample(range(len(word_list)), num_changes)
        
        for pos in positions:
            char = word_list[pos]
            if char in phonetic_map:
                word_list[pos] = random.choice(phonetic_map[char])
        
        result = ''.join(word_list)
        if word[0].isupper():
            result = result.capitalize()
        return result
    
    def generate_typo_error(self, word: str) -> str:
        """Generate typing errors (missing, extra, transposed characters)."""
        error_type = random.choice(['delete', 'insert', 'transpose', 'substitute'])
        word_list = list(word)
        
        if len(word_list) <= 1:
            return word
        
        if error_type == 'delete':
            pos = random.randint(0, len(word_list) - 1)
            word_list.pop(pos)
        
        elif error_type == 'insert':
            pos = random.randint(0, len(word_list))
            char = random.choice(string.ascii_lowercase)
            word_list.insert(pos, char)
        
        elif error_type == 'transpose':
            pos = random.randint(0, len(word_list) - 2)
            word_list[pos], word_list[pos + 1] = word_list[pos + 1], word_list[pos]
        
        elif error_type == 'substitute':
            keyboard_neighbors = {
                'a': 'sqwz', 'b': 'vghn', 'c': 'xdfv', 'd': 'sfcxe', 'e': 'wrd',
                'f': 'dgcvr', 'g': 'fhbvt', 'h': 'gjnby', 'i': 'uko', 'j': 'hknmu',
                'k': 'jlmi', 'l': 'kop', 'm': 'njk', 'n': 'bhjm', 'o': 'ilp',
                'p': 'ol', 'q': 'wa', 'r': 'etf', 's': 'awdxz', 't': 'rygf',
                'u': 'yij', 'v': 'cfgb', 'w': 'qase', 'x': 'zsdc', 'y': 'tuh',
                'z': 'asx'
            }
            pos = random.randint(0, len(word_list) - 1)
            char = word_list[pos].lower()
            if char in keyboard_neighbors:
                word_list[pos] = random.choice(keyboard_neighbors[char])
        
        return ''.join(word_list)
    
    def generate_repetition_error(self, word: str) -> str:
        """Generate character repetition errors."""
        word_list = list(word)
        if len(word_list) <= 1:
            return word
        
        if random.random() > 0.5:
            pos = random.randint(0, len(word_list) - 1)
            word_list.insert(pos, word_list[pos])
        else:
            for i in range(len(word_list) - 1):
                if word_list[i].lower() == word_list[i + 1].lower():
                    word_list.pop(i)
                    break
        
        return ''.join(word_list)
    
    def generate_combined_error(self, word: str) -> str:
        """Generate multiple types of errors combined."""
        num_errors = random.randint(2, 3)
        error_functions = [
            self.generate_case_error,
            self.generate_phonetic_error,
            self.generate_typo_error,
            self.generate_repetition_error
        ]
        
        result = word
        selected_errors = random.sample(error_functions, num_errors)
        for error_func in selected_errors:
            result = error_func(result)
        
        return result
    
    def generate_errors(self, word: str, count: int = 2) -> list:
        """Generate multiple error variations of a word."""
        errors = []
        error_generators = [
            self.generate_case_error,
            self.generate_phonetic_error,
            self.generate_typo_error,
            self.generate_repetition_error,
            self.generate_combined_error
        ]
        
        for _ in range(count):
            error_func = random.choice(error_generators)
            error_word = error_func(word)
            if error_word != word and error_word not in errors:
                errors.append(error_word)
        
        return errors
    
    def generate_files(self, reference_file: str = 'reference.txt', 
                      errors_file: str = 'errors.txt',
                      num_reference_words: int = 5000,
                      num_error_words: int = 10000):
        """Generate reference and errors files."""
        print(f"Generating {num_reference_words} reference words...")
        
        while len(self.base_words) < num_reference_words:
            self._expand_word_list()
        
        reference_words = list(set(self.base_words[:num_reference_words]))
        
        with open(reference_file, 'w', encoding='utf-8') as f:
            for word in sorted(reference_words):
                f.write(word + '\n')
        
        print(f"Generated {len(reference_words)} reference words in {reference_file}")
        
        print(f"Generating {num_error_words} error words...")
        error_words = []
        
        while len(error_words) < num_error_words:
            word = random.choice(reference_words)
            errors = self.generate_errors(word, count=random.randint(1, 3))
            error_words.extend(errors)
        
        error_words = error_words[:num_error_words]
        random.shuffle(error_words)
        
        with open(errors_file, 'w', encoding='utf-8') as f:
            for error in error_words:
                f.write(error + '\n')
        
        print(f"Generated {len(error_words)} error words in {errors_file}")
        print("\nTest data generation complete!")
        print(f"\nExample errors generated:")
        for i in range(min(20, len(error_words))):
            print(f"  {error_words[i]}")


def main():
    """Main function to generate test data."""
    generator = TestDataGenerator()
    generator.generate_files(
        reference_file='reference.txt',
        errors_file='errors.txt',
        num_reference_words=5000,
        num_error_words=10000
    )


if __name__ == '__main__':
    main()
