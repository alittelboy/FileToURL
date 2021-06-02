import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import pyperclip
import requests
# https://oss.chaojibiaoge.com/uploadfile/2021/06/main_MNsRzy[small].png
def upload(filePath):
    url = 'https://www.deepsheet.net/System/TableEdit/saveUploadedFile/istemp/false/modelid/undefined/fieldid/attach' \
          '/recordid/null/projectid/undefined/sharekey/ '
    files = {
        'mcssuploadfile[image1]': open(filePath, 'rb')
    }
    response = requests.post(url, files=files)

    body = (response.content.decode('utf8'))
    print(body)
    if (body.find("value='") < 0):
        return "上传失败，上传的文件路径请不要有中文"
    else:
        d_url = body.split("value=")[1].split("'")[1]
        if d_url.find("~") < 0:
            return "上传失败，上传的文件路径请不要有中文"
        d_url = d_url.split("~")[1]
        return "https://oss.chaojibiaoge.com/uploadfile/" + d_url


def chooseUpload():
    default_dir = r"文件路径"
    file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    print(file_path)
    if not os.path.exists(file_path):
        tkinter.messagebox.showinfo(title='err', message="文件地址错误，文件不存在")
    else:
        url = upload(file_path)
        print(url)
        if(url.find("上传失败")<0):
            pyperclip.copy(url)
            tkinter.messagebox.showinfo(title='ok', message="文件上传成功，网址已经复制到剪切板。")

        else:
            tkinter.messagebox.showinfo(title='ok', message=url)


if __name__ == '__main__':
    root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
    root.title("文件上传工具  ——by辣鸡土豆")
    root.geometry('400x100')
    b = tkinter.Button(root, text='上传文件', font=('Arial', 12), width=10, height=1, command=chooseUpload)
    b.pack()
    b.place(x=200, y=30, anchor='n')
    root.mainloop()
    # root.withdraw()       # 将Tkinter.Tk()实例隐藏
