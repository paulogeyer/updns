import urllib2, sys, re, base64, ConfigParser, os

def check_ip():
    url = "http://192.168.1.1/cgi/cgi_atm_info.cgi"
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # this creates a password manager
    passman.add_password(None, url, "admin", "gvt12345")
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(url)
    page = pagehandle.read()
    ip = re.search(r"\[\[(.+)\]\]", page, re.S).group(1).split(",")[5][1:-1]
    return ip

# def main():

if __name__ == u'__main__':
    ip_file = "/tmp/cur_ip"
    configFile = os.getenv("HOME")+"/.updns"

    if not os.path.exists(configFile):
        print("~/.updns not found")
        sys.exit()
    else:
        config = ConfigParser.RawConfigParser()
        config.read(configFile)
        urls = config.get('Config','urls').strip('[]').split(",")
        
    if os.path.exists(ip_file):
        f = open(ip_file)
        cur_ip = r.read()
        f.close()
    else:
        cur_ip = False

    new_ip = check_ip()

    if cur_ip != new_ip:
        for url in urls:
            urllib2.urlopen(url)
        f = open("/tmp/updns_ip","w")
        f.write(new_ip)
        f.close

    
