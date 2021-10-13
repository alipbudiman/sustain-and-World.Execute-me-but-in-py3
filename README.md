# sustain++; And World.Execute(me); but in python3


# World.Execute(me);

![Ungu Kuning Hitam Neon Fiksi Ilmiah Seni Kanal YouTube](https://user-images.githubusercontent.com/82330418/137039756-2f5477ce-a791-48cf-a1f2-660896702f39.png)

Whatch Video

https://www.youtube.com/watch?v=OnWktOJHrjQ

code:

https://github.com/alipbudiman/sustain-and-World.Execute-me-but-in-py3/blob/a3735561b17d672bbe1acc6262303b916ee6e460/World.Execute.me.py

installation:
    
    pip3 install pywhatkit && itertools && pytz && numpy && datetime

running:
    
    python3 World.Execute.me.py

# sustain++;

![Ungu Kuning Hitam Neon Fiksi Ilmiah Seni Kanal YouTube (2)](https://user-images.githubusercontent.com/82330418/137043193-aab3ba9f-3c22-409e-8e49-b03a6a6a28fb.png)

Whatch Video

https://www.youtube.com/watch?v=GteSuAwHwFg

code:

https://github.com/alipbudiman/sustain-and-World.Execute-me-but-in-py3/blob/c1132754d8624c6c01e6dc471ca6d549539df896/SustainPP.py

installation:

    pip3 install itertools

running:
    
    python3 SustainPP.py
    
    
# Real Code of Sustain++ (IN JAVA)

https://gist.github.com/laike9m/bbe3b4843b593ff2d3015a0cce2b270e


        /**
         * The goal of this program is to obtain a HEALTHY
         * and SUSTAINABLE relationship, darling.
         *
         * @author Cassie Wei from Mili
         */
        public class sustainPlusPlus {
            public static void main(String[] args) {
                World world = new World();
                Life me = new Ghost();
                Life you = new Ghost();

                /**
                 * If abstraction is the definition of beauty
                 * Are those of us chasing after clarity
                 * A representation of ugly?
                 */
                world.getObjects().sortByAttribute("beauty");
                if (world.getObjects().getFirst().getArtTags().indexOf("abstract") != -1) {
                    me.addPhysicalAttribute("ugly");
                    you.addPhysicalAttribute("ugly");
                }
                world.giveBestAward("ugly", me);
                world.giveBestAward("ugly", you);

                /**
                 * CALL ME MOMMY
                 * JUST LIKE YOUR FANTASY
                 * there is no crime in ideality
                 */
                if (you.getFetishes().searchByType("name calling", "mommy") != -1) {
                    you.addToMemory(me);
                    you.setNicknameFor(you.getMemory(me), "mommy");
                }
                Rule r = new Rule("Oedipus complex is okay", true);
                world.addRule(r);

                /** 
                 * MUX>>>DEMUX
                 * Can't you understand me?
                 * I'm not mine NAND I'm not yours
                 * Ah
                 */
                try {
                    you.decodeMessage(me.codeMessage("I'm not mine NAND I'm not yours", "mux"), "mux");
                } catch (InsufficientIntelligenceQuotientException e) {
                    world.sendMessage("Oh you dummy.", you);
                    me.announce("Ah");
                }

                /**
                 * This can end right here if you don't let it out
                 * Let it out
                 */
                if (you.getThoughts().size() != 0) {
                    try {
                        you.sayTo(you.getThoughts(), me);
                        you.clearThoughts();
                    } catch (TooMuchOfAPussyException e) {
                        world.getRelationship(you, me).end();
                    }
                }

                /**
                 * Give up or give me your all
                 * Tell me now
                 * Tell me now
                 */
                if (you.getMemories(me).getLove() < 0.5) {
                    world.getRelationship(me, you).setSustain(0);
                } else {
                    you.transferThoughts(me);
                    you.transferAttributes(me);

                    //sustain++;
                    world.getRelationship(me, you).increaseSustain();
                }

                // TO BE CONTINUED
            }
        }
