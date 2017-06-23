import bioinfo_dicts as bd
def one_to_three(seq):
    """
    Converts a prot seq
    """

    #COnvert the seq
    seq = seq.upper()

    #Do the conversion
    aa_list = []
    for amino_acid in seq:
        if amino_acid not in bd.aa.keys():
            raise RuntimeError(amino_acid + ' is not valid.')
        aa_list += [bd.aa[amino_acid], '-']
    return ''.join(aa_list[:-1])
