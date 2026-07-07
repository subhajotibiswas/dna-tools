#validation

VALID_BASES = {"A", "T", "G", "C"}

def is_valid_dna(sequence: str) -> bool:
    for base in sequence:
        if base not in VALID_BASES:
            return False
    return True