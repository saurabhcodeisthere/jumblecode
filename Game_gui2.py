from tkinter import *
import random
fi =['game of thrones','the umbrella academy', 'the walking dead',' beverly hills, 90210',
         'the order','riverdale','true detective','the widow','northern rescue',
         'doom patrol','shameless','grey Anatomy','the orville',' workin moms','brooklyn nine-nine','dirty john',
         'arrow','supernatural', 'star trek: discovery','sex education',
         'whiskey cavalier','gotham','vikings',' the office','the big bang theory','peaky blinders',
         'the flash','suits','the good doctor','good girls']
fields=[]
newword=""
fie=list(random.sample(fi,k=10))
for i in fie:
    j=i.split()
    for k in j:
        temp=list(k)
        random.shuffle(temp)
        shuffledword="".join(temp)
        newword=newword+shuffledword+" "
    fields.append(newword)
    newword=""
c=0
def fetch(entries):
   global c
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      if(text in fi):
          c=c+1
   print(c)
   thelabel=Label(text="Your score is:"+str(c),fg="Black")
   thelabel.pack()

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()