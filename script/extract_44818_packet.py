from tqdm import tqdm
import os

folder_path = os.getcwd()
file_list = []
for file in [pcapng for pcapng in os.listdir(folder_path)
	if pcapng.endswith(".pcapng")]:
		file_list.append(file)

os.system('   mkdir /tmp/0420     ')

for file in tqdm(file_list):
	tmp = "tshark -r " + file  + " -w /tmp/0420/44818_" + file + " -Y \'tcp.port == 44818\'"
	os.system(tmp)

#os.system(' cp /tmp/0401/* /root/share/deal_0401/  ')

## put all pcapng file in the same folder
## run python2 in the same folder 
## usage: python2 convert.py
## 假設當前資料夾底下有很多 .pcapng ，放此 .py 在底下，執行 python2 convert.py
## 他會將檔案裡面是 tcp port 44818 的取出放在 /tmp/0420 底下，
## 他會將萃取的封包標頭加上 44818_ 存在 /tmp/0420 裡面