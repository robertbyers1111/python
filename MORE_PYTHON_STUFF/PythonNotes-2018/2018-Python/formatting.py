#!/usr/bin/python3

import math

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use these in an example..
#
#   format
#   repr
#   zfill
#   rjust
#   ljust
#   format chars: .,:lfd{}
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Additonal format notes
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# FROM http://www.diveintopython3.net/refactoring.html
#
# I don’t think I’ve mentioned this yet anywhere in this book, so let
# this serve as your final lesson in string formatting. Starting in
# Python 3.1, you can skip the numbers when using positional indexes in a
# format specifier. That is, instead of using the format specifier {0} to
# refer to the first parameter to the format() method, you can simply use
# {} and Python will fill in the proper positional index for you. This
# works for any number of arguments; the first {} is {0}, the second {}
# is {1}, and so forth. 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   {7:6.2f}
#      to the left of ':' (7) is the argument number
#      to the right of ':' (6.2f) is a printf-style format specifier
#
#   {} by default, grabs next available format arg (python3)
#   {:,} formats next arg with thousands separator
#   {name} grabs a named arg (e.g., '{0}, {1}, and {other}.'.format('X1', 'X2', other='Z0')
#
#   '!a' (apply ascii() before formatting)
#   '!s' (apply str() before formatting)
#   '!r' (apply repr() before formatting)
#
#
# Use a dict to name the args. Two examples..
#
#     table = {'Amy': 4127, 'Jack': 4098, 'Cam': 8637678}
#
# Ex1:
# print('Jack: {0[Jack]:d}; Amy: {0[Amy]:d}; Cam: {0[Cam]:d}'.format(table))
#
# Ex2:
# print('Jack: {Jack:d}; Amy: {Amy:d}; Cam: {Cam:d}'.format(**table))

table = {'Amy': 4127, 'Jack': 4098, 'Cam': 8637678}

print()
print('Jack: {0[Jack]:d}; Amy: {0[Amy]:d}; Cam: {0[Cam]:d}'.format(table))
print('Jack: {Jack:d}; Amy: {Amy:d}; Cam: {Cam:d}'.format(**table))

print()
print('The value of PI is approximately {!r:s}'.format(math.pi))
print('The value of PI is approximately {:0.40f}'.format(math.pi))

def init():
  print()
  return -25.42, 1.3456, 22.0/7

def piapprox():
  print()
  return \
   7/2, \
   10/3, \
   13/4, \
   16/5, \
   19/6, \
   22/7, \
   179/57, \
   201/64, \
   223/71, \
   245/78, \
   267/85, \
   289/92, \
   311/99, \
   333/106, \
   355/113, \
   52163/16604, \
   52518/16717, \
   52873/16830, \
   53228/16943, \
   53583/17056, \
   53938/17169, \
   54293/17282, \
   54648/17395, \
   55003/17508, \
   55358/17621, \
   55713/17734, \
   56068/17847, \
   56423/17960, \
   56778/18073, \
   57133/18186, \
   57488/18299, \
   57843/18412, \
   58198/18525, \
   58553/18638, \
   58908/18751, \
   59263/18864, \
   59618/18977, \
   59973/19090, \
   60328/19203, \
   60683/19316, \
   61038/19429, \
   61393/19542, \
   61748/19655, \
   62103/19768, \
   62458/19881, \
   62813/19994, \
   63168/20107, \
   63523/20220, \
   63878/20333, \
   64233/20446, \
   64588/20559, \
   64943/20672, \
   65298/20785, \
   65653/20898, \
   66008/21011, \
   66363/21124, \
   66718/21237, \
   67073/21350, \
   67428/21463, \
   67783/21576, \
   68138/21689, \
   68493/21802, \
   68848/21915, \
   69203/22028, \
   69558/22141, \
   69913/22254, \
   70268/22367, \
   70623/22480, \
   70978/22593, \
   71333/22706, \
   71688/22819, \
   72043/22932, \
   72398/23045, \
   72753/23158, \
   73108/23271, \
   73463/23384, \
   73818/23497, \
   74173/23610, \
   74528/23723, \
   74883/23836, \
   75238/23949, \
   75593/24062, \
   75948/24175, \
   76303/24288, \
   76658/24401, \
   77013/24514, \
   77368/24627, \
   77723/24740, \
   78078/24853, \
   78433/24966, \
   78788/25079, \
   79143/25192, \
   79498/25305, \
   79853/25418, \
   80208/25531, \
   80563/25644, \
   80918/25757, \
   81273/25870, \
   81628/25983, \
   81983/26096, \
   82338/26209, \
   82693/26322, \
   83048/26435, \
   83403/26548, \
   83758/26661, \
   84113/26774, \
   84468/26887, \
   84823/27000, \
   85178/27113, \
   85533/27226, \
   85888/27339, \
   86243/27452, \
   86598/27565, \
   86953/27678, \
   87308/27791, \
   87663/27904, \
   88018/28017, \
   88373/28130, \
   88728/28243, \
   89083/28356, \
   89438/28469, \
   89793/28582, \
   90148/28695, \
   90503/28808, \
   90858/28921, \
   91213/29034, \
   91568/29147, \
   91923/29260, \
   92278/29373, \
   92633/29486, \
   92988/29599, \
   93343/29712, \
   93698/29825, \
   94053/29938, \
   94408/30051, \
   94763/30164, \
   95118/30277, \
   95473/30390, \
   95828/30503, \
   96183/30616, \
   96538/30729, \
   96893/30842, \
   97248/30955, \
   97603/31068, \
   97958/31181, \
   98313/31294, \
   98668/31407, \
   99023/31520, \
   99378/31633, \
   99733/31746, \
   100088/31859, \
   100443/31972, \
   100798/32085, \
   101153/32198, \
   101508/32311, \
   101863/32424, \
   102218/32537, \
   102573/32650, \
   102928/32763, \
   103283/32876, \
   103638/32989, \
   103993/33102, \
   104348/33215, \
   208341/66317, \
   312689/99532, \
   833719/265381, \
   1146408/364913, \
   3126535/995207, \
   4272943/1360120, \
   5419351/1725033, \
   42208400/13435351, \
   47627751/15160384, \
   53047102/16885417, \
   58466453/18610450, \
   63885804/20335483, \
   69305155/22060516, \
   74724506/23785549, \
   80143857/25510582, \
   165707065/52746197, \
   245850922/78256779, \
   411557987/131002976, \
   657408909/209259755, \
   1068966896/340262731, \
   2549491779/811528438, \
   3618458675/1151791169, \
   6167950454/1963319607, \
   14885392687/4738167652, \
   21053343141/6701487259, \
   899125804609/286200632530, \
   920179147750/292902119789, \
   941232490891/299603607048, \
   962285834032/306305094307, \
   983339177173/313006581566, \
   1004392520314/319708068825, \
   1025445863455/326409556084, \
   1046499206596/333111043343, \
   1067552549737/339812530602, \
   1088605892878/346514017861, \
   1109659236019/353215505120, \
   1130712579160/359916992379, \
   1151765922301/366618479638, \
   1172819265442/373319966897, \
   1193872608583/380021454156, \
   1214925951724/386722941415, \
   1235979294865/393424428674, \
   1257032638006/400125915933, \
   1278085981147/406827403192, \
   1299139324288/413528890451, \
   1320192667429/420230377710, \
   1341246010570/426931864969, \
   1362299353711/433633352228, \
   1383352696852/440334839487, \
   1404406039993/447036326746, \
   1425459383134/453737814005, \
   1446512726275/460439301264, \
   1467566069416/467140788523, \
   1488619412557/473842275782, \
   1509672755698/480543763041, \
   1530726098839/487245250300, \
   1551779441980/493946737559, \
   1572832785121/500648224818, \
   1593886128262/507349712077, \
   1614939471403/514051199336, \
   1635992814544/520752686595, \
   1657046157685/527454173854, \
   1678099500826/534155661113, \
   1699152843967/540857148372, \
   1720206187108/547558635631, \
   1741259530249/554260122890, \
   1762312873390/560961610149, \
   1783366216531/567663097408, \
   3587785776203/1142027682075, \
   5371151992734/1709690779483, \
   8958937768937/2851718461558, \
   77042654144230/24523438471947, \
   86001591913167/27375156933505, \
   94960529682104/30226875395063, \
   103919467451041/33078593856621, \
   112878405219978/35930312318179, \
   121837342988915/38782030779737, \
   130796280757852/41633749241295, \
   139755218526789/44485467702853, \
   288469374822515/91822653867264, \
   428224593349304/136308121570117, \
   3137327371971917/998642318693672, \
   3565551965321221/1134950440263789, \
   3993776558670525/1271258561833906, \
   4422001152019829/1407566683404023, \
   4850225745369133/1543874804974140, \
   5278450338718437/1680182926544257, \
   5706674932067741/1816491048114374, \
   6134899525417045/1952799169684491, \
   17976473982901831/5722089387483356, \
   24111373508318876/7674888557167847, \
   30246273033735921/9627687726852338, \
   36381172559152966/11580486896536829, \
   66627445592888887/21208174623389167, \
   230128609812402582/73252211597019839, \
   296756055405291469/94460386220409006, \
   363383500998180356/115668560843798173, \
   430010946591069243/136876735467187340, \
   1356660285366096616/431838381024951187, \
   1786671231957165859/568715116492138527, \
   2216682178548235102/705591851959325867, \
   2646693125139304345/842468587426513207

a,b,c = init()
for i in range(1,5):
  a*=i
  b*=i
  c*=i
  print('   ',repr(a).zfill(5).ljust(20), repr(b).ljust(20), repr(c).ljust(20))

a,b,c = init()
for i in range(1,10):
  print('{2:6.0f} {2:6.1f} {2:6.2f} {2:7.3f} {2:8.4f} {2:9.5f}'.format(a,b,c))

pies = piapprox()

for i,pi in enumerate(pies):
  err=abs(math.pi - pi)
  print('{:4d} {:0.40f} {:0.40f}'.format(i,pi,err))
  if err < 0.0000000000000004:
    break

#-- ANOTHER FORMATTING METHOD

word='OMGWTF?'
pword='whatever'

print('%10s %s' % (word,pword) )
