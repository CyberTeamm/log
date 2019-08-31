from getpass import getpass
import os
import time
									       												
def menu():
      while True:
           print("")
           os.system("clear")                				
           os.system('figlet -f pagga  CyberTeam  | lolcat')
           print("")
           print('\033[1;36;40m<─────────────── CyberTeam Login Panel ───────────────>')
           print('')						 
           print("\033[1;93m")					
           print(" \033[1;92m  786 => CyberTeam Güvenlik Duvarı Girişi')")
           print("\033[1;93m")                
           print("  <───────[ Sinyalci ]───────>")
           print("")
           try:					 
                x = str(input('\033[1;92mKullanıcı Adınız \033[1;93m: '))
                print("")			
                e = getpass('\033[1;92mŞifreniz \033[1;93m: ')
                print ("")                    
                if x=="Unknown" and e=="F1u2r3k4a5n6adpas":
                   print('Giriş Yapılıyor...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
		                             							    
                   os.system('figlet -f slant ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Giriş Hatalı")
                      time.sleep(2)			   
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Giriş Hatalı")
                      time.sleep(2)			  
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Giriş Hatalı")
                      time.sleep(2)			  
menu()
