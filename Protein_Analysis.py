import random
"""
Calculating the molecular weight of a protein sequence
"""

AMINO_ACID_WEIGHTS = {
    'A': 89.094, 'R': 174.203, 'N': 132.119, 'D': 133.104,
    'C': 121.154, 'E': 147.131, 'Q': 146.146, 'G': 75.067,
    'H': 155.156, 'I': 131.175, 'L': 131.175, 'K': 146.189,
    'M': 149.208, 'F': 165.192, 'P': 115.132, 'S': 105.093,
    'T': 119.120, 'W': 204.228, 'Y': 181.191, 'V': 117.148
}

def generate_protein_seq(amino_amount=50):
    protein_sequence = random.choices(list(AMINO_ACID_WEIGHTS.keys()), k=amino_amount)
    protein_sequence = ''.join(protein_sequence)
    return protein_sequence



def calculate_molecular_weight(protein_sequence):
    """ Units of amino_acid_weights: g/mol """
    molecular_weight = 0
    for amino_acid in protein_sequence:
        molecular_weight += AMINO_ACID_WEIGHTS.get(amino_acid, 0)
    return molecular_weight

protein_seq = generate_protein_seq(150)
print(protein_seq, "\n")
print(f'{calculate_molecular_weight(protein_seq):.2f} g/mol')
