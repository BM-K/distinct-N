from __future__ import absolute_import 
from __future__ import division 
from __future__ import print_function

import argparse
import logging

from distinct_n import distinct_n_sentence_level
from pathlib import Path

NAME = 'distinct_n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hypothesis', help="predicted text file, one example per line")
    parser.add_argument('-n', dest='n_range', type=int, nargs='+', help="n to use as in distinct-N")
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    logging.info('loading hypothesis file...')
    with open(args.hypothesis) as f:
        hypothesis = [sentence.split() for sentence in f.readlines()]
    
    print(hypothesis)
    
    for n in args.n_range:
        name=NAME
        params={'n': n}
        scores=[distinct_n_sentence_level(s, n) for s in hypothesis]
        
        print(scores)
        print("----")
        
