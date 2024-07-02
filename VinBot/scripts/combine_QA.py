# combine_QA.py

import json
from transformers import AutoTokenizer
import os
import glob

def combine_QA(data_dir, save_dir):
    tokenizer = AutoTokenizer.from_pretrained("unsloth/gemma-7b-it-bnb-4bit")

    INSTRUCTION = "You are a customer support agent from schneider electric, please provide customer support regarding the vinplus software."

    os.makedirs(save_dir, exist_ok=True)

    INSTRUCTIONS_FILENAME = os.path.join(save_dir, "instructions.jsonl")
    QUERIES_FILENAME = os.path.join(save_dir, "queries.jsonl")
    ANSWERS_FILENAME = os.path.join(save_dir, "answers.jsonl")

    print(f"{'Total':<12}{'Instruction':<12}{'Query':<12}{'Answer':<12}")

    query_files = sorted(glob.glob(os.path.join(data_dir, "query-*.txt")))
    answer_files = sorted(glob.glob(os.path.join(data_dir, "answer-*.txt")))

    if len(query_files) != len(answer_files):
        raise ValueError("The number of query and answer files does not match")

    for query_file, answer_file in zip(query_files, answer_files):

        try:
            with open(query_file, 'r', encoding='latin-1') as file:
                query = "".join(file.readlines())
            with open(answer_file, 'r', encoding='latin-1') as file:
                answer = "".join(file.readlines())
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            continue

        if not query or not answer:
            print(f"Empty file(s) found: {query_file} or {answer_file}")
            continue

        instruction_tokens = tokenizer(INSTRUCTION, return_tensors="pt")["input_ids"].shape[1]
        query_tokens = tokenizer(query, return_tensors="pt")["input_ids"].shape[1]
        answer_tokens = tokenizer(answer, return_tensors="pt")["input_ids"].shape[1]

        total_tokens = instruction_tokens + query_tokens + answer_tokens
        print(f"{total_tokens:<12}{instruction_tokens:<12}{query_tokens:<12}{answer_tokens:<12}")

        try:
            with open(INSTRUCTIONS_FILENAME, 'a', encoding='utf-8') as file:
                file.write(json.dumps({"text": INSTRUCTION}) + "\n")
            with open(QUERIES_FILENAME, 'a', encoding='utf-8') as file:
                file.write(json.dumps({"text": query}) + "\n")
            with open(ANSWERS_FILENAME, 'a', encoding='utf-8') as file:
                file.write(json.dumps({"text": answer}) + "\n")
        except Exception as e:
            print(f"Error writing to JSONL files: {e}")

        # Delete the processed query and answer files
        try:
            os.remove(query_file)
            os.remove(answer_file)
        except Exception as e:
            print(f"Error deleting files: {e}")

if __name__ == "__main__":
    data_dir = 'C:/Users/RNRaku/Desktop/VinBot/data'
    save_dir = 'C:/Users/RNRaku/Desktop/VinBot/Jsonl'
    #data_dir = 'VinBot/data'
    #save_dir = 'VinBot/Jsonl'
    combine_QA(data_dir, save_dir)
