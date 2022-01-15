import re
import xlwt
from bs4 import BeautifulSoup

findItem = re.compile(r'<li style="height: 80px;">(.*?)</li>')


def getdata():
    datalist = []
    file = open("./lqsj.html", 'rb')
    # html = askURL(baseurl)
    html = file.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('ul', class_="tbu th-b"):
        data = []
        item = str(item)
        data = re.findall(findItem, item)
        datalist.append(data)

    print(datalist)
    return datalist


def savedata(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet('武汉理工大学2021年录取数据', cell_overwrite_ok=True)
    col = ("类型", "专业（类）", "省控线", "最高分", "最低分", "位次值", "平均分", "选考科目")
    for i in range(0, 8):
        worksheet.write(0, i, col[i])

    for i in range(0, len(datalist)):
        print("%d" % i)
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i + 1, j, data[j])

    workbook.save(savepath)


def main():
    # URL = "https://zs.whut.edu.cn/bklqqk/"
    savePath = ".\\武汉理工大学2021年录取数据1.xls"
    datalist = getdata()
    savedata(datalist, savePath)


if __name__ == '__main__':
    main()
