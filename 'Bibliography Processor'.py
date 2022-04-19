'Bibliography Processor'

import numpy as np
import pandas as pd
import seaborn as sns

class bibliography_processor():
    '''Process research paper bibliographies. Input a .txt file containing the bibliography. Code assumes txt is well-formatted.
    Code will break if there is a mistake in the bibliography.
    txt_file: [txt_file] or [str] the input file containing the bibliography
    bibstyle: [str], current support for 'APA' and 'MLA'.
    Since performance for any given paper is most likely not a problem (<300 references), 
    the script will loop through in base Python code. OOM runtime should be <10s.'''
    def __init__(self, txt_file, bibstyle):
        if bibstyle=='APA':
            self.df = pd.DataFrame({'First Author':[], 'Other Authors':[], 'Year':[], 'Title':[], 'Journal':[], 'Edition':[]\
            'First Page': [], 'Last Page':[]})
        else: pass
        '''Loop through the text file here. I think I'll use a while loop which breaks down the bibliography first by
        periods. It will then take each . I need to learn some string processing functionality for this to work as intended.'''

    
    def show_years(self, vertical=True):
        '''Make a histogram outlinining which years the papers referenced in the bibliography were published.
            Vertical [bool]: if true, orientation will be vertical; otherwise, horizontal'''
        if vertical:
            sns.histplot(data=self.df, x='Year')
        else:
            # sns.histplot
            pass
    def make_barplots(self, by='First Author'):
        '''Make a histogram outlinining which years the papers referenced in the bibliography were published.
            by [str]: decides which attribute to base the barplot on.
            Vertical [bool]: if true, orientation will be vertical; otherwise, horizontal'''
        if by=='First Author':
            self.by_author = self.df['Author'].value_counts()
            return sns.barplot(x=self.by_author.index, y=self.by_journal)
        else:
            self.by_journal = self.df['Journal'].value_counts()
            return sns.barplot(x=self.by_journal.index, y=self.by_journal)