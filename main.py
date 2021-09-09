import eel
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory,askopenfilename,askopenfilenames
import time
from glob import glob

#
# target=r"D:\Download\Documents\34779154304018873.pdf"
# reader=PdfFileReader(target)
# write=PdfFileWriter()
# page=reader.getPage(0)
# page.cropBox.setLowerLeft((30,100))
# page.cropBox.setUpperLeft((30,842))
# page.cropBox.setUpperRight((595,842))
# page.cropBox.setLowerRight((595,100))
# write.addPage(page)
# with open("test_crop.pdf","wb") as out:
#     write.write(out)

@eel.expose
def start(target):
    # target=r"D:\Download\Documents\34779154304018873.pdf"
    c = canvas.Canvas(r"D:/grid.pdf")
    width=10
    space=10
    c.setDash([2,4,width,space])
    c.setLineWidth(6)
    c.line(300,0,300,850)
    c.line(0,420,600,420)
    c.save()
    result_name=datetime.now().strftime(f"result %Y-%m-%d at %I.%M.%S %p")
    grid=PdfFileReader("D:/grid.pdf","rb")
    output = PdfFileWriter()
    output.insertPage(grid.getPage(0))
    # output.getPage(0)
    blank_page = output.getPage(0)
    itr = 0
    # measures = [('0', '450'), ('320', '450'), ('0', '0'), ('320', '0')]
    measures = [('0', '450'), ('250', '450'), ('0', '0'), ('250', '0')]
    page_capacity = 4
    scale = 0.45
    if len(target)==1:
        print(f"current file {target[0]}")
        with open(fr"{target[0]}", 'rb') as current_file:
            input1 = PdfFileReader(current_file)
            for count, i in enumerate(range(0, input1.getNumPages(), 1)):
                page = input1.getPage(i)
                if (input1.getNumPages() / 2) <= 3:
                    print("file page <=3")
                    blank_page.mergeScaledTranslatedPage(page2=page, scale=f'{scale}', tx=f'{measures[count][0]}', ty=f'{measures[count][1]}')

                elif (input1.getNumPages() / 2) > 3:
                    print("file page >3")
                    blank_page.mergeScaledTranslatedPage(page2=page, scale=f'{scale}', tx=f'{measures[itr][0]}', ty=f'{measures[itr][1]}')
                    itr = (itr + 1) % len(measures)
                    if (count + 1) % page_capacity == 0 and (count+1) < input1.getNumPages():
                        print("add blank page")
                        # output.insertPage(grid.getPage(0))
                        blank_page = output.getPage(0)
                with open(f'D:/{result_name}.pdf', "wb") as out_f:
                    output.write(out_f)
    else:
        scale=0.45
        if len(target)<=4:
            print("enter 4 file case")
            for count, pdf in enumerate(target):
                with open(f'{pdf}','rb') as current_file:
                    input1=PdfFileReader(current_file)
                    bill=input1.getPage(0)
                    bill.cropBox.setLowerLeft((30, 100))
                    bill.cropBox.setUpperLeft((30, 842))
                    bill.cropBox.setUpperRight((595, 842))
                    bill.cropBox.setLowerRight((595, 100))
                    # target=r"D:\Download\Documents\34779154304018873.pdf"
                    # reader=PdfFileReader(target)
                    # write=PdfFileWriter()
                    # page=reader.getPage(0)
                    # page.cropBox.setLowerLeft((30,100))
                    # page.cropBox.setUpperLeft((30,842))
                    # page.cropBox.setUpperRight((595,842))
                    # page.cropBox.setLowerRight((595,100))
                    # write.addPage(page)
                    # with open("test_crop.pdf","wb") as out:
                    #     write.write(out)

                    blank_page.mergeScaledTranslatedPage(page2=bill, scale=f'{scale}', tx=f'{measures[count][0]}', ty=f'{measures[count][1]}')
                    with open(f'D:/{result_name}.pdf', "wb") as out_f:
                        output.addPage(bill)

                        output.write(out_f)
        else:
            print("enter more 4 case")
            for count, pdf in enumerate(target):
                with open(f'{pdf}','rb') as current_file:
                    input1=PdfFileReader(current_file)
                    bill=input1.getPage(0)
                    blank_page.mergeScaledTranslatedPage(page2=bill, scale=f'{scale}', tx=f'{measures[count%len(measures)][0]}', ty=f'{measures[count%len(measures)][1]}')
                    with open(f'D:/{result_name}.pdf', "wb") as out_f:
                        output.write(out_f)
                    if (count + 1) % page_capacity == 0 and (count + 1) < len(target):
                        # output.insertPage(grid.getPage(0))
                        # output.getNumPages()
                        blank_page = output.getPage(0)


    print("done")
    time.sleep(1)
    eel.say_hello_js('Python World!')


@eel.expose
def get_path():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder_path = askopenfilenames(filetypes=[("pdf files", "*.pdf")])
    # print(folder_path)
    return folder_path

lis=(
    'D:/Download/Documents/reportlab-reference.pdf',
    'D:/Download/Documents/reportlab-userguide.pdf',
    'D:/Download/Documents/sql-basics-cheat-sheet-a4.pdf'
)
len(lis)
@eel.expose
def test(file):
    print(file,type(file))

eel.init('D:/Python/Amazon_bills/web')
# eel.t
eel.start('main.html')


