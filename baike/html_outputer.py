class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.md', 'w', encoding='utf8')

       
        fout.write('#百度百科\n')
        for data in self.datas:
            fout.write("##[%s](%s)##\n" % (data['title'], data['url']))
            fout.write("> %s" % (data['summary']))
            fout.write('\n\n---------\n\n') 

        fout.close()
