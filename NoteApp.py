from datetime import datetime


def work_with_notebook():
	

    choice=show_menu()

    note_book=read_txt('MyNotes.txt')

    while (choice!=9):

        if choice==1:
            print_result(read_txt('MyNotes.txt'))
            read_txt('MyNotes.txt')
            #print_result(note_book)
        elif choice==2:
            date=input('Введите дату (ГГГГ-ММ-ЧЧ): ')
            print_result(find_by_date(note_book,date))
        elif choice==3:
            content=input('Введите текст для поиска: ')
            print_result(find_by_content(note_book,content))
	    	
        elif choice==4:
            noteid=input('введите идентификатор заметки, которую хотите изменить: ')
            change_note(note_book,noteid)
            
        elif choice==5:
            noteid=input('введите идентификатор заметки, которую хотите удалить: ')
            delete_note(note_book,noteid)
        elif choice==6:
            NoteHeader=input('Название новой заметки: ')
            NoteBody=input('Введите текст новой заметки: ')
            
            add_note(note_book,NoteHeader,NoteBody)
              
        elif choice==7:
            write_csv(note_book) 
        elif choice==8:
            print_result(read_csv('MyNotes_exp.csv')) 

        choice=show_menu()

      



def show_menu():
    print("\nMyNoteApp привествует Вас, выберите необходимое действие:\n"
          "1. Отобразить все заметки (новые заметки вверху списка).\n"
          "2. Найти заметку по дате последнего изменения: \n"
          "3. Найти заметку по содержанию слова в названии или в тексте\n"
          "4. Изменить заметку (название или содержимое)\n"
          "5. Удалить заметку\n"
          "6. Добавить заметку\n"
          "7. Сохранить все заметки в формате CSV\n"
          "8. Открыть заметки в формате CSV\n"
          "9. Завершить работу\n")
         
    choice = int(input())
    return choice



def key_function(item_dictionary):
    datetime_string = item_dictionary["Дата"]
    return datetime.strptime(datetime_string, '%Y-%m-%d %H:%M')


def print_result(data):
    
    #print(data)
    data.sort(key=key_function)
   
    print('\n')
    print('Номер', 'Дата_изменения', '<Название>', '[Содержимое]')
    print('_____________________________________')
    
    for i in reversed(range(len(data))):
        for j in data[i].values():   
           print (j, end=' ')
        print()
    print('\n')
    

    
    
    
          
        
        

def find_by_date(note_book,date):
    found=[]
    found1=0
    for i in range(len(note_book)):
        #if date in note_book[i].values():
        for j in note_book[i].values():
            if j.find(date)!=-1:
              found.append(note_book[i])
              found1+=1
    if found1==0: print("заметка с такой датой создания/изменения не найдена!")
    else: print("Найдены заметки: ")
    return found


def change_note(note_book_,id):
    
    changes=0
    changed_book=[]

    #note_book[len(note_book)-1]["Идентификатор"])
    
    for i in range(len(note_book_)):
       
        if note_book_[i]["Идентификатор"]==id:
            newname=input(f"отредактируйте название заметки {note_book_[i]["Название"]}: ")
            if len(newname)!=0:
             note_book_[i]["Название"]="<" + newname+ ">"
             note_book_[i]["Дата"]=str(datetime.now().date())+" "+str(datetime.now().time().strftime("%H:%M"))
           
            newbody=input(f"отредактируйте содержимое заметки {note_book_[i]["Текст"]}: ")
            if len(newbody)!=0:
             note_book_[i]["Текст"]="["+newbody+"]"
             note_book_[i]["Дата"]=str(datetime.now().date())+" "+str(datetime.now().time().strftime("%H:%M"))


            if len(newname)==0 and len(newbody)==0: 
                print ("Вы ничего не изменили!")
                return
       
            changes+=1
            
        changed_book.append(note_book_[i])
     
    if changes==0:
        print("заметка с таким идентификатором не найдена, проверьте данные!")
        return
    else:
        write_txt('MyNotes.txt',changed_book)
        print("заметка успешно изменена, данные сохранены!")
    


def delete_note(note_book,id):
    changes=0
    changed_book=note_book
    
    for i in range(len(changed_book)):
       
         #print (f" i is {i} now")
         if changed_book[i]["Идентификатор"]==id:

            confirm=input(f"Вы уверены что хотите удалить заметку {changed_book[i]["Название"]}{changed_book[i]["Текст"]}  ?:[y/n] ")
            
            if confirm=="Y" or confirm=="y":
              
              changed_book.pop(i)
              changes+=1
              break
            else: 
                print(f"Заметка {changed_book[i]["Идентификатор"]} не была удалена, попробуйте еще раз")
                return
            

    if changes==0:
        print("заметка с таким идентификатором не найдена, проверьте данные!")
        return
    else:
        write_txt('MyNotes.txt',changed_book)
        print("заметка успешно удалена, данные сохранены!")


def find_by_content(note_book,content):
    found=[]
    found1=0
    for i in range(len(note_book)):
        for j in note_book[i].values():
            if j.find(content)!=-1:
             found.append(note_book[i])
             found1+=1
    if found1==0: print("заметок с таким названием или содержанием не найдено!")
    return found


def add_note(note_book,head,body):
    new_book=note_book
    new_id= int (note_book[len(note_book)-1]["Идентификатор"]) + 1
    

    new_record=dict()
    new_record["Идентификатор"]=str(new_id)
    new_record["Дата"]=str(datetime.now().date())+" "+str(datetime.now().time().strftime("%H:%M"))
    new_record["Название"]="<"+head+">"
    new_record["Текст"]="["+body+"]"

    new_book.append(new_record)

    write_txt('MyNotes.txt',new_book)
    print("заметка успешно добавлена, данные сохранены!")




def read_txt(filename): 
 note_book=[]
 fields=['Идентификатор', 'Дата', 'Название', 'Текст']
 
 with open(filename,'r',encoding='utf-8') as phb:
    for line in phb:
        record=dict()
        if len(line)!=1:
          #record = dict(zip(fields, line.replace(' ','').replace('\t','').replace('\n','').split(',')))
          #record = dict(zip(fields, line.replace('\t','').replace('\n','').split(',',3)))
          record = dict(zip(fields, line.replace('\t','').replace('\n','').split(';')))


          note_book.append(record)
		   
 return note_book




def write_txt(filename , note_book):
    with open('MyNotes.txt','w' ,encoding='utf-8') as phout:
        for i in range(len(note_book)):
            s='' 
            for v in note_book[i].values():
                #s+=v+','
                s+=v+';'
            phout.write(f'{s[:-1]}\n')



def write_csv(note_book):
    import csv
    filednames=['Идентификатор', 'Дата', 'Название', 'Текст']

    with open('MyNotes_exp.csv','w', encoding='utf-8') as phcsv:
        writer=csv.DictWriter(phcsv, lineterminator="\r", fieldnames=filednames)
        writer.writeheader()
        for i in note_book:
          writer.writerow(i)
       
    print('данные успешно сохранены в файл "MyNotes_exp.csv"')


def read_csv(filename):
    note_book=[]
    import csv
    #filednames=["Фамилия", "Имя", "Телефон", "Описание"]

    with open(filename,'r', encoding='utf-8') as r_phcsv:
        
        reader=csv.DictReader(r_phcsv)
        for row in reader:
                        
          note_book.append(row)
          
    print('данные успешно загружены из файла "MyNotes_exp.csv"')
    return note_book


work_with_notebook()
