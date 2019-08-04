import requests, time, os

pt = {'pid':'7cpe4e95', 'oids':'check24454789'}

headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "*/*",
            "Accept-Encoding":"gzip, deflate",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://strawpoll.com/7cpe4e95",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"}
            
cont_request = 0
for i in range(100):
      r = requests.post("https://strawpoll.com/vote", params=pt, headers=headers)
      time.sleep(5)
      print('Sucess!')
      cont_request += 1
      print('Numero de requests %i ' % cont_request)
      os.system('systemctl restart tor') #archlinux restart tor service
      print('Reiniciando o tor')
      time.sleep(10)
