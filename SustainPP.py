import time, sys, itertools, os
from AlipThreading import*



class SustainPlusPlus:
    
    def slow_print(text:str,speed):
        for karakter in text:
            print(karakter,end="",flush=True)
            time.sleep(speed)



    def glitch_print(text:str,times):
        def thed():
            listx = [text,text,text,text,text,text,text,text,text,text,text,text,text,text," "+text+" "," "+text,text+" "]
            for c in itertools.cycle(listx):
                    sys.stdout.write('\r' + c)
                    time.sleep(0.001)
        t1 = thread_with_trace(target=thed)
        t1.start()
        time.sleep(times)
        t1.kill()
        t1.join()



    def Load():
        print("play your music in")
        time.sleep(1)
        for x in range(2):
            print("# :::::: ",x+1)
            time.sleep(1)
        print("# :::::: start")



    def ex():
        os.system("cls")



    def ex1():
        time.sleep(1)
        SustainPlusPlus.slow_print("/**\n* ",0)
        SustainPlusPlus.slow_print("If abstraction",0.2) #1
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" is the definition",0.15)
        time.sleep(0.7)
        SustainPlusPlus.slow_print(" of...  ",0.2)
        time.sleep(1.5)
        SustainPlusPlus.slow_print(" beauty... ",0.2)
        time.sleep(3.5)
        print("\n")
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("Are those",0.2) #16
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" of us",0.1)
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" chasing",0.1)
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" after ",0.2)
        SustainPlusPlus.slow_print("clar",0.4)
        time.sleep(2)
        SustainPlusPlus.slow_print("rity ....",0.2)
        time.sleep(2.4)
        print("\n")
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("A representation",0.15) #31
        SustainPlusPlus.slow_print(" of ugly ... ?",0.2)
        SustainPlusPlus.slow_print("\n*/",0)
        time.sleep(2)



    def ex2():
        print("\n")
        SustainPlusPlus.slow_print("/**\n",0)
        SustainPlusPlus.glitch_print("CALL ME MOMMY",1) #38
        time.sleep(0.3)
        print("\n")
        SustainPlusPlus.glitch_print("JUST LIKE YOUR FANTASY",1)
        time.sleep(1)
        print("\n")
        SustainPlusPlus.glitch_print("there is no crime           ",1)
        time.sleep(0.8)
        SustainPlusPlus.glitch_print("there is no crime in        ",1)
        time.sleep(0.5)
        SustainPlusPlus.glitch_print("there is no crime in IDEALITY",1)
        SustainPlusPlus.slow_print("\n*/",0)
        time.sleep(0.2)



    def ex3():
        print("\n")
        SustainPlusPlus.slow_print("/**\n",0)
        SustainPlusPlus.glitch_print("MUX ",0.5) #46
        time.sleep(0.2)
        SustainPlusPlus.glitch_print("MUX >>> DEMUX",1) 
        time.sleep(0.25)
        print("\n")
        SustainPlusPlus.glitch_print("Can't you understand me?",1) 
        time.sleep(0.4)
        print("\n")
        SustainPlusPlus.slow_print("I'm not mine NAND I'm not yours",0.05)
        time.sleep(0.45)
        SustainPlusPlus.slow_print(" Ah ... ",0.05)
        SustainPlusPlus.slow_print("\n*/",0)
        time.sleep(1)



    def ex4():
        print("\n")
        SustainPlusPlus.slow_print("/**\n",0)
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("This.. can...",0.2) #54
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" end right here",0.2)
        SustainPlusPlus.slow_print(" if you don't",0.05)
        time.sleep(0.5)
        SustainPlusPlus.slow_print(" let it out...  ",0.2)
        time.sleep(0.6)
        print("\n")
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("Let it out...      ",0.15)
        SustainPlusPlus.slow_print("\n*/",0)
        time.sleep(1)
    
    def ex5():
        print("\n")
        SustainPlusPlus.slow_print("/**\n",0)
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("Give up ...",0.2) #54
        time.sleep(0.2)
        SustainPlusPlus.slow_print(" or give me your all",0.2)
        time.sleep(0.2)
        print("\n")
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("Tell me now ...",0.3)
        time.sleep(0.2)
        print("\n")
        SustainPlusPlus.slow_print("* ",0)
        SustainPlusPlus.slow_print("Tell me now ...",0.15)
        SustainPlusPlus.slow_print("\n*/",0)
        print("\n")
        SustainPlusPlus.slow_print("..........",0.1)
        time.sleep(0.2)
        print("\n")

def write():
    x = """

public class sustainPlusPlus {
    public static void main(String[] args) {
        World world = new World();
        Life me = new Ghost();
        Life you = new Ghost();
    """
    print(x)

def write1():
    x = """

        world.getObjects().sortByAttribute("beauty");
        if (world.getObjects().getFirst().getArtTags().indexOf("abstract") != -1) {
            me.addPhysicalAttribute("ugly");
            you.addPhysicalAttribute("ugly");
        }
        world.giveBestAward("ugly", me);
        world.giveBestAward("ugly", you);
    """
    print(x)

def write2():
    x = """

        if (you.getFetishes().searchByType("name calling", "mommy") != -1) {
            you.addToMemory(me);
            you.setNicknameFor(you.getMemory(me), "mommy");
        }
        Rule r = new Rule("Oedipus complex is okay", true);
        world.addRule(r);
    """
    print(x)

def write3():
    x = """

        try {
            you.decodeMessage(me.codeMessage("I'm not mine NAND I'm not yours", "mux"), "mux");
        } catch (InsufficientIntelligenceQuotientException e) {
            world.sendMessage("Oh you dummy.", you);
            me.announce("Ah");
        }
    """
    print(x)

def write4():
    x = """

        if (you.getThoughts().size() != 0) {
            try {
                you.sayTo(you.getThoughts(), me);
                you.clearThoughts();
            } catch (TooMuchOfAPussyException e) {
                world.getRelationship(you, me).end();
            }
        }
    """
    print(x)

def write5():
    x = """

        if (you.getMemories(me).getLove() < 0.5) {
            world.getRelationship(me, you).setSustain(0);
        } else {
            you.transferThoughts(me);
            you.transferAttributes(me);

            //sustain++;
            world.getRelationship(me, you).increaseSustain();
        }
    """
    print(x)


#system
def World():
    SustainPlusPlus.Load()
    SustainPlusPlus.ex();write()
    SustainPlusPlus.ex1();write1()
    SustainPlusPlus.ex2();write2()
    SustainPlusPlus.ex3();write3()
    SustainPlusPlus.ex4();write4()
    SustainPlusPlus.ex5();write4()

def Sustain_P_P():
    World()
    time.sleep(1)
    for x in range(15000):
        SustainPlusPlus.slow_print("GHOST IN THE SHELL ",0)


#sustain++;
#Mili - sustain++; (ending ver.)
#Ghost In The Shell: SAC_2045 Ending Theme
#This java code show in console made by Mili
#code for Running Text with Python3, by Alif Budiman
Sustain_P_P()
