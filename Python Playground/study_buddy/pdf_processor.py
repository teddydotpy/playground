import glob, random, re
import PyPDF2

random.seed(any)
class PdfProcessor:
    def __init__(self):
        self.fileName = ''
        self.subject = ''

    def getSubject(self):
        return self.subject

    def getfileName(self):
        txtfiles = []
        for file in glob.glob("exampapers/*.pdf"):
            txtfiles.append(file)
             
        self.fileName = txtfiles[random.randrange(1,len(txtfiles)-1)]
        return self.fileName

    def getPage(self):
        fileName = self.getfileName()
        pdfFileObj = open(fileName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(random.randint(2,pdfReader.numPages - 2)) 

        QuestionRe = re.compile(r'Geography | Mathematics | Physical Science |Biology | English', re.IGNORECASE)
        QuestionGr = QuestionRe.search(pdfReader.getPage(0).extractText())

        print(QuestionGr)
        if QuestionGr != None:
            self.subject = QuestionGr.group()
            return pageObj.extractText()
        else:
            self.subject = 'Well bud you have to figure this one out.'
            return pageObj.extractText()

        
    def getQuestion(self):
        textobj = self.getPage()
        QuestionRe = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.IGNORECASE)
        QueList = QuestionRe.findall(textobj)

        return QueList
    





