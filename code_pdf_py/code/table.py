import camelot
import os

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]

def get_chunks(filepath, pages, chunk=10):
    """
    Divide the extraction work into n chunks and return this chunks.

    filepath : str
        Filepath or URL of the PDF file.
    pages : str, optional (default: '1')
        Comma-separated page numbers.
        Example: '1,3,4' or '1,4-end' or 'all'.
    """

    # get list of pages from camelot.handlers.PDFHandler
    handler = camelot.handlers.PDFHandler(filepath)
    page_list = handler._get_pages(pages=pages)
    # chunk pages list
    page_chunks = list(chunks(page_list, chunk))

    return page_chunks

def check_information_table(tables, position_record_table, metrics):
    for table in tables:
        table_df = table.df
        columns = table_df.shape[1]
        for key_word,value_words  in metrics.items():
            for col in range(columns):
                contains = any(table.df[col].str.contains("|".join(value_words), case=False, regex=True).tolist())
                if contains:
                    position_record_table[key_word].append(str(table.page))
                    break

def parseTable(input_path, file, metrics):
    print("parsing table from " + file)
    position_record_table = {key_word:[] for key_word in metrics.keys()}
    try:
        filepath = os.path.join(input_path, file)
        page_chunks = get_chunks(filepath, "all")
        for chunk in page_chunks:
            pages_string = str(chunk).replace("[", "").replace("]", "")
            tables = camelot.read_pdf(filepath, pages=pages_string)
            if len(tables) > 0:
                check_information_table(tables, position_record_table, metrics)
    except Exception as e:
        print("error parsing table from " + file)    
        print(e)  
    return position_record_table