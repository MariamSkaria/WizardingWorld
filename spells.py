import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root",\
                           passwd="student",database="H22_24_20")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE SPELL(SNO INT(3)PRIMARY KEY, \
SPELL VARCHAR(30),\
DESCRIPTION VARCHAR(500)")
mycursor.execute("INSERT INTO Spell VALUES(1,'Aberto','Opens locked doors')")
mycursor.execute("INSERT INTO Spell VALUES(2,'Accio','Summons objects')")
mycursor.execute("INSERT INTO Spell VALUES(3,'Aguamenti','Summons water')")
mycursor.execute("INSERT INTO Spell VALUES(4,'Alohomora','Unlocks objects')")
mycursor.execute("INSERT INTO Spell VALUES(5,'Anapneo','Clears someones airway')")
mycursor.execute("INSERT INTO Spell VALUES(6,'Aparecium','Reveals secret, written messages')")
mycursor.execute("INSERT INTO Spell VALUES(7,'Apparate','A non-verbal transportation spell that \
allows a witch or wizard to instantly travel on the spot and appear at another location \
(Disapparate is the opposite)')")
mycursor.execute("INSERT INTO Spell VALUES(8,'Ascendio','Propels someone into the air')")
mycursor.execute("INSERT INTO Spell VALUES(9,'Avada Kedavra','Also known as The Killing Curse, \
the most evil spell in the Wizarding World; one of three Unforgivable Curses; Harry Potter is the \
only known witch or wizard to survive it')")
mycursor.execute("INSERT INTO Spell VALUES(10,'Avis','Conjures a small flock of birds')")
mycursor.execute("INSERT INTO Spell VALUES(11,'Bat-Bogey Hex','Turns the targets boogers into bats')")
mycursor.execute("INSERT INTO Spell VALUES(12,'Bombardo','Creates an explosion')")
mycursor.execute("INSERT INTO Spell VALUES(13,'Brackium Emendo','Heals broken bones')")
mycursor.execute("INSERT INTO Spell VALUES(14,'Capacious Extremis','Known as the Extension Charm, it \
is a complicated spell that can greatly expand or extend the capacity of an object or space without \
affecting it externally')")
mycursor.execute("INSERT INTO Spell VALUES(15,'Confundo','Known as the Confundus Charm, it causes \
confusion of the target')")
mycursor.execute("INSERT INTO Spell VALUES(16,'Conjunctivitis Curse','Affects the eyes and sight of a target')")
mycursor.execute("INSERT INTO Spell VALUES(17,'Crinus Muto','Changes hair color and style')")
mycursor.execute("INSERT INTO Spell VALUES(18,'Crucio','One of three Unforgivable Curses, it causes \
unbearable pain in the target')")
mycursor.execute("INSERT INTO Spell VALUES(19,'Diffindo','Used to precisely cut an object.')")
mycursor.execute("INSERT INTO Spell VALUES(20,'Disillusionment Charm','Causes the target to take on \
the appearance of its surroundings')")
mycursor.execute("INSERT INTO Spell VALUES(21,'Disapparate','A non-verbal transportation spell that \
allows a witch or wizard to instantly travel on the spot and leave for another location')")
mycursor.execute("INSERT INTO Spell VALUES(22,'Engorgio','Causes rapid growth in the targeted object')")
mycursor.execute("INSERT INTO Spell VALUES(23,'Episkey','Heals minor injuries')")
mycursor.execute("INSERT INTO Spell VALUES(24,'Expecto patronum','The Patronus Charm is a powerful projection\
of hope and happiness that drives away Dementors; a corpeal Patronus takes the the respective animal form\
of the caster, while a non-corpeal appears as a wisp of light; at 13, Harry Potter was the youngest known \
witch or wizard to produce a corpeal Patronus')")
mycursor.execute("INSERT INTO Spell VALUES(25,'Erecto','Allows a witch or wizard to build a structure, like a tent')")            
mycursor.execute("INSERT INTO Spell VALUES(26,'Evanesco','Vanishes objects')")
mycursor.execute("INSERT INTO Spell VALUES(27,'Expelliarmus','Forces an opponent to drop whatever is in their \
possession')")
mycursor.execute("INSERT INTO Spell VALUES(28,'Ferula','A healing charm that conjures wraps and bandages for wounds')")
mycursor.execute("INSERT INTO Spell VALUES(29,' Fidelius Charm','A complex charm that conceals a secret into the \
soul of a chosen ,Secret Keeper if a location is the subject of concealment, it becomes undetectable to others')")
mycursor.execute("INSERT INTO Spell VALUES(30,'Fiendfyre Curse','Conjures destructive, enormous enchanted flames')")
mycursor.execute("INSERT INTO Spell VALUES(31,'Finite Incantatem','A general counter-spell thats used to reverse \
or counter already cast charms')")
mycursor.execute("INSERT INTO Spell VALUES(32,'Furnunculus Curse','A jinx that causes a breakout of boils or pimples')")
mycursor.execute("INSERT INTO Spell VALUES(33,'Geminio','Duplicates objects')")
mycursor.execute("INSERT INTO Spell VALUES(34,'Glisseo','Transforms a staircase into a slide')")
mycursor.execute("INSERT INTO Spell VALUES(35,'Homenum Revelio','Reveals the presence of another person')")
mycursor.execute("INSERT INTO Spell VALUES(36,'Homonculus Charm','Detects anyones true identity and location on a\
piece of parchment used to create the Marauders Map')")
mycursor.execute("INSERT INTO Spell VALUES(37,'Immobulus','Immobilizes living targets')")
mycursor.execute("INSERT INTO Spell VALUES(38,'Impedimenta','A temporary jinx that slows the movement of the target')")
mycursor.execute("INSERT INTO Spell VALUES(39,'Incarcerous','Conjures ropes')")
mycursor.execute("INSERT INTO Spell VALUES(40,'Imperio','One of the three Unforgivable Curses, it places the target \
under the complete control of the caster')")
mycursor.execute("INSERT INTO Spell VALUES(41,'Impervius','Makes an object waterproof')")
mycursor.execute("INSERT INTO Spell VALUES(42,'Incendio','Conjures flames')")
mycursor.execute("INSERT INTO Spell VALUES(43,'Langlock','Causes the targets tongue to stick to the roof of their \
mouth')")
mycursor.execute("INSERT INTO Spell VALUES(44,'Legilimens','Invading or navigating another mind')")
mycursor.execute("INSERT INTO Spell VALUES(45,'Locomotor Mortis','The Leg-Locker curse bounds the targets legs')")
mycursor.execute("INSERT INTO Spell VALUES(46,'Lumos','Illuminates the casters wand')")
mycursor.execute("INSERT INTO Spell VALUES(47,'Morsmordre','Conjures and projects Lord Voldemorts Dark Mark')")
mycursor.execute("INSERT INTO Spell VALUES(48,'Nox','Reverses the lumos charm, extinguishing a wands light')")
mycursor.execute("INSERT INTO Spell VALUES(49,'Obliviate','Erases the targets memory')")
mycursor.execute("INSERT INTO Spell VALUES(50,'Oculus Reparo','Repairs eyeglasses')")
mycursor.execute("INSERT INTO Spell VALUES(51,'Petrificus Totalus,',Temporarily freezes or petrifies the body of\
the target')")
mycursor.execute("INSERT INTO Spell VALUES(52,'Periculum','Conjures flares/red sparks')")
mycursor.execute("INSERT INTO Spell VALUES(53,'Protego','Casts an invisible shield around the caster, protecting \
against spells and objects (except for The Killing Curse)')")

mydb.commit()
