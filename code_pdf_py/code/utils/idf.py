import os
import math
import PyPDF2
import pandas as pd
from .normalize import normalize

def cal_idf(input_path_idf, metrics):
    # input_path_idf = "./pdf_files_idf/pdf_files/"
    pdf_files = os.listdir(input_path_idf)
    pages = 0
    keywords = [" ".join(value) for key, value in metrics.items()]
    keywords = " ".join(keywords)
    keywords = set(normalize(keywords))
    keywords_dict = {key:0 for key in keywords}
    for file in pdf_files:
        try:
            object = PyPDF2.PdfFileReader(os.path.join(input_path_idf, file))
            num_pages = object.getNumPages()
            pages += num_pages
            for i in range(0, num_pages):
                page = object.getPage(i)
                text = page.extractText()
                text = text.replace('\n',' ')
                text = text.replace(str(i+1), "", 1)
                text = set(normalize(text))
                for word in keywords_dict.keys():
                    if word in text:
                        keywords_dict[word] += 1
        except:
            print(file + "is invalid!")
    keywords_idf = {key: (math.log(pages / (1 + value))) for key, value in keywords_dict.items()}
    return keywords_idf
    
