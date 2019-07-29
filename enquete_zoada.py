import requests, time, os

pt = {'pid':'7cpe4e95', 'oids':'check24454789'}

headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "*/*",
            "Accept-Encoding":"gzip, deflate",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
            "Cookie":"__atutc=; __atuuc=5185443; _ga=GA1.2.1114325762.1564363850; _gid=GA1.2.1706429745.1564363850; _gat_gtag_UAlgum001217_1=1; hibext_instdsigdipv2=1"}

cont_request = 0
for i in range(100):
      r = requests.post("https://strawpoll.com/vote", params=pt, headers=headers)
      time.sleep(2)
      print('Sucess!')
      cont_request += 1
      print('Numero de requests %f0' % cont_request)
      os.system('systemctl restart tor')
      print('Reiniciando o tor')
      time.sleep(7)


