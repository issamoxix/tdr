import os
import pathlib
from bs4 import BeautifulSoup
import requests


def pdf_dwl(self, filename, pdfname, link):
    link = link
    fol = str(pathlib.Path().absolute())+'/'+self.endingPath+'/'
    folder_location = fol+filename
    filename = os.path.join(folder_location, str(pdfname)+'.pdf')
    with open(filename, 'wb') as f:
        f.write(requests.get(link).content)
    print(filename, 'Done ############################')


def get_pdf_link(self, doc, pdf_1, pdf_2):
    pdf_n = '/'+pdf_1+'/'+pdf_2
    course_link = []
    pdf_links = []
    for list_ in doc.find_all('li', "element"):
        link = list_.a
        try:
            if str(link.span.get('class')[1]) == self.pdf_class:
                res2 = requests.get(link.get('href'))
                doc2 = BeautifulSoup(res2.text, "html.parser")
                div_a = doc2.find('div', [self.div_pdf_link])
                pdf_link = div_a.a.get("href")

                pdf_dwl(pdf_n, str(
                    doc2.find('title').get_text()), pdf_link)

        except:
            error = 'Not a pdf link'
