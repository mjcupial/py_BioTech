import random

"""
Write a Python script to read a DNA sequence and count the occurrences of each nucleotide (A, T, C, G).
Create a function to transcribe DNA into RNA.
"""

_nucleotydes_pairs = tuple({"A": "T", "T": "A", "C": "G", "G": "C"}.items())
_DNA = [random.choice(_nucleotydes_pairs) for i in range(2137)]


def inject_point_mutation(nuc_pair):
    """ Changing the order or losing a single nucleotide results in the creation of a non-functional protein encoded
    by a damaged gene or a complete inhibition of its production.
    Examples: ('A','C') or ('T', None) """
    index_to_inject = random.choice(range(len(_DNA)))
    _DNA.insert(index_to_inject, nuc_pair)
    print(f"Mutation injected into {index_to_inject} possition...")


def check_if_mutation(nuc_a, nuc_c, nuc_g, nuc_t):
    """ Raise exception when the number of nucleotydes A != T and C != G """
    if nuc_a != nuc_t or nuc_c != nuc_g:
        raise Exception("number of occurences: 'A' != 'T' or 'C' != 'G'")
    diff = abs(nuc_a - nuc_c)
    print(f"\nA/T occurences: {nuc_a} | C/G occurences: {nuc_c}\tdiff: {diff}")


def count_nucleotyde(nuc):
    counter = 0
    for nucleotyde in _DNA:
        if nucleotyde[0] == nuc or nucleotyde[1] == nuc:
            counter += 1
    return counter


def read_template_strand(num=2):
    """" Read the sequence of nucleotydes from Template Strand """
    template_strand = [a[num - 1] for a in _DNA]
    return template_strand


def rna_transcription(template_strand):
    rna = {"T": "A", "C": "G", "G": "C", "A": "U"}
    mrna = [rna[i] for i in template_strand]
    return mrna


# inject_point_mutation(("A","C"))
# print(_DNA)
nuc_a = count_nucleotyde("A")
nuc_c = count_nucleotyde("C")
nuc_g = count_nucleotyde("G")
nuc_t = count_nucleotyde("T")
check_if_mutation(nuc_a, nuc_c, nuc_g, nuc_t)
template_strand = read_template_strand()
print(rna_transcription(template_strand))


