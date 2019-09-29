import datetime
import random
import sqlite3 as sql

conn = sql.connect('database.db')

conn.execute("CREATE TABLE register ( \
    user_id TEXT, \
    password    TEXT, \
    PRIMARY KEY(user_id)  \
);")

conn.execute("CREATE TABLE login ( \
    user_id TEXT, \
    password    TEXT, \
    PRIMARY KEY(user_id)  \
);")

conn.execute("CREATE TABLE cate ( \
    category    TEXT, \
    num INT, \
    PRIMARY KEY(category)  \
);")
conn.execute("CREATE TABLE upload ( \
             category TEXT NOT NULL,\
             act_id int ,\
             username TEXT NOT NULL,\
             cap TEXT NOT NULL,\
             upvotes  int ,\
             time_stamp TEXT NOT NULL,\
             imgB64 TEXT NOT NULL\
);")


cate_insertion=[
"INSERT INTO cate values ('Petlove',31);",
"INSERT INTO cate values ('Env Conservation',13);",
"INSERT INTO cate values ('Humanitarian Acts',53);",
"INSERT INTO cate values ('Natural Resource Conservation',45);"]

for i in cate_insertion:
    conn.execute(i)
    conn.commit()

r_insertion=[
"INSERT INTO register values ('abc','123');"
]
for i in r_insertion:
    conn.execute(i)
    conn.commit()

u_insertion=[
"INSERT INTO upload values        ('Env Conservation',4429,'wibgy','zdsejuxccp',46,'wicep','zi29c3gj');",
"INSERT INTO upload values        ('Natural Resource Conservation',32,'qathw','drfwuijsqz',83,'qaswz','da06s7hu');",
"INSERT INTO upload values        ('Humanitarian Acts',118,'qutyn','zrrcxdmqlz',132,'quqcz','zu08q2yx');",
"INSERT INTO upload values        ('Humanitarian Acts',4451,'woafw','lkuryydizt',5,'woirt','lo11i@fy');",
"INSERT INTO upload values        ('Env Conservation',2039,'syorv','wojsmrhufk',29,'syusk','wy50u6rm');",
"INSERT INTO upload values        ('Env Conservation',1036,'aeldv','glzkasdmrc',8,'aemkc','ge2@m8da');",
"INSERT INTO upload values        ('Humanitarian Acts',1344,'sjppe','jrazjskkjo',111,'sjkzo','jj61k0pj');",
"INSERT INTO upload values        ('Petlove',736,'xgbsc','qvnjszepkj',195,'xgpjj','qg24p1ss');",
"INSERT INTO upload values        ('Petlove',4261,'izucl','atuwgzanpt',93,'iznwt','az11n6cg');",
"INSERT INTO upload values        ('Humanitarian Acts',761,'ixnmc','lokvrjdnmz',18,'ixnvz','lx41n3mr');",
"INSERT INTO upload values        ('Natural Resource Conservation',1755,'amvdo','ohjgygonwy',82,'amngy','om30n5dy');",
"INSERT INTO upload values        ('Petlove',1586,'iogdg','ctgaafhdcx',93,'iodax','co77d3da');",
"INSERT INTO upload values        ('Env Conservation',1788,'pslpq','pwuxjrypeu',157,'pspxu','ps21p5pj');",
"INSERT INTO upload values        ('Petlove',2253,'uhbzm','zypmubneth',128,'uhemh','zh26e0zu');",
"INSERT INTO upload values        ('Env Conservation',1542,'uoipm','xktlddtjgs',159,'uojls','xo90j7pd');",
"INSERT INTO upload values        ('Natural Resource Conservation',1312,'clzyg','jrqacrhckm',126,'clcam','jl@7c1yc');",
"INSERT INTO upload values        ('Natural Resource Conservation',2588,'himzu','rqpsssyind',163,'hiisd','ri36i4zs');",
"INSERT INTO upload values        ('Petlove',4647,'tixqq','fihfjkpkio',115,'tikfo','fi78k9qj');",
"INSERT INTO upload values        ('Natural Resource Conservation',1738,'tlizu','dhfhfhwoes',167,'tlohs','dl96o5zf');",
"INSERT INTO upload values        ('Natural Resource Conservation',4288,'ljwum','latjltqcix',116,'ljcjx','lj50c9ul');",
"INSERT INTO upload values        ('Natural Resource Conservation',60,'yhwkx','enoxwvdmrp',53,'yhmxp','eh55m8kw');",
"INSERT INTO upload values        ('Humanitarian Acts',3361,'glqnf','hcrutbczzd',114,'glzud','hl78z@nt');",
"INSERT INTO upload values        ('Env Conservation',4599,'bywqg','tejonyvvar',40,'byvor','ty50v1qn');",
"INSERT INTO upload values        ('Env Conservation',3076,'ldvyv','owjtgmwfsq',154,'ldftq','od30f9yg');",
"INSERT INTO upload values        ('Petlove',4913,'mvndf','fyorpyqxoe',155,'mvxre','fv45x5dp');",
"INSERT INTO upload values        ('Natural Resource Conservation',1849,'vfoco','ewofpphmgm',30,'vfmfm','ef55m7cp');",
"INSERT INTO upload values        ('Env Conservation',85,'stazz','zwsknrjzwj',125,'stzkj','zt19z5zn');",
"INSERT INTO upload values        ('Humanitarian Acts',597,'ixqzz','hzhgttmvej',113,'ixvgj','hx78v5zt');",
"INSERT INTO upload values        ('Natural Resource Conservation',375,'yykrg','umivqqixyx',8,'yyxvx','uy19x9rq');",
"INSERT INTO upload values        ('Env Conservation',2513,'rtcru','tbafrfncnk',168,'rtcfk','tt31c4rr');",
"INSERT INTO upload values        ('Humanitarian Acts',4266,'uoprw','ouhombswxc',104,'uowoc','oo68w7rm');",
"INSERT INTO upload values        ('Petlove',1912,'onzau','txahtjbvti',196,'onvhi','tn@1v0at');",
"INSERT INTO upload values        ('Env Conservation',3965,'fxjtn','piwjmjmsov',180,'fxsjv','px05s5tm');",
"INSERT INTO upload values        ('Petlove',372,'gnhum','jkbfwfncgb',88,'gncfb','jn82c7uw');",
"INSERT INTO upload values        ('Petlove',4275,'cfgdn','gcuyyromoo',153,'cfmyo','gf71m5dy');",
"INSERT INTO upload values        ('Natural Resource Conservation',2045,'ncfob','vmjqaltnay',185,'ncnqy','vc60n1oa');",
"INSERT INTO upload values        ('Natural Resource Conservation',4079,'gndkp','atkezmzjyf',59,'gnjef','an41j9kz');",
"INSERT INTO upload values        ('Env Conservation',4093,'cvqpw','jkmxzbfsrp',184,'cvsxp','jv73s8pz');",
"INSERT INTO upload values        ('Natural Resource Conservation',1925,'lrpsm','qzzmkohlkt',144,'lrlmt','qr6@l1sk');",
"INSERT INTO upload values        ('Humanitarian Acts',142,'rmgto','vlkfmrsjtr',166,'rmjfr','vm71j0tm');",
"INSERT INTO upload values        ('Petlove',4460,'dzvap','bpgwitxmcb',77,'dzmwb','bz37m3ai');",
"INSERT INTO upload values        ('Natural Resource Conservation',4858,'qkkdi','oqeduzgwyd',60,'qkwdd','ok15w9du');",
"INSERT INTO upload values        ('Natural Resource Conservation',3504,'bhfes','amzezclvth',63,'bhveh','ah6@v0ez');",
"INSERT INTO upload values        ('Humanitarian Acts',410,'xtkgp','zlaxxxpblz',91,'xtbxz','zt11b2gx');",
"INSERT INTO upload values        ('Humanitarian Acts',2966,'dgcfz','lflgxfchac',1,'dghgc','lg32h1fx');",
"INSERT INTO upload values        ('Env Conservation',936,'kbwfk','ufdsfxcdkm',57,'kbdsm','ub54d1ff');",
"INSERT INTO upload values        ('Petlove',608,'fjgex','ktyriiedfh',37,'fjdrh','kj79d6ei');",
"INSERT INTO upload values        ('Petlove',881,'dbnin','qsgofnedep',136,'dbdop','qb47d5if');",
"INSERT INTO upload values        ('Natural Resource Conservation',2044,'mfygc','lipyrbpdsp',177,'mfdyp','lf96d9gr');",
"INSERT INTO upload values        ('Humanitarian Acts',2801,'qfeqa','juhnqhamln',42,'qfmnn','jf58m2qq');",
"INSERT INTO upload values        ('Petlove',1985,'bknpe','rpbsecxqeq',38,'bkqsq','rk42q5pe');",
"INSERT INTO upload values        ('Natural Resource Conservation',3579,'ooilf','gysieuazcd',102,'oozid','go99z3le');",
"INSERT INTO upload values        ('Env Conservation',2105,'trygs','dqlkvdzjce',116,'trjke','dr92j3gv');",
"INSERT INTO upload values        ('Env Conservation',2950,'nsxri','pxilrogwgn',135,'nswln','ps79w7rr');",
"INSERT INTO upload values        ('Natural Resource Conservation',1343,'etzaj','lotnrzfzpy',46,'etzny','lt@0z6ar');",
"INSERT INTO upload values        ('Petlove',237,'buyht','ruzwclovhz',173,'buvwz','ru9@v8hc');",
"INSERT INTO upload values        ('Env Conservation',2131,'zdlkf','odvteqdtsa',114,'zdtta','od23t9ke');",
"INSERT INTO upload values        ('Humanitarian Acts',2542,'jevcy','fpzscozlnq',190,'jelsq','fe3@l4cc');",
"INSERT INTO upload values        ('Natural Resource Conservation',3785,'swtoi','vcemifxfyf',199,'swfmf','vw05f9oi');",
"INSERT INTO upload values        ('Petlove',361,'oeahg','vmkeafbytq',168,'oeyeq','ve11y0ha');",
"INSERT INTO upload values        ('Petlove',4825,'dtrbl','fyyidbhtiu',191,'dttiu','ft89t9bd');",
"INSERT INTO upload values        ('Env Conservation',4554,'mqixe','vhwavtzmkd',25,'mqmad','vq95m1xv');",
"INSERT INTO upload values        ('Natural Resource Conservation',2998,'ihddm','uusrgaftca',172,'ihtra','uh49t3dg');",
"INSERT INTO upload values        ('Natural Resource Conservation',1239,'stkqs','yzwjdfdivj',52,'stijj','yt15i3qd');",
"INSERT INTO upload values        ('Env Conservation',1788,'fpuan','nobymobqtw',17,'fpqyw','np12q0am');",
"INSERT INTO upload values        ('Petlove',1106,'uedfd','wlgvnfjwyw',126,'uewvw','we47w9fn');",
"INSERT INTO upload values        ('Natural Resource Conservation',1441,'ukngl','etkamxlnwn',105,'uknan','ek41n5gm');",
"INSERT INTO upload values        ('Humanitarian Acts',1442,'vsqcl','nsyveweedm',115,'vsevm','ns79e4ce');",
"INSERT INTO upload values        ('Env Conservation',86,'htnjj','tkcnorsqdz',70,'htqnz','tt43q4jo');",
"INSERT INTO upload values        ('Humanitarian Acts',2142,'mmurp','afvelmyzsr',74,'mmzer','am13z9rl');",
"INSERT INTO upload values        ('Natural Resource Conservation',1936,'awgao','vvjnlxlnpa',159,'awnna','vw70n6al');",
"INSERT INTO upload values        ('Env Conservation',2324,'fhjyt','itgfnnfmjm',2,'fhmfm','ih07m0yn');",
"INSERT INTO upload values        ('Env Conservation',3780,'jhbfh','tstbpdkggj',164,'jhgbj','th20g7fp');",
"INSERT INTO upload values        ('Humanitarian Acts',1042,'hfzmt','wpcxzaytsx',59,'hftxx','wf@3t9mz');",
"INSERT INTO upload values        ('Env Conservation',4139,'jgkaq','tzanayooko',97,'jgono','tg11o1aa');",
"INSERT INTO upload values        ('Natural Resource Conservation',3628,'xzvzc','hwjepyftiz',19,'xztez','hz30t9zp');",
"INSERT INTO upload values        ('Natural Resource Conservation',1781,'osyjt','wcqyuqarhr',195,'osryr','ws97r8ju');",
"INSERT INTO upload values        ('Humanitarian Acts',961,'nonoe','dfnwhehsjp',64,'noswp','do44s0oh');",
"INSERT INTO upload values        ('Humanitarian Acts',1878,'omcac','avjrqsfxrp',32,'omxrp','am30x8aq');",
"INSERT INTO upload values        ('Humanitarian Acts',324,'wjssg','mktryjomcw',47,'wjmrw','mj90m3sy');",
"INSERT INTO upload values        ('Natural Resource Conservation',395,'bhthr','vkfaqmzozs',144,'bhoas','vh06o@hq');",
"INSERT INTO upload values        ('Humanitarian Acts',304,'evnyg','girivuylfa',24,'evlia','gv48l6yv');",
"INSERT INTO upload values        ('Petlove',1521,'vvjrs','itbschxbem',37,'vvbsm','iv02b5rc');",
"INSERT INTO upload values        ('Natural Resource Conservation',289,'cjqky','cwasxzcggh',174,'cjgsh','cj71g7kx');",
"INSERT INTO upload values        ('Humanitarian Acts',1902,'ugrdw','xcxwolyphy',63,'ugpwy','xg87p8do');",
"INSERT INTO upload values        ('Petlove',2992,'bkygq','yjvntuvfuf',170,'bkfnf','yk93f1gt');",
"INSERT INTO upload values        ('Humanitarian Acts',1716,'tfwjw','kbrdfmjzfg',184,'tfzdg','kf58z6jf');",
"INSERT INTO upload values        ('Humanitarian Acts',3949,'ijtsw','flcfffbgbk',30,'ijgfk','fj03g2sf');",
"INSERT INTO upload values        ('Petlove',4948,'zrebk','wdulrjaagd',149,'zrald','wr51a7br');",
"INSERT INTO upload values        ('Env Conservation',1165,'epiia','gzcjkkksvc',110,'epsjc','gp93s3ik');",
"INSERT INTO upload values        ('Env Conservation',3526,'uuihu','lgpmlxnjhg',54,'uujmg','lu96j8hl');",
"INSERT INTO upload values        ('Env Conservation',3373,'jkvfd','hphzryauzg',183,'jkuzg','hk38u@fr');",
"INSERT INTO upload values        ('Petlove',2790,'wwsjp','bxcwdchznp',180,'wwzwp','bw93z4jd');",
"INSERT INTO upload values        ('Env Conservation',1035,'kpixh','kshayvecyi',55,'kpcai','kp98c9xy');",
"INSERT INTO upload values        ('Petlove',2480,'ofzcl','ychaxnrsyi',91,'ofsai','yf@8s9cx');",
"INSERT INTO upload values        ('Env Conservation',3529,'bjgfv','zzuzqfvvdg',90,'bjvzg','zj71v4fq');",
"INSERT INTO upload values        ('Env Conservation',69,'qqegb','moypxvyusv',134,'qqupv','mq59u9gx');",
"INSERT INTO upload values        ('Petlove',1284,'cekhh','qcuxmnlkak',10,'cekxk','qe11k1hm');",
"INSERT INTO upload values        ('Env Conservation',1999,'jzbzp','ncfwtffsnx',148,'jzswx','nz26s4zt');",
"INSERT INTO upload values        ('Env Conservation',827,'vbuov','mdnzixhcbs',155,'vbczs','mb14c2oi');",
"INSERT INTO upload values        ('Env Conservation',4693,'bghdb','opapzkafyl',139,'bgfpl','og81f9dz');",
"INSERT INTO upload values        ('Humanitarian Acts',2211,'mzqcf','rwjgjhpeeq',197,'mzegq','rz70e5cj');",
"INSERT INTO upload values        ('Humanitarian Acts',3429,'ewvvu','ehchfoqsta',87,'ewsha','ew33s0vf');",
"INSERT INTO upload values        ('Petlove',4218,'ilooi','ifzgztzzns',196,'ilzgs','il5@z4oz');",
"INSERT INTO upload values        ('Humanitarian Acts',2314,'nckuo','dxhikbfdkq',26,'ncdiq','dc18d1uk');",
"INSERT INTO upload values        ('Petlove',3005,'hmqus','efnzouormu',46,'hmrzu','em74r3uo');",
"INSERT INTO upload values        ('Natural Resource Conservation',206,'kdswk','gzwwbtvqdy',194,'kdqwy','gd95q4wb');",
"INSERT INTO upload values        ('Natural Resource Conservation',1091,'hecaw','inbkmszwfh',132,'hewkh','ie32w6am');",
"INSERT INTO upload values        ('Petlove',1742,'uunfo','ehpzxumjdh',149,'uujzh','eu46j4fx');",
"INSERT INTO upload values        ('Env Conservation',104,'chlva','wychhqhqlo',20,'chqho','wh23q2vh');",
"INSERT INTO upload values        ('Humanitarian Acts',4039,'omqdt','sddpdvvqmy',100,'omqpy','sm74q3dd');",
"INSERT INTO upload values        ('Natural Resource Conservation',3053,'nyaty','tffqnxkylp',56,'nyyqp','ty16y2tn');",
"INSERT INTO upload values        ('Env Conservation',1013,'eonbn','mkynjplkut',183,'eoknt','mo49k1bj');",
"INSERT INTO upload values        ('Petlove',568,'typex','unosjzznbh',167,'tynsh','uy65n2ej');",
"INSERT INTO upload values        ('Petlove',829,'xtlmr','krnbvpuorz',135,'xtobz','kt24o8mv');",
"INSERT INTO upload values        ('Humanitarian Acts',3622,'colyg','tdxzbxqlxn',101,'colzn','to27l7yb');",
"INSERT INTO upload values        ('Env Conservation',2831,'fever','wbmzuflron',74,'ferzn','we33r5eu');",
"INSERT INTO upload values        ('Petlove',2739,'ihwpw','brfdhclxvb',79,'ihxdb','bh56x3ph');",
"INSERT INTO upload values        ('Env Conservation',120,'acybe','pgxtfzlddd',121,'acdtd','pc97d4bf');",
"INSERT INTO upload values        ('Env Conservation',2868,'szsbs','rrsebukwvx',128,'szwex','rz99w3bb');",
"INSERT INTO upload values        ('Natural Resource Conservation',4283,'wfzdl','xgnnlxuwdt',127,'wfwnt','xf@4w4dl');",
"INSERT INTO upload values        ('Petlove',1367,'xdlnx','mhkxzxaxfq',33,'xdxxq','md21x6nz');",
"INSERT INTO upload values        ('Natural Resource Conservation',3732,'jkoen','rbodbsbbzj',32,'jkbdj','rk55b@eb');",
"INSERT INTO upload values        ('Humanitarian Acts',1905,'cgocu','ijipibyxmy',6,'cgxpy','ig59x3ci');",
"INSERT INTO upload values        ('Petlove',2066,'uaugu','nkkkfrqvgc',20,'uavkc','na11v7gf');",
"INSERT INTO upload values        ('Env Conservation',4854,'ggvvp','bjamqcjfto',193,'ggfmo','bg31f0vq');",
"INSERT INTO upload values        ('Natural Resource Conservation',4003,'rawgq','lgwyaakdmz',157,'radyz','la55d3ga');",
"INSERT INTO upload values        ('Env Conservation',4234,'sdmfa','oukhgisdhk',64,'sddhk','od31d8fg');",
"INSERT INTO upload values        ('Humanitarian Acts',550,'vyrme','tbyxawlizu',113,'vyixu','ty89i@ma');",
"INSERT INTO upload values        ('Natural Resource Conservation',1678,'qmmbj','ohlwtubvml',164,'qmvwl','om32v3bt');",
"INSERT INTO upload values        ('Env Conservation',1277,'shwlp','vrpmavmhkx',69,'shhmx','vh56h1la');",
"INSERT INTO upload values        ('Petlove',1907,'rbnfn','vdyyghjktb',187,'rbkyb','vb49k0fg');",
"INSERT INTO upload values        ('Env Conservation',4437,'jubng','ihcwpxbayj',142,'juawj','iu23a9np');",
"INSERT INTO upload values        ('Env Conservation',4401,'zhvjo','xazlfmdchj',199,'zhclj','xh3@c8jf');",
"INSERT INTO upload values        ('Env Conservation',4358,'rihpt','cnpwayuawh',28,'riawh','ci86a5pa');",
"INSERT INTO upload values        ('Natural Resource Conservation',1786,'btdeh','zrlvxytjvu',101,'btjvu','zt42j3ex');",
"INSERT INTO upload values        ('Natural Resource Conservation',2086,'qieex','dbuuocvpuf',82,'qipuf','di51p1eo');",
"INSERT INTO upload values        ('Natural Resource Conservation',4573,'ruezu','nponhdfsdb',111,'rusnb','nu55s4zh');",
"INSERT INTO upload values        ('Petlove',2371,'pbwgd','peoodlnmtv',163,'pbmov','pb55m0gd');",
"INSERT INTO upload values        ('Env Conservation',1352,'faftx','ikvyrddwnv',72,'fawyv','ia63w4tr');",
"INSERT INTO upload values        ('Humanitarian Acts',2115,'hqani','ndbstznlfa',59,'hqlsa','nq12l6nt');",
"INSERT INTO upload values        ('Petlove',2270,'rumhi','mcdlcecmbl',196,'rumll','mu34m2hc');",
"INSERT INTO upload values        ('Natural Resource Conservation',1902,'jjyiw','ydxerjprsd',187,'jjred','yj97r9ir');",
"INSERT INTO upload values        ('Petlove',246,'djizk','klcjcixbzd',179,'djbjd','kj93b@zc');",
"INSERT INTO upload values        ('Env Conservation',2555,'jmlom','fvulpspfee',152,'jmfle','fm21f5op');",
"INSERT INTO upload values        ('Humanitarian Acts',1214,'msflu','qzorefstmk',164,'mstrk','qs65t3le');",
"INSERT INTO upload values        ('Humanitarian Acts',3488,'sajfz','oioulkvkrw',131,'sakuw','oa05k8fl');",
"INSERT INTO upload values        ('Humanitarian Acts',1395,'nauke','xaqtehiwvj',123,'nawtj','xa17w3ke');",
"INSERT INTO upload values        ('Env Conservation',3947,'zrnbu','vhaakucbfw',144,'zrbaw','vr41b6bk');",
"INSERT INTO upload values        ('Env Conservation',1743,'zqzra','dvknipfkic',96,'zqknc','dq@1k9ri');",
"INSERT INTO upload values        ('Humanitarian Acts',1788,'qcxgy','nmbuetgsjc',107,'qcsuc','nc72s0ge');",
"INSERT INTO upload values        ('Humanitarian Acts',4757,'wbvpn','hloojzpxbx',117,'wbxox','hb35x2pj');",
"INSERT INTO upload values        ('Petlove',3920,'zlvwu','goolrjvyuo',167,'zlylo','gl35y1wr');",
"INSERT INTO upload values        ('Natural Resource Conservation',1797,'ymekr','tagnhxsceg',194,'ymcng','tm57c5kh');",
"INSERT INTO upload values        ('Humanitarian Acts',1843,'xnsew','dyvxurrrzd',137,'xnrxd','dn93r@eu');",
"INSERT INTO upload values        ('Humanitarian Acts',3611,'haals','dkdfwoyvkd',156,'havfd','da14v1lw');",
"INSERT INTO upload values        ('Natural Resource Conservation',966,'shwfz','hbikeqrbtx',2,'shbkx','hh59b0fe');",
"INSERT INTO upload values        ('Env Conservation',295,'dupwd','uatthhcvyj',17,'duvtj','uu60v9wh');",
"INSERT INTO upload values        ('Env Conservation',1553,'oxaag','lsamatirny',28,'oxrmy','lx11r4aa');",
"INSERT INTO upload values        ('Natural Resource Conservation',1783,'cbygp','eidcurvdsx',82,'cbdcx','eb94d9gu');",
"INSERT INTO upload values        ('Humanitarian Acts',198,'zonqk','cnkzdfdtdx',138,'zotzx','co41t4qd');",
"INSERT INTO upload values        ('Natural Resource Conservation',1570,'mqegc','lkaiwvzqqz',199,'mqqiz','lq51q7gw');",
"INSERT INTO upload values        ('Env Conservation',823,'ipslm','tmypzqgemk',148,'ipepk','tp99e3lz');",
"INSERT INTO upload values        ('Env Conservation',2360,'tsnxt','jlhaujsijt',130,'tsiat','js48i0xu');",
"INSERT INTO upload values        ('Natural Resource Conservation',4295,'okhzt','feluzouvbm',187,'okvum','fk82v2zz');",
"INSERT INTO upload values        ('Humanitarian Acts',3497,'pluan','oiiiphtehj',7,'pleij','ol19e8ap');",
"INSERT INTO upload values        ('Humanitarian Acts',4899,'kqedd','lquyughjtg',92,'kqjyg','lq51j0du');",
"INSERT INTO upload values        ('Petlove',2025,'whzes','vaycxtbbdb',59,'whbcb','vh@9b4ex');",
"INSERT INTO upload values        ('Humanitarian Acts',4554,'dazyd','krkostjeyl',26,'daeol','ka@1e9ys');",
"INSERT INTO upload values        ('Natural Resource Conservation',982,'qzhru','whhomjucri',126,'qzcoi','wz88c8rm');",
"INSERT INTO upload values        ('Humanitarian Acts',3232,'gtpcg','ethzeegbtj',35,'gtbzj','et68b0ce');",
"INSERT INTO upload values        ('Env Conservation',1809,'dcfuq','uhgoxezvar',111,'dcvor','uc67v1ux');",
"INSERT INTO upload values        ('Humanitarian Acts',2698,'vbohs','nvwlsnbpnv',37,'vbplv','nb55p4hs');",
"INSERT INTO upload values        ('Humanitarian Acts',4772,'kzhhk','uxofrcpwzi',113,'kzwfi','uz85w@hr');",
"INSERT INTO upload values        ('Natural Resource Conservation',1840,'zegtb','rxzatoebek',173,'zebak','re7@b5tt');",
"INSERT INTO upload values        ('Natural Resource Conservation',4765,'eqlii','nxwlxvuzhz',172,'eqzlz','nq25z8ix');",
"INSERT INTO upload values        ('Humanitarian Acts',3425,'whjfh','siihcjouct',120,'whuht','sh09u3fc');",
"INSERT INTO upload values        ('Petlove',4489,'hthwm','xgxbgzztou',173,'httbu','xt87t5wg');",
"INSERT INTO upload values        ('Humanitarian Acts',933,'ldtxz','lkkngbllod',108,'ldlnd','ld01l5xg');",
"INSERT INTO upload values        ('Env Conservation',4760,'xcavn','yroclhtwga',124,'xcwca','yc15w7vl');",
"INSERT INTO upload values        ('Env Conservation',2009,'atkum','liwdnozoft',130,'atodt','lt15o6un');",
"INSERT INTO upload values        ('Petlove',1695,'xbpne','cupuwuxthd',180,'xbtud','cb66t8nw');",
"INSERT INTO upload values        ('Petlove',3270,'hovhe','fluivtvagf',99,'hoaif','fo31a7hv');",
"INSERT INTO upload values        ('Natural Resource Conservation',4077,'cyshi','prtejsrzja',42,'cyzea','py90z0hj');",
"INSERT INTO upload values        ('Natural Resource Conservation',722,'dqpuw','wzfrwxzmbj',49,'dqmrj','wq66m2uw');",
"INSERT INTO upload values        ('Petlove',2360,'kelqx','xatgbujntv',136,'kengv','xe20n0qb');",
"INSERT INTO upload values        ('Natural Resource Conservation',3185,'xxjbx','brygwfxtko',124,'xxtgo','bx09t1bw');",
"INSERT INTO upload values        ('Env Conservation',1679,'mhvgl','zmtibvdwut',44,'mhwit','zh30w1gb');",
"INSERT INTO upload values        ('Natural Resource Conservation',4512,'sftqt','uujuwtcvte',53,'sfvue','uf00v0qw');",
"INSERT INTO upload values        ('Natural Resource Conservation',1347,'ygnyb','oivxljkevf',110,'ygexf','og43e3yl');",
"INSERT INTO upload values        ('Petlove',1386,'ctrtu','wydjzglqan',10,'ctqjn','wt84q1tz');",
"INSERT INTO upload values        ('Petlove',4292,'rjfxj','tzlvbwycjd',158,'rjcvd','tj62c0xb');",
"INSERT INTO upload values        ('Natural Resource Conservation',4358,'uicrv','sfgtjamfmc',163,'uiftc','si37f3rj');",
"INSERT INTO upload values        ('Natural Resource Conservation',593,'pdgye','edsialyyxe',110,'pdyie','ed79y7ya');",
"INSERT INTO upload values        ('Env Conservation',959,'qwscd','blrejiifnj',148,'qwfej','bw98f4cj');",
"INSERT INTO upload values        ('Humanitarian Acts',2089,'xkreo','vygnewuoen',155,'xkonn','vk87o5ee');",
"INSERT INTO upload values        ('Petlove',4815,'jkwcp','xagnptnpjk',111,'jkpnk','xk57p0cp');",
"INSERT INTO upload values        ('Petlove',306,'tmonb','wygufhmwwz',6,'tmwuz','wm57w5nf');",
"INSERT INTO upload values        ('Env Conservation',3791,'ladxl','ngqnignigv',147,'lainv','na47i7xi');",
"INSERT INTO upload values        ('Humanitarian Acts',360,'nghzg','oadsvflvbx',182,'ngvsx','og84v2zv');",
"INSERT INTO upload values        ('Humanitarian Acts',2519,'kqvot','wcqgbjitiz',25,'kqtgz','wq37t9ob');",
"INSERT INTO upload values        ('Natural Resource Conservation',2265,'rxwmu','infnmlybkf',10,'rxbnf','ix56b1mm');",
"INSERT INTO upload values        ('Humanitarian Acts',420,'uewae','gdcdbdytry',7,'uetdy','ge53t8ab');",
"INSERT INTO upload values        ('Petlove',1702,'bwala','jksmlvuevy',58,'bwemy','jw19e3ll');",
"INSERT INTO upload values        ('Natural Resource Conservation',2689,'jrblu','mpkviljdmw',137,'jrdvw','mr21d3li');",
"INSERT INTO upload values        ('Petlove',884,'plboh','jqwuwcoslz',151,'plsuz','jl25s2ow');",
"INSERT INTO upload values        ('Natural Resource Conservation',881,'xvsbl','irrwzsmxkn',106,'xvxwn','iv98x1bz');",
"INSERT INTO upload values        ('Petlove',628,'gcbtz','ogqijphzfw',170,'gcziw','oc27z6tj');",
"INSERT INTO upload values        ('Natural Resource Conservation',714,'dyxad','rgxchnnzau',168,'dyzcu','ry77z1ah');",
"INSERT INTO upload values        ('Humanitarian Acts',1727,'ernrf','xklqhccspj',64,'ersqj','xr42s6rh');",
"INSERT INTO upload values        ('Humanitarian Acts',2575,'qdgwe','nltqqgllsp',72,'qdlqp','nd70l9wq');",
"INSERT INTO upload values        ('Env Conservation',2751,'sylnf','usboiedvrx',93,'syvox','uy22v8ni');",
"INSERT INTO upload values        ('Env Conservation',1092,'bllid','ryvphmrgdq',6,'blgpq','rl23g4ih');",
"INSERT INTO upload values        ('Petlove',1575,'zszco','ikxyyasyfg',6,'zsyyg','is@7y6cy');",
"INSERT INTO upload values        ('Petlove',2301,'lvbkq','ganlodgrkt',120,'lvrlt','gv24r1ko');",
"INSERT INTO upload values        ('Petlove',3118,'slihv','rceinitlfr',136,'sllir','rl95l6hn');",
"INSERT INTO upload values        ('Humanitarian Acts',2842,'txipc','vyynlqorlp',165,'txrnp','vx99r2pl');",
"INSERT INTO upload values        ('Humanitarian Acts',482,'pcjig','mszwhchhpb',198,'pchwb','mc0@h6ih');",
"INSERT INTO upload values        ('Humanitarian Acts',1626,'vcnuz','yhratsngkz',148,'vcgaz','yc48g1ut');",
"INSERT INTO upload values        ('Natural Resource Conservation',4818,'rndve','bvvbxkjjrc',176,'rnjbc','bn43j8vx');",
"INSERT INTO upload values        ('Env Conservation',2213,'tbkwm','hgyzkwjxul',80,'tbxzl','hb19x1wk');",
"INSERT INTO upload values        ('Env Conservation',2015,'plztl','ibgdxzfoui',133,'plodi','il@7o1tx');",
"INSERT INTO upload values        ('Natural Resource Conservation',1552,'jcuvf','gnqpqsyqfr',47,'jcqpr','gc17q6vq');",
"INSERT INTO upload values        ('Humanitarian Acts',3596,'lghyw','jvpfrawbwy',119,'lgbfy','jg86b5yr');",
"INSERT INTO upload values        ('Humanitarian Acts',4505,'rpspu','tgcnvxiwnc',189,'rpwnc','tp93w4pv');",
"INSERT INTO upload values        ('Humanitarian Acts',4662,'niwys','eqvgohmfrb',20,'nifgb','ei53f8yo');",
"INSERT INTO upload values        ('Env Conservation',1736,'lnplq','fwnvikrcow',93,'lncvw','fn64c5li');",
"INSERT INTO upload values        ('Petlove',2330,'bqafh','uhwkxdnvtg',33,'bqvkg','uq15v0fx');",
"INSERT INTO upload values        ('Natural Resource Conservation',1381,'muzys','pllcjzckvh',111,'mukch','pu@2k3yj');",
"INSERT INTO upload values        ('Natural Resource Conservation',692,'apobv','yrbcrainyq',84,'apncq','yp52n9br');",
"INSERT INTO upload values        ('Petlove',2964,'ffuls','fklqcaxnfr',160,'ffnqr','ff12n6lc');",
"INSERT INTO upload values        ('Natural Resource Conservation',1861,'rvffm','rzbxswklll',164,'rvlxl','rv62l2fs');",
"INSERT INTO upload values        ('Humanitarian Acts',2874,'bgagu','miaegnmrkd',4,'bgred','mg11r1gg');",
"INSERT INTO upload values        ('Humanitarian Acts',2790,'vxhyh','ihlvyywhqa',119,'vxhva','ix82h7yy');",
"INSERT INTO upload values        ('Natural Resource Conservation',2105,'dqadt','xsdebdzxjt',169,'dqxet','xq14x0db');",
"INSERT INTO upload values        ('Humanitarian Acts',908,'obswl','mvfofdssac',105,'obsoc','mb96s1wf');",
"INSERT INTO upload values        ('Natural Resource Conservation',4888,'ognkh','nwpjtamfzr',78,'ogfjr','ng46f@kt');",
"INSERT INTO upload values        ('Env Conservation',4745,'kqobk','vmhntltpag',48,'kqpng','vq58p1bt');",
"INSERT INTO upload values        ('Env Conservation',4580,'xcfkm','pjzkfrkbif',8,'xcbkf','pc6@b9kf');",
"INSERT INTO upload values        ('Humanitarian Acts',452,'ubyzy','zhodkgogrj',89,'ubgdj','zb95g8zk');",
"INSERT INTO upload values        ('Env Conservation',3339,'hspnp','myieeyptfl',188,'hstel','ms69t6ne');",
"INSERT INTO upload values        ('Natural Resource Conservation',1757,'ogvzo','guoxsdyjpc',64,'ogjxc','gg35j6zs');",
"INSERT INTO upload values        ('Humanitarian Acts',3792,'yoyhk','zbcqsrazsl',9,'yozql','zo93z9hs');",
"INSERT INTO upload values        ('Humanitarian Acts',2856,'xwemy','lsqhskmbph',138,'xwbhh','lw57b6ms');",
"INSERT INTO upload values        ('Natural Resource Conservation',1111,'zrwcg','tgawtseuei',135,'zruwi','tr51u5ct');",
"INSERT INTO upload values        ('Petlove',2344,'gbzpk','vlbvrpyjiq',150,'gbjvq','vb@2j9pr');",
"INSERT INTO upload values        ('Humanitarian Acts',3515,'mwqot','mjonykjzct',155,'mwznt','mw75z3oy');",
"INSERT INTO upload values        ('Petlove',2322,'msvpx','hlfyncsdnm',69,'msdym','hs36d4pn');",
"INSERT INTO upload values        ('Petlove',3123,'dewdp','bfsnowznfs',196,'denns','be59n6do');",
"INSERT INTO upload values        ('Natural Resource Conservation',1450,'xzjxl','fecyvazwgl',143,'xzwyl','fz03w7xv');",
"INSERT INTO upload values        ('Petlove',2988,'ehtwt','mckutgrfmn',110,'ehfun','mh01f3wt');",
"INSERT INTO upload values        ('Petlove',3125,'akvxy','rtmflatzhc',16,'akzfc','rk33z8xl');",
"INSERT INTO upload values        ('Petlove',2378,'wxnoy','oycumqutwb',166,'wxtub','ox43t5om');",
"INSERT INTO upload values        ('Petlove',2445,'gjvdu','gksnjahifu',6,'gjinu','gj39i6dj');",
"INSERT INTO upload values        ('Humanitarian Acts',3270,'bgadf','vfacpewguv',17,'bggcv','vg11g1dp');",
"INSERT INTO upload values        ('Env Conservation',2047,'jzgqd','alrqqcfqgg',27,'jzqqg','az78q7qq');",
"INSERT INTO upload values        ('Env Conservation',3762,'rtiaw','jdnxteueps',112,'rtexs','jt94e6at');",
"INSERT INTO upload values        ('Humanitarian Acts',25,'kjdhj','qrsfsltqis',5,'kjqfs','qj49q9hs');",
"INSERT INTO upload values        ('Petlove',281,'pkizm','wddahcymby',152,'pkmay','wk94m2zh');",
"INSERT INTO upload values        ('Natural Resource Conservation',4010,'zgyqm','yhshzdcpqo',88,'zgpho','yg99p7qz');",
"INSERT INTO upload values        ('Petlove',936,'sqcfl','jbbpyjyuaf',46,'squpf','jq32u1fy');",
"INSERT INTO upload values        ('Env Conservation',1212,'ermnn','ekpkxojcbl',111,'erckl','er36c2nx');",
"INSERT INTO upload values        ('Humanitarian Acts',3152,'nmorj','dkfnuribmu',147,'nmbnu','dm56b3ru');",
"INSERT INTO upload values        ('Humanitarian Acts',4350,'rvsid','kiyxzzfjrf',200,'rvjxf','kv99j8iz');",
"INSERT INTO upload values        ('Natural Resource Conservation',1555,'admsl','nbpnttulkx',63,'adlnx','nd36l1st');",
"INSERT INTO upload values        ('Humanitarian Acts',501,'mirxi','qeelqxowev',173,'miwlv','qi85w5xq');",
"INSERT INTO upload values        ('Humanitarian Acts',2500,'nrvzp','xduywrcbmo',115,'nrbyo','xr31b3zw');",
"INSERT INTO upload values        ('Env Conservation',4716,'ucsry','gdurjgwzxi',68,'uczri','gc91z7rj');",
"INSERT INTO upload values        ('Petlove',1256,'zsfbl','mkdnhzawlx',41,'zswnx','ms64w2bh');",
"INSERT INTO upload values        ('Env Conservation',3230,'rtmth','qjekgdirxb',4,'rtrkb','qt35r7tg');",
"INSERT INTO upload values        ('Natural Resource Conservation',158,'gtgko','tvsvmmkgwb',17,'gtgvb','tt79g5km');",
"INSERT INTO upload values        ('Env Conservation',970,'xjpcg','rjcahycgjk',118,'xjgak','rj63g0ch');",
"INSERT INTO upload values        ('Env Conservation',654,'jafik','ympjrzvlfq',190,'jaljq','ya66l6ir');",
"INSERT INTO upload values        ('Petlove',3156,'fctsu','rmspybugbm',71,'fcgpm','rc09g2sy');",
"INSERT INTO upload values        ('Petlove',546,'bogrt','uksiujqmoe',138,'bomie','uo79m5ru');",
"INSERT INTO upload values        ('Humanitarian Acts',3489,'vdlwd','arlzgoafte',129,'vdfze','ad22f0wg');",
"INSERT INTO upload values        ('Humanitarian Acts',4080,'ybmlh','pcjdrhchbk',13,'ybhdk','pb30h2lr');",
"INSERT INTO upload values        ('Humanitarian Acts',973,'yttkf','tggynrtpst',173,'ytpyt','tt07p9kn');",
"INSERT INTO upload values        ('Natural Resource Conservation',4495,'iijss','ehvhxfejru',14,'iijhu','ei03j8sx');",
"INSERT INTO upload values        ('Env Conservation',1979,'guzwb','gbyspwfzwd',97,'guzsd','gu@9z5wp');",
"INSERT INTO upload values        ('Humanitarian Acts',3883,'ruszw','cjnzlwmfzj',43,'rufzj','cu94f@zl');",
"INSERT INTO upload values        ('Petlove',3788,'idpcz','bgyjwracgd',13,'idcjd','bd69c7cw');",
"INSERT INTO upload values        ('Natural Resource Conservation',4378,'lkhuc','qthcbushvl',138,'lkhcl','qk88h3ub');",
"INSERT INTO upload values        ('Humanitarian Acts',3414,'vlxns','sqinknsgxi',20,'vlgni','sl79g7nk');",
"INSERT INTO upload values        ('Humanitarian Acts',3558,'ybsru','zeqtymyuwo',147,'ybuto','zb97u5ry');",
"INSERT INTO upload values        ('Natural Resource Conservation',2517,'ncmap','ukrwaknriy',91,'ncrwy','uc38r9aa');",
"INSERT INTO upload values        ('Env Conservation',1764,'kwaii','jimezpqglp',82,'kwgep','jw13g2iz');",
"INSERT INTO upload values        ('Humanitarian Acts',4641,'evztq','nlqsqwzdlm',68,'evdsm','nv@7d2tq');",
"INSERT INTO upload values        ('Petlove',3742,'wuqtc','vgpombzbqm',81,'wubom','vu76b7tm');",
"INSERT INTO upload values        ('Natural Resource Conservation',3932,'hznha','zbxcwqbegw',104,'hzecw','zz47e7hw');",
"INSERT INTO upload values        ('Natural Resource Conservation',2143,'hkxcg','exehjfjpep',43,'hkphp','ek75p5cj');",
"INSERT INTO upload values        ('Natural Resource Conservation',2023,'mlnve','wwdwshhjbd',160,'mljwd','wl44j2vs');",
"INSERT INTO upload values        ('Humanitarian Acts',3637,'apmkv','prssushxze',58,'apxse','pp39x@ku');",
"INSERT INTO upload values        ('Natural Resource Conservation',4476,'uiqoj','tkhsnxvato',173,'uiaso','ti78a0on');",
"INSERT INTO upload values        ('Petlove',4826,'lgqov','wrwgliysxq',59,'lgsgq','wg75s7ol');",
"INSERT INTO upload values        ('Petlove',4823,'mnviw','mxakysiagx',108,'mnakx','mn31a7iy');",
"INSERT INTO upload values        ('Humanitarian Acts',1535,'dxlrn','oquettcmod',68,'dxmed','ox21m5rt');",
"INSERT INTO upload values        ('Petlove',1935,'hgytj','eotzuyrerx',15,'hgezx','eg90e8tu');",
"INSERT INTO upload values        ('Natural Resource Conservation',3072,'ftdlf','yhjgibblmr',199,'ftlgr','yt40l3li');",
"INSERT INTO upload values        ('Env Conservation',1001,'xyiir','tjlnuuohdh',80,'xyhnh','ty92h4iu');"
]

for i in u_insertion:
    conn.execute(i)
    conn.commit()