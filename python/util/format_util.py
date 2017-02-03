import re, datetime

class utils:
    @staticmethod
    def numberChange(str):
        return re.sub('[^0-9]','',str)

    # def dateFormat(str):
    #     return numberChange(str).rjust(4, '0')
    @staticmethod
    def dateFormat():
        datetime.today().strftime("%Y-%m-%d HH-mm-ss")

    @staticmethod
    def euc2utf(str):
        return unicode(str, 'utf-8').encode('utf-8')
