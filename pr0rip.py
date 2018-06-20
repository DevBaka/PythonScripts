import requests
import urllib2
import re
import urllib


def file_path(url):

    
    req = urllib2.Request('https://pr0gramm.com/static/2611242')
    response = urllib2.urlopen(req)
    the_page = response.read()
    print "HTML: " + the_page
    
    urls = re.findall('(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png)', the_page)
    #urls = re.findall('img(?:[-\w.]|(?:%[\da-fA-F]{2}))+', the_page)
    #urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', the_page)
    print "URL: " + urls[0]
    urllib.urlretrieve("http://" + urls[0], "local-filename3423.jpg")    
    #download_file(urls)
    

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

file_path("https://pr0gramm.com/static/2611242")
#download_file("https://pr0gramm.com/static/2611242")