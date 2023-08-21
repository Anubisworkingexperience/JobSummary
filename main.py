from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime


# Creating window

root = Tk()
root.title('Резюме')
root.geometry('750x600')

icon = PhotoImage(file = "./icons/briefcase.png")
root.iconphoto(True, icon)

#window content
# canvas= Canvas(root, width= 100, height= 100)
# canvas.pack()

# # russianFlag = (Image.open('./icons/russian.png'))
# # resized_russianFlag = russianFlag.resize((100, 100), Image.ANTIALIAS)
# # new_russianFlag = ImageTk.PhotoImage(resized_russianFlag)

# # canvas.create_image(100, 100, anchor=E, image=new_russianFlag)

#photo
btn = ttk.Button(text='Here should be image')
btn.place(relx=0.1, rely=0.1, relheight=0.25, relwidth=0.25)

#general frame
generalFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=10)

lastNameLabel = ttk.Label(generalFrame, text='Фамилия')
lastNameLabel.pack(anchor=CENTER)
lastName = ttk.Entry(generalFrame)
lastName.pack(anchor=CENTER)

firstNameLabel = ttk.Label(generalFrame, text='Имя')
firstNameLabel.pack(anchor=CENTER)
firstName = ttk.Entry(generalFrame)
firstName.pack(anchor=CENTER)

patronymicLabel = ttk.Label(generalFrame, text='Отчество')
patronymicLabel.pack(anchor=CENTER)
patronymic = ttk.Entry(generalFrame)
patronymic.pack(anchor=CENTER)

departmentList = ['Инженерия', 'Финансы и бухгалтерия', 'Data science и аналитика', 'Дизайн', 'Маркетинг и коммуникации', 'Продуктовый менеджмент', 'Юриспруденция']

departmentLabel = ttk.Label(generalFrame, text='Отдел')
departmentLabel.pack(anchor=CENTER)
department = ttk.Combobox(generalFrame, values=departmentList)
department['state'] = 'readonly'
department.pack(anchor=CENTER)

jobList = []
jobLabel = ttk.Label(generalFrame, text='Желаемая должность')
jobLabel.pack(anchor=CENTER)

def addJobs(event):
    jobList = []
    jobDepartment = department.get()
    print(jobDepartment + 'yes')
    if jobDepartment == 'Инженерия':
        jobList.append('Frontend разработчик', 'Backend разработчик', 'Principal software engineer', 'Engineering manager', 'Network security engineer')

job = ttk.Combobox(generalFrame, values=jobList)
job['state'] = 'readonly'
job.bind("<<ComboboxSelected>>", addJobs)
job.pack(anchor=CENTER)

educationList = ['Дошкольное',
                  'Начальное общее',
                    'Основное общее',
                      'Среднее общее',
                        'Среднее профессиональное',
                         'Высшее']

educationLabel = ttk.Label(generalFrame, text='Образование')
educationLabel.pack(anchor=CENTER)
education = ttk.Combobox(generalFrame, values=educationList)
education['state'] = 'readonly'
education.pack(anchor=CENTER)

now = datetime.now()
dateString = now.strftime("%d/%m/%Y")
dateList = dateString.split('/')



def showCalendar():
    clickCount = 0
    if clickCount % 2 == 0:
        date.pack(anchor=CENTER)
    else:
        hideCalendar()
    clickCount += 1

def hideCalendar():
    date.destroy()

dateBtn = ttk.Button(generalFrame, text='Дата рождения', command=showCalendar)
dateBtn.pack(anchor=CENTER)

date = Calendar(generalFrame, selectmode='day', year=int(dateList[2]), month=int(dateList[1]), day=int(dateList[0]))

phoneNumberLabel = ttk.Label(generalFrame, text='Телефон')
phoneNumberLabel.pack(anchor=CENTER)
phoneNumber = ttk.Entry(generalFrame)
phoneNumber.pack(anchor=CENTER)

emailLabel = ttk.Label(generalFrame, text='Email')
emailLabel.pack(anchor=CENTER)
email = ttk.Entry(generalFrame)
email.pack(anchor=CENTER)

generalFrame.pack(anchor=CENTER, fill=Y)

root.mainloop()

