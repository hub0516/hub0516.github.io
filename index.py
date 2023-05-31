import os
f=open("index.html","r+")
text=f.readlines()
f.seek(0,0)
f.writelines([i.replace("URL",os.popen("git config --global Ngrok.py").read().strip()) if i.find("URL")+1 else i for i in text])
f.close()
# os.remove(__file__)
