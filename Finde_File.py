import os
from time import ctime
import shutil
print(os.getcwd())
# هذه الصيغة التي يدعمها البرنامج يمكنك أضافة المزيد هنا أيضا
lsitoption = [".mp3", '.pdf', '.mp4', '.png', '.docx', '.jpg', '.jpeg', '.jpe', '.gif', '.bmp', '.wav', '.rtf', '.doc',
'.wri', '.txt', '.zip', '.rar', '.arj', '.lzh', '.ace', '.tra', '.gzip', '.jar', '.exe', '.apk', '.html', '.ai', '.Psd ',
'.bmp', '.z', '.7z', '.py', '.bin ', '.fnt ', '.fon ', '.otf', '.ttf', '.js', '.css', '.asp', '.vb', '.java', '.cpp', '.c',
'.dll', '.bak', '.ico', '.sys', '.tmp', '.xlr', '.xls', '.lnk']


# وحدات قياس تم أستخدامها ل ضبط الكود ب دقة
bite_ = 0
x = 0
y = 0

# موقع المجلد التي تريد العثور على الفات به
file_op = input("أدخل القسم الذي تريد فحصه هنا:")


# أداة فحص المسار
while not os.path.exists(file_op):
    file_op = input("the file is not exists X_X\npleas try again:")
else:
    print("ok the file  is found.^_^")



# خاصة ب العناصر التي يضيفها المستخدم
formats = []


path = file_op

how_math = int(input('يرجى أدخال كم صيغة تريد البحث عنها ب الأرقام:'))

# أداة سؤال عن المسارات
while y < how_math:
    formats.append(input(f"#{y+1}pleas enter the format").strip().lower())
    y += 1


# ل ضبط مدخلات المستخدم بحيث يتناسقوا مع الكود
for m in range(len(formats)):
    if formats[m].startswith('.'):
        continue
    else:
        formats[m] = "." + formats[m]


check = all(item in lsitoption for item in formats)

copy_option = input("هل تريد عمل نسخة للمفات في مكان ما Y/N").strip().capitalize()

if copy_option == 'Y' or copy_option == 'Yes':
    file_sy = input("يرجى وضع المسا هنا:")
    while not os.path.exists(file_sy):
        file_sy = input("لم يتم العثور على المسا يرجى أعادة المحاولة")
    else:
        print("تم أيجاد المسا.")

else:
    print("حسنا لا مشكلة")
    file_sy = ''
# هنا لايعمل الكود في حال أدخل المستخدم صيغة خطأ
if not check:
    print("the file format is not correct!!!\n pleas try again ^.^")


else:
    for root, dirs, files in os.walk(path):
        for _file in files:
            for x in range(len(formats)):
                if _file.endswith(formats[x]):
                    orginal = root + "\\" + _file
                    if os.path.exists(orginal):
                        if file_sy != '':
                            if orginal.startswith(file_sy):
                                continue
                            else:
                                with open(fr"{file_sy}\information.txt", 'a') as my_file:
                                    my_file.write(f'The file name is {_file} and is created in {ctime(os.path.getmtime(orginal))}\n')
                                    my_file.close()
                                try:
                                    shutil.copy(orginal, file_sy)
                                except Exception:
                                    print("Unfortunately, we cannot transfer this file")
                                print(root+"\\"+_file)
                                x = x + 1
                                bite_ += int(os.path.getsize(orginal))
                        else:
                            print(root + "\\" + _file)
                            x = x + 1
                            bite_ += int(os.path.getsize(orginal))
path = file_sy
files = os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if not file.endswith('information.txt'):
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

Gbayt = bite_ / 1000000000
MGbayt = bite_ /1000000
options_By = input("هل تريد معرفة حجم الملفات التي تم العثور عليها? Y/N").strip().capitalize()
if options_By == "Y" or options_By == "Yes":
    print("the size of all files is %.3f G and in MB is %.3f" % (Gbayt, MGbayt))
else:
    print("ok(★‿★)")
x_ = input("هل تريد معرفة عدد الملفات التي تم العتور عليها Y/N").strip().capitalize()
if x_ == "Y" or x_ == "Yes":
    print(f"The number of files found is: {x} today is {ctime()}")
else:
    print("ok(★‿★)")
