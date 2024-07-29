import json
import argparse

def is_discontinuous(ent):
    if len(ent) == 5:
        return True
    return False

def generate_relation(ent_list, relations):
    result = []
    for rel in relations:
        head_ent = ent_list[rel[0]]
        tail_ent = ent_list[rel[1]]
        # remove triplets related to discontinuous entitis 
        if is_discontinuous(head_ent) or is_discontinuous(tail_ent):
            continue
        result.append([head_ent[0], head_ent[1], tail_ent[0], tail_ent[1], rel[2]])
    return result

def generate_entity(ent_list):
    result = []
    for ent in ent_list:
        # remove discontinuous entity
        if is_discontinuous(ent):
            continue
        result.append(ent)
    return result

def to_pure_format(data):
    result = []
    for idx, item in enumerate(data):
        pure_item = {}
        pure_item["doc_key"] = idx
        pure_item["sentences"] = [item["tokens"]]
        pure_item["ner"] = [generate_entity(item["ner"])]
        pure_item["relations"] = [generate_relation(item["ner"], item["relations"])]
        result.append(pure_item)
    return result

def read_file(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def write_file(data, file_path):
    with open(file_path, "w+") as f:
        for item in data:
            print(json.dumps(item), file=f)

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--input_file", type=str, default="./data/train.jsonl")
    args_parser.add_argument("--output_file", type=str, default="./data/pure_train.jsonl")
    args = args_parser.parse_args()
    data = read_file(args.input_file)
    pure_data = to_pure_format(data)
    write_file(pure_data, args.output_file)