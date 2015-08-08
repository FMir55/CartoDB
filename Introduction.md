#CartoDB
- GIS Database
- Open Source
- Reference

http://blog.infographics.tw/2015/04/visualize-on-map-using-cartodb/

http://blog.changyy.org/2014/09/python-apache-web-server-accesslog.html

- 上傳原始檔案不等於使用到的儲存空間大小，而免費空間限制在 50MB 以下
- 付費選項不便宜， 4500 元新台幣 / 月，

故以python 對csv檔 篩檢所需Data Column，File Open 後再上傳檔案
https://github.com/FMir55/CartoDB/blob/master/CSV_Edit.py

所需欄位:
  - Longitude 
  - Latitude 
  - Value (欲觀測的值)
  
額外欄位:
  - DateTime (用於時間序列)
  
範例:

https://s1006005.cartodb.com/viz/90865306-3767-11e5-b737-0e9d821ea90d/public_map
