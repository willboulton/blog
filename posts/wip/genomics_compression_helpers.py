import matplotlib.pyplot as plt
import glob

DATA_FOLDER = "/home/will/Desktop/projects/genomics-1/data/sar-cov-2/txtfiles/"

COG_DATA = "/home/will/Desktop/projects/genomics-1/data/sar-cov-2/cog/"

def get_text_file(filename):
    
    with open(DATA_FOLDER + filename, "r") as fh:
        genome = ""
        for l in fh:
            genome += l[:-1]

    return genome[1:]


def get_fasta_file_generator(filename):

    with open(COG_DATA + filename, "r") as fh:
        
        genome = ""     
        name = fh.readline().strip()
        
        for line in fh:
            if line.startswith(">"):
                yield (name[1:], genome)
                name = line.strip()
                genome = ""
            else:
                genome += line.strip()
                
        yield (name[1:], genome.upper())
        
def cvt_numeric(x):
    
    d = {
        'A': 0,
        'T': 1, 
        'G': 2,
        'C': 3,
        'N': 10,
        'Y': 10,
        'K': 10,
        'M': 10, 
        'R': 10, 
        'S': 10, 
        'V': 10, 
        'W': 10,
        '?': 10
    }
    
    return d[x]

def plot_diffs(genome1, genome2, offset=0):
    print(genome1[100+offset:200+offset])
    print(genome2[100:200])
    n1 = [cvt_numeric(x) for x in genome1]
    n2 = [cvt_numeric(x) for x in genome2]
    length = int(min(len(n1) - offset, len(n2)))
    plt.plot([n1[i+offset] - n2[i] for i in range(length)])