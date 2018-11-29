# # pip install fpdf
# from fpdf import FPDF
# import os
# # imagelist is the list with all image filenames
# pdf = FPDF()
# dirpath = 'E:/image'

# imagelist = []
# for filename in os.listdir(dirpath):
#     imagelist.append(filename)

# for image in imagelist:
#     print(image)
#     pdf.add_page()
#     path = dirpath +"/"+image

#     pdf.image(path,w=100,h=100,x=0,y=200)

# pdf.output("yourfile.pdf", "F")

from mynotiy import balloon_tip

balloon_tip('test','test2')