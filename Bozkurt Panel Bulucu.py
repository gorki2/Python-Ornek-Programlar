import requests
                                                                                              
panellinkleri = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','siteadmin/login.htm','admin/account.html','admin/account.htm','admin/index.html','admin/index.htm','admin/login.html','admin/login.htm','admin/admin.html','admin/admin.htm',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/login.htm','admin_area/index.html','admin_area/index.htm','admin/controlpanel.php','admin.php','admincp/index.php','admincp/login.php','admincp/index.html','admincp/index.htm','admin/account.html','admin/account.htm','adminpanel.html','adminpanel.htm','webadmin.html','webadmin.htm',
'webadmin/index.html','webadmin/index.htm','webadmin/admin.html','webadmin/admin.htm','webadmin/login.html','webadmin/login.htm','admin/admin_login.html','admin/admin_login.htm','admin_login.html','admin_login.htm','panel-administracion/login.html','panel-administracion/login.htm',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','admin_area/admin.htm','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/index.htm','bb-admin/login.html','bb-admin/login.htm','acceso.php','bb-admin/admin.html','bb-admin/admin.htm','admin/home.html','admin/home.htm','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','pages/admin/admin-login.htm','admin/admin-login.html','admin/admin-login.htm','admin-login.html','admin-login.htm','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','admin/adminLogin.htm','adminLogin.html','adminLogin.htm','admin/adminLogin.html','admin/adminLogin.htm','home.html','home.htm','rcjakar/admin/login.php','adminarea/index.html','adminarea/index.htm','adminarea/admin.html','adminarea/admin.htm',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin/controlpanel.htm','administrator/controlpanel.php','administrator/controlpanel.html','administrator/controlpanel.htm','admin.html','admin.htm','admin/cp.html','admin/cp.htm','cp.html','cp.html','adminpanel.php','moderator.html','moderator.htm',
'administrator/index.html','administrator/index.htm','administrator/login.html','administrator/login.htm','user.html','user.htm','administrator/account.html','administrator/account.htm','administrator.html','administrator.htm','login.html','login.htm','modelsearch/login.html','modelsearch/login.htm',
'moderator/login.html','moderator/login.htm','adminarea/login.html','adminarea/login.htm','panel-administracion/index.html','panel-administracion/index.htm','panel-administracion/admin.html','panel-administracion/admin.htm','modelsearch/index.html','modelsearch/index.htm','modelsearch/admin.html','modelsearch/admin.htm',
'admincontrol/login.html','admincontrol/login.htm','adm/index.html','adm/index.htm','adm.html','adm.htm','moderator/admin.html','moderator/admin.htm','moderator/admin.htm','user.php','account.html','account.htm','controlpanel.html','controlpanel.htm','admincontrol.html','admincontrol.htm',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','kpanel/','cpadmin.php','admin/cpadmin.php','administrator/cpadmin.php','adminpage/cpadmin.php','admin-page/cpadmin.php','user/cpadmin.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','secur-login.php','wp-admin/','administrator/login.html','login/','log-in.php','member.php','cpmember.php','cp-member.php','member.html','cpmember.html','cp-member.html','member.htm','cpmember.htm',
'cp-member.htm','sign_in.php','sign-in.php','signin.php','accounts.php','relogin.php','check.php','blog/wp-login.php','processlogin.php','checklogin.php','checkuser.php','checkadmin.php','isadmin.php','authenticate.php','authentication.php','auth.php','authuser.php','authadmin.php','fileadmin.php','sysadmin.php','yonetim.php','yonetici.php','ur-admin.php','administr8.php','websiteadmin.php','admins.php','pages/administrator/admin-login.php','pages/administrator/admin.php','pages/administrator/login.php','pages/admin/login.php','pages/admin/admin.php','admincp/admin-login.php',
'vorod.php','voroud.php','vorud.php','join.php','admincp/join.php','admin/join.php','administrator/join.php','webmaster.php','autologin.php','userlogin.php','userjoin.php','user-login.php','admincp/user-login.php','admin-cp/user-login.php','administrator/user-login.php','admincp/user-join.php','admin-cp/user-join.php','administrator/user-join.php','cmsadmin.php','yonetici.php','cgi-bin/login.php','login1.php','login_admin.php','login_out/','login_out.php','login_user.php','loginsuper.php','super1.php','super_index.php','super_login.php','super_join.php','supermanager.php','superman.php','superuser.php','supervise/Login.php','letmein.php','superuser.php','sysadm.php','access.php',
'mn-admin/index.php','mn-admin/login.php','mn-admin/admin.php','security/','admini/','letmein','admin_user/','admin_users','0admin/login.php','0manager/admin.php','a_main.php','aaa.php','aadmin/','abc/','acct/login.php','d_admin/admin_login.php',
'ad_login/','ad_login.php','add_admin/','add_user/','addfile.php','addmember/','addmember.php','adduser/','adduser.php','admanage/','adminpro/','adminmember.php','adminmember/','admins/','adsystem/index.php','adsystem/login.php','adsystem/admin.php','myadmin/','myadmin/login.php','myadmin/admin.php','my-admin/','my-admin/admin.php','my-admin/login.php','yonetim.php','indy_admin/','liveUser_admin/','lotus_domino_admin/','p/w/','psuser/','personal/','accounts/',
'acesso/','acesso.php','banneradmin/','cadmins/','ccms/','ccms/index.php','ccms/login.php','ccp14admin/','cms/','config/','configuration/','configure/','customer_login/','dir-login/','directadmin/','donos/','edit/','ezsqliteadmin/','fileadmin/','formslogin/','funcoes/','globes_admin/','hpwebjetadmin/','irc-macadmin/','joomla/administrator/','login-us/','login-redirect/','macadmin/','maintenance/','manage/','management.php',
'manager/','manuallogin/','members/','members.php','membro/','membros/','memlogin/','meta_login/','modcp/','navsiteadmin/','newsadmin/','newsadmin.php','news-admin/','news-admin.php','funadmin/','fun-admin/','funadmin.php/','fun-admin.php','nsw/admin/login.php','openvpnadmin/','painel/','panelc/','paneldecontrol/','passe/','password/','pgadmin/','php/','phpsqliteadmin/','phpldapadmin/','platz_login/','power_user/',
'processlogin/','project-admins/','pureadmin/','radmind-1/','raiz/','rcLogin/','registration/','root/','root/login.php','root/admin.php','roots/','roots/admin.php','roots/login.php','saff/','secret/','secrets/','secure/','senha/','senhas/','server_admin_small/','showlogin/','sff/','simplelogin/','sistema/','siteadmin/login.php','siteadmin/admin.php','smblogin/','sql-admin/','ss_vms_admin_sm/','sshadmin/','staradmin/','sub-login/','superman/','administrator/?h','GeneratedItems/','sw/','dynpoll/admin/','mailer/admin/',
'newposts/']

print(" ____           _               _     _____                 _   ____        _                  ")
print("|  _ \         | |             | |   |  __ \               | | |  _ \      | |                ") 
print("| |_) | ___ ___| | ___   _ _ __| |_  | |__) |_ _ _ __   ___| | | |_) |_   _| |_   _  ___ _   _ ")
print("|  _ < / _ \_  / |/ / | | | '__| __| |  ___/ _` | '_ \ / _ \ | |  _ <| | | | | | | |/ __| | | |")
print("| |_) | (_) / /|   <| |_| | |  | |_  | |  | (_| | | | |  __/ | | |_) | |_| | | |_| | (__| |_| |")
print("|____/ \___/___|_|\_\\__,_|_|   \__| |_|   \__,_|_| |_|\___|_| |____/ \__,_|_|\__,_|\___|\__,_|")
print("")
link = input("Başında http:// ve sonunda / olmalı Link Girin: ")
print("")
for i in panellinkleri:
   req = requests.get(link + i)

   if req.status_code == 200:
   	  print( req.url + " Admin Paneli Bulundu!")

   else:
   	 print( req.url + " Panel Bulunamadı!")
