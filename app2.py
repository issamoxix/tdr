import requests as req 
from bs4 import BeautifulSoup
import os 
import pathlib


url = "https://www.alloschool.com/category/middle-school"
res = req.get(url)
doc  = BeautifulSoup(res.text,'html.parser')
# targetd variables 
div_pdf_link = "pdf-tag-hide"
pdf_class = "mdi-file-pdf"

# download the pdf 
def pdf_dwl(filename,pdfname, link):
    link =link
    fol = str(pathlib.Path().absolute())
    folder_location = fol+filename
    filename = os.path.join(folder_location,str(pdfname)+'.pdf')
    with open(filename, 'wb') as f:
        f.write(req.get(link).content)
    print(filename,'Done ############################')



# get pdf from the course page
def get_pdf_link(doc,pdf_1,pdf_2):
    pdf_n = f'\{pdf_1}\{pdf_2}'
   
    course_link = []
    pdf_links = []
    for list_ in doc.find_all('li',"element"):
        link = list_.a
        try:
            if str(link.span.get('class')[1]) == pdf_class:
                res2 = req.get(link.get('href'))
                doc2 = BeautifulSoup(res2.text,"html.parser")
                div_a = doc2.find('div',[div_pdf_link])
                pdf_link = div_a.a.get("href")
                print(pdf_link)  #uncomment for debugg
                
                pdf_dwl(pdf_n,str(doc2.find('title').get_text()),pdf_link) #remove this to deploy
                # add_to_file(pdf_link,'./'+str(pdf_1)+'/'+str(pdf_2))
                # sys.exit() #debugg
                # course_link.append(link.get('href'))

        except:
            # print('Not a pdf link') 
            error = 'Not a pdf link'

selected_li_class = 'category-u'
unlisted_lists = doc.find_all('li',selected_li_class)
for i in unlisted_lists:
    print(i.a.get('title'),"######################")
    file_name= str(i.a.get('title'))
    os.mkdir(file_name)
    # getting to the pdf's pages
    nested_lists = i.ul.find_all('li')
    for r in nested_lists:
        # print(r.a.get('title'))
        pdf_link = r.a.get('href')
        file_file_name = str(r.a.get('title'))[0:4]
        os.mkdir("./"+file_name+"/"+file_file_name)
        res3 = req.get(pdf_link)
        doc3 = BeautifulSoup(res3.text,'html.parser')
        get_pdf_link(doc3,file_name,file_file_name)
        