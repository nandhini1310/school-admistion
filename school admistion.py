def search(t2):
   t2=(('xxx',1),('yyy',2),('zzz',3))
   s=input('Enter student ID=')
   for i in range(len(t2)):
       for ch in t2:
           if ch==s:
               print'Student =>',t2[i],'of Id number',t2[i+1]
               break
   else:
       print'Invalid Entry, try again'


def details(t1):
       n=raw_input('Enter applicant name=')
       t2=(('xxx',1),('yyy',2),('zzz',3))
       for i in range(len(t1)):
           if len(t1)<5:
               t2=t2+(n,i)
               break
           elif len(t1)==5:
               print'Sorry, class full'
           else:
               print'Sorry, class full'
       print'Student added successfully to class'
   def delete(t2):
       l=list(t2)
       j=input('Enter the student ID=')
       for i in range(len(t2)):
           for ch in l:
               if j==ch:
                   del l[i]
                   del l[i+1]
                   break
               else:
                   print'Student not found. Please try again'
       print tuple(l)
   n=input('Enter the number of students=')
   t1=tuple()
   t2=(('xxx',1),('yyy',2),('zzz',3)) 
   name=raw_input('Enter the student name=')
   idn=input('Enter the Id no.=')
   for i in range(n):
       t1=t1+(name,)
       t1=t1+(idn,)
   while True:
       print'\n\n\t\t----Admission Menu----'
       print'\t\t1->Apply for admission'
       print'\t\t2->Search for a student'
       print'\t\t3->Remove a student'
       print'\t\t4->Exit'

       ch=input('Enter your choice=')
       if ch==1:
           details(t1)
       elif ch==2:
           search(t1)
       elif ch==3:
           delete(t1)
       elif ch==4:
           print'Thank You for visiting --School Name--'
           exit()
       else:
           print'Wrong choice, please select a valid choice and try again'
