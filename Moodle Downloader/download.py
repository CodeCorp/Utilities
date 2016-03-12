import os
import requests
import sys
from bs4 import BeautifulSoup

s=requests.session()

USERNAME = ''   #Username and password are command line arguments
PASSWORD = ''   
COURSE_ID={}    
MAX_ID=0

#Function parses through the parameters entered in the command line. eg: python download.py -u https://bitcoin.org/bitcoin.pdf -d abc/
def get_args():
    
    if(len(sys.argv) != 3):
        print "Enter User name and password as command line arguments"
        sys.exit()
    else:
        global USERNAME
        global PASSWORD
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
    '''else:
        global USERNAME
        global PASSWORD
        try:
            opts, args = getopt.getopt(argv,"hi:o:",["uid=","password="])
        except getopt.GetoptError:
            print 'test.py -i <username> -o <password>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'test.py -i <username> -o <password>'
                sys.exit()
            elif opt in ("-i", "--uid"):
                USERNAME = arg
            elif opt in ("-o", "--password"):
                PASSWORD = arg
            print 'Username is "', sys.argv[1]
            print 'Password is "', PASSWORD
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, default=None, help='search text')
    parser.add_argument('-d', '--directory', type=str, default=os.getcwd(), action='store', help='the directory you want to use')
    return parser.parse_args()'''


#Function to save the downloaded file in the specified directory
def save_image(image, savepath):
    if not os.path.isdir(savepath):
        raise Exception
    fname = os.path.join(savepath, os.path.basename(image.url))
    fname = str(fname)
    fname1=""
    for a in fname:
        if a!='?':
            fname1 = fname1+a
        else:
            break
    fname2 = unicode(fname1)
    print fname2
    with open(fname2, 'wb') as f:
        f.write(image.content)
        f.close()


#Function to download the file from the specified url
def download_images(url,savepath):
 #   savepath = args.directory
 #   url = args.url
 #   url = 'https://bitcoin.org/bitcoin.pdf'      
     image = s.get(url)
     save_image(image, savepath)


#Establishes connection with moodle and creates the directory structure if it has not been created yet. If the structure has been created, it simply downloads all files.

def connect():
    payload={'username': USERNAME,'password':PASSWORD}
    r = s.post('http://10.1.1.242/moodle/login/index.php',data=payload)
    t = open('data.txt','r+')
    status=t.read()
    t.close()
    if status=="0":
        course = BeautifulSoup(r.text,"html5lib")
        for c in course.findAll('h2',{'class':'title'}):           
             COURSE_ID.update({c.a['href'][44:]:c.a.get_text()})
             makemydir(c.a.get_text())
        for k,v in COURSE_ID.items():
            fw = open('data.txt','a')
            fw.write(k + ':'+ v + '\n')
            fw.close()
        #m = open('xyz.txt','w')
        #m.write('1')
        #m.close()

    elif status!="0": 
        z=open('data.txt','r').read()
        for t in z.splitlines():
            k=t.split(':')
            COURSE_ID.update({k[0]:k[1]})

    global MAX_ID
    dummyMAXID = MAX_ID
    for i in COURSE_ID.items():
        k=i[0]
        v=i[1]
        #print k
        print "\n"+v
        payload1={'id':k}
        os.chdir(v)
        q = s.get('http://10.1.1.242/moodle/course/view.php',params=payload1)
        dummyMAXID = parser(q.text, dummyMAXID)
        os.chdir('../')
    MAX_ID = dummyMAXID


#Makes directories in the system

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
#  os.chdir(whatever)


#Parses the html document to download files
def parser(page, dummyMAXID):
    soup = BeautifulSoup(page,"html5lib")
    for link in soup.findAll('li',{'class':'section main clearfix'}):
        if(link.h3!=None):
            folder = link.h3.get_text()
            makemydir(folder)
#            os.chdir(folder)
            for file in link.findAll('li',{'class':'activity resource modtype_resource'}):
                if( int(file['id'][7:]) > MAX_ID):
                    dummyMAXID = max(int(file['id'][7:]), dummyMAXID)
                    verify('http://10.1.1.242/moodle/mod/resource/view.php', {'id':file['id'][7:]}, folder)
    return dummyMAXID


#Checks whether the link passed is an html link or a application(eg: ppt/pdf)
def verify(path,payload1,folder):
    p=s.get(path,params=payload1)
    if (p.headers['Content-Type']=='text/html; charset=utf-8'):
        soup = BeautifulSoup(p.text,"html5lib")
        file = soup.find('object',{'id':'resourceobject'})
        download_link = file.a['href']
        download_images(download_link, folder)   

    else:
        fullpath=path+'?id='+payload1['id']
        download_images(fullpath, folder)

    

def main(argv):
    get_args()
    
    print "hey?"
    r = open('last.txt', 'r+');
    maxid = r.read()
    r.close()
    global MAX_ID
    MAX_ID = int(maxid)
    connect()
    s = open('last.txt', 'w')
    s.write(str(MAX_ID))

if __name__ == '__main__':
    main(sys.argv[1:])
