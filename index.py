import webbrowser
import os 
import getpass
os.system("banner Menu")
print("Enter the choice..........")
def inventory(x,y,z):
    xy="{0} ansible_ssh_user={1} ansible_ssh_pass={2}".format(x,y,z)
    file1 = open("/etc/myhosts", "a") 
    file1.write(xy) 
    file1.write("\n")
    file1.close() 
while True:
 print("""
 	press 0: Basic Opertaing system
 	press 1: Docker
 	press 2: Kubernetes
 	Press 3: Git
 	Press 4: Ansible
 	Press 5: Hadoop
 	Press 6: Openshift
 	Press 7: Linux Partition
 	Press 8: Jenkins
 	Press 9: Exit
 	""")
 p=int(input())
 if p == 0:
 	os.system("banner 'Basic CMD' ")
 	while True:
 		print("""
 			press 1: Show How many process are run in my system........
 			press 2: show memory uses in the systems...
 			press 3: Show how many port running listen in the systems.......
 			press 4: show whih shell you used...........
 			press 5: Show prevoius command executed sucefully or not...........
 			press 6: Ping ip to check network connectivity...................
 			press 7: show the Ip adress of the systems............
 			press 8: Exit..
 			""")
 		cmd=int(input())
 		if cmd == 1:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ps -aux")
 			#webbrowser.open('firefox').open_new_tab("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ps -aux")
 			#webbrowser.register('firefox',None))
 		elif cmd == 2:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=free -m")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=free -m")
 		elif cmd == 3:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=netstat -tnlp")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=netstat -tnlp")
 			#os.system("netstat -tnlp")
 		elif cmd == 4:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=echo $SHELL")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=echo $SHELL")
 			#os.system(" echo $SHELL")
 		elif cmd == 5:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=echo $?")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=echo $?")
 			#os.system(" echo $?")
 		elif cmd == 6:
 			ip=input("Enter the Ip: ")
 			ip_add=" ping "+ ip
 			webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=%s")
 			#os.system(" ping " + ip )
 		elif cmd == 7:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ifconfig wlp3s0")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ifconfig wlp3s0")
 			#os.system("ifconfig wlp3s0")
 		elif cmd == 8:
 			break
 		else:
 			print("Press choie is not use full")
 elif p == 1:
 	while  True:
 		os.system("banner Docker")
 		print("""
 			press 0: Show Docker versions.........
 			Press 1: Check the Status of Docker..........
 			Press 2: Strat the Docker...............
 			Press 3: Stop the Docker..............
 			Press 4: Show all Images..........
 			Press 5: Show all running containers.....
 			press 6: Remove Container...........
 			press 7: Delete Docker images......
 			press 8: Delete all Running Containers.......
 			press 9: Run web Container and expose outside port 80......
 			press 10: Information about running containers..........
 			press 11: Exit
 			""")
 		docker=int(input())
 		if docker == 0:
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker version")
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker version")
 			#os.system("docker version")
 		elif docker == 1:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl status docker")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl status docker")
 			#os.system("systemctl status docker")
 		elif docker == 2:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x= systemctl start docker")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl start docker")
 			#os.system("systemctl start docker")
 		elif docker == 3:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x= systemctl stop docker")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl stop docker")
 			#os.system("systemctl stop docker")
 		elif docker == 4:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=sudo docker images")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x= sudo docker images")
 			#os.system("docker images")
 		elif docker == 5:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=sudo docker ps -a")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=sudo docker ps -a")
 			#os.system("docker ps -a")
 		elif docker == 6:
 			con_name=input("Enter the container name")
 			os.system("docker rm -f "+ con_name)
 		elif docker == 7:
 			doc_image=input("Enter the name of Image you want to delete")
 			os.system("docker rm -f " + doc_image)
 		elif docker == 8:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker rm -f $(docker container ls -a -q)")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker rm -f $(docker container ls -a -q)")
 			#os.system("docker rm -f $(docker container ls -a -q)")
 		elif docker == 9:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker run -dit -p 4444:80 --name menu-web vimal13/apache-webserver")
 			#os.system("banner container")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=banner container")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=docker run -dit -p 4444:80 --name menu-web vimal13/apache-webserver")
 			#os.system("docker run -dit -p 4444:80 --name menu-web vimal13/apache-webserver")
 		elif docker == 10:
 			con_name=input("Enter the container name")
 		elif docker == 11:
 			break
 		else:
 			print("Press Choice is not Use full")
 elif p== 2:
 	while True:
 		os.system("banner Kubernetes")
 		print("""
 			Press 1: Check the status of Minikube............
 			Press 2: Start minikube................
 			Press 3: Stop minikube Cluster.............
 			press 4: Show all pods.......
 			press 5: Show all runnig Deployments
 			press 6: Show all replica set......
 			press 7: Show all the services
 			press 8: Exit
 			""")
 		kube=int(input())
 		if kube == 1:
 			#os.system("minikube status")
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube status")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube status")
 		elif kube == 2:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube start --driver=none")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube start --driver=none")
 			#os.system("minikube start --driver=none")
 		elif kube == 3:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube stop")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minikube stop")
 			#os.system("minikube stop")
 		elif kube == 4:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get pods")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get pods")
 			#os.system("kubectl get pods")
 		elif kube == 5:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get deployment")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get deployment")
 			#os.system("kubectl get deployment")
 		elif kube == 6:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get rc")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get rc")
 			#os.system("kubectl get rc")
 		elif kube == 7:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get svc")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=kubectl get svc")
 			#os.system("kubectl get svc")
 		elif kube == 8:
 			break
 		else:
 			print("Press Choice is not use full")
 elif p == 3:
 	while True:
 		os.system("banner Git")
 		print("""
 			press 1: Create a directroy...........
 			press 2: Show created directory........
 			press 3: Change the diretory..........
 			press 4: Intialize the repository.......
 			press 5: Create a file
 			press 6: Add the files..............
 			press 7: Commit the repository........
 			press 8: Push the repository on github..........
 			press 9: Exit..............
 			""")
 		g_i_t=int(input())
 		if g_i_t == 1:
 			d_i_r=input("Enter the Directory Name: ")
 			os.system(" mkdir "+ d_i_r)
 		elif g_i_t == 2:
 			os.system("ls")
 		elif g_i_t == 3:
 			c_d=input("Enter the directory name to change: ")
 			os.chdir(c_d)
 		elif g_i_t == 4:
 			os.system("git init")
 		elif g_i_t == 5:
 			file=input("Enter the files name:")
 			os.system(" gedit "+ file)
 		elif g_i_t == 6:
 			os.system(" git add . ")
 		elif g_i_t == 7:
 			com_mit=input("Enter the commit message: ")
 			os.system("git commit -m " + com_mit)
 		elif g_i_t == 8:
 			os.system(" git push -u origin master ")
 		elif g_i_t == 9:
 			break
 		else:
 			print("Choice is not use full........")
 elif p == 4:
 	while True:
 		os.system("banner Ansible")
	 	print("""
	 			press 1: Add Inventory
	 			press 2: Installation of Ansible...............
	 			press 3: Check the Ansible Install or not ...........
	 			press 4: Check How many host are presents.............
	 			press 5: Ping all the Target node................
	 			press 6: Run any command using ansible in the local systems...............
	 			press 7: configure servers................
	 			press 8: Exit.............
	 			""")
	 	ans=int(input())
	 	if ans == 1:
	 		ip_address=str(input("Enter the IP adress: "))
	 		user_name=str(input("Enter the User name: "))
	 		pass_word=getpass.getpass("Enter the passwords: ")
	 		inventory(ip_address,user_name,pass_word)
	 	elif ans == 2:
	 		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=pip3 install ansible")
	 		#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=pip3 install ansible")
	 		#os.system("pip3 install ansible")
	 	elif ans == 3:
	 		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible --version")
	 		#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible --version")
	 		#os.system("ansible --version")
	 	elif ans == 4:
	 		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible all --list-hosts")
	 		#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible all --list-hosts")
	 		#os.system("ansible all --list-hosts")
	 	elif ans == 5:
	 		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible all -m ping")
	 		#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible all -m ping")
	 		#os.system("ansible all -m ping")
	 	elif ans == 6:
	 		cmd=input("Enter the command to run on local systems.....")
	 		#os.system("ansible localhost -a " + cmd )
	 	elif ans == 7:
	 		os.system("banner CM")
	 		while True:
	 			print("""
	 				Press 1: Configure Webserver cluster.........
	 				press 2: Configure Hadoop DataNode...
	 				press 3: Configure yum............
	 				press 4: Update webconfigure file and
	 				press 5: Configure Jenkins server..........
	 				press 6: Exit
	 				""")
	 			con_man=int(input())
	 			if con_man == 1:
	 				#os.system("banner webserver")
	 				webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible-playbook /root/python-specilist/Menu-Program-WebBrowser/ansible/configure-web-server/webserver.yml")
	 				#os.system("ansible-playbook /root/python-specilist/Menu-Program/ansible/configure-web-server/webserver.yml")
	 			elif con_man == 2:
	 				os.system("banner DataNode")
	 				webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible-playbook /root/python-specilist/Menu-Program-WebBrowser/ansible/hadoop-configure/hadoop-con.yml")
	 				#os.system("ansible-playbook /root/python-specilist/Menu-Program/ansible/hadoop-configure/hadoop-con.yml")
	 			elif con_man == 3:
	 				os.system("banner YUM")
	 				#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible all -m pin")
	 				#os.system()
	 			elif con_man == 4:
	 				webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible-playbook /root/python-specilist/Menu-Program-WebBrowser/ansible/web_conf_update/web-update.yml")
	 				#os.system("ansible-playbook /root/python-specilist/Menu-Program/ansible/web_conf_update/web-update.yml")
	 			elif con_man == 5:
	 				webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ansible-playbook /root/python-specilist/Menu-Program-WebBrowser/ansible/jenkins_conf/jenkins_conf.yml")
	 				#os.system("ansible-playbook /root/python-specilist/Menu-Program/ansible/jenkins_conf/jenkins_conf.yml")
	 			elif con_man == 6:
	 				break
	 			else:
	 				print("Press key is not use full.........")
	 	elif ans ==8:
	 		break
	 	else:
	 		print("Press is not use full")
 elif p == 5:
 	while True:
 		os.system("banner Hadoop Cluster")
 		print("""
 			press 1: Master Node 
 			press 2: Name Node
 			press 3: Exit
 			""")
 		had_oop=int(input())
 		if had_oop == 1:
 			while True:
 				os.system("banner Master Node")
 				print("""
 					press 1: Start Hadoop Master node..........
 					press 2: Stop Data node..........
 					press 3: Show all share storage.........
 					press 4: Show Data node start or not.......
 					press 5: Exit
 					""")
 				mas_ter_node=int(input())
 				if mas_ter_node== 1:
 					webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=hadoop-daemon.sh start datanode")
 					#os.system("hadoop-daemon.sh start datanode")
 				elif mas_ter_node == 2:
 					webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=hadoop-daemon.sh stop datanode")
 					#os.system("hadoop-daemon.sh stop datanode")
 				elif mas_ter_node == 3:
 					webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=hadoop dfsadmin -report")
 					#os.system("hadoop dfsadmin -report")
 				elif mas_ter_node == 4:
 					webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=jps")
 					#os.system("jps")
 				elif mas_ter_node == 5:
 					break
 				else:
 					print("Choie is not use full")
 		elif had_oop == 2:
 			os.system("banner DataNode")
 		elif had_oop == 3:
 			break
 		else:
 			print("Press choice is not use full")
 elif p == 6:
 	while True:
 		os.system("banner Openshift")
 		print("""
	 		press 1: Check the Status of Minishift.............
	 		press 2: Start the Minishift single node cluster...............
	 		press 3: Stop the Minishift single node cluster............
	 		press 4: Find the web url of Minishift console..............
	 		press 5: Openshift Client(OC)............
	 		press 6: Exit...........
 		""")
 		open_shift=int(input())
 		if open_shift == 1:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift status")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift status")
 			#os.system("minishift status")
 		elif open_shift == 2:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift start")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift start")
 			#os.system("minishift start")
 		elif open_shift == 3:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift stop")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift stop")
 			#os.system("minishift stop")
 		elif open_shift == 4:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift console --url")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift console --url")
 			#os.system("minishift console --url")
 		elif open_shift == 5:
 			os.system("banner OC")
 			while True:
 				print("""
 					press 1: Find the Path of Openshift Client.....
 					press 2: Find the Url of minishift console..... 
 					press 3: Login with Oc commands.......
 					press 4: Exit
 					""")
 				oc=int(input())
 				if oc == 1:
 					os.system(" minishift oc-env")
 				elif oc == 2:
 					os.system(" minishift console --url")
 				elif oc == 3:
 					login=input("Enter the minishift url to connect with oc login: ")
 					os.system("oc login " + login + " -u system:admin ")
 					while True:
 						os.system("banner Login")
 						print("""
 							press 1: Create new project
 							press 2: Show all the created projects
 							press 3: Add gitHub Url with oc project
 							press 4: Get Pods...
 							press 5: Get Deployments..
 							press 6: Get services.......
 							press 7: Get Build configure
 							press 8: Describe the Openshift pods.
 							press 9: Get Persistent Volumes......
 							press 10: Get Secrets.....
 							press 11: Get Route.........
 							press 12: Exit
 							""")
 						oc_login=int(input())
 						if oc_login == 1:
 							new_project=input("Enter the New Project Name: ")
 							os.system(" oc new-project " + new_project )
 						elif oc_login == 2:
 							os.system(" oc get projects ")
 						elif oc_login == 3:
 							gitHub=input("Enter the GitHub Url........")
 							os.system(" oc new-app " + gitHub)
 						elif oc_login == 4:
 							os.system(" oc get pods")
 						elif oc_login == 5:
 							os.system(" oc get deployments")
 						elif oc_login == 6:
 							os.system(" oc get svc")
 						elif oc_login == 7:
 							os.system("oc get bc")
 						elif oc_login == 8:
 							oc_des=input("Enter the Openshift Pods name: ")
 							os.system("oc describe pods " + oc_des)
 						elif oc_login == 9:
 							os.system("oc get pvc")
 						elif oc_login == 10:
 							os.system("oc get svc")
 						elif oc_login == 11:
 							os.system(" oc get route ")
 						elif oc_login == 12:
 							break
 						else:
 							print("Press key is not Use full")
 				elif oc == 4:
 					break
 				else:
 					print("Press key is not use full...")
 		elif open_shift == 6:
 			break
 		else:
 			print("Choice is not use full")
 elif p == 7:
 	while True:
 		os.system("banner Partition")
	 	print("""
				press 1: Physical Partition
				press 2: Logical Partition
				press 3: Exit
			""")
	 	partition=int(input())
	 	if partition == 1:
	 		while True:
		 		print("""
		 				press 1: Show All Partition
		 				press 2: Show all mount Partition
		 				press 3: Acess new Partition and craete partion
		 				press 4: Format the partition
		 				press 5: Create Directory
		 				press 6: Mount the Partition
		 				press 7: Exit
		 			""")
		 		phy=int(input())
		 		if phy == 1:
		 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=fdisk -l")
		 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift status")
		 			#os.system("fdisk -l")
		 		elif phy == 2:
		 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=df -h")
		 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=minishift status")
		 			#os.system("df -h")
		 		elif phy == 3:
		 			cmd=input("Enter the New Partition name: ")
		 			os.system(" fdisk " + cmd )
		 		elif phy == 4:
		 			Format=input("Enter the Format Partition name: ")
		 			os.system(" mkfs.ext4 "  + Format)
		 		elif phy == 5:
		 			dir_name=input("Enter the directory name: ")
		 			os.system(" mkdir " + dir_name)
		 		elif phy == 6:
		 			partition=input("Enter the New Partition name: ")
		 			dir_name=input("Enter the directory name: ")
		 			os.system(" mount " + partition + dir_name)
		 		elif phy == 7:
		 			break
		 		else:
		 			print("Press key is not use full")

	 	elif partition == 2:
	 		while True:
		 		print("""
		 				press 1: Show All Partition
		 				press 2: Show all mount Partition
		 				press 3: Physial volume
		 				press 4: Volume Group
		 				press 5: Logical Volumes
		 				press 6: Exit
		 			""")
		 		lvm =int(input())
		 		if lvm == 1:
		 			os.system("fdisk -l")
		 		elif lvm == 2:
		 			os.system("df -h")
		 		elif lvm == 3:
		 			while True:
		 				print("""
		 					press 1: Create a Physical Partitions
		 					press 2: Show All Physial Partitions
		 					press 3: Show craeted physical Partitions created or not
		 					press 4: Exit
		 					""")
		 				php=int(input())
		 				if php == 1:
		 					partition=input("Enter the partiton name to create Physical Partitions")
		 					os.system("pvcreate" + partition )
		 				elif php == 2:
		 					os.system("pvdisplay")
		 				elif php == 3:
		 					partition=input("Enter the create Partion to show Physical partition created or not")
		 					os.system("pvdisplay" + partition)
		 				elif php == 4:
		 					break
		 				else:
		 					print("Press choice is not use full")
		 		elif lvm == 4:
		 			while True:
			 			print("""
			 					press 1: Create a Vloume Groups
			 					press 2: Show All Volume Groups
			 					press 3: Mount Volume groups with Physical Volumes
			 					press 4: Extend the Volume Groups
			 					press 5: Exit
			 					""")
			 			vg=int(input())
			 			if vg == 1:
			 				partition=input("Enter Name to create Volume Group")
			 				os.system("vgcreate " + partition )
			 			elif vg == 2:
			 				os.system("vgdisplay")
			 			elif vg == 3:
			 				partition=input("Enter the Volume Groups")
			 				volum1=input("Enter the Physical volume mount with Volume Groups")
			 				os.system("vgcreate" + partition + volum1)
			 			elif vg == 4:
			 				partition=input("Enter the partiton extend the size of Volume Groups") 
			 				vg_group=input("Enter the name Volume Group")
			 				os.system("vgextend"+ vg + partition) 
			 			elif vg == 5:
			 				break
			 			else:
			 				print("Press choice is not use full")
		 		elif lvm == 5:
		 			while True:
			 			print("""
			 				Press 1: Show Logial Volumes.....
			 				Press 2: Create Logical volumes with Volume Groups....
			 				Press 3: Format the partitions.....
			 				Press 4: Create directory
			 				Press 5: Mount the direcotry with LVM partitions..........
			 				Press 6: Extend The LVM partitions..........
			 				Press 7: Resize the LVM extend partitions...........
			 				Press 8: Exit
			 				""")
			 			log=int(input())
			 			if log == 1:
			 				os.system("lvdisplay")
			 			elif log == 2:
			 				size=int(input("Enter the size of partion you want to use reate lvm partion"))
			 				partiton=input("Enter the LVM partition name")
			 				vg=input("Enter the volume group")
			 				os.system("lvcreate --size" +size+"G --name "+ partition + vg)
			 			elif log == 3:
			 				partition=input("Enter the lvmpartion name")
			 				os.system(" mkfs.ext4 "+partition)
			 			elif log == 4:
			 				partition=int(input("Enter the name Create Directory"))
			 				os.system("mkdir"+partition)
			 			elif log == 5:
			 				partition=input("Enter the LVM Partition Name")
			 				dir_name=input("Enter the directory name")
			 				os.system("mount"+ partition + dir_name)
			 			elif log == 6:
			 				size=int(input("Enter the size of partion you want to use reate lvm partion"))
			 				partiton=input("Enter the LVM partition name")
			 				os.system("lvextend --size"+"+"+size+"G"+ partition)
			 			elif log == 7:
			 				partition=input("Enter the partitions of resize extends partition")
			 				os.system("resize2fs"+ partition)
			 			elif log == 8:
			 				break
			 			else:
			 				print("Press choice is not use full")
		 		elif lvm == 6:
		 			break
		 		else:
		 			print("Press choie is not use full")
	 	elif partition == 3:
	 		break
	 	else:
	 		print("Press choice is not use full")

 elif p == 8:
 	while True:
 		os.system("banner Jenkins")
 		print("""
 			Press 1: Check Jenkins Install or not My system.....
 			Press 2: Check jenkins activate run or not..........
 			Press 3: Stop Jenkins..........
 			Press 4: Start Jenkins.........
 			Press 5: Exit
 			""")
 		jen=int(input())
 		if jen == 1:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=rpm -q jenkins")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=rpm -q jenkins")
 			#os.system("rpm -q jenkins")
 		elif jen == 2:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl status jenkins")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl status jenkins")
 			#os.system(" systemctl status jenkins")
 		elif jen == 3:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl stop jenkins")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl stop jenkins")
 			#os.system(" Systemctl stop jenkins")
 		elif jen == 4:
 			webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl start jenkins")
 			#webbrowser.open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=systemctl start jenkins")
 			#os.system(" systemctl start jenkins")
 		elif jen == 5:
 			break
 		else:
 			print("Press is not use full")
 elif p == 9:
 	exit()
 else:
 	print("Press choice is not use-full")