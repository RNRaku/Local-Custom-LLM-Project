import sys
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'scripts'))
#sys.path.append(script_dir)

from scripts.create_QA import create_QA
from scripts.combine_QA import combine_QA

input_file = os.path.join(script_dir, 'docs', 'QA.txt')
data_dir = os.path.join(script_dir, 'data')
save_dir = os.path.join(script_dir, 'Jsonl')

def main():
    create_QA(input_file, data_dir)
    combine_QA(data_dir, save_dir)

if __name__ == "__main__":
    main()
