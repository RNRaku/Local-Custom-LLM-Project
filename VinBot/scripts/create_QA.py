# create_QA.py

import re
import os

def create_QA(input_file, output_dir):
    def save_to_file(filename, text):
        with open(filename, 'w') as file:
            file.write(text)

    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regex patterns to match questions and answers
    question_pattern = re.compile(r'Q\d*:|[Qq][Uu][Ee][Ss][Tt][Ii][Oo][Nn]:')
    answer_pattern = re.compile(r'A\d*:|[Aa][Nn][Ss][Ww][Ee][Rr]:')

    sections = re.split(f'({question_pattern.pattern}|{answer_pattern.pattern})', data)

    question_counter = 1
    current_question = None
    current_answer = None

    for i in range(len(sections)):
        section = sections[i].strip()
        if question_pattern.match(section):
            if current_question and current_answer:
                save_to_file(os.path.join(output_dir, f'query-{question_counter}.txt'), current_question.strip())
                save_to_file(os.path.join(output_dir, f'answer-{question_counter}.txt'), current_answer.strip())
                question_counter += 1

            current_question = sections[i+1].strip()
            current_answer = None
        
        elif answer_pattern.match(section):
            current_answer = sections[i+1].strip()

    if current_question and current_answer:
        save_to_file(os.path.join(output_dir, f'query-{question_counter}.txt'), current_question.strip())
        save_to_file(os.path.join(output_dir, f'answer-{question_counter}.txt'), current_answer.strip())

if __name__ == "__main__":
    input_file = 'C:/Users/RNRaku/Desktop/VinBot/docs/QA.txt'
    output_dir = 'C:/Users/RNRaku/Desktop/VinBot/data'
    #input_file = 'VinBot/docs/QA.txt'
    #output_dir = 'VinBot/data'
    create_QA(input_file, output_dir)
