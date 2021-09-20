import numpy as np


# These are some short snippets that appear in the reference genome and there is a high chance that one of them
# will appear in some other genome. They can be used for alignment. 
HASHES = {
    "CGAACTTTAAAATCTGT": 70, 
    "GTTTCGTCCGGGTGT": 236, 
    "ATGGAGAGCCTTGTCCCTGG": 265, 
    "CAACTTGAACAGCCCTATGTGTT": 451, 
    "GCCTATTGGGTTCCACGTGCTAG": 1525
}


def sub_matrix(x1, x2):
    return int(x1 != x2)

def sub_matrix_2(x1, x2):
    if x1 == x2:
        return 0
    
    y = x1+x2
    
    if y =="AT" or y == "TA" or y == "GC" or y == "CG":
        return 1
    
    return 2


def edit_transcript(s1, s2, D, del_cost, ins_cost, sub_cost):
    
    # complexity of O(m+n)
    i = len(s1)
    j = len(s2)
    ed_trans = ""
    
    while (i > 0 or j > 0):
        if D[i,j] == D[i-1,j-1] + sub_cost(s1[i-1], s2[j-1]):
            i -= 1
            j -= 1 
            if s1[i] == s2[j]:
                ed_trans = "M" + ed_trans
            else:
                ed_trans = "R" + ed_trans
        
        elif D[i,j] == D[i-1,j] + del_cost:
            i -= 1
            ed_trans = "D" + ed_trans


        elif D[i,j] == D[i,j-1] + ins_cost:
            j -= 1
            ed_trans = "I" + ed_trans
            
        #print(ed_trans, i, j)
        
    return ed_trans

def d_matrix(s1, s2, del_cost, ins_cost, sub_cost, obj_fn):

    m = len(s1)
    n = len(s2)
    D = np.zeros([m+1, n+1], dtype=int)
    D[0,:] = ins_cost*np.arange(0, n+1, dtype=int)
    D[:,0] = del_cost*np.arange(0, m+1, dtype=int)

    # complexity of O(m*n)
    for i in range(m):
        for j in range(n):
            D[i+1,j+1] = obj_fn([
                D[i, j+1] + ins_cost, 
                D[i+1, j] + del_cost,
                D[i, j] + sub_cost(s1[i], s2[j])
            ])
    
    return (m, n, D)


def align_general(s1, s2, del_cost=1, ins_cost=1, sub_cost=sub_matrix, obj_fn = np.min):

    m, n, D = d_matrix(s1, s2, del_cost, ins_cost, sub_cost, obj_fn)
    
    ed_trans = edit_transcript(s1, s2, D, del_cost, ins_cost, sub_cost)
    
    return (D[-1,-1], ed_trans)


def d_matrix_faster(s1, s2, del_cost, ins_cost, sub_cost, obj_fn, window):

    m = len(s1)
    n = len(s2)
    D = del_cost*(m + n)*np.ones([m+1, n+1], dtype=int)
    D[0,:] = ins_cost*np.arange(0, n+1, dtype=int)
    D[:,0] = del_cost*np.arange(0, m+1, dtype=int)
    
    # complexity of O(m*n)
    for i in range(m):
        for j in range(max(i-window, 0), min(i+window, n)):
            D[i+1,j+1] = obj_fn([
                D[i, j+1] + ins_cost, 
                D[i+1, j] + del_cost,
                D[i, j] + int(s1[i] != s2[j])
            ])
    
    return (m, n, D)

def align_faster(s1, s2, del_cost=1, ins_cost=1, sub_cost=sub_matrix, obj_fn = np.min, window=100):
    
    m, n, D = d_matrix_faster(s1, s2, del_cost, ins_cost, sub_cost, obj_fn, window)
    
    ed_trans = edit_transcript(s1, s2, D, del_cost, ins_cost, sub_matrix)
    
    return (D[-1,-1], ed_trans)


def align_by_exact_matching(s1, reference):
    
    for h in HASHES:
        index = s1.find(h)
        if index > 0:
            return (index - HASHES[h], get_qs(s1, reference, offset=index - HASHES[h]))
    
    return (-1, -1)
        
def get_qs(s1, s2, offset=0):
    length = int(min(len(s1) - offset, len(s2)))
    return sum(int(s1[i-offset] != s2[i]) for i in range(length))   


def hash_align(genome, reference, branching_factor, kmer_length):
    print("call to hash align")
    B = branching_factor
    K = kmer_length
    n = len(genome)
    m = len(reference)
    

    
    gap = int(m/B)
    
    print(B, K, n, m, gap, min(n,m))
    
    if min(n,m) < 100:
        print("resolve manually")
        return align_faster(genome, reference)    
    
    prev = 0
    old_offset = 0
    first = True
    
    for i in range(1, B+1):
        hashstring = reference[gap*i - K:gap*i]
        new_offset = genome.find(hashstring) - gap*i + K
        
        print(hashstring, new_offset)
        
        if new_offset > -100 and new_offset != old_offset and (not first):
            print("recursing: ", prev, i, new_offset, old_offset)
            hash_align(genome[gap*prev:gap*i], reference[gap*prev:gap*i], branching_factor, kmer_length)
        
        elif new_offset < -100:
            print("too small")
            continue
        
        else:
            print("updating")
            prev = i
        
        first = False