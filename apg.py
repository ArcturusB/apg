#!/usr/bin/env python3

# title: A Passphrase Generator (APG)
# author: Gabriel "ArcturusB" Pelouze
# changed: 2016-08-05 22:21:51 (CEST)
# copyright: 2016 Gabriel Pelouze
# licence: GNU GPL version 3 (see http://www.gnu.org/licenses)
# disclaimer: >
    # This program is distributed in the hope that it will be useful, but without
    # any warranty; without even the implied warranty of merchantability or
    # fitness for a particular purpose. See the GNU General Public License for
    # more details.

''' A Passphrase Generate (APG)

To get started, see the PassphraseGenerator class:

>>> p = apg.PassphraseGenerator('apg_wordlist.txt', words=5)
>>> p()
'phthor,frapper&asina*casher.iniquo'
>>> p.entropy()
101.87799785438538

'''

import os
import math
import random

class WordSet(set):
    ''' Set of word, with enhanced init function to allow loading words
    from a text file.
    '''

    def __init__(self, wordset):
        ''' Initialize WordSet

        Parameters
        ==========
        wordsets: list or set of words, or string
            - list or set: use it directly to initialise the WordSet.
            - str: use it as a filename: load each line of the file as a word.

        Notes
        =====
        Currently, only utf8-encoded files are supported.
        '''

        if isinstance(wordset, str):
            with open(wordset) as f:
                data = [l.strip('\n') for l in f.readlines()]
        elif type(wordset) in [list, set]:
            data = wordset
        else:
            raise ValueError('WordSet received wrong parameter type.')

        super(WordSet, self).__init__(data)


class PassphraseGenerator():
    ''' A passphrase generator.

    Add here description of passphrase format. Advertise easily-remembered
    passphrases vs entropy (128 bit of entropy is achieved with 6 words, while
    it would require 22 random case-sensitive alphanumeric characters.)

    Attributes
    ==========
    wordset : set
        Set of words used to generate passphrases.
    delimset : str
        Set of caracters used as word delimiters when generating passphrases.
    words : int
        Default number of words.

    TODO
    ====
    - command-line interface
    '''

    wordset = {}
    delimset = ''
    words = 0

    def __init__(self, wordset, delimset='+-*/=^><:;,.|_%!&# ', words=5):
        ''' Initialize the passphrase generator.

        Parameters
        ==========
        word_sets : str, list, or set
            A value (list, set, or filaneme) used to initialise a WordSet
            object.
        delimset : str (default: '+-*/=^><:;,.|_%!&# ')
            The set of delimiters.
        words : int (default: 5)
            The default number of words in a passphrase.
        '''
        self.random = random.SystemRandom()
        self.wordset = WordSet(wordset)
        self.delimset = delimset
        self.words = words

    def __call__(self, words='default'):
        ''' Generate a new passphrase.

        words : int or 'default'
            Number of words in the passphrase. If 'default', use self.words.
        '''
        if words == 'default':
            words = self.words
        w = self.random.sample(self.wordset, words)
        d = self.random.sample(self.delimset, words - 1)
        pw = '{}'.join(w)
        pw = pw.format(*d)
        return pw

    def entropy(self, words='default'):
        ''' Estimate the entropy of a passphrase of a given number of words.

        Let:
            - w the number of words in the passphrase (hence the passphrase
              contains w - 1 delimiters),
            - Nw the number of possible words,
            - Nd the number of possible delimiters.
        Hence, the number of possible passphrases is:
            Np = Nw**w * Nd**(w-1),
        and the passphrase entropy:
            S = log2(Np) = log2(Nw**w * Nd**(w-1)).

        Parameters
        ==========
        words : int or 'default'
            Number of words in the passphrase. If 'default', use self.words.
        '''
        if words == 'default':
            words = self.words
        Nw = len(self.wordset)
        Nd = len(self.delimset)
        S = math.log2(Nw**words * Nd**(words-1))
        return S


if __name__ == '__main__':

    p = PassphraseGenerator('apg_wordlist.txt', words=5)
    print('passphrase:', p())
    print('entropy:', p.entropy())
