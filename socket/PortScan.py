#coding=UTF-8
import optparse
import scoket
import threading
import nmap

screenLock=threading.Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('HaveFun\r\n')
        results=connSkt.resv(100)
        screenLock.acquire()
        print('[+]%d/tcp open'% tgtPort)
        print('[+]' + str(results))
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed'% tgtPort)
    finally:
        screenLock.release()
        connSkt.close()
        
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unkkonwn host" %tgtHost)
        return
    try:
        tgtName=socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for:' +tgtName[0])
    except:
        print('\n[+] Scan Results for:' +tgtIP)
    scoket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port'+str(tgtPort))
        t=threading.Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()
        
def nmapScan(tgtHost,tgtPort):
    nmScan=nmap.PortScanner()
    results=nmScan.scan(tgtHost,tgtPort)
    state=results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*]"+tgtHost+" tcp/"+tgtPort+" "+state)
        
parser=optparse.OptionParser('usage % prog -H <targethost> -p <target port>')
parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
parser.add_option('-p,'dest='tgtPort',type='int',help='specify target port')
(options,args)=parser.parser_args()
tgtHost=options.tgtHost
tgtPort=options.tgtPort
if (tgtHost == None) or (tgtPort==None):
    print(parser.usage)
    exit(0)
else:
    print(tgtHost)
    print(tgtPort)
portScan('www.baidu.com',[80,443,3389,1433,23,445])    
