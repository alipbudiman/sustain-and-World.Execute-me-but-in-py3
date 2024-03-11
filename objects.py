import sys, time, itertools, os, pytz, json, math
import numpy as np
from datetime import datetime
from playsound import playsound 


class World:
    
    def play_audio(file_path):
        playsound(file_path)
    
    def slow_print(text:str,speed):
            for karakter in text:
                print(karakter,end="",flush=True)
                time.sleep(speed)
    def getPass(pswd):
        passwd = ["ᛞ","ᚫ","ᛉ","ᚵ","ᛒ","ᛍ","ᛣ","ᛤ","ᛄ"]
        if pswd == passwd:
            print(" >>> LOGIN SUCCESS ")
        else:
            sys.exit()
    
    def layDown():
        listx = ["ᛞ","ᛞᚫ","ᛞᚫᛉ","ᛞᚫᛉᚵ","ᛞᚫᛉᚵᛒ","ᛞᚫᛉᚵᛒᛍ","ᛞᚫᛉᚵᛒᛍᛣ","ᛞᚫᛉᚵᛒᛍᛣᛤ","ᛞᚫᛉᚵᛒᛍᛣᛤᛄ"]
        count = 0
        for c in listx:
            if count != len(listx):
                sys.stdout.write('\r' + c)
                time.sleep(0.0001)
                count +=1
        sys.stdout.flush()
        listy = ["ᛄ","  ᛄ","    ᛄ","       ᛄ","          ᛄ","                      ᛄ"]
        count2 =0
        for cc in itertools.cycle(listy):
            if count2 == len(listy):
                break
            else:
                sys.stdout.write('\r' + cc)
                time.sleep(0.1)
                count2 +=1
                sys.stdout.flush()
    def INITIALIZATION():
        listx = ["     ██ 39%","     ███ 49%","     ████ 76%","     █████ 89%","     ██████ 100%","     ██████  INITIALIZATION","     ██████  INITIALIZATION","     ██████  INITIALIZATION","     ██████  INITIALIZATION","     ██████  INITIALIZATION","     ██████  INITIALIZATION","     ██████  INITIALIZATION"]
        count = 0
        for c in listx:
            if count != len(listx):
                sys.stdout.write('\r' + c)
                time.sleep(0.1)
                count +=1
                sys.stdout.flush()
    
    def START_SIMULATION():
        obj = """\033[32m \n________________________________________________________________________________________
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
. *      .   .    .  .     .  *      .      .        .     .-o--.   .    *  .
.  .        .     .     .      .    .     *      *   .   :O o O :      .     .
____   *   .    .      .   .           .  .   .      .    : O. Oo;    .   .
`. ````.---...___      .      *    .      .       .   * . `-.O-'  .     * . .
\_    ;   \`.-'```--..__.       .    .      * .     .       .     .        .
,'_,-' _,-'             ``--._    .   *   .   .  .       .   *   .     .  .
-'  ,-'                       `-._ *     .       .   *  .           .    .
    ,-'            _,-._            ,`-. .    .   .     .      .     *    .   .
    '--.     _ _.._`-.  `-._        |   `_   .      *  .    .   .     .  .    .
        ;  ,' ' _  `._`._   `.      `,-''  `-.     .    .     .    .      .  .
    ,-'   \    `;.   `. ;`   `._  _/\___     `.       .    *     .    . *
    \      \ ,  `-'    )        `':_  ; \      `. . *     .        .    .    *
    \    _; `       ,;               __;        `. .           .   .     . .
    '-.;        __,  `   _,-'-.--'''  \-:        `.   *   .    .  .   *   .
        )`-..---'   `---''              \ `.        . .   .  .       . .  .
___________________________________________________________________________________________\033[0m"""
        for karakter in obj:
            print(karakter,end="",flush=True)
        listx = ["     ██ 39%","     ███ 49%","     ████ 76%","     █████ 89%","     ██████ 100%","     ██████  GENERATE DATA","     ██████         GENERATE OBJECT","     ██████                      GENERATE FUNCTION","     ██████                         COLLECTIONG DATA","     ██████                      DOING WORK","     ██████               CONNECTING TO SERVER............","     ██████          CONNECTING TO SERVER DONE.............","     ██████  S T A R T    T H E     S I M U L A T I O N"]
        count = 0
        for c in listx:
            if count != len(listx):
                sys.stdout.write('\r' + c)
                time.sleep(1)
                count +=1
                sys.stdout.flush()
        
    def set_of_point():
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        setpoint = datetime.strftime(timeNow, "%H:%M:%S")
        return setpoint
    
    def prettyPrint(djson, ind=4):
        print(json.dumps(djson, indent=ind, sort_keys=True))
    
    def GiveDimension(data):
        arr = np.array(data)
        print("\n>>> Dimension of set point ::: "+str(arr))
    
    def giveCIRCUMFERENCE(data):
        luas = math.pi*(data*data)
        keliling = 2*math.pi*data
        print ("\n>>> CIRCUMFERENCE of set point ::: ",keliling)
    
    def loopInfinity():
        for c in itertools.cycle(['|', '/', '-', '\\','   Then you can be my']):
            sys.stdout.write('\r' +"\033[31m"+ c+"\033[0m")
            sys.stdout.flush()
            time.sleep(0.0001)
    
    def BlindMYVision():
        blind = """\033[32m
        

        88          88 88                      88  
        88          88 ""                      88  
        88          88                         88  
        88,dPPYba,  88 88 8b,dPPYba,   ,adPPYb,88  
        88P'    "8a 88 88 88P'   `"8a a8"    `Y88  
        88       d8 88 88 88       88 8b       88  
        88b,   ,a8" 88 88 88       88 "8a,   ,d88  
        8Y"Ybbd8"'  88 88 88       88  `"8bbdP"Y8  



        \033[0m
        """
        print(blind)
    
    def GiveAllSumulation():
        return "Dummy"
    
    def run_Exec(me):
        if me == "happy":
            return "\n-- S U C C E S S    E X E C U T E --"
    
    def TRAPPED():
        for c in itertools.cycle(['💀   Though we are trapped', '   Though we are trapped']):
            sys.stdout.write('\r' +"\033[31m"+ c+"\033[0m")
            sys.stdout.flush()
            time.sleep(0.0001)
    
    def IMTRAPPED():
        for c in itertools.cycle(['❤️   Though IM trapped', '   Though IM trapped']):
            sys.stdout.write('\r' +"\033[31m"+ c+"\033[0m")
            sys.stdout.flush()
            time.sleep(0.0001)
    
    def GET_NUTRIENTS():
        return "-- S U C C E S S  G E T  N U T R I E N T S --"
    
    def GET_ANTIOXIDANTS():
        return "-- S U C C E S S  A N T I O X I D A N T S --"
    
    def GET_ENJOYMENT():
        return "-- S U C C E S S  E N J O Y M E N T --"
    
    def GOD_EXISTENCE():
        return "-- S U C C E S S  U P G R A D E  T O  [G O D] --"
    
    def GetTimeNow():
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        localtimes = datetime.strftime(timeNow, "%a %I.%M ")
        return localtimes
    
    def EnterTrance(target):
        os.system(f"python -m trace --listfuncs {target}")
    
    def LeftSystem():
        sys.exit("LEFT THE SIMULATION")

    def ChallengingYourGod():
        for c in itertools.cycle(['|', '/', '-', '\\','   Challenging your god']):
            sys.stdout.write('\r' +"\033[31m"+ c+"\033[0m")
            sys.stdout.flush()
            time.sleep(0.0001)
    
    def FxingIllegalArgument():
        for c in itertools.cycle(
            ["ᛞ Fixing Illegal Arguments","ᛞᚫ Fixing Illegal Arguments","ᛞᚫᛉ Fixing Illegal Arguments","ᛞᚫᛉᚵ Fixing Illegal Arguments","ᛞᚫᛉᚵᛒ Fixing Illegal Arguments","ᛞᚫᛉᚵᛒᛍ Fixing Illegal Arguments","ᛞᚫᛉᚵᛒᛍᛣ Fixing Illegal Arguments","ᛞᚫᛉᚵᛒᛍᛣᛤ Fixing Illegal Arguments","ᛞᚫᛉᚵᛒᛍᛣᛤᛄ Fixing Illegal Arguments"]
            ):
            sys.stdout.write('\r' +"\033[31m"+ c+"\033[0m")
            sys.stdout.flush()
            time.sleep(0.0001)
    
    def run_execution():
        print("\n")
        exec("print('SYSTEM TRY ::: EXECUTION!!')")
    
    def announce(num,say):
        datas = {"number":num,"says":say}
        print(json.dumps(datas, indent=4, sort_keys=True))

    def Execute(me):
        if me != "":
            fire = """
 _ _ _  _  ___ _    __    _____ _____ __  _ _  ___  ___   _ _   _  ___ _   
| | | |/ \| o \ |  |  \  | __\ V / __/ _|| | ||_ _|| __| //| \_/ || __|\\  
| V V ( o )   / |_ | o ) | _| ) (| _( (_ | U | | | | _| || | \_/ || _|  |()
 \_n_/ \_/|_|\\___||__() |___/_n_\___\__||___| |_| |___||| |_| |_||___| |()
                                                         \\            //V 

CREATE BY ALIF BUDIMAN
MUSIC BY MILI 'WORLD.EXECUTE(ME);'
                                                                         
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
EXECUTION!!
""" 
            for karakter in fire:
                print(karakter,end="",flush=True)
                time.sleep(0.001)
        