from pathlib import Path
from datetime import datetime
with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers_Array_WO_Signs.txt', "w") as newopen:
    d = datetime.today()               
    print(d.strftime("%d/%m/%y %H:%M:%S"), file=newopen)
    p = Path('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\')
    list_path = list(p.glob('*'))
    for i in list_path:
        with open(i, encoding="utf8") as o:
            for line in o:
                print(line, end="", file=newopen)
            print("\n", file=newopen)
print("Преобразование в один файл завершено")