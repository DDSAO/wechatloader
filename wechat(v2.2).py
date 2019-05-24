import tkinter as tk

__author__ = 'ddsao'

class HTMLEditor():
    def __init__(self):
        self._text = ""
        self._location_dict= {}
        self._content = {}

    def find_location(self, text):
        location_list = ['北京','上海','广州','深圳']
        found = False
        current_location = ''

        for location in location_list:
            if found == False and text.find(location) != -1:
                found = True
                current_location = location
            elif found == True and text.find(location) != -1:
                current_location = "多地"
                break

        if found == False:
            return "未知"
        else:
            return current_location

    def add_location_dict(self, text):
        location = self.find_location(text)
        if location in self._location_dict.keys():
            self._location_dict[location].append(text)
        else:
            self._location_dict[location] = [text]

    def get_dict(self):
        return self._location_dict

    def encode(self):
        content = self.generate_table()
        format = '<style>*{font-size:0.9em;}' \
                 'table,th,tr,td{border-collapse:collapse}' \
                 'td{text-align:center;border:1px solid lightblue}' \
                 'th{color:white;background-color:#003399;border:transparent}' \
                 'p{padding:0 15px;}' \
                 '.content{border:1px solid grey;margin-top:50px;box-shadow:grey 3px 3px 3px}' \
                 'label{padding:10px 10px; background-color: #003399; color:white; position:relative; left:45%; bottom:12px; box-shadow:grey 3px 3px 2px;}' \
                 'section>p:first-of-type {margin-top:15px}' \
                 '</style>'
        for location in self._location_dict.keys():
            content += self.generate_section(self._location_dict.get(location,""),location)
        return format + content

    def generate_table(self):
        content=""
        preformat = '<table width=100%>' +\
            '<tr style="text-align: center;">' +\
                '<th width=30% height=40px>地区</th>' +\
                '<th width=%70 height=40px>公司</th></tr>'
        postformat = '</table>'
        for location in self._location_dict.keys():
            content += '<tr>' +\
            '<td height=40px>' +\
            location + '*' + str(len(self._location_dict[location])) + '</td>' +\
            '<td height=40px style="text-align: left; padding-left:5px;">' +\
            self.get_company_name(self._location_dict[location]) + '</td></tr>'
        return preformat + content + postformat

    def get_company_name(self, list):
        name = ""
        for i, text in enumerate(list):
            if i != len(list)-1:
                name += text.split('\n',1)[0] + ', '
            else:
                name += text.split('\n',1)[0]
        return name

    def generate_section(self, list,location):
        content=''
        preformat = '<section class="content">' +\
        '<label>' +\
                    location + '*' + str(len(list)) + '</label>'
        postformat = '</section>'
        for text in list:
            content += self.add_p(text) + '<br>'
        return preformat + content + postformat

    def add_p(self,text):
        text_list = text.split('\n');
        content = ''
        for paragraph in text_list:
            content += '<p>' + paragraph + '</p>'
        return content
class APP():
    def __init__(self,root):
        self._root = root
        self._root.title("今日实习编辑器")
        self._editor = HTMLEditor()
        self._record_num = 0

        tk.Label(self._root, text="将一段实习内容粘贴至下方，点击添加").pack()
        self._e = tk.Entry(self._root)
        self._e.focus()
        self._e.pack()

        self._option_f = tk.Frame(self._root)
        self._option_f.pack()

        tk.Button(self._option_f, text="添加",command=self.add_to_editor).pack(side=tk.LEFT)
        tk.Button(self._option_f, text="查看表格", command = self.see_record).pack(side=tk.LEFT)
        tk.Button(self._option_f, text="获取神秘代码", command=self.generate_html).pack(side=tk.LEFT)

        self._record_l = tk.Label(self._root, text="当前录入总数: 0")
        self._record_l.pack()

        self._record_f = tk.Frame(self._root)



        self._html_f = tk.Frame(self._root)


    def add_to_editor(self):
        text = self._e.get()
        self._editor.add_location_dict(text)
        self._record_num += 1
        self._record_l.config(text = "当前录入总数: " + str(self._record_num))
        self._e.delete(0,'end')


    def see_record(self):
        self._record_f.destroy()
        self._record_f = tk.Frame(self._root)
        self._record_f.pack()
        for location in self._editor.get_dict().keys():
            tk.Label(self._record_f, text = location + " :" + str(len(self._editor.get_dict().get(location, "")))).pack()


    def generate_html(self):
        self._html_f.destroy()
        self._html_f = tk.Frame(self._root)
        self._html_f.pack()

        content = self._editor.encode()
        self._text = tk.Text(self._html_f,width=30, height=2)
        self._text.focus()
        self._text.pack()
        if len(content) == 0 or content == None:
            self._text.insert(tk.INSERT, '文件空')
        else:
            self._text.insert(tk.INSERT, content)

if __name__ == '__main__' :
    root = tk.Tk()
    app = APP(root)
    root.mainloop()

