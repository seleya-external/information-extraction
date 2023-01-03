import os
import json
import pandas as pd
from text import parseText
from table import *

def get_metrics(metrics_path):
    with open(metrics_path, "r") as f_obj:
        metrics = json.load(f_obj)
    metrics = {key:list(value.split(",")) for key, value in metrics.items()}
    return metrics

def get_keywords_idf(idf_path):
    with open(idf_path, "r") as f_obj:
        idf = json.load(f_obj)
    idf = {key:float(value) for key, value in idf.items()}
    return idf

def save_result(position_record_text, position_record_table, metrics, file_name, output_path):
    name = ["output_metric", "text_page", "table_page"]
    position_record = [[keyword, " ".join(position_record_text[keyword]), 
                        " ".join(position_record_table[keyword])] for keyword in metrics.keys()]
    data = pd.DataFrame(columns=name, data=position_record)
    data.to_csv(output_path + file_name.replace(".pdf", "_prediction.csv"))    

if __name__ == "__main__":

    input_pdf_path = "./code_pdf_py/input/pdf_files"
    pdf_files = os.listdir(input_pdf_path)

    metrics_path = "./code_pdf_py/input/metrics.json"
    metrics = get_metrics(metrics_path)

    idf_path = "./code_pdf_py/input/idf.json"
    keywords_idf = get_keywords_idf(idf_path)

    output_path = "./code_pdf_py/output/"
    
    for file in pdf_files:
        # step1 parsing the table
        position_record_table = parseTable(input_pdf_path, file, metrics)
        
        # step2 parsing the text
        position_record_text_meta = parseText(input_pdf_path, file, metrics, keywords_idf)
        # choose the top 3 pages based on the term frequency
        position_record_text = {}
        for keys in position_record_text_meta.keys():
            position_record_text[keys] = [x[0] for x in sorted(position_record_text_meta[keys], 
                                          key= lambda x: x[1], reverse=True)][:3]
        
        # step3 save the result
        save_result(position_record_text, position_record_table, metrics, file, output_path)