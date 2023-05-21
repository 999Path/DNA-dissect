# defining the class
class RNA():
    def __init__(self,Name,DNA):
        self.DNA = DNA
        self.RNA = []
        self.CDNA = []
        self.New_RNA = ''
        self.New_CDNA =''
        self.A_content = 0 
        self.C_content = 0 
        self.G_content = 0 
        self.U_content = 0
        self.gc_con = 0

        if Name == '': 
            self.Name = 'Unknown'
        else: 
            self.Name = Name
        
        if DNA == '': 
            print("Error: Input a DNA seqeuence")
# This function transcribe the DNA to RNA 
    def transcribe_seq(self):
        length = len(str(self.DNA))
        self.RNA = list(self.DNA)
        for i in range(len(self.RNA)): 
            x = i 
            if self.RNA[x] == 'T':
                self.RNA[x] = "U"
            else: 
                self.RNA[x] = self.RNA[x]
        self.New_RNA = ''.join(self.RNA)

    
    # This function counts the A,U,C,G content  
    def count_seq(self):

            for i in range(len(self.RNA)): 
                x = i 
                if self.RNA[x] == "A":
                    self.A_content += 1 
                if self.RNA[x] == "U":  
                    self.U_content += 1
                if self.RNA[x] == "C":
                    self.C_content += 1
                if self.RNA[x] == "G":    
                    self.G_content += 1 
                    
    # This function gives the gc_content
    def gc_content(self):
        m = int(len(self.RNA))
        k = 0
        for i in range(len(self.RNA)): 
            x = i 
            if self.RNA[x] == "C":
                k += 1
            if self.RNA[x] == "G":    
                k += 1 
            else: 
                self.gc_con = k/m * 100
    
    # This function gives out the complementing DNA strand
    def complementing_DNA(self):
        length = len(str(self.DNA))
        self.CDNA = list(self.DNA)
        for i in range(len(self.DNA)): 
            x = i 
            if self.DNA[x] == 'T':
                self.CDNA[x] = "A"
            if self.DNA[x] == 'A':
                self.CDNA[x] = "T"
            if self.DNA[x] == 'G':
                self.CDNA[x] = "C"
            if self.DNA[x] == 'C':
                self.CDNA[x] = "G"
                
        self.New_CDNA = ''.join(self.CDNA)
    # This function generate the results file
    def save(self):
        output_file = f'{self.Name}.txt'
        with open(output_file, 'w') as file:
            file.write(f'>{self.Name}')
            file.write('\n')
            file.write(self.DNA)
            file.write('\n')
            file.write('\n')
            file.write(f'>{self.Name} Complementary strand')
            file.write('\n')
            file.write(self.New_CDNA)
            file.write('\n')
            file.write('\n')
            file.write(f'>{self.Name} RNA strand:')
            file.write('\n')
            file.write(self.New_RNA)
            file.write('\n')
            file.write('\n')
            file.write('Sequence Count:')
            file.write('\n')
            file.write(f'A content;{self.A_content},U content;{self.U_content},G content;{self.G_content},C content;{self.C_content}')
            file.write('\n')
            file.write('\n')
            file.write(f'GC content:')
            file.write('\n')
            file.write(f'{self.gc_con}')
            file.write('\n')   



def main():
    testing = RNA("Testing","ATGCATGCGCTAGGCGTACCGGCGGCGCGCCAGGTGCGGACCGCGCGCCTCTGGCGGGCTGCCTGTCACCGGGGCGTCCGCTGCGCGCTAGTCCCTTCTGCTTGGCGTGCCAGGCTCCGCTGCCGGCCGAGGCCAGCCCTGGCCGAGGCCAGCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCTGCTGGCCAGCTGCTGGCCGAGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGGTGAGCCCGGGCCGCGGCTCTGCCGGCCAGCCTGCGGG")
    testing.transcribe_seq()
    testing.count_seq()
    testing.gc_content()
    testing.complementing_DNA()
    testing.save()
    testing2 = RNA("","GCAGGTTCTCTTACATCGACCGCCTAAGAGTCGCGCTGTAAGAAGCAACAACCTCTCCTCTTCGTCTCCGCCATCAGCTCGGCAGTCGCGAAGCAGCAACCATGGTGAGAATCGGCTTCGGCTCTTTGTGGCCGTTGGGTGGAGTCAGCGCCCCCAGGCTCTACTTGGAAAACCTTTAAGCTCTTTTCTTTCGTAAGCTCTCTGGGCGAGGGTGGTGGTATGTTTTGTGAGGTTTAGCTTAGCCCCAAATCCTCAAGCCCCGCCGCCGCCGCAGTGCGGGTGCAGGAACCGGGCCAGTACTGCGCCCAGGGCGCAGCAGAGCGCTGGGGAGGAACAAAGGCGGCGCCTAGGCGCCTGTGTTATCCGAGAGACTTTCGGGGGCCGCGGGCAGCCCGTCTGCCGCGACCGAGGGGTCTGGGGCGTCCCGGCTGGGCCCCGTGTCTGTGCGCACGGTTTCGCTGATGCTGAGGGGCCACTTTCTGTCTCGCGTTGTTCTCTGGGGACCGGGAGAGGAGGAGGCACCCAAAAAGAGCGGGGGCGTTGGGCGAGCTGGGGGACGTGGGAGGGGGAACGGGAACAAAGCGCAGCCTAGGGTTAGCGTGGGAAGACCCTCCGCGGTCTTTGGCGTTTTGGAAAGATACCCACACATTCCCGGGAAAACATGGTGAGTTTCTGCCGGAGCCCCCGGCAGCGGGTGTCAGGGCGGCGCAGGGGCGGGGTTGTTTGTTTCTGGCTTCTATGGCGTTGGAGCCACTGGGCGGGGTTCGCCCTCACTGAACCTCTTCTGTCAGGAGCTGACTGAAAAAAAAACAAAAAAACCTTTCATCATTGCGGAACTGTAGGCTCCAAAAGGGTTTTCTTCACTATTATAAGTTAGATGACTTTTTTTTTTCTTGAGCAAAATCATAATTCACTTCACAAGCTCTTTAATGTCTGGTCTGGGGACGCCCTGCCCTGACCGACTGAAGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTCTGTGGGACGCCCTGCCCTGACCGACTGAAGTGTGTGTGTGTGTGTGTGTGTGTCTGTCTGTCTGTCTGGACTGCACGTTCAGCGAGGGAGAAAGCCCACTTTGTGAGCCCCAGGGTACCCTGATGGTCAGGACCCAGGGAAACGCCCTTCCCCGCCGCCCCCCCGCCCCGCCCCCACCACATCAGC")
    testing2.transcribe_seq()
    testing2.count_seq()
    testing2.gc_content()
    testing2.complementing_DNA()
    testing2.save()
    testing3 = RNA("Error",'')


if __name__ == "__main__":
    main()







