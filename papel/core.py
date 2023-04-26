# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['path', 'search', 'x', 'dl', 'results', 'pdf', 'papers_vector', 'train_test_partition', 'dataset']

# %% ../nbs/00_core.ipynb 2
import arxiv_dl.arxiv_dl
from pathlib import Path
path = Path("/home/nex/Downloads/ArXiv_Papers")
def dl(lista):
    for e in lista:
        try:
            arxiv_dl.arxiv_dl.main(e)
        except:
            print("error downloading: ", str(e))

# %% ../nbs/00_core.ipynb 4
import arxiv
search = arxiv.Search

# %% ../nbs/00_core.ipynb 6
def results(s):
    return list(map(lambda r: r.entry_id, search(s, max_results=100).results()))

# %% ../nbs/00_core.ipynb 16
from PyPDF2 import PdfReader
def pdf(path):
    text = ""
    reader = PdfReader(path)
    for page in reader.pages:
        text += page.extract_text()
    return text
#print(pdf(Path('/home/nex/Downloads/ArXiv_Papers/2002.04688_fastai_A_Layered_API_for_Deep_Learning.pdf')))

# %% ../nbs/00_core.ipynb 19
def papers_vector():
  return [pdf(entry) for entry in path.ls() if str(entry).endswith("pdf")]

# %% ../nbs/00_core.ipynb 21
from fastai.data.transforms import RandomSplitter

# %% ../nbs/00_core.ipynb 24
import numpy
# x is your dataset
x = papers_vector
def train_test_partition(X):
  l = len(X)
  l80porc = int(80 * l / 100)
  numpy.random.shuffle(X)
  training, test = X[:l80porc], X[l80porc:]
  return training, test

# %% ../nbs/00_core.ipynb 27
def dataset():
    return train_test_partition(papers_vector())
