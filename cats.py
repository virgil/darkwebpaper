#!/usr/local/bin/python3.3


from pprint import pprint

'''
c&c
childabuse
anonymity
bitcoin
blog
books
chat
directory
drugs
forum
fraud
gambling
guns
hacking
hosting
mail
market
news
piracy	# added for sites offering torrents etc
porn
search
terrorism	# can be combined with guns
unsure			# if unsure, put it here and I'll look at it
whistleblower
wiki
down
'''

Hs = {}

Hs['5fpp2orjc2ejd2g7'] = ('blog',)
Hs['xnordic6virmmls3'] = ('porn',)
Hs['apfront5qxkubpis'] = ('directory',)
Hs['wqapyiztripnwcgr'] = ('market',)
Hs['ev3h5yxkjz4hin75'] = ('wiki',)
Hs['kav3udmxn34tke34'] = ('forum',)
Hs['n3groac7k6scjpsa'] = ('c&c',)
Hs['uj3wazyk5u4hnvtk'] = ('piracy','search')
Hs['lulzwrzcle5ks3se'] = ('porn',)
Hs['hacker47nad4udho'] = ('hacking',)
Hs['hrhqqimwgua5vxgs'] = ('software',)
Hs['7rmatpsvygnpjhrt'] = ('news',)
Hs['diaperedxrx4yxwv'] = ('childabuse',)
Hs['haklab4ulibiyeix'] = ('software',)
Hs['underdj5ziov3ic7'] = ('directory',)
Hs['cpvls4gi2cvvirrk'] = ('childabuse',)
Hs['z2jjpz2pl45sj76l'] = ('childabuse',)
Hs['thehub7gqe43miyc'] = ('forum','hacking','market')
Hs['flibustahezeous3'] = ('books',)
Hs['poverty4657tlx6h'] = ('wiki',)
Hs['deepirc23ukiben3'] = ('chat',)
Hs['frwikisfa6myvgyx'] = ('wiki',)
Hs['hackmeon2teb4ixo'] = ('forum','hacking')
Hs['7mdzuqhtqzaxhxpi'] = ('forum','childabuse',)
Hs['saemf4erbrvhfddd'] = ('childabuse',)
Hs['uxxasdkkxtrzppvv'] = ('wiki',)
Hs['cruel2ijkqggizy5'] = ('forum',)
Hs['oniichanylo2tsi4'] = ('forum',)
Hs['v3is2aomdap3cjgn'] = ('porn',)
Hs['l5ernlr4d54yz7o7'] = ('blog',)
Hs['tq32o7mvfueaq23p'] = ('skip',)
Hs['sy44dubmbet27dzn'] = ('forum','porn')
Hs['warrenguyis3q3tw'] = ('blog',)	#personal website
Hs['4yjes6zfucnh7vcj'] = ('drugs',) #could not confirm the contents
Hs['darknet4x3hcv5zp'] = ('hosting',)
Hs['kingskx44kxlushc'] = ('drugs',)
Hs['loun7zzy63gtd3pr'] = ('forum',) #connects but internal server failure
Hs['3vxmucb43bs4lert'] = ('blog',)
Hs['t5eglgwxa43dmbn3'] = ('skip',)
Hs['diamouwksmsuquw7'] = ('market',)
Hs['z2gu35md7bi3ceew'] = ('directory','search')
Hs['wypwtzc2kaceyufw'] = ('mail',)
Hs['k4btcjyd3gkvocuh'] = ('market',)
Hs['cbnujyutccrk267j'] = ('blog','anonymity')
Hs['alphaz3etex326u2'] = ('market',)

Hs['satoriify6xf74ut'] = ('market',)
Hs['cidr6kt4la4slizf'] = ('bitcoin','market')
Hs['mx5dwqbkplnhcdzp'] = ('skip',)
Hs['superkuhbitj6tul'] = ('blog',)
Hs['udsmewv45lunzoo4'] = ('directory','fraud')
Hs['vertigovoyxztwj6'] = ('books',)
Hs['duskgytldkxiuqc6'] = ('wiki',)
Hs['zilionrvcrzixedi'] = ('blog',) #hits the server but taking too long to load, no idea what is going on
Hs['mb4z3nlfyrcjnoqf'] = ('hacking','forum')
Hs['ewokqwbnd3wrnbxg'] = ('skip',)


Hs['kaufmichob4rdqje'] = ('market',)
Hs['v2q73k54fvnhtouv'] = ('wiki',)
Hs['fkzkqpxfvr7i5p4k'] = ('wiki','hacking')
Hs['torwikignoueupfm'] = ('wiki',)
Hs['kanepesf4fytldpw'] = ('forum','drugs')
Hs['torwi647pyrt476m'] = ('wiki',)
Hs['627k32evfgy2cnue'] = ('forum','hacking')
Hs['suprbayoubiexnmp'] = ('search','piracy')
Hs['relicd7edydsci7u'] = ('search',)
Hs['suppow4bks3vdysc'] = ('forum',)
Hs['25g7i3ykzh4qsmgh'] = ('hacking',)
Hs['hss3uro2hsxfogfq'] = ('search',)
Hs['vault43z5vxy3vn3'] = ('market','forum')
Hs['oxwugzccvk3dk6tj'] = ('forum',)
Hs['nco5rodtsha5tm6n'] = ('forum','news')
Hs['nco5ranerted3nkt'] = ('forum','news')
Hs['qia2vpjf3bubn5he'] = ('books',)
Hs['vj5pbopejlhcbz4n'] = ('porn',)
Hs['gv5dwucqmkmuy2xr'] = ('wiki','blog')
Hs['rutorc6mqdinc4cz'] = ('piracy','search')
Hs['hwikis25cffertqe'] = ('wiki',)
Hs['dosug4rea4kvnk5f'] = ('market',)
Hs['papyrefb2tdk6czd'] = ('books',)
Hs['www.papyrefb2tdk6czd'] = ('books',)
Hs['lv2hgds6hpqzgg4y'] = ('wiki',)
Hs['bi42hupl3ypdta4t'] = ('hosting',)
Hs['j4ni3npmz6p4c5xq'] = ('childabuse','porn')
Hs['fullchan4jtta4sx'] = ('forum',)
Hs['zqktlwi4fecvo6ri'] = ('wiki',)

Hs['rn2moiq5wo6mgcwb'] = ('wiki',)


Hs['torvps7kzis5ujfz'] = ('wiki',)

Hs['giftexnqgi53o24r'] = ('forum',)

Hs['uhwikih256ynt57t'] = ('wiki',)
Hs['kpvz7kpmcmne52qf'] = ('wiki',)
Hs['supportpdsv7ydm5'] = ('forum',)
Hs['auutwvpt2zktxwng'] = ('directory',)
Hs['freenet7cul5qsz6'] = ('directory','search')
Hs['neozdy2mipzjzk6t'] = ('wiki',)
Hs['kpvz7no2c347rcey'] = ('wiki',)

Hs['a4yedjgciupu7zzt'] = ('piracy',)
Hs['5sm2vp55n6cxly6z'] = ('porn',)
Hs['xplayyyyyirxui4n'] = ('porn',)
Hs['gurochanocizhuhg'] = ('forum',)
Hs['exwljei3bfvchv6p'] = ('blog',)
Hs['rfwtogljhrrzxyrl'] = ('market',)
Hs['n6pbizsbykwxmydz'] = ('wiki',)

Hs['c3jemx2ube5v5zpg'] = ('books',)
Hs['teensexmskgqhmuo'] = ('childabuse','porn')

Hs['wecttp234pgkcxoh'] = ('directory','search','piracy')
Hs['sigaintevyh2rzvw'] = ('mail',)
Hs['k4jmdeccpnsfe43c'] = ('porn',)
Hs['fappen53mnvayq4o'] = ('porn',)
Hs['w363zoq3ylux5rf5'] = ('forum',)
Hs['lcdsm7da2y46xnqs'] = ('forum',)
Hs['mt3plrzdiyqf6jim'] = ('skip',)
Hs['chatrapi7fkbzczr'] = ('chat',)
Hs['e4unrusy7se5evw5'] = ('hacking',)
Hs['vbrik4rxd3dksux6'] = ('wiki',)
Hs['xcomics5vvoiary2'] = ('book','porn')
Hs['blockchatntqnf7o'] = ('bitcoin',)
Hs['lwplxqzvmgu43uff'] = ('forum','hacking')

Hs['dmzwvie2gmtwszof'] = ('forum',)
Hs['xiwayy2kn32bo3ko'] = ('forum','market')
Hs['csmania3ljzhig4p'] = ('forum',)
Hs['abraxasgacelesox'] = ('forum','market')
Hs['nymphetowhsn3gpf'] = ('forum',)
Hs['yiswhxmewwothck6'] = ('skip',)
Hs['crimenc5wxi63f4r'] = ('market','drugs','guns','bitcoin','fraud')
Hs['22u75kqyl666joi2'] = ('market','fraud')
Hs['mvx7igua26khad3k'] = ('hosting',)
Hs['hiotuxliwisbp6mi'] = ('hosting',)
Hs['ye4x7dzr6w2dpa7c'] = ('books',)
Hs['2fap3cpmi3coso5y'] = ('porn',)
Hs['shitscats6qomwxm'] = ('porn',)
Hs['blkbook3fxhcsn3u'] = ('directory',)
Hs['dmirrgetyojz735v'] = ('chat','forum','hosting')
Hs['pinkmetheribnpvt'] = ('porn',)
Hs['savkhz37olwuub37'] = ('books',)
Hs['darksdsp6iexyidx'] = ('porn','childabuse') #another blackmailing site
Hs['njsq2jeyc527mol7'] = ('hosting','hacking')
Hs['3dboysnh6cia5uul'] = ('porn',)
Hs['hwikiiwc4igbolzn'] = ('wiki',)
Hs['twlba5j7oo5g4kj5'] = ('hosting',)
Hs['nicce3665574md6e'] = ('blog',)
Hs['bdpuqvsqmphctrcs'] = ('directory',)
Hs['www.bdpuqvsqmphctrcs'] = ('directory',)
Hs['abraxcdb2wk7iwne'] = ('forum','market')

Hs['a64r6szrpegnggoj'] = ('forum','wiki')
Hs['filehostucjtfzj2'] = ('hosting',)
Hs['cmoqohtgyilgec7y'] = ('news',)
Hs['7rmath4ro2of2a42'] = ('news','books')
Hs['swehackmzys2gpmb'] = ('forum','hacking')
Hs['jl4m7ubpotnu2yos'] = ('piracy','hosting')
Hs['kpvz7ki2lzvnwve7'] = ('wiki',)

Hs['obscuredtzevzthp'] = ('hosting',)
Hs['snowdenap6zpvwuf'] = ('hosting',)
Hs['s6cco2jylmxqcdeh'] = ('forum',)
Hs['mjt54q6pagohhimn'] = ('porn',)
Hs['tvrc2ydjgz5r45dp'] = ('porn','market')
Hs['wdpwzykrrqq4p7w7'] = ('news','anonymity','software')
Hs['pyl7a4ccwgpxm6rd'] = ('hacking','whistleblower','forum','anonymity')

Hs['nzwolake3hokkjwq'] = ('books','piracy')
Hs['6mtyxwochl2qalak'] = ('wiki','hacking')

Hs['freedomsct2bsqtn'] = ('hosting',)
Hs['gqe5keek4vzphqqs'] = ('childabuse','porn') 

Hs['felixxxboni3mk4a'] = ('hosting',)
Hs['m27q7ebzptr3ouw7'] = ('forum',)
Hs['3cpleimu2getp5q7'] = ('books',)
Hs['bv23gwyn6yecpakd'] = ('forum',)
Hs['deepdot35wvmeyd5'] = ('news',)
Hs['sqtluqnjl6txj2n2'] = ('forum','childabuse')
Hs['mbxsrn5ijmioznn7'] = ('news',)
Hs['6gprsi33qvzcun7u'] = ('forum',)
Hs['kpvz7vokigja2k5x'] = ('wiki',)
Hs['ogatl57cbva6tncg'] = ('forum',)
Hs['jlve2y45zacpbz6s'] = ('directory',)

Hs['222222avkcjpcbwi'] = ('bitcoin','fraud','hacking')
Hs['25g7i3ykzh4qsmgh'] = ('forum',)
Hs['2nq3v6fnrwp72nao'] = ('directory',)
Hs['4c7pcgkpjlwg67zo'] = ('market','fraud')
Hs['5ybuj4qudrmyijbk'] = ('hacking',)
Hs['6nv3ix7omzrty6cm'] = ('anonymity',)
Hs['6w2nyvsf77q72ue6'] = ('skip','c&c')
Hs['6xukrlqedfabdjrb'] = ('blog','hacking')
Hs['7ogfxi6wfprmzms5'] = ('porn',)
Hs['7uyfawf73hungcjo'] = ('bitcoin',)
Hs['abkjckdgoabr7bmm'] = ('whistleblower',)
Hs['abraxasjhcybfhxh'] = ('skip',)
Hs['arcadian4nxs3pjr'] = ('forum',)
Hs['atewoqywd2seh77s'] = ('market',)
Hs['awjhchcem652axna'] = ('forum','anonymity')
Hs['b4d3igwmoo5355ur'] = ('skip',)

Hs['ba434tkccyddp2oq'] = ('skip',)
Hs['c3jembnkdnbcdniu'] = ('books',)
Hs['ccpawalvkishrhlm'] = ('books',)
Hs['ccpawalvkishrhlm'] = ('market',)
Hs['cyruselfgi7islfk'] = ('skip',)
Hs['cyruservvvklto2l'] = ('anonymity','hosting')
Hs['d4wqkm2lmg3y4day'] = ('directory',)
Hs['dadfphseqv75isg7'] = ('hacking',)
Hs['darkodei7qdze3pl'] = ('forum',)
Hs['easycoinsayj7p5l'] = ('bitcoin',)
Hs['es2adizg32j3kob5'] = ('directory',)
Hs['eucasmsl7zhsz2un'] = ('drugs',)
Hs['fne53vgk73f563k7'] = ('market',)
Hs['glle7yomrioczp6w'] = ('hosting',)
Hs['gutstgbx6ymfajj3'] = ('fraud',)
Hs['hackeonon7k7pnhi'] = ('hacking',)
Hs['hjndkbaoisuh63h3'] = ('blog',)
Hs['i43gksam7lhhc3cy'] = ('search',)
Hs['kaarvixjxfdy2wv2'] = ('directory',)
Hs['killbrzyq5q4rcll'] = ('forum',)
Hs['knigiclz5epjvf36'] = ('books',)
Hs['lmfraudnsrntxqb4'] = ('market',)
Hs['monitortwo3m3d4b'] = ('search',)
Hs['nt4f7fzcjoe3f5aj'] = ('blog','market')
Hs['nximq4nynt7e3gxm'] = ('mail',)
Hs['onionoorcazzotwa'] = ('anonymity','software') #open source maybe ?
Hs['oofvttk46u5gletu'] = ('directory',)
Hs['plrl7yp6iilqlnxm'] = ('fraud',)
Hs['pms5n4czsmblkcjl'] = ('drugs',)
Hs['ppccfspmvnqmxtmj'] = ('market','fraud')
Hs['prinnkfsf4czx4ad'] = ('fraud',)
Hs['qqtkaeeddornla2l'] = ('skip',)
Hs['r7umpv6r5djthykt'] = ('books',)
Hs['smoker32pk4qt3mx'] = ('drugs',)
Hs['strngkwdy65o6ebt'] = ('hosting',)
Hs['tfsux6hiihj7qvxh'] = ('fraud','bitcoin')
Hs['timaq4ygg2iegci7'] = ('skip','software') 
Hs['trfn4cs6mqo2yfbz'] = ('wiki',)
Hs['tytbeta57rw2onit'] = ('market',)
Hs['vendor7zqdpty4oo'] = ('market','bitcoin')
Hs['vqfe4xmhxzi7w2uv'] = ('directory',)
Hs['wpzvprpnhhcypnn4'] = ('skip',)
Hs['wuxdb4woamcmyqlk'] = ('search','directory','books')
Hs['wx3wmh767azjjl4v'] = ('anonymity',)
Hs['yey5tn37kepnxnbi'] = ('skip',)
Hs['zs423f3cfzlm5slu'] = ('blog',)

#print(Hs)