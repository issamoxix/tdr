from bs4 import BeautifulSoup
import requests as req 
import pathlib
import os
# url = "https://www.alloschool.com/assets/documents/course-40/mbadi-fi-almntq-aldrs-1-2.pdf"
# filename = wget.download(url)

class app:
    def __init__(self):
        self.url = "https://www.alloschool.com/category/high-school"
        self.pdf_class = "mdi-file-pdf"
        self.div_pdf_link = "pdf-tag-hide"
        self.endingPath = "scrapped"
        if not os.path.exists('./'+self.endingPath):
            os.mkdir('./'+self.endingPath)
        self.teil_1()
    def teil_1(self):
        res = req.get(self.url)
        doc = BeautifulSoup(res.text,"html.parser")
        ul_fachs = doc.find('div',["category"]).ul
        links_for_fach = []
        for lis in ul_fachs.find_all('li'):
            try:
                for zt in (lis.ul.find_all("li")):
                    link_href = zt.a.get("href")
                    link_link_href = str(link_href).split('/')
                    os.mkdir('./'+self.endingPath+'/'+link_link_href[len(link_link_href)-1])
                    # print(link_link_href[len(link_link_href)-1]) # fach name
                    links_for_fach.append(link_href)
            except:
                error = 1
        # print(links_for_fach)
        for f in links_for_fach:
            used = f.split('/')
            res3 = req.get(f)
            doc3 = BeautifulSoup(res3.text,'html.parser')
            div_div = doc3.find('div', ["category"]).ul

            # print(used[len(used)-1]) #uncomment for debugg
            for u in div_div.find_all('li'):
                res4 = req.get(u.a.get('href'))
                doc4 = BeautifulSoup(res4.text,"html.parser")
                # print(doc4.find('title').get_text())
                if os.path.exists("./"+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5]):
                    for fi in range(0,19):
                        if not os.path.exists("./"+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5]+str(fi)):
                            os.mkdir("./"+self.endingPath+'/'+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5]+str(fi))
                            uo = str(doc4.find('title').get_text())[0:5]+str(fi)
                            break
                else:
                    os.mkdir("./"+self.endingPath+'/'+str(used[len(used)-1])+"/"+str(doc4.find('title').get_text())[0:5])
                    uo = str(doc4.find('title').get_text())[0:5]
                    # get_pdf_link(doc4,r'\'+str(used[len(used)-1])+r'\'+str(doc4.find('title').get_text())[0:5])
                print("./"+str(used[len(used)-1]))
                # print(f'\{str(used[len(used)-1])}\{str(doc4.find('title').get_text())[0:5])}')
                self.get_pdf_link(doc4,str(used[len(used)-1]),uo)
        # get pdf page and links

    def get_pdf_link(self,doc,pdf_1,pdf_2):
        pdf_n = f'\{pdf_1}\{pdf_2}'
    
        course_link = []
        pdf_links = []
        for list_ in doc.find_all('li',"element"):
            link = list_.a
            try:
                if str(link.span.get('class')[1]) == self.pdf_class:
                    res2 = req.get(link.get('href'))
                    doc2 = BeautifulSoup(res2.text,"html.parser")
                    div_a = doc2.find('div',[self.div_pdf_link])
                    pdf_link = div_a.a.get("href")
                    # print(pdf_link)  #uncomment for debugg
                    
                    self.pdf_dwl(pdf_n,str(doc2.find('title').get_text()),pdf_link) #remove this to deploy
                    # add_to_file(pdf_link,'./'+str(pdf_1)+'/'+str(pdf_2))
                    # sys.exit() #debugg
                    # course_link.append(link.get('href'))

            except:
                # print('Not a pdf link') 
                error = 'Not a pdf link'

    def pdf_dwl(self,filename,pdfname, link):
        link =link
        fol = str(pathlib.Path().absolute())+"/"+self.endingPath+"/"
        folder_location = fol+filename
        filename = os.path.join(folder_location,str(pdfname)+'.pdf')
        with open(filename, 'wb') as f:
            f.write(req.get(link).content)
        print(filename)
        print('Done ######################################')
# for link in doc.find_all('a'):

# def add_to_file(val,path):
#     file = open(path+'/file.txt','a')
#     file.write(val+'\n')
#     file.close()
#     print('Added Successfully !')



#     # print(link.get('href'))
#     if str(link.get('href')).endswith('pdf'):
#         print(link.get('href'))
# x = doc.find('li', "element").a
