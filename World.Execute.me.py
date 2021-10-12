from time import sleep
from objects import*
from AlipThreading import*

data = {
    "objectCreation":False,
    "Parameter":None,
    "NewWorld":""
}

class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[;1m"
    RESET = "\033[0m"

Complite = False
while Complite == False:
    #World.singAsong()
    cnt = 3
    for x in range(3):
        if cnt != 0:
            print(f"play yout music in {cnt}")
            cnt -= 1
            time.sleep(1)
    print(f"START !!!")
    time.sleep(0.5)
    power_line = False
    World.slow_print(style.RED+"Switch on the power line"+style.RESET,0.03 )
    power_line = True
    print("\n>>> power line : "+str(power_line))
    time.sleep(0.3)
    rtpp = [style.RED+"!!! Remember to put on !!!"+style.RESET,style.RED+"!!! Remember to put on PROTECTION !!!"+style.RESET]
    count =0
    for cc in itertools.cycle(rtpp):
        if count == len(rtpp):
            break
        else:
            sys.stdout.write('\r' + cc)
            time.sleep(1)
            count +=1
            sys.stdout.flush()
    print()
    password = ["ᛞ","ᚫ","ᛉ","ᚵ","ᛒ","ᛍ","ᛣ","ᛤ","ᛄ"]
    World.getPass(password)
    World.slow_print(style.RED+"Lay down your pieces"+style.RESET,0.02 )
    World.layDown()
    World.slow_print(style.RED+"And let's begin"+style.RESET,0.02 )
    World.slow_print(style.GREEN+" OBJECT_CREATION"+style.RESET,0.02 )
    data["objectCreation"] = True
    print("\n>>> object Creation : "+str(data["objectCreation"]))
    time.sleep(0.5)
    World.slow_print(style.GREEN+"\n Fill in my data"+style.RESET,0.04 )
    World.slow_print(style.GREEN+" PARAMETER"+style.RESET,0.0004 )
    World.INITIALIZATION()
    data["Parameter"] = "100%"
    time.sleep(0.2)
    World.slow_print(style.RED+"\n Set up a new World"+style.RESET,0.03  )
    data["NewWorld"] = "setup done"
    print("\n>>> New World : "+str(data["NewWorld"]))
    time.sleep(1)
    if data["objectCreation"] == True and data["Parameter"] == "100%" and data["NewWorld"] == "setup done":
        World.slow_print(style.RED+"\n And let's begin the "+style.RESET,0.02 )
        time.sleep(0.1)
        World.slow_print(style.GREEN+"\n T H E   S I M U L A T I O N \n "+style.RESET,0.001 )
        World.slow_print(style.GREEN+"\n ***************************************** \n "+style.RESET,0.005 )
        time.sleep(0.5)
        World.START_SIMULATION()
        os.system("cls")
        World.prettyPrint(data)
        time.sleep(0.5)
        World.slow_print(style.RED+"\n If I'm a set of "+style.RESET,0.02 )
        World.slow_print(style.RED+"points\n\n"+style.RESET,0.02 )
        point = World.set_of_point()
        data["setOfPoint"] = str(point)
        World.prettyPrint(data)
        if data["setOfPoint"] != "":
            data["im"] = len(data["setOfPoint"])
            World.slow_print(style.RED+"\n Then I will give you "+style.RESET,0.03 )
            World.slow_print(style.RED+" my"+style.RESET,0.04 )
            time.sleep(0.02)
            World.slow_print(style.YELLOW+" DIMENSION"+style.RESET,0.01 )
            World.GiveDimension(data["im"])
            time.sleep(0.2)
            World.slow_print(style.RED+"\n If I'm a "+style.RESET,0.02 )
            World.slow_print(style.RED+"circle\n\n"+style.RESET,0.04 )
            data["Circel"] = len(data["setOfPoint"])
            if data["Circel"] == len(data["setOfPoint"]):
                data["im"] = data["Circel"]
                World.prettyPrint(data)
                World.slow_print(style.RED+"\n Then I will give you "+style.RESET,0.03 )
                World.slow_print(style.RED+" my"+style.RESET,0.04 )
                time.sleep(0.2)
                World.slow_print(style.YELLOW+" CIRCUMFERENCE"+style.RESET,0.01 )
                World.giveCIRCUMFERENCE(data["im"])
                time.sleep(0.1)
                World.slow_print(style.RED+"\n If I'm a "+style.RESET,0.02 )
                World.slow_print(style.RED+"sine wave\n\n"+style.RESET,0.02 )
                data["sineWave"] = "299.792.458"
                if len(data["sineWave"]) == 11:
                    data["im"] = data["sineWave"]
                    time.sleep(0.2)
                    World.prettyPrint(data)
                    World.slow_print(style.RED+"\n Then you can sit "+style.RESET,0.02 )
                    World.slow_print(style.RED+"on all  my"+style.RESET,0.02 )
                    time.sleep(0.2)
                    World.slow_print(style.YELLOW+" TANGENTS______________"+style.RESET,0.0001 )
                    time.sleep(0.2)
                    World.slow_print(style.RED+"\n If I approach  "+style.RESET,0.02 )
                    World.slow_print(style.RED+"infinity\n\n"+style.RESET,0.02 )
                    data["im"] = "INFINITY"
                    if data["im"] == "INFINITY":
                        t1 = thread_with_trace(target=World.loopInfinity)
                        t1.start()
                        time.sleep(1)
                        t1.kill()
                        t1.join()
                        World.slow_print(style.YELLOW+"                  LIMITATIONS\n\n"+style.RESET,0.02 )
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+"\nSwitch my current"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"\nto ----------- > AC"+style.RESET,0.02 )
                        x = World.set_of_point()
                        data["currenct1"] = x
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+" ----------- > DC"+style.RESET,0.02 )
                        y = World.set_of_point()
                        data["currenct2"] = y
                        print("\n>>> Your Current AC at : "+data["currenct1"])
                        print("\n>>> Your Current DC at : "+data["currenct2"])
                        time.sleep(0.5)
                        World.BlindMYVision()
                        World.slow_print(style.GREEN+"\nM  Y       V  I  S  I  O  N"+style.RESET,0.02 )
                        World.slow_print(style.RED+"\nSo dizzy, "+style.RESET,0.04 )
                        time.sleep(0.04)
                        World.slow_print(style.RED+"So dizzy"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"\nOh..., we can travel"+style.RESET,0.02 )
                        time.sleep(0.5)
                        start = time.time()
                        World.slow_print(style.GREEN+"\nFrom ----------- > A.D"+style.RESET,0.02 )
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+" ----------- > B.C"+style.RESET,0.02 )
                        wkwk = time.time() - start
                        print("\n>>> Speed\n>>> Log: {}\n>>> Debug: {}".format(round(wkwk, 3), round(wkwk, 10)))
                        time.sleep(1)
                        World.slow_print(style.RED+"And we can unite"+style.RESET,0.04 )
                        time.sleep(0.2)
                        World.slow_print(style.RED+"\nSo deeply, "+style.RESET,0.02 )
                        World.slow_print(style.RED+"So deeply\n"+style.RESET,0.03 )
                        time.sleep(0.002)
                        storage = str(data)
                        data = {}
                        data = {"unite1":storage}
                        World.prettyPrint(data)
                        time.sleep(1)
                        print(style.MAGENTA+"\nIF I CAN")
                        time.sleep(1)
                        World.slow_print(style.MAGENTA+"IF I CAN "+style.RESET,0)
                        World.slow_print(style.MAGENTA+"give you all "+style.RESET,0.04 )
                        World.slow_print(style.YELLOW+" THE SIMULATIONS"+style.RESET,0.04 )
                        if "AllSimulationAccess" not in data:
                            print(style.RED+"\n>>>SYSTEM ERROR : YOU DONT HAVE ACCESS TO RUN ALL SIMULATION"+style.RESET)
                            data["simulation"] = "ᛞᚫᛉᚵᛒᛍᛣᛤᛄ"
                        else:
                            x = World.GiveAllSumulation()
                            data["simulation"] = x
                        time.sleep(1)
                        print(style.MAGENTA+"\nTHEN I CAN")
                        time.sleep(1)
                        World.slow_print(style.MAGENTA+"THEN I CAN "+style.RESET,0)
                        World.slow_print(style.MAGENTA+"be your only "+style.RESET,0.04 )
                        World.slow_print(style.YELLOW+" SATISFACTION"+style.RESET,0.04 )
                        if data["simulation"] == "ᛞᚫᛉᚵᛒᛍᛣᛤᛄ":
                            print(style.RED+"\n>>>SYSTEM SAYS : SO SAD :'("+style.RESET)
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I can make you happy"+style.RESET,0.02)
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+" Then I'll run the "+style.RESET,0.02)
                        time.sleep(0.2)
                        World.slow_print(style.YELLOW+" E  X  E  C  U  T  I  O  N "+style.RESET,0.001)
                        me = random.choice(["happy","happy","happy","not happy"])
                        if me == "happy":
                            print(World.run_Exec(me))
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : EXECUTION DENAY !!'("+style.RESET)
                        print("\n\n")
                        time.sleep(1)
                        t1 = thread_with_trace(target=World.TRAPPED)
                        t1.start()
                        time.sleep(1)
                        t1.kill()
                        t1.join()
                        print("\n\n")
                        time.sleep(0.3)
                        World.slow_print(style.RED+"\nIn this strange, "+style.RESET,0.02 )
                        World.slow_print(style.RED+"  strange"+style.RESET,0.02 )
                        World.slow_print(style.YELLOW+" SIMULATIONS"+style.RESET,0.02 )
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I'm an eggplant "+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"Then I will give you my "+style.RESET,0.02)
                        World.slow_print(style.YELLOW+"NUTRIENTS"+style.RESET,0.02 )
                        data["you"] = []
                        data["me"] = random.choice(["eggplant","eggplant","eggplant","eggplant-eggplant an"])
                        if data["me"] == "eggplant":
                            print("\n"+World.GET_NUTRIENTS())
                            data["you"].append(World.GET_NUTRIENTS())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET NUTRIENTS DENAY !!'("+style.RESET)
                            data["you"].append("NUTRIENTS DENAY")
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I'm an tomato "+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"Then I will give you "+style.RESET,0.02)
                        World.slow_print(style.YELLOW+"ANTIOXIDANTS"+style.RESET,0.02 )
                        data["me"] = random.choice(["tomato","tomato","tomato","ikan hiu makan tomat"])
                        if data["me"] == "tomato":
                            print("\n"+World.GET_ANTIOXIDANTS())
                            data["you"].append(World.GET_ANTIOXIDANTS())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET ANTIOXIDANTS DENAY !!'("+style.RESET)
                            data["you"].append("ANTIOXIDANTS DENAY")
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I'm a tabby cat "+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"Then I will purr for your "+style.RESET,0.02)
                        World.slow_print(style.YELLOW+"ENJOYMENT"+style.RESET,0.02 )
                        data["me"] = random.choice(["tomato","tomato","tomato","ikan hiu makan tomat"])
                        if data["me"] == "tomato":
                            print("\n"+World.GET_ENJOYMENT())
                            data["you"].append(World.GET_ENJOYMENT())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : GET ENJOYMENT DENAY !!'("+style.RESET)
                            data["you"].append("ENJOYMENT DENAY")
                        time.sleep(0.3)
                        World.slow_print(style.GREEN+"\nIf I'm the only god "+style.RESET,0.04 )
                        time.sleep(0.02)
                        World.slow_print(style.GREEN+"Then your the proof of my "+style.RESET,0.04)
                        World.slow_print(style.YELLOW+"EXISTENCE"+style.RESET,0.04 )
                        data["me"] = random.randint(0,999)
                        if data["me"] == 666:
                            print("\n"+World.GOD_EXISTENCE())
                            data["you"].append(World.GOD_EXISTENCE())
                        else:
                            print(style.RED+"\n>>>SYSTEM ERROR : IM JUST SYSTEM !!'("+style.RESET)
                            data["you"].append("JUST SYSTEM")
                        print("\n\n::: Your ::: ")
                        World.prettyPrint(data["you"])
                        print("\n\n")
                        time.sleep(0.04)
                        World.slow_print(style.RED+"Switch my "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"gender"+style.RESET,0.02 )
                        time.sleep(0.5)
                        World.slow_print(style.GREEN+"\nTo ----------- > F"+style.RESET,0.02 )
                        data["you"].append("GANDER ::: FEMALE")
                        print(style.RED+"\n>>>SYSTEM SAYS : SUCCESS SET TO FEMALE !!"+style.RESET)
                        time.sleep(0.2)
                        World.slow_print(style.GREEN+" ----------- > M"+style.RESET,0.02 )
                        data["you"].remove("GANDER ::: FEMALE")
                        data["you"].append("GANDER ::: MALE")
                        print(style.RED+"\n>>>SYSTEM SAYS : SUCCESS SWITCH TO MALE !!"+style.RESET)
                        time.sleep(0.04)
                        World.slow_print(style.RED+"And then do "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"whatever"+style.RESET,0.02 )
                        World.slow_print(style.GREEN+"\nTo ----------- > AM"+style.RESET,0.02 )
                        x = World.GetTimeNow()
                        timess = str(x)
                        data["you"].append(f"TIME ::: {timess} AM")
                        print(style.RED+f"\n>>>SYSTEM SAYS : {x} AM"+style.RESET)
                        data["you"].remove(f"TIME ::: {timess} AM")
                        World.slow_print(style.GREEN+"\nTo ----------- > PM"+style.RESET,0.02 )
                        x = World.GetTimeNow()
                        tmiexx = str(x)
                        print(style.RED+f"\n>>>SYSTEM SAYS : {tmiexx} PM"+style.RESET)
                        data["you"].append(f"TIME ::: {tmiexx} PM")
                        time.sleep(0.04)
                        World.slow_print(style.RED+"I will switch "+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"my role"+style.RESET,0.02 )
                        World.slow_print(style.GREEN+"\nTo ----------- > S"+style.RESET,0.02 )
                        data["you"].append(f"ROLE ::: S")
                        print(style.RED+f"\n>>>SYSTEM SAYS : SET ROLE TO 'S'"+style.RESET)
                        World.slow_print(style.GREEN+"\nTo ----------- > M"+style.RESET,0.02 )
                        print(style.RED+f"\n>>>SYSTEM SAYS : CHANGE ROLE TO 'M'"+style.RESET)
                        data["you"].remove(f"ROLE ::: S")
                        data["you"].append(f"ROLE ::: M")
                        time.sleep(0.05)
                        World.slow_print(style.RED+"\nSo we can enter "+style.RESET,0.08 )
                        World.slow_print(style.GREEN+"the trance,"+style.RESET,0.04 )
                        World.slow_print(style.GREEN+"the trance"+style.RESET,0.04 )
                        time.sleep(0.5)
                        World.EnterTrance("WorldExecuteMe.py")
                        print(style.MAGENTA+"\nIF I CAN")
                        time.sleep(1)
                        World.slow_print(style.MAGENTA+"IF I CAN "+style.RESET,0)
                        World.slow_print(style.MAGENTA+" feel your"+style.RESET,0.04)
                        World.slow_print(style.YELLOW+" VIBRATIONS"+style.RESET,0.02)
                        time.sleep(1)
                        print(style.BLUE+"\nThen I can")
                        time.sleep(1)
                        World.slow_print(style.BLUE+"Then I can "+style.RESET,0)
                        World.slow_print(style.BLUE+" finally be"+style.RESET,0.08)
                        World.slow_print(style.BOLD+" C O M P L E T I O N"+style.RESET,0.03)
                        Complite = True

World.prettyPrint(data)
print("\n\n\n\n")
World.slow_print(style.RED+"\n Though you have left"+style.RESET,0)
data = {}
for x in range(4):
    World.slow_print(style.RED+"\n You have left"+style.RESET,0.04)
    if data == {}:
        print(style.RED+f"\n>>>SYSTEM ERROR : CAN'T LEFT SIMULATION"+style.RESET)
World.slow_print(style.BOLD+"\n You have left me in"+style.RESET,0.02)
World.slow_print(style.YELLOW+" ISOLATION"+style.RESET,0.03)
data["status"] = {"ISOLATION":True}
World.prettyPrint(data)
sleep(0.5)
print(style.MAGENTA+"\nIF I CAN")
time.sleep(1)
World.slow_print(style.MAGENTA+"IF I CAN "+style.RESET,0)
World.slow_print(style.MAGENTA+" erase all the pointless"+style.RESET,0.04)
World.slow_print(style.YELLOW+" FRAGMENTS"+style.RESET,0.02)
World.slow_print(style.GREEN+"\nThen maybe"+style.RESET,0.02)
World.slow_print(style.GREEN+"\nThen maybe,  "+style.RESET,0.02)
World.slow_print(style.GREEN+" you won't leave me so  "+style.RESET,0.02)
World.slow_print(style.YELLOW+" DISHEARTENED"+style.RESET,0.02)
print("\n\n")
time.sleep(1)
t1 = thread_with_trace(target=World.ChallengingYourGod)
t1.start()
time.sleep(3)
t1.kill()
t1.join()
World.slow_print(style.RED+"\n !! Warning "+style.RESET,0)
World.slow_print(style.YELLOW+" # You have made some  !!"+style.RESET,0.05)
try:
    x = [1,2,3]
    print(x[99])
except:
    time.sleep(1)
    World.slow_print(style.RED+"\n>>>SYSTEM ERROR : "+style.RESET,0)
    World.slow_print(style.RED+" IllegalArgumentException  !!\n"+style.RESET,0.1)

xxnx = thread_with_trace(target=World.FxingIllegalArgument)
xxnx.start()
time.sleep(10)
xxnx.kill()
xxnx.join()
print("\n")
# EXECUTION
time.sleep(1)
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EXECUTION
time.sleep(0.5)
World.run_execution()
# EIN
time.sleep(0.7)
World.announce("1", "EIN") # ein; German
# DOS
time.sleep(0.7)
World.announce("2", "DOS") # dos; Español
# TROIS
time.sleep(0.7)
World.announce("3", "TROIS") # trois; French
# NE
time.sleep(0.7)
World.announce("4", "NE") # 넷; Korean
# FEM
time.sleep(0.7)
World.announce("5", "FEM") # fem; Swedish
# LIU
time.sleep(0.7)
World.announce("6", "LIU") # 六; Chinese
# EXECUTION
time.sleep(0.7)
World.run_execution()


print(style.MAGENTA+"\nIF I CAN")
time.sleep(1)
World.slow_print(style.MAGENTA+"IF I CAN, "+style.RESET,0)
World.slow_print(style.MAGENTA+" give you all the"+style.RESET,0.04)
World.slow_print(style.YELLOW+" EXECUTION"+style.RESET,0.02)
print(style.BLUE+"\nThen I can")
time.sleep(1)
World.slow_print(style.BLUE+"Then I can, "+style.RESET,0)
World.slow_print(style.BLUE+" be your only"+style.RESET,0.08)
World.slow_print(style.BOLD+" E  X  E  C  U  T  I  O  N"+style.RESET,0.03)

sleep(0.5)
World.slow_print(style.MAGENTA+"\nIF I CAN, "+style.RESET,0)
World.slow_print(style.MAGENTA+" have you back"+style.RESET,0.04)
World.slow_print(style.BLUE+"\nThen I will, "+style.RESET,0)
World.slow_print(style.BLUE+" run the"+style.RESET,0.08)
World.slow_print(style.BOLD+" E  X  E  C  U  T  I  O  N\n"+style.RESET,0.03)
trapz = thread_with_trace(target=World.TRAPPED)
trapz.start()
time.sleep(1)
trapz.kill()
trapz.join()
World.slow_print(style.RED+"\nWe are trapped ah .... "+style.RESET,0.04)

time.sleep(1)
World.slow_print(style.BLUE+"\nI've studied"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.BLUE+" I've studied"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.BLUE+" how to properly"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.BLUE+" LO"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.BLUE+" -O-"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.BLUE+" OVE"+style.RESET,0)
time.sleep(1)
World.slow_print(style.RED+"\nQuestion me"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" Question me"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" I can answer all"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" LO"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" -O-"+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" OVE"+style.RESET,0)
time.sleep(1)
World.slow_print(style.RED+"\nI know the "+style.RESET,0)
time.sleep(0.5)
World.slow_print(style.RED+" algebraic expression of"+style.RESET,0)
time.sleep(1)
World.slow_print(style.RED+" LO"+style.RESET,0)
time.sleep(0.2)
World.slow_print(style.RED+" -O-"+style.RESET,0)
time.sleep(0.2)
World.slow_print(style.RED+" OVE"+style.RESET,0)
time.sleep(1.2)
World.slow_print(style.RED+"\nThough you are free\n\n"+style.RESET,0.04)
trapz = thread_with_trace(target=World.IMTRAPPED)
trapz.start()
time.sleep(1)
trapz.kill()
trapz.join()
World.slow_print(style.RED+"\ntrapped in"+style.RESET,0.04)
time.sleep(0.1)
World.slow_print(style.RED+" LO"+style.RESET,0)
time.sleep(0.1)
World.slow_print(style.RED+" -O-"+style.RESET,0)
time.sleep(0.1)
World.slow_print(style.RED+" OVE"+style.RESET,0)
me = "Code by Alif Budiman, Music by Mili"
World.Execute(me)

                    



                    


