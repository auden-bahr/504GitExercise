def get_nuc_freq(seq):
    nuc_dict = dict()
    for nuc in seq:
        if nuc not in nuc_dict:
            nuc_dict[nuc] = 1
        else:
            nuc_dict[nuc] += 1
    return nuc

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(get_nuc_freq('ATCTGACGCGCGCCGC'))
