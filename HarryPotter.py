from tkinter import *
import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk

# Initialize the main window
root=Tk()
root.title("WIZARDING WORLD")
root.geometry("2000x2000")
root.configure(bg='burlywood4')

# Header Frame
H=LabelFrame(root,bd=2,relief="groove",bg="burlywood4")
H.place(x=0,y=0,width=2020,height=65)
label_logo=Label(H,bg="burlywood4")
label_logo.grid(row=0,column=0)

# Load the header logo image
image_logo_large=ptk.PhotoImage(p.Image.open("Images\Logo2.jpg"))

# Add title and tagline in the header frame
name=Label(H,text="",font="arial 20 bold italic",bg="burlywood4",fg="black").grid(row=0,column=1)
tagline=Label(H,text="WIZARDING WORLD",font="algerian 40",fg="white",bg="burlywood4").grid(row=0,column=2,padx=530)

# Main Content Frame
P_frame=LabelFrame(root,bd=2,relief="groove",text="",font="arial 16 bold",fg="burlywood4")
P_frame.place(x=370,y=110,width=908,height=510)
P_frame.configure(bg='burlywood4')

# Display the large logo inside the content frame
label_logo_large=Label(P_frame,image=image_logo_large,bd=2,bg="grey18").place(x=0,y=0)

# Sidebar Frame
H.place
B_frame=LabelFrame(root,bd=2,relief="groove",bg="burlywood4")
B_frame.place(x=2,y=120,width=350,height=480)

# Add labels for different sidebar options
B_1=Label(B_frame,text="| INTRODUCTION |",font="TimesNewRoman 15",fg="cornsilk1",bg="burlywood4")
B_2=Label(B_frame,text="| SUMMARY OF THE BOOKS |",font="TimesNewRoman 15",fg="cornsilk1",bg="burlywood4")
B_3=Label(B_frame,text="| SORTING |",font="TimesNewRoman 15",fg="cornsilk1",bg="burlywood4")
B_4=Label(B_frame,text="| SPELLS |",font="TimesNewRoman 15",fg="cornsilk1",bg="burlywood4")
B_5=Label(B_frame,text="| QUIZ |",font="TimesNewRoman 15",fg="cornsilk1",bg="burlywood4")

# Arrange sidebar options in a grid
B_1.grid(row=0,column=0,padx=10,pady=30)
B_2.grid(row=1,column=0,padx=10,pady=30)
B_3.grid(row=2,column=0,padx=10,pady=30)
B_4.grid(row=3,column=0,padx=10,pady=30)
B_5.grid(row=4,column=0,padx=10,pady=30)
B_frame.place

# Footer Content in Main Content Frame
P_1=Label(P_frame,text="CLOSE TO CONTINUE",font="impact 20",fg="black",bg="burlywood4")
P_1.grid(row=3,column=5,padx=690,pady=460)'

# Run the main loop to display the window
root.mainloop()
#Introduction line
def intro():
    print("""Hey welcome to Pottermore. A miniature form of Harry Potter Official site 'Wizarding World'.
    This hub is for fans of Harry Potter and Fantastic Beasts. The website contains images,quizes, and many more from the Harry Potter and Fantastic
    Beasts films.""")

#Summary 
def summarize_text():
    return "\n Wish you found that helpful \n"

#Sorting hat quiz
def sortinghouse():
    gryffindor=0
    ravenclaw=0
    hufflepuff=0
    slytherin=0
    print("\nHarry Potter House Quiz:\nFind y5our perfect house!\n")
    print("\nAre you wondering which Hogwarts house do you belong to? This Harry Potter House quiz will give you the answer. In the Harry Potter series,the four Houses of Hogwarts are called Hufflepuff, Gryffindor, Slytherin, and Ravenclaw. Each house has its majestic history. They have given the world some of the most outstanding wizards and witches. If you are a true Potterhead, you must have imagined yourself in Hogwarts. But if you are confused about which house you'll fit in, look no further and take this Hogwarts House quiz to find out.\n")

    print("\nQuestion 1:You are trapped in a burning building and only 10 seconds to get out.What would you do?\n")
    print("(a) Save myself,of course!")
    print("(b) Run and grab my friend who is still in the building.")
    print("(c) It depends, if I have a way to save my friends,then yes, but if there's no way,then I am above everbody else.")
    print("(d) I'll try, but i am not sure!\n")
    q_1=input("Answer:")
    if q_1=='d':
        gryffindor+=1
    elif q_1=='b':
        ravenclaw+=1
    elif q_1=='c':
        hufflepuff+=1
    elif q_1=='a':
        slytherin+=1
    else:
        print("Invalid")
    print("\nQuestion 2:What smell is most appealing to you\n")
    print("(a) home")
    print("(b) Sea")
    print("(c) fresh parchment")
    print("(d) a log fire\n")
    q_2=input("Answer:")
    if q_2=='a':
        hufflepuff+=1
    elif q_2=="b":
        gryffindor+=1
    elif q_2=='c':
        ravenclaw+=1
    elif q_2=='d':
        slytherin+=1
    else:
        print("Invalid")
    print("\nQuestion 3:During the end-of-year exams, you notice that one of your classmates was using an enchanted quill.You come top of the class anyway, but they are second. What do you do?\n")
    print("(a) tell the professor immediately -cheating is wrong ,no matter what ")
    print("(b) nothing ,but if I hadn't come top of the class I would definitely tell the professor")
    print("(c) encourage the other student to admit what they'd done to the professor")
    print("(d) give them a high five for managing to sneak the quill into the exam\n")
   
    q_3=input("Answer:")
    if q_3=='c':
        hufflepuff+=1
    elif q_3=="a":
        gryffindor+=1
    elif q_3=='b':
        ravenclaw+=1
    elif q_3=='d':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 4:Which is your favorite location when you want to spend some free time?\n")
    print("(a) library")
    print("(b) any dark place")
    print("(c) cafe")
    print("(d) forest\n")
    q_4=input("Answer:")
    if q_4=='c':
        hufflepuff+=1
    elif q_4=="d":
        gryffindor+=1
    elif q_4=='a':
        ravenclaw+=1
    elif q_4=='b':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 5: What's your best trait you think you have got?\n")
    print("(a)bravery")
    print("(b)loyalty")
    print("(c)ambition")
    print("(d)intelligence\n")
    
    q_5=input("Answer:")
    if q_5=='b':
        hufflepuff+=1
    elif q_5=="a":
        gryffindor+=1
    elif q_5=='d':
        ravenclaw+=1
    elif q_5=='c':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 6: Which color do you love to wear the most?\n")
    print("(a) black")
    print("(b) white")
    print("(c) red")
    print("(d) blue\n")
    q_6=input("Answer:")
    if q_6=='d':
        hufflepuff+=1
    elif q_6=="c":
        gryffindor+=1
    elif q_6=='b':
        ravenclaw+=1
    elif q_6=='a':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 7: People know you as___ \n")
    print("(a) brave ")
    print("(b) wicked")
    print("(c) loyal")
    print("(d) smart\n")
    q_7=input("Answer:")
    if q_7=='c':
        hufflepuff+=1
    elif q_7=="a":
        gryffindor+=1
    elif q_7=='d':
        ravenclaw+=1
    elif q_7=='b':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 8: If given a choice, which house do you wish to be in?\n ")
    print("(a) gryffindor ")
    print("(b) slytherin")
    print("(c) hufflepuff  ")
    print("(d) ravenclaw \n")
    q_8=input("Answer:")
    if q_8=='c':
        hufflepuff+=1
    elif q_8=="a":
        gryffindor+=1
    elif q_8=='d':
        ravenclaw+=1
    elif q_8=='b':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 9: Have you ever cheated in classes? \n")
    print("(a) never")
    print("(b) I have only shared answers to friends in need.")
    print("(c) I cheat any moment I get the opportunity. ")
    print("(d) sometimes.\n")
    q_9=input("Answer:")
    if q_9=='b':
        hufflepuff+=1
    elif q_9=="d":
        gryffindor+=1
    elif q_9=='a':
        ravenclaw+=1
    elif q_9=='c':
        slytherin+=1
    else:
        print("Invalid")

    print("\nQuestion 10:What is your favorite animal? \n")
    print("(a) eagle ")
    print("(b) snake")
    print("(c) cat ")
    print("(d) owl\n")

    q_10=input("Answer:")
    if q_10=='c':
        hufflepuff+=1
    elif q_10=="a":
        gryffindor+=1
    elif q_10=='d':
        ravenclaw+=1
    elif q_10=='b':
        slytherin+=1
    else:
        print("Invalid")

    if gryffindor>ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
        return "\n\n\nGRYFFINDOR!!!!!\n\n\n"
    elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
        return "\n\n\nRAVENCLAW!!!!!\n\n\n"
    elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
        return "\n\n\nHUFFLEPUFF!!!!!\n\n\n"
    elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
        return "\n\n\nSLYTHERIN!!!!!\n\n\n"
    else:
        print("\n\n\nToo difficult to decide... Maybe this quiz needs more questions.\n\n\n")
def quiz2():
    mark=0
    print('\n\nQuiz begins...\n\n')
    ##print()
   
    print('''\n\nQUESTION 1
From which platform at Kings Cross does the Hogwarts Express train depart?\n
    a)Gringotts
    b)Wand
    c)Nine and three-quaters
    d)The trolls club\n''')
    opt=input('Answer:')
    if opt=='c':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option c')
        print('\n')
       
    print('''\n\nQUESTION 2
Harry has a scar on his forehead. What shape is it?\n
    a)Like a pigs tail
    b)Like a lightning bolt
    c)Like a shining star
    d)Like an egg\n''')
    opt=input('Answer:')
    if opt=='b':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option b\n')
    print()

    print('''\n\nQUESTION 3
Hermiones parents are not wizards. What non-wizard jobs do they do?\n
    a)Physician
    b)Tailor
    c)Dentists
    d)Mechanic\n''')
    opt=input('Answer:')
    if opt=='c':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option c\n')
    print()
    print('''\n\nQUESTION 4
How do the Dursleys say that Harrys parents died?\n
    a)In a car crash
    b)In an aeroplane crash
    c)By heart attack
    d)By cancer\n''')
    opt=input('Answer:')
    if opt=='a':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option a\n')
    print()

    print('''\n\nQUESTION 5
How old was Voldemort when he opened the Chamber of Secrets?\n
    a)15 years
    b)16 years
    c)17 years
    d)18 years\n''')
    opt=input('Answer:')
    if opt=='b':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option b\n')
    print()

    print('''\n\nQUESTION 6
In their second year, Hermione drank Polyjuice Potion that gave her lasting rat-like features.\n
    a)True statememt
    b)False statement\n''')
    opt=input('Answer:')
    if opt=='b':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option b\n')
    print()
    print('''\n\nQUESTION 7
On a Quidditch pitch, how many goal posts are there in total?\n
    a)5
    b)6
    c)4
    d)3\n''')
    opt=input('Answer:')
    if opt=='d':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option d\n')
    print()

    print('''\n\nQUESTION 8
 What does Hagrid name his baby dragon?\n
    a)Fluffy
    b)Hedwig
    c)Baby dragon
    d)Norbert\n''')
    opt=input('Answer:')
    if opt=='d':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option d\n')
    print()

    print('''\n\nQUESTION 9
Sirius Black was sorted into Slytherin house.\n
    a)True statememt
    b)False statement\n''')
    opt=input('Answer:')
    if opt=='b':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option b\n')
    print()

    print('''\n\nQUESTION 10
What is the term for non-magical people?\n
    a)Dentists
    b)Muggles
    c)Wizards
    d)Hogwarts\n''')
    opt=input('Answer:')
    if opt=='b':
        print('\ncorrect answer\n')
        mark+=1
    else:
        print('\nincorrect answer\n')
        print('\ncorrect answer is option b\n')
    print()

    print('\ncongragulations...you have completed the quiz\n')
    print('\n\nYOUR SCORE\n\n')
    print('\t',mark,'/10')

def get_user_choice():
    while True:
        try:
            print("So how do you wish to start\n")
            print("1. Summary of books(advised only if you haven't watched the movies)\n")
            print("2. Sorting Hat\n")
            print("3. Table of spells\n")
            print("4. Harry Potter Quiz\n")
            print("5. Exit \n")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                bookname = input("\nSummary of which book do you want\n\n1.HARRY POTTER AND THE PHILOSOPHER STONE\n\n2.HARRY POTTER BOOK AND THE CHAMBER OF SECRETS\n\n3.HARRY POTTER AND THE PRISONER OF AZKABAN\n\n4.HARRY POTTER AND THE GOBLET OF FIRE\n\n5.HARRY POTTER AND THE ORDER OF PHEONIX\n\n6.HARRY POTTER AND THE HALF BLOOD PRINCE\n\n7.HARRY POTTER BOOK AMD THE DEATHLY HALLOWS\n\n Enter the number corresponding to your choice: ")
                if bookname== '1':
                    summary = summarize_text()
                    print("""\nSummary:
Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J. K. Rowling. The first novel in the Harry Potter series and Rowling's debut novel, it follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry. Harry makes close friends and a few enemies during his first year at the school and with the help of his friends, Ron Weasley and Hermione Granger, he faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harry's parents, but failed to kill Harry when he was just 15 months old.
  The book was first published in the United Kingdom on 26 June 1997 by Bloomsbury. It was published in the United States the following year by Scholastic Corporation under the title Harry Potter and the Sorcerer's Stone. It won most of the British book awards that were judged by children and other awards in the US. The book reached the top of the New York Times list of best-selling fiction in August 1999 and stayed near the top of that list for much of 1999 and 2000. It has been translated into at least 73 other languages and has been made into a feature-length film of the same name, as have all six of its sequels. The novel has sold in excess of 120 million copies, making it the third best-selling book of all time.""")
                    print(summary)
                elif bookname=='2':
                    summary = summarize_text()
                    print("""\nSummary:
Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series. The plot follows Harry's second year at Hogwarts School of Witchcraft and Wizardry, during which a series of messages on the walls of the school's corridors warn that the "Chamber of Secrets" has been opened and that the "heir of Slytherin" would kill all pupils who do not come from all-magical families. These threats are found after attacks that leave residents of the school petrified. Throughout the year, Harry and his friends Ron and Hermione investigate the attacks.
  The book was published in the United Kingdom on 2 July 1998 by Bloomsbury and later in the United States on 2 June 1999 by Scholastic. Although Rowling says she found it difficult to finish the book, it won high praise and awards from critics, young readers, and the book industry, although some critics thought the story was perhaps too frightening for younger children.""")
                   
                    print(summary)
                elif bookname=='3':
                    summary = summarize_text()
                    print("""\nSummary:
Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author J. K. Rowling and is the third in the Harry Potter series. The book follows Harry Potter, a young wizard, in his third year at Hogwarts School of Witchcraft and Wizardry. Along with friends Ronald Weasley and Hermione Granger, Harry investigates Sirius Black, an escaped prisoner from Azkaban, the wizard prison, believed to be one of Lord Voldemort's old allies.
   The book was published in the United Kingdom on 8 July 1999 by Bloomsbury and in the United States on 8 September 1999 by Scholastic, Rowling found the book easy to write, finishing it just a year after she began writing it. The book sold 68,000 copies in just three days after its release in the United Kingdom and since has sold over three million in the country.The book won the 1999 Whitbread Children's Book Award, the Bram Stoker Award, and the 2000 Locus Award for Best Fantasy Novel and was short-listed for other awards, including the Hugo.
   The film adaptation of the novel was released in 2004, grossing more than $796 million and earning critical acclaim. Video games loosely based on Harry Potter and the Prisoner of Azkaban were also released for several platforms, and most obtained favourable reviews.""")
                 
                    print(summary)
                elif bookname=='4':
                    summary = summarize_text()
                    print("""Summary:
Harry Potter and the Goblet of Fire is a fantasy novel written by British author J. K. Rowling and the fourth novel in the Harry Potter series. It follows Harry Potter, a wizard in his fourth year at Hogwarts School of Witchcraft and Wizardry, and the mystery surrounding the entry of Harry's name into the Triwizard Tournament, in which he is forced to compete.
   The book was published in the United Kingdom by Bloomsbury and in the United States by Scholastic. In both countries, the release date was 8 July 2000. This was the first time a book in the series was published in both countries at the same time. The novel won a Hugo Award, the only Harry Potter novel to do so, in 2001. The book was adapted into a film, released worldwide on 18 November 2005, and a video game by Electronic Arts.""")
                 
                    print(summary)
                elif bookname=='5':
                    summary = summarize_text()
                    print("""\nSummary:
Harry Potter and the Order of the Phoenix is a fantasy novel written by British author J. K. Rowling and the fifth novel in the Harry Potter series. It follows Harry Potter's struggles through his fifth year at Hogwarts School of Witchcraft and Wizardry, including the surreptitious return of the antagonist Lord Voldemort, O.W.L. exams, and an obstructive Ministry of Magic. The novel was published on 21 June 2003 by Bloomsbury in the United Kingdom, Scholastic in the United States, and Raincoast in Canada. It sold five million copies in the first 24 hours of publication.
   Harry Potter and the Order of the Phoenix won several awards, including the American Library Association Best Book Award for Young Adults in 2003. The book was also made into a 2007 film, and a video game by Electronic Arts.""")
                   
                    print(summary)
                elif bookname=='6':
                    summary = summarize_text()
                    print("""\nSummary:
Harry Potter and the Half-Blood Prince is a fantasy novel written by British author J. K. Rowling and the sixth and penultimate novel in the Harry Potter series. Set during Harry Potter's sixth year at Hogwarts, the novel explores the past of the boy wizard's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.
   The book was published in the United Kingdom by Bloomsbury and in the United States by Scholastic on 16 July 2005, as well as in several other countries. It sold almost seven million copies in the first 24 hours after its release, a record eventually broken by its sequel, Harry Potter and the Deathly Hallows. There were many controversies before and after it was published, including the right-to-read copies delivered before the release date in Canada. Reception to the novel was generally positive, and it won several awards and honours, including the 2006 British Book of the Year award.
   Reviewers noted that the book had a darker tone than its predecessors, though it did contain some humour. Some considered the main themes love, death, trust, and redemption. The considerable character development of Harry and many other teenage characters also drew attention.""")
                 
                    print(summary)
                elif bookname=='7':
                    summary = summarize_text()
                    print("""Summary:
Harry Potter and the Deathly Hallows is a fantasy novel written by British author J. K. Rowling and the seventh and final novel in the Harry Potter series. It was released on 21 July 2007 in the United Kingdom by Bloomsbury Publishing, in the United States by Scholastic, and in Canada by Raincoast Books. The novel chronicles the events directly following Harry Potter and the Half-Blood Prince (2005) and the final confrontation between the wizards Harry Potter and Lord Voldemort.
   Deathly Hallows shattered sales records upon release, surpassing marks set by previous titles of the Harry Potter series. It holds the Guinness World Record for most novels sold within 24 hours of release, with 8.3 million sold in the US and 2.65 million in the UK. Reception to the book was generally positive, and the book won the 2008 Colorado Blue Spruce Book Award, and the American Library Association named it the "Best Book for Young Adults". A play, Harry Potter and the Cursed Child, was written by Jack Thorne, and based on an original story written by J. K. Rowling, John Tiffany, and Thorne, premiering at the Palace Theatre in London on 30 July 2016. Rowling has referred to the play as "the eighth Harry Potter story", and is set nineteen years after the events of the Deathly Hallows, effectively picking up where the epilogue of the seventh book ended.
   A film adaptation of the novel was released in two parts: Harry Potter and the Deathly Hallows – Part 1 in November 2010 and Part 2 in July 2011.""")
                    print(summary)
                else:
                    print('sorry not yet a book')

            elif choice == 2:
                print("\nSorting:",sortinghouse())
            elif choice == 3:
                import mysql.connector
                mydb=mysql.connector.connect(host="localhost",user="root",\
                                 passwd="mariam",database="harrypotter")
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * from spell")
                for x in mycursor:
                    print(x)
            elif choice == 4:
                print("\nQuiz:",quiz2())
            elif choice == 5:
                print("\n THANK YOU \n Exiting...")
                break

            else:
                print("Invalid choice. Please enter the right choice.")
               
        except ValueError:
            print("Invalid choice. Please enter a number.")
                 
intro()
get_user_choice()

