import getpass
import os
while True:
	os.system("clear")
	print('''\033[91m		             .                  
		     -`     +`                  
		      /-   ++  -:`              \033[92mWelcome user\033[37m @\033[36m''',getpass.getuser(),'''\033[91m
		       :o. ys o:``              
		      `.-ssoN+d +` -+`          
		  `/shhyysyhNMMsd+:y`           \033[92m Select your choice:\033[91m
		 `+oso+/:.+y:NMMMNNy            \033[94m 1. \033[93mYum\033[91m
	      -/sdNNdsoss+--+sdMMmsd+           \033[94m 2. \033[93mDocker\033[91m
	   .+yydNMNy++m+`   ./+NMhymNh:`        \033[94m 3. \033[93mJenkins\033[91m
	   -..yNMmys. -   `-:y:sNs+:ydNy`       \033[94m 4. \033[93mExit\033[91m
	    .dNMMsMmo:  `ddoshhmN/-o``s.        
	    yyyMM/NmMs  yMNd/-:-..``/-.`        
	    o`sMMy/yhNy:hyh:s:       `-`        
	    ` +MhMh/:/hNh..+`o         .`       
	      .d.yMNho//:..- :                  
	       ::yoh+mNmdys+/:--..``            
	       `hMh/:.+dNNhdNMNy//:/::.`        
	       .yMMm.`.-/yh+::+ooo/:/oydho-`    
	       .yMM/-o/:--...`     `.-+/hNh/-   
		-dMsNh+:-.`           :h+sMm:   
		 `omNNs/:-`           `ym+mMN+  
		  `--:.```.`          .+ddyM+y/ 
	      `/+o+/+:..`           `:sdNyhM/`+`
	    .ohdyosydMdmh//:``--`.//+hmNh/MM-   
	   /mh/` `.:+syhdmdmmy/ymsoMNdho/NMy    
	  -Ns`       `-+ydmNNNNdNNmdhhyyoMy`    
	  sM-             ``.--:ymmmho-`o+`     
	  .Ms`             `-:/+/:.`  `-`       
	   yMh/`       `..           `-:        
	   `hMMNs+///:::.````   `:+::+/.        
	     oNmmNmdhyso+/:.`   :/+/-`          
	      -s/-+hNdysyssssoo+/-`             
		./:.`:oo/-`                     
		   `-.`  .--.``                                       
	\033[0m''')
	a=input("Enter your choice : ")
#-----------------------------yum---------------------------------------------
	if int(a) == 1:
		while True:
			os.system("clear")
			print(''' \033[94m 
                   `.-/ym       `-.               
             `..--::----d.    ./:/o/:-`           
 ./:-...--:::---os/:::::/h:..o:://+oo--::::/:`    
 .o+:------ohoosN:       ```````  `do-------:/+++-
    .::----:d  `y.              ```h:.---------:y-
      -s:..-y: `+             `````d-...------:/` 
       +Mo///o``+          ````````m+/-...---.    
     .-:/hs--h.`h`      ``````````.m/-+s+/s`      
 `--:----.:+/ho.ys    `````````.-:-hs:::/oy`     `---     ---`.--.   `--- `... `...   ...`    
:m/--------...:-/h//:..-...-----..........-:-`   `oyy:   :yyo +yyo   -yyy .///://///-/:///:`  
  -/+/-------.......oMm```.............------::--``syy. .yys` +yyo   :yyy .///.  :///`  ///- 
     -+o:-----......-Mm+............------:----/+- .yys`oyy-  +yyo   :yyy .///   -//:   ://- 
       /oso:----....+M:N........---/+++/o-          -yysyy/   /yys-`-syyy .///   -//:   ://- 
       -/--///+o/-..hm`sh-..-:::/++:----/.           :yyyo    `+yyyyo+yyy .///   -//:   ://- 
       :o----..-+yhsNd.-ho/:-....-------/-           .yys.
       ho------....:+s..........--------/:         syyy+``---..--...-: .:..--.-- ..-..-.--.. 
      `my:------....os.......-----------ss         ```                                       
        `:/+:-----..hh.....---------:///o:        
           `+so:----dh...----:/+/::-.             
              `-:/+sds:---::--.                   

	\033[92m Select your choice:\033[91m  
	\033[92m---------------------\033[91m
	\033[94m 1. \033[93mYum Configuration\033[91m
	\033[94m 2. \033[93mInstall Application\033[91m
	\033[94m 3. \033[93mRemove Application\033[91m
	\033[94m 4. \033[93mExit\033[91m
	\033[0m''')
			b=input("Enter your choice : ")
			if int(b) == 1:
				f=open("/etc/yum.repos.d/yum.repo","w")
				f.write("[dvd1] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/ \ngpgcheck=0 \n[dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/ \ngpgcheck=0 \n")
				f.close()
				print("Cofigured !")
				input()
			elif int(b) == 2: 
				app=input("Enter the name of App : ")
				os.system('yum install %s'%(app))
				print("Press enter to continue !")
				input()
			elif int(b) == 3: 
				app=input("Enter the name of App : ")
				os.system('yum remove %s'%(app))
				print("Press enter to continue !")
				input()
			elif int(b) == 4: 
				print("Press Enter to Main Menu !")
				input()
				os.system("clear")
				break;
			else : 
				print("Invalid Option")
				input()



#---------------------------------docker---------------------------------------------

	elif int(a) == 2:
		while True:
			os.system("clear")
			print(''' \033[96m 
                                                                                   
                                       /yssssssy.                                  
                                       /y++++++h.                                  
                                       /y++++++h.                                  
                         .-------------+yooooood-                  `               
                        `yysssssyysssssshssssssd.                `/so-`            
                        `hsoooooys+++++ohooooood.                /yooyo.           
                        `hsoooooys+++++ohooooood.               `ys+++sy.          
                 .///////hysssssyyoooooshssssssh+//////-        `ho++++ss..---..`  
                 -hsssssshsoooooyysssssshoooooohssssssh/        `ss++++ohsyyssyss+`
                 -hooooooho+++++syooooosy++++++hooooooh/         -yoo++oooooooosy+`
                 -hsoooooho+++++syooooosy++++++hooooooh+     ```.:syooooooosssso-  
           :oooooshyyyyyyhysssssyyyyyyyyysssssshyyyyyyhsoooooossssooooyssso+/:.    
      `    oyooo++++++++++++++++o+++++++++++++++o++++++++++++++++ooooys`           
     `o/.``oyooooosso+++++++++++ooyyoo++++++o+osysoo++++++++++ooysssys` ```-o:`    
 ``-/ossso+shyyyyhhhhyyyssssyyyyhhhhhyyyssssyyyhhhhhyyysssssyyhhhhhhy+///+osss+:.` 
           `hyyyssssssssssssssssssssssssssssssssssssssssssssyyyyyyh+               
            +hyyysssssssssssss O ossssssssssssssssssssssyyyyyyyyyy-                
            `ohyyyssssssssssss/ys/ssssssssssssssssssssyyyyyyyyyh/`                 
             `+hyyyyysssyyyyyysoossssssssssssssssssyyyyyyyyyyy+`                   
               :ys+++++//:-..+sssssssssssssssyyyyyyyyyyyyyhs:`                     
                `/s+:-------.-/sssssssyyyyyyyyyyyyyyyyyys/.`                       
                  `-+o+/--------+syyyyyyyyyyyyyyyyyys+:.                           
                     `./+oo++//:::/oyyyyyyyyyyso+/-``                              
                         ``.-:://///++//::-.```                                    
            ``                    \033[34m             `                                 
             -yy`                               sy:                                
             :dd`                               dd/                                
    `-/+oo+:.:dd`   `-/+oo+/-`      `-/+oo+/-   dd/  ./+.   `.:+ooo/:.       .:/++-
  `+yhyoooshhydd` `/yhysoosyhs:   `/yhyo++sys.  dd/`/yhs.  -shyso+oyhy+`   .oyhyso-
 .yhy-`   `.+hhd``shy:`    ./hh+ `ohy:`    ``   dhsyhs:`  /hh+.`   .ohh+  -hho-`   
 /dh.        +dd`:dd.        /dd`-dd:           dhhy:`   `hd+    ./yhy/` `yds      
 +dh`        /dd`:dd`        :dd.-dd-           ddhs.    .hh+ `-ohhs-`   `yh+      
 .ydo.     `:hho `yds.`    `-yds `sdy-`         dhyhh+.   +dh/shho-``    `yh+      
  .shho/:/+shy/`  .ohhs+//+shh+`  `ohhs+//+so`  dd/-ohh+`  /yhdho/+os-   `yh+      
   `-/syyyso:.      -/osyyso:.      -/osyyso/`  oy-  -oy-   `:+syyyo/.    oy:   

		   	\033[92m Select your choice:\033[91m  
			\033[92m---------------------\033[91m
	\033[94m 1. \033[93mDocker Configuration\033[91m	\033[94m 5. \033[93mDownload Docker Image\033[91m
	\033[94m 2. \033[93mInstall Docker\033[91m		\033[94m 6. \033[93mCheck running os\033[91m
	\033[94m 3. \033[93mDocker Status\033[91m		\033[94m 7. \033[93mCheck all os created\033[91m
	\033[94m 4. \033[93mCheck Docker Images\033[91m		\033[94m 8. \033[93mExit !\033[91m

	\033[0m''')
			c=input("Enter your choice : ")
			if int(c) == 1:
				f=open("/etc/yum.repos.d/docker.repo","w")
				f.write("[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ \ngpgcheck=0 \n")
				f.close()
				print("Cofigured !")
				input()
			elif int(c) == 2: 
				print("Please wait while installing !")
				os.system('yum install docker-ce --nobest')
				os.system('systemctl start docker')
				print("Press enter to continue !")
				input()
			elif int(c) == 3: 
				print("Please wait while checking status..\n\033[33mPress Q to exit !\033[0m")
				os.system('systemctl status docker')
			elif int(c) == 4: 
				print("Please wait while Collecting Data !")
				os.system('docker images')
				print("Press enter to continue !")
				input()
			elif int(c) == 5:
				docker_image=input("Enter the name of docker image to pull with version (Default latest) : ")
				print("Please wait image is pulling !")
				os.system('docker pull %s'%(docker_image))
				print("Press enter to continue !")
				input()
			elif int(c) == 6: 
				print("Please wait while checking running os in docker !")
				os.system('docker ps')
				print("Press enter to continue !")
				input()
			elif int(c) == 7: 
				print("Please wait while collecting data !")
				os.system('docker ps -a')
				print("Press enter to continue !")
				input()
			elif int(c) == 8: 
				print("Press Enter to Main Menu !")
				input()
				os.system("clear")
				break;
			else : 
				print("Invalid Option\nPress Enter to continue...")
				input()
#-------------------------------------------------------jenkins---------------------------------------------------------------
	elif int(a) == 3: 
		while True:
			os.system("clear")
			print(''' \033[33m 
                                       `                                         
                                 `/ohhsoossss+.                                   
                              .++so/-........:sy-                                 
                             oyoy/`............+do                                
                           .hso+y:../so/......-:/y/                               
                           sssssh-..:...-.......-.y                               
                         -hmyhhss.......-o-.:+.:+oy+                              
                       `yhsd+o+hh-...../o+.../s:-.yhd-                            
                      .dysyh.+:--..............y/.dssd/                           
                     `dyssshs:-/..........-+//++:/hsssd/                          
                     shsssssyhm:...-..../+oss/so:dssssym`                         
                    `mssssssssyy`..//...-ooo+/./dssssssd+                         
                    -msssssssyhmy...-/+:....-+ydddysssshs                         
                    -mssssyddhyshms/+hyddhsydhydhyddssshs                         
                    `msshmhyyhhhhhhddysssydhhssydhhdsssd/                         
                     ohsymyyhhhhhhhhhhssyyy:+ysydhdyssym`                         
                     `dysymyhhhhhdhhhhdh+/s+.+/yhhdsssd:                          
                      `hysdyyhhhhdyhhhddys+s+shhhdyyhmo                           
                        sdhdyhhhddhdddhhhhddmmdddh++.`s+                          
                         -ymyhhhhho`       `yyhs.o`-. `d`                         
                           dyhhhhhs        `ohhd`y`-:..h`                         
                           sddhhhhh`       `+ddm///so/+-                          
                             .+shhd/       `/+o/                                  
                                  .h        :/:y                                  
                                   ++       -d+-                                  
                                    osooooooo+                                    
                                                                                  
    .:::::::                          /hmNd`        sNNs                          
     .oMMM:`                           :MMm`        +dd+                          
      :MMM`     -://:`  `---:``-//-    :MMm` -----`---:-  .--:- .:/:.     -://--- 
      :MMM`   oNN: /MMy``/NMMs++hMMd   :MMm` .dy/- -yMMd  -sMMNo++mMM+  -mMs``:ds 
      :MMM`  oMMm+++MMM/  mMM:  .NMM`  :MMm.sN:     :MMd   :MMm`  oMMh  +MMNhs+-. 
`ymd: :MMM`  yMMm         mMM:  .NMM`  :MMNoNMMo    :MMd   :MMm`  +MMh  .:shNMMMh`
.NMm- yMMs   .mMMs`  .s-  mMM:  .NMM.  :MMm`.dMMd.  /MMm   :MMm`  +MMh  hs`  `mMm`
 .oo+yyo-      :syhys+` .+ssss-.+ssso-:osss+. osss//sssso.:osss+`:ssss+`++o+/+y+` 
\033[0m''')
			d=input("Enter your choice : ")
			if int(d) == 1:
				f=open("/etc/yum.repos.d/docker.repo","w")
				f.write("[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ \ngpgcheck=0 \n")
				f.close()
				print("Cofigured !")
				input()
			elif int(d) == 4: 
				print("Press Enter to Main Menu !")
				input()
				os.system("clear")
				break;
			else : 
				print("Invalid Option\nPress Enter to continue...")
				input()
#----------------------------------GIT------------------------------------------------------------------------
	elif int(e) == 5: 
		while True:
			os.system("clear")
			print(''' \033[94m 
\033[0m''')
			d=input("Enter your choice : ")
			if int(e) == 1:
				f=open("/etc/yum.repos.d/docker.repo","w")
				f.write("[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ \ngpgcheck=0 \n")
				f.close()
				print("Cofigured !")
				input()
			elif int(e) == 4: 
				print("Press Enter to Main Menu !")
				input()
				os.system("clear")
				break;
			else : 
				print("Invalid Option\nPress Enter to continue...")
				input()
#--------------------------------------------------------------------------------------------------------------
	elif int(a) == 4: 
		print("Bye !")
		input()
		os.system("clear")
		break;
	else : 
		print("Invalid Option")
		input()

