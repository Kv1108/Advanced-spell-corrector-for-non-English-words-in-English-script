import re
import time
from collections import defaultdict
from typing import List, Tuple, Dict, Set
import unicodedata


class SpellCorrector:
    """Advanced spell corrector for non-English words in English script."""
    
    def __init__(self, dictionary_file: str):
        self.dictionary = self._load_dictionary(dictionary_file)
        self.dictionary_lower = {word.lower(): word for word in self.dictionary}
        self.dictionary_set = set(self.dictionary)
        self.dictionary_lower_set = set(self.dictionary_lower.keys())
        
        self.phonetic_map = self._build_phonetic_map()
        self.char_similarity = self._build_char_similarity_map()
        
        self.stats = {
            'total_words': 0,
            'exact_match': 0,
            'case_corrected': 0,
            'edit_distance_1': 0,
            'edit_distance_2': 0,
            'phonetic_match': 0,
            'no_match': 0
        }
    
    def _load_dictionary(self, filepath: str) -> Set[str]:
        """Load dictionary from file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    
    def _build_phonetic_map(self) -> Dict[str, str]:
        """Build phonetic similarity mapping for common sound-alike characters."""
        return {
            'a': 'aeiou',
            'e': 'aeiou',
            'i': 'eiyu',
            'o': 'aou',
            'u': 'aou',
            'b': 'bpv',
            'p': 'bp',
            'v': 'bvw',
            'w': 'vw',
            'f': 'fv',
            'c': 'ckqs',
            'k': 'ckq',
            'q': 'ckq',
            's': 'szcx',
            'z': 'sz',
            'x': 'ksx',
            'd': 'dt',
            't': 'dt',
            'g': 'gjk',
            'j': 'gj',
            'm': 'mn',
            'n': 'mn',
            'r': 'rl',
            'l': 'rl',
        }
    
    def _build_char_similarity_map(self) -> Dict[str, str]:
        """Build character similarity map for visually similar characters."""
        return {
            '0': 'o',
            'o': '0',
            '1': 'il',
            'i': '1l',
            'l': '1i',
            '5': 's',
            's': '5',
            '8': 'b',
            'b': '8',
        }
    
    def normalize_word(self, word: str) -> str:
        """Normalize word by removing accents and special characters."""
        word = ''.join(
            c for c in unicodedata.normalize('NFD', word)
            if unicodedata.category(c) != 'Mn'
        )
        return word
    
    def edit_distance_1(self, word: str) -> Set[str]:
        """Generate all words at edit distance 1 from the input word."""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        
        return set(deletes + transposes + replaces + inserts)
    
    def edit_distance_2(self, word: str) -> Set[str]:
        """Generate all words at edit distance 2 from the input word."""
        return set(
            e2 for e1 in self.edit_distance_1(word)
            for e2 in self.edit_distance_1(e1)
        )
    
    def phonetic_variations(self, word: str) -> Set[str]:
        """Generate phonetic variations of a word."""
        variations = {word}
        word_lower = word.lower()
        
        for i, char in enumerate(word_lower):
            if char in self.phonetic_map:
                similar_chars = self.phonetic_map[char]
                for similar in similar_chars:
                    if similar != char:
                        new_word = word_lower[:i] + similar + word_lower[i+1:]
                        variations.add(new_word)
        
        return variations
    
    def get_candidates(self, word: str) -> Set[str]:
        """Get all candidate corrections for a word."""
        word_lower = word.lower()
        
        if word_lower in self.dictionary_lower_set:
            return {self.dictionary_lower[word_lower]}
        
        candidates = set()
        
        ed1 = self.edit_distance_1(word_lower)
        candidates.update(w for w in ed1 if w in self.dictionary_lower_set)
        
        if candidates:
            return {self.dictionary_lower[w] for w in candidates}
        
        phonetic = self.phonetic_variations(word_lower)
        candidates.update(w for w in phonetic if w in self.dictionary_lower_set)
        
        if candidates:
            return {self.dictionary_lower[w] for w in candidates}
        
        ed2 = self.edit_distance_2(word_lower)
        candidates.update(w for w in ed2 if w in self.dictionary_lower_set)
        
        if candidates:
            return {self.dictionary_lower[w] for w in candidates}
        
        for phon_var in phonetic:
            ed1_phon = self.edit_distance_1(phon_var)
            candidates.update(w for w in ed1_phon if w in self.dictionary_lower_set)
        
        if candidates:
            return {self.dictionary_lower[w] for w in candidates}
        
        return candidates
    
    def levenshtein_distance(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def phonetic_distance(self, s1: str, s2: str) -> float:
        """Calculate phonetic similarity score (lower is better)."""
        s1, s2 = s1.lower(), s2.lower()
        
        if s1 == s2:
            return 0.0
        
        base_distance = self.levenshtein_distance(s1, s2)
        
        phonetic_penalty = 0
        min_len = min(len(s1), len(s2))
        
        for i in range(min_len):
            if s1[i] != s2[i]:
                if s1[i] in self.phonetic_map:
                    if s2[i] in self.phonetic_map[s1[i]]:
                        phonetic_penalty -= 0.5
        
        return base_distance + phonetic_penalty
    
    def select_best_candidate(self, word: str, candidates: Set[str]) -> str:
        """Select the best candidate from multiple options."""
        if not candidates:
            return word
        
        if len(candidates) == 1:
            return list(candidates)[0]
        
        scored_candidates = []
        word_lower = word.lower()
        
        for candidate in candidates:
            candidate_lower = candidate.lower()
            
            edit_dist = self.levenshtein_distance(word_lower, candidate_lower)
            phon_dist = self.phonetic_distance(word_lower, candidate_lower)
            
            len_diff = abs(len(word) - len(candidate))
            
            case_bonus = 0
            if word[0].isupper() == candidate[0].isupper():
                case_bonus = -0.5
            
            score = edit_dist + phon_dist * 0.7 + len_diff * 0.3 + case_bonus
            
            scored_candidates.append((score, candidate))
        
        scored_candidates.sort(key=lambda x: x[0])
        return scored_candidates[0][1]
    
    def correct_word(self, word: str) -> str:
        """Correct a single word."""
        self.stats['total_words'] += 1
        
        word = word.strip()
        
        if not word:
            return word
        
        if word in self.dictionary_set:
            self.stats['exact_match'] += 1
            return word
        
        word_lower = word.lower()
        if word_lower in self.dictionary_lower_set:
            self.stats['case_corrected'] += 1
            return self.dictionary_lower[word_lower]
        
        candidates = self.get_candidates(word)
        
        if not candidates:
            self.stats['no_match'] += 1
            return word
        
        corrected = self.select_best_candidate(word, candidates)
        
        edit_dist = self.levenshtein_distance(word_lower, corrected.lower())
        if edit_dist == 1:
            self.stats['edit_distance_1'] += 1
        elif edit_dist == 2:
            self.stats['edit_distance_2'] += 1
        else:
            self.stats['phonetic_match'] += 1
        
        return corrected
    
    def correct_file(self, input_file: str, output_file: str):
        """Correct all words in a file and write results."""
        start_time = time.time()
        
        print(f"Loading errors from {input_file}...")
        with open(input_file, 'r', encoding='utf-8') as f:
            errors = [line.strip() for line in f if line.strip()]
        
        print(f"Correcting {len(errors)} words...")
        results = []
        
        for i, error_word in enumerate(errors):
            if (i + 1) % 1000 == 0:
                print(f"Progress: {i + 1}/{len(errors)} words processed...")
            
            corrected_word = self.correct_word(error_word)
            results.append((error_word, corrected_word))
        
        print(f"Writing results to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{'Error':<30} {'Corrected':<30}\n")
            f.write("=" * 60 + "\n")
            
            for error, corrected in results:
                f.write(f"{error:<30} {corrected:<30}\n")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self.print_statistics(elapsed_time)
    
    def print_statistics(self, elapsed_time: float):
        """Print correction statistics."""
        print("\n" + "=" * 60)
        print("SPELL CORRECTION STATISTICS")
        print("=" * 60)
        print(f"Total words processed: {self.stats['total_words']}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Words per second: {self.stats['total_words'] / elapsed_time:.2f}")
        print("\nCorrection Breakdown:")
        print(f"  Exact matches: {self.stats['exact_match']} ({self.stats['exact_match'] / self.stats['total_words'] * 100:.1f}%)")
        print(f"  Case corrected: {self.stats['case_corrected']} ({self.stats['case_corrected'] / self.stats['total_words'] * 100:.1f}%)")
        print(f"  Edit distance 1: {self.stats['edit_distance_1']} ({self.stats['edit_distance_1'] / self.stats['total_words'] * 100:.1f}%)")
        print(f"  Edit distance 2: {self.stats['edit_distance_2']} ({self.stats['edit_distance_2'] / self.stats['total_words'] * 100:.1f}%)")
        print(f"  Phonetic match: {self.stats['phonetic_match']} ({self.stats['phonetic_match'] / self.stats['total_words'] * 100:.1f}%)")
        print(f"  No match found: {self.stats['no_match']} ({self.stats['no_match'] / self.stats['total_words'] * 100:.1f}%)")
        
        accuracy = (self.stats['total_words'] - self.stats['no_match']) / self.stats['total_words'] * 100
        print(f"\nAccuracy: {accuracy:.2f}%")
        print("=" * 60)


def main():
    """Main function to run spell correction."""
    import sys
    
    dictionary_file = 'reference.txt'
    errors_file = 'errors.txt'
    output_file = 'corrected_output.txt'
    
    import os
    if not os.path.exists(dictionary_file):
        print(f"Error: Dictionary file '{dictionary_file}' not found!")
        sys.exit(1)
    
    if not os.path.exists(errors_file):
        print(f"Error: Errors file '{errors_file}' not found!")
        sys.exit(1)
    
    corrector = SpellCorrector(dictionary_file)
    corrector.correct_file(errors_file, output_file)
    
    print(f"\nCorrection complete! Results saved to {output_file}")


if __name__ == '__main__':
    main()
