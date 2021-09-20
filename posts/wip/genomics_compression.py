import bisect
from itertools import product
from functools import reduce

from bitstring import BitStream, BitArray
from hmmlearn import hmm
import numpy as np

def naive_compression(genome):
    
    d = {
        "A":BitArray("0b00"),
        "G":BitArray("0b01"),
        "C":BitArray("0b10"),
        "T":BitArray("0b11")
    }
    
    bits = BitArray(2*len(genome))
    for pos, character in enumerate(genome):
        bits[2*pos:2*pos+2] = d[character]
    
    return bits

class Tree():
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({str(self.left)}, {str(self.right)})"

def message_tree(message_probs_dictionary):
    
    messages_as_list = list(message_probs_dictionary.items())
    messages_as_list.sort(key=lambda x: x[1])
    messages = [x[0] for x in messages_as_list]
    message_probs = [x[1] for x in messages_as_list]
    
    return message_tree_internal(messages, message_probs)


def message_tree_internal(messages, message_probs):
    
    while(len(messages) > 1):
        
        leaves = Tree(messages[0], messages[1])
        leaf_prob = message_probs[0] + message_probs[1]
        new_index = bisect.bisect_right(message_probs[2:], leaf_prob)
        messages = messages[2:]
        messages.insert(new_index, leaves)
        message_probs = message_probs[2:]
        message_probs.insert(new_index, leaf_prob)
        
    return messages[0]
    
# python is terrible at doing high-depth recursion but this function 
# should only go to a depth of log(n) and therefore should be ok.
def tree_to_encoding(message_tree):
    coding_dict = {}
    
    if isinstance(message_tree, Tree):
        for k, v in tree_to_encoding(message_tree.left).items():
            v.insert("0b0", 0)
            coding_dict[k] = v
        
        for k, v in tree_to_encoding(message_tree.right).items():
            v.insert("0b1", 0)
            coding_dict[k] = v
    
        return coding_dict
    
    else:
        return {message_tree: BitArray()}
    

def compute_huffman_code(message_probs):
    """
    The input is a dictionary of messages, and their relative probabilities (which must add to 1). 
    The output is a dictionary of each message and it's new codeword (a bytestring) in the Huffman encoding. 
    """
    
    return tree_to_encoding(message_tree(message_probs))


def expected_compression(message_probs, message_encoding):
    """
    It is implicit that the messages are strings from the alphabet {A, C, G, T} so each symbol occupies 2 bits. 
    """
    
    expected_original_size = 2 * sum([len(m[0]) * m[1] for m in message_probs.items()])
    
    expected_compressed_size = sum([len(message_encoding[k]) * message_probs[k] for k in message_encoding.keys()])
    
    return expected_compressed_size/expected_original_size


def get_kmer_frequency(genomes, k, ignore_zeros=True, get_raw_counts=False):
    
    alphabet = "ATGC"
    
    countk = {}
    if not ignore_zeros:
        countk = {reduce(lambda s, t: s+t, x) : 0 for x in product(alphabet, repeat=k)}
    

    for g in genomes:
        i = 0
        buffer = ""
        for x in g:
            i += 1
            buffer += x

            if i <= k:
                continue

            else:
                buffer = buffer[1:]
                if buffer in countk:
                    countk[buffer] +=1
                else:
                    countk[buffer] = 1

    if get_raw_counts:
        return countk
    
    l = sum(len(g) for g in genomes)
    
    for x in countk:
        countk[x]/= k*l
        
    return countk