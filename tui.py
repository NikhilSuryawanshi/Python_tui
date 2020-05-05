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
	   .+yydNMNy++m+`   ./+NMhymNh:`        \033[94m 3. \033[93mServices\033[91m
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

	if int(a) == 1:
		print("1")
		input()
	elif int(a) == 2: 
		print("2")
		input()
	elif int(a) == 3: 
		print("3")
		input()
	elif int(a) == 4: 
		print("Bye !")
		input()
		os.system("clear")
		break;
	else : 
		print("Invalid Option")
		input()

