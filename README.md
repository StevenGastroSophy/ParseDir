# ParseDir.py
爬取資料夾結構

Demo以 treeviz來繪製樹狀圖，執行 Demo後會印出

0  
├── 1-1  
│   ├── 2-1  
│   └── 2-2  
├── 1-2  
│   └── 2-3  
│       ├── 3-2  
│       └── 3-1  
└── 1-3

會在 Demo.py所在的目錄下產生 ParseDir.xml，內容如下

<dir name="0">  
  <dir name="1-1">  
    <dir name="2-1" />  
    <dir name="2-2" />  
  </dir>  
	<dir name="1-2">  
	  <dir name="2-3">  
	    <dir name="3-2" />  
	    <dir name="3-1" />  
	  </dir>  
	</dir>  
	<dir name="1-3" />  
</dir>  
