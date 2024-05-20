import sys
import fasta_functions

# main function to read the fasta file and output the NEXUS file to STDOUT
if len(sys.argv) < 2:
    print("Usage: python Converter.py <fasta_file>")
    sys.exit(1)
fasta_file = sys.argv[1]
fasta_functions.make_nexus_file(fasta_functions.read_fasta(fasta_file))


    

