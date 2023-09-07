'''
from tkinter import Tk
win=Tk()
win.mainloop()
'''
'''
import requests
from bs4 import BeautifulSoup
page=requests.get('http://www.flag.com.tw')
soup=BeautifulSoup(page.text, "html.parser")
print(soup.title)
'''
'''
import requests
r=requests.get('http://www.flag.com.tw')
if r.status_code==200:
    print(r.text)
else:
    print(r.status_code,r.reason)
'''
'''
import requests
url='https://httpbin.org/get'
hd={'user-key':'7ADGS9S'}
pm={'id':1023,'name':'joe'}
r=requests.get(url,headers=hd,params=pm)
print(r.text)
'''
'''
import requests
url='https://httpbin.org/post'
r=requests.post(url,data='Hello')
print(r.text)
r=requests.post(url,data={'id':"123",'name':'joe'})
print(r.text)
'''
'''
import requests
r=requests.put('https://httpbin.org/put',data={'key':'abc'})
print(r.text)
r=requests.patch('https://httpbin.org/patch',data={'key':'yxz'})
print(r.text)
r=requests.delete('https://httpbin.org/delete')
print(r.text)
'''

page="""
<html>
	<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
	<title>旗標科技</title>
	<link rel="stylesheet" href="https://www.flag.com.tw/assets/css/home/normalize.css">
	<link rel="stylesheet" href="https://www.flag.com.tw/assets/css/home/style.css">
	<link rel="stylesheet" href="https://www.flag.com.tw/assets/css/home/animate.css">
	<link rel="stylesheet" href="https://www.flag.com.tw/assets/css/home/font-awesome.css">
  <link rel="stylesheet" href="https://www.flag.com.tw/assets/css/home/bigvideo.css">
  <meta property="og:image" content="https://www.flag.com.tw/assets/img/flag-32.png">
  <link href="https://www.flag.com.tw/assets/css/home/applauncher.css" rel="stylesheet" type="text/css">
	<script type="text/javascript" src="https://www.flag.com.tw/assets/js/jquery-3.2.1.min.js"></script>
    <script src="https://www.flag.com.tw/assets/js/jquery-ui.min.js"></script>
	<script src="//vjs.zencdn.net/4.3/video.js"></script>
  <script src="https://www.flag.com.tw/assets/js/bigvideo.js"></script>
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script> 
  <script src="https://www.flag.com.tw/assets/js/applauncher.js"></script>

<link rel="icon" href="https://www.flag.com.tw/assets/img/flag.png" sizes="32x32" />
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-122475394-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-122475394-1');
</script>
<!-- Microsoft Clarity Web Analytics -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "4hfmycs491");
</script>
<!-- 亂數出現底圖1101013新增 -->
<script type="text/javascript">
    //<!CDATA[
        var bodyBgs = [];
        bodyBgs[0] = "https://www.flag.com.tw/assets/img/home/01.jpg";
        bodyBgs[1] = "https://www.flag.com.tw/assets/img/home/02.jpg";
        bodyBgs[2] = "https://www.flag.com.tw/assets/img/home/03.jpg";
        bodyBgs[3] = "https://www.flag.com.tw/assets/img/home/04.jpg";
        bodyBgs[4] = "https://www.flag.com.tw/assets/img/home/05.jpg";
        var randomBgIndex = Math.round( Math.random() * 4 );

    //輸出隨機的背景圖
        document.write('<style>body{background:url(' + bodyBgs[randomBgIndex] + ') no-repeat 100% 0}</style>');
    //]]>
    </script>

<!-- 亂數出現底圖結束 -->

	</head>
	<body class="homepage">
  <div id="BackgroundArea"> 

  <!-- Demo applauncher -->
  <div class="container">
        <div class="launcher">
          <div class="button icon"><img src="https://www.flag.com.tw/assets/img/applauncher_white.png"></div>
          <div class="app-launcher">
            <div class="apps">
              <ul class="first-set">        
                <li class="icon"><a href="https://www.flag.com.tw/flag/activity"><img src="https://www.flag.com.tw/assets/img/4-1.svg" title="活動"></a></li>
                <li class="icon"><a href="https://www.flag.com.tw/VIP/Bonus"><img src="https://www.flag.com.tw/assets/img/5-1.svg" title="會員Bonus"></a></li>                            
                <li class="icon"><a href="https://www.flag.com.tw/flag/recruit"><img src="https://www.flag.com.tw/assets/img/6-1.svg" title="徵才資訊"></a></li> 
                <li class="icon"><a href="https://www.flag.com.tw/flag/contact"><img src="https://www.flag.com.tw/assets/img/2-1.svg" title="聯絡我們"></a></li>  
                <li class="icon"><a href="https://www.flag.com.tw/flag/aboutflag"><img src="https://www.flag.com.tw/assets/img/1-1.svg" title="關於旗標"></a></li>
                <!--                
                <li class="icon"><a href="https://www.flag.com.tw/flag/privacy"><img src="https://www.flag.com.tw/assets/img/3-1.svg" title="隱私權規約"></a></li>
                -->
                <!--
                <li><a href="#"><img src="https://www.flag.com.tw/assets/img/bookpic/F0753.jpg" width="50px" title="關於旗標"></a> </li>          
                -->
              </ul>
            </div>
          </div>
        </div>
      </div>
  <!-- Demo applauncher -->
  </div>
  </div>
<section class="homeheader">
      <div class="home">
     
	  	  <!--  <div class="home-title"><img src="https://www.flag.com.tw/assets/img/home/F0318_title.png" alt="Logo"></div> -->  
       
   
          
        <form action="https://www.flag.com.tw/books/book_searching" method="post" class="search" role="search">
          <div class="form__field">
           <input type="text" name="book_search" placeholder="關鍵字搜尋" class="form__input" value=""  autofocus>
          </div>
        </form>
       <!--  <div class="home-logo"><img class="home-loc" src="https://www.flag.com.tw/assets/img/home/flag-logo-black-nologo.png"></div>--> 
      </div>

<div class="mainbtn">
    <div class="sub-main">
      <button class="button-three bluebtn"  onclick="location.href='https://www.flag.com.tw/books'"><p>Books</p><h4>圖書</h4></button>
    </div>
    <div class="sub-main">
      <button class="button-three orangebtn" onclick="location.href='https://www.flag.com.tw/maker'"><p>Maker</p><h4>創客</h4></button>
    </div>
    <div class="sub-main">
      <button class="button-three pinkbtn" onclick="location.href='https://www.flag.com.tw/books/school'"><p>Textbooks</p><h4>教科書</h4></button>
    </div>
	 <div class="sub-main">
      <button class="button-three purplebtn" onclick="location.href='https://www.flag.com.tw/teachaid/'"><p>Teach Aid</p><h4>教具</h4></button>
    </div>
  </div>
     
</section>

<!--		<footer role="contentinfo">
    <table class="clmtable">
      <tr>
        <td><a href="https://www.flag.com.tw/flag/contact">聯絡我們</a></td>
		<td><a href="https://www.flag.com.tw/flag/aboutflag">關於旗標</a></td>
        <td><a href="https://www.flag.com.tw/flag/privacy">隱私權規約</a></td>
      </tr>
    </table>
 <div class="footer-bottom">
    <p class="footer-left"> <strong>旗標科技股份有限公司</strong></p><p>台北市中正區
      杭州南路一段15-1號19樓 </p>
    <p class="footer-right">© Flag Technology CO.,LTD.
      All rights reserved.</p>
  </div>
</footer>-->
</body>

</html>
"""
from bs4 import BeautifulSoup
bs=BeautifulSoup(page,'lxml')

# print(bs.title)
# print('------')
# print(bs.a)
# print('------')
# print(bs.a.get('href'))
print('------')
print(bs.a['href'])
print('------')
print(bs.find('h4'))
print('------')
print(bs.find('h4').text)
print('------')
print(bs.find('h4',{'class':'pk'}))
print('------')
print(bs.find_all('h4'))
print('------')
print(bs.find_all('h4',{'class':'pk'}))
print('------')
print(bs.find_all(['title','p']))
print('------')
print(bs.find_all(['title','p'])[1].text)






















