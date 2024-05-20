import pytest
import fasta_functions



def test_make_nexus_data_header():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=22;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n'
    assert fasta_functions.make_nexus_data_header(known_inputs) == expected_outputs
        
def test_make_nexus_matrix():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='seq1 ATGCAACACAGACCAGCACAAC\nseq2 ATATATATATATATAATATATA\n'
    assert fasta_functions.make_nexus_matrix(known_inputs) == expected_outputs
        
def test_make_nexus_file():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=22;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\nseq1 ATGCAACACAGACCAGCACAAC\nseq2 ATATATATATATATAATATATA\nEND;\n'
    assert fasta_functions.make_nexus_file(known_inputs) == expected_outputs
        
        