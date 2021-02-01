import requests as req 
from bs4 import BeautifulSoup
import os 
import pathlib


url = "https://www.alloschool.com/category/primary"
# targetd variables 
class app1:
    def __init__(self,n):
        if n ==0:
            self.url = "https://www.alloschool.com/category/primary"
        elif n ==1:
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
        res = req.get(self.url)
        doc  = BeautifulSoup(res.text,'html.parser')
        selected_li_class = 'category-u'
        unlisted_lists = doc.find_all('li',selected_li_class)
        for i in unlisted_lists:
            print(i.a.get('title'),"######################")
            file_name= str(i.a.get('title'))
            os.mkdir('./'+self.endingPath+'/'+file_name)
            # getting to the pdf's pages
            nested_lists = i.ul.find_all('li')
            for r in nested_lists:
                # print(r.a.get('title'))
                pdf_link = r.a.get('href')
                for ir in range(0,10):
                    if not os.path.exists("./"+file_name+"/"+str(r.a.get('title'))[0:4]):    
                        file_file_name = str(r.a.get('title'))[0:4]
                        os.mkdir("./"+self.endingPath+'/'+file_name+"/"+file_file_name)
                        break
                    else:
                        file_file_name = str(r.a.get('title'))[0:4]+str(ir)
                        if not os.path.exists("./"+file_name+"/"+file_file_name):
                            os.mkdir("./"+self.endingPath+'/'+file_name+"/"+file_file_name)
                            break
                        else:
                            continue

                res3 = req.get(pdf_link)
                doc3 = BeautifulSoup(res3.text,'html.parser')
                self.get_pdf_link(doc3,file_name,file_file_name)

    # get pdf from the course page
    def get_pdf_link(self,doc,pdf_1,pdf_2):
        #pdf_n = f'\{pdf_1}\{pdf_2}' #uncomment for window
        pdf_n = '/'+pdf_1+'/'+pdf_2
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
                    print(pdf_link)  #uncomment for debugg
                    
                    self.pdf_dwl(pdf_n,str(doc2.find('title').get_text()),pdf_link) 
                    # add_to_file(pdf_link,'./'+str(pdf_1)+'/'+str(pdf_2))
                    # sys.exit() #debugg
                    # course_link.append(link.get('href'))

            except:
                # print('Not a pdf link') 
                error = 'Not a pdf link'

            
    # download the pdf 
    def pdf_dwl(self,filename,pdfname, link):
        link =link
        fol = str(pathlib.Path().absolute())+'/'+self.endingPath+'/'
        folder_location = fol+filename
        filename = os.path.join(folder_location,str(pdfname)+'.pdf')
        with open(filename, 'wb') as f:
            f.write(req.get(link).content)
        print(filename,'Done ############################')
