import requests
from bs4 import BeautifulSoup
import os

from common import get_pdf_link, pdf_dwl


class app1:
    def __init__(self, n):
        if n == 0:
            self.url = "https://www.alloschool.com/category/primary"
        elif n == 1:
            self.url = "https://www.alloschool.com/category/middle-school"
        else:
            self.url = "https://www.alloschool.com/category/primary"

        self.div_pdf_link = "pdf-tag-hide"
        self.pdf_class = "mdi-file-pdf"
        self.endingPath = "scrapped"
        if not os.path.exists('./'+self.endingPath):
            os.mkdir('./'+self.endingPath)
        self.teil_1()

    def teil_1(self):
        res = requests.get(self.url)
        doc = BeautifulSoup(res.text, 'html.parser')
        selected_li_class = 'category-u'
        unlisted_lists = doc.find_all('li', selected_li_class)
        for i in unlisted_lists:
            print(i.a.get('title'), "######################")
            file_name = str(i.a.get('title'))
            os.mkdir('./'+self.endingPath+'/'+file_name)
            nested_lists = i.ul.find_all('li')
            for r in nested_lists:
                pdf_link = r.a.get('href')
                for ir in range(0, 10):
                    if not os.path.exists("./"+file_name+"/"+str(r.a.get('title'))[0:4]):
                        file_file_name = str(r.a.get('title'))[0:4]
                        os.mkdir("./"+self.endingPath+'/' +
                                 file_name+"/"+file_file_name)
                        break
                    else:
                        file_file_name = str(r.a.get('title'))[0:4]+str(ir)
                        if not os.path.exists("./"+file_name+"/"+file_file_name):
                            os.mkdir("./"+self.endingPath+'/' +
                                     file_name+"/"+file_file_name)
                            break
                        else:
                            continue

                res3 = requests.get(pdf_link)
                doc3 = BeautifulSoup(res3.text, 'html.parser')
                get_pdf_link(doc3, file_name, file_file_name)
