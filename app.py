from bs4 import BeautifulSoup
import requests
import os

from common import get_pdf_link, pdf_dwl

# url = "https://www.alloschool.com/assets/documents/course-40/mbadi-fi-almntq-aldrs-1-2.pdf"
# filename = wget.download(url)


class app:
    pdf_class = "mdi-file-pdf"
    div_pdf_link = "pdf-tag-hide"
    endingPath = "scrapped"
    url = "https://www.alloschool.com/category/high-school"

    def __init__(self):
        if not os.path.exists('./'+self.endingPath):
            os.mkdir('./'+self.endingPath)
        self.teil_1()

    def _get_request(self, url):
        respond = requests.get(url, timeout=30)
        return respond

    def teil_1(self):
        _dom = self._get_request(self.url).text
        doc = BeautifulSoup(_dom, "html.parser")
        ul_fachs = doc.find('div', ["category"]).ul
        links_for_fach = []
        for lis in ul_fachs.find_all('li'):
            try:
                for zt in (lis.ul.find_all("li")):
                    link_href = zt.a.get("href")
                    link_link_href = str(link_href).split('/')
                    os.mkdir('./'+self.endingPath+'/' +
                             link_link_href[len(link_link_href)-1])
                    links_for_fach.append(link_href)
            except:
                error = 1
        # print(links_for_fach)
        for f in links_for_fach:
            used = f.split('/')
            _dom = self._get_request(f).text
            doc3 = BeautifulSoup(_dom, 'html.parser')
            div_div = doc3.find('div', ["category"]).ul

            for u in div_div.find_all('li'):
                doc4 = BeautifulSoup(self._get_request(
                    u.a.get('href')).text, "html.parser")
                if os.path.exists("./"+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5]):
                    for fi in range(0, 19):
                        if not os.path.exists("./"+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5]+str(fi)):
                            os.mkdir("./"+self.endingPath+'/'+str(used[len(used)-1])+"/"+str(
                                doc4.find('title').get_text())[0:5]+str(fi))
                            uo = str(doc4.find('title').get_text())[
                                0:5]+str(fi)
                            break
                else:
                    os.mkdir("./"+self.endingPath+'/' +
                             str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5])
                    uo = str(doc4.find('title').get_text())[0:5]
                print("./"+str(used[len(used)-1]))
                get_pdf_link(doc4, str(used[len(used)-1]), uo)
