import re
from pyopenjtalk import g2p
import tkinter.filedialog as fd

class kanji2phone():
    
    def __init__():
        super().__init()
    
    def read_file(file):
    
        #Open file, split lines by \n and return list
        #ファイルを開く、ラインは「\n」でスプリットしてリストをリターンする
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
        
        return lines
    
    def split_delimiter(lines):
        
        kanji = ''
        files = []
        phones = []
        
        #Split each line at '|' and return two lists, files + phones
        #各ラインは「|」でスプリットして2つリストをリターンする、files + phones
        for i in range(len(lines)):
            
            splitted = lines[i].split('|')[-1]
            
            phones.append(g2p(splitted))
            
            files.append(lines[i].split('|')[0])
        
        return phones, files
    
    def convert_phones(phones):
        
        conv_phones = []
        
        #We're converting phonemes, in this case just turning 'pau' into '.' for sake of the ASR models.
        #音素の転換、ASRモデルの簡単のために、「pau」は「.」になる。
        for i in range(len(phones)):
            
            conv_phones.append(re.sub('pau', '.', phones[i]))
        
        return conv_phones

    def convert_phones_talqu(phones):

        conv_phones = []
        #We're converting phonemes in the format for TalQu, a voice synthesizer by Haruqa.
        #音素の転換、HaruqaのTalQuのためにフォーマットしている。

        for i in range(len(phones)):

            line = phones[i]

            new_line = re.sub('pau', '.', line
                             ).sub('sh', 'sy', line
                             ).sub('ch', 'cy', line
                             ).sub('j', 'jy', line
                             ).sub('cl', 'Q', line
                             ).sub('k i', 'kyi', line
                             ).sub('g i', 'gyi', line
                             ).sub('t i', 'tyi', line
                             ).sub('d i', 'dyi', line
                             ).sub('n i', 'nyi', line
                             ).sub('h i', 'hyi', line
                             ).sub('b i', 'byi', line
                             ).sub('p i', 'pyi', line
                             ).sub('m i', 'myi', line
                             ).sub('r i', 'ryi', line
                             ).sub('I', '', line
                             ).sub('U', '', line
                             ).sub(' ', '', line)

            conv_phones.append(new_line)

            return conv_phones
    
    def rebuild_files(files, conv_phones):
        
        new_text = ''
        
        #Match up files and converted phonemes into one big string
        #ファイルを合わせて、転換した音素は一つのストリングになる。
        if len(files) == len(conv_phones):
            for i in range(len(files)):
                new_text += files[i] + '|' + conv_phones[i] + '\n'
        else:
            print('[DEBUG] Somehow, files and phonemes do not match up')
    
        return new_text
    
    def export_file(new_text):
        
        files = [('Text Document', '*.txt'),
                 ('TSV Document', '*.tsv'),
                 ('All Files', '*.*')]
        
        file = fd.asksaveasfile(filetypes=files, defaultextension=files)
        
        #Save file to chosen directory.
        #選んだディレクトリにファイルを保存する。
        with open(file.name, 'w', encoding='utf-8') as f:
            f.write(new_text)
    
def main():
    
    file = kanji2phone.read_file(fd.askopenfilename())
    phones, files = kanji2phone.split_delimiter(file)
    if sys.argv.lower() == yes or y:
        conv_phones = kanji2phone.convert_phones_talqu(phones)
    else:
        conv_phones = kanji2phone.convert_phones(phones)
    new_text = kanji2phone.rebuild_files(files, conv_phones)
    kanji2phone.export_file(new_text)

if __name__ == '__main__':
    main()