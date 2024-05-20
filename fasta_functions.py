#This function reads the fasta file and returns a dictionary with the sequences 
def read_fasta(fasta_file):
    sequences = {}
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                name = line.strip()[1:]
                sequences[name] = ''
            else:
                sequences[name] += line.strip()
    return sequences
#This function accepts the dictionary sequences and returns the NEXUS DATA header
def make_nexus_data_header(sequences):
    nexus_data_header = 'NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=' + str(len(sequences)) + ' NCHAR=' + str(len(sequences[list(sequences.keys())[0]])) + ';\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n'
    return nexus_data_header
#This function accepts the dictionary sequences and returns the NEXUS matrix
def make_nexus_matrix(sequences):
    nexus_matrix = ''
    for name, sequence in sequences.items():
        nexus_matrix += name + ' ' + sequence + '\n'
    return nexus_matrix
#NEXUS file is outputted to STDOUT
def make_nexus_file(sequences):
    nexus_file = make_nexus_data_header(sequences) + make_nexus_matrix(sequences) + 'END;\n'
    print(nexus_file)
    return nexus_file