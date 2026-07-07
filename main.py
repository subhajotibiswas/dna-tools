from tools.validation import is_valid_dna
from tools.transcription import transcribe

def main():

    while True:
        dna = input("Enter a DNA sequence: ").strip().upper()
    
        if not is_valid_dna(dna):
            print("Invalid DNA sequence. Please enter a sequence containing only A, T, G, C.")
            continue

        rna = transcribe(dna)

        print(f"RNA sequence: {rna}")
        break

if __name__ == "__main__":
     main()