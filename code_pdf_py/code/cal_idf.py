import json
from utils import *

def parse_metrics(metrics_path):
    with open(metrics_path, "r") as f_obj:
        metrics = json.load(f_obj)
    metrics = {key:list(value.split(",")) for key, value in metrics.items()}
    return metrics

def save_idf(keywords_idf, idf_path):
    with open(idf_path, "w") as f_obj:
        json.dump(keywords_idf, f_obj)

if __name__ == "__main__":
    input_path_idf = "./code_pdf_py/input/pdf_files_idf/"
    metrics_path = "./code_pdf_py/input/metrics.json"
    output_path_idf = "./code_pdf_py/input/idf.json"
    metrics = parse_metrics(metrics_path)
    keywords_idf = cal_idf(input_path_idf, metrics)
    
    keywords = []
    for values in metrics.values():
        keywords += values
    keywords = " ".join(keywords)
    keywords = list(set(normalize(keywords)))
    print("idf of each term is:")
    print(sorted([(key,value) for key, value in keywords_idf.items() if key in keywords], key = lambda x: x[1], reverse=True))

    save_idf(keywords_idf, output_path_idf)