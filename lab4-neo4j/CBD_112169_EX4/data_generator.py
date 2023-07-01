from random import randrange
import random as random
import datetime 
BUILDING_LETTERS = "ABCDEFGH"
BUILDING_NUMBERS = 8
DATE_FORMAT = "%Y-%m-%d"
CLASS_ID_CNT = -1
STUDENT_NMEC_CNT = 88887
ROWS_TOTAL = 900
STUDENTS_IN_CLASS = 30
CLASSES_AMOUNT = int(ROWS_TOTAL/STUDENTS_IN_CLASS)
TEACHERS_AMOUNT = CLASSES_AMOUNT
STUDENTS_AMOUNT = ROWS_TOTAL

subjects = [
    "Analysis and Exploration of Vulnerabilities",
    "Databases",
    "Security Information and Organization",
    "Software Engineering",
    "Master's Thesis",
    "Portuguese A1",
    "Portuguese A2",
    "Integrated Project Management"
    "Portuguese B1",
    "Portuguese B2",
    "Portuguese C1",
    "Portuguese C2",
    "Polish A1",
    "Polish A2",
    "Polish B1",
    "Polish B2",
    "Polish C1",
    "Polish C2",
    "English A1",
    "English A2",
    "English B1",
    "English B2",
    "English C1",
    "English C2",
    "Japanese A1",
    "Japanese A2",
    "Japanese B1",
    "Japanese B2",
    "Japanese C1",
    "Japanese C2",
    "Mobile Computing"
]

surnames = [
    "SMITH",
    "JOHNSON",
    "WILLIAMS",
    "JONES",
    "BROWN",
    "DAVIS",
    "MILLER",
    "WILSON",
    "MOORE",
    "TAYLOR",
    "ANDERSON",
    "THOMAS",
    "JACKSON",
    "WHITE",
    "HARRIS",
    "MARTIN",
    "THOMPSON",
    "GARCIA",
    "MARTINEZ",
    "ROBINSON",
    "CLARK",
    "RODRIGUEZ",
    "LEWIS",
    "LEE",
    "WALKER",
    "HALL",
    "ALLEN",
    "YOUNG"
]

names = [
    "Roch",
    "Rochell",
    "Rochella",
    "Rochelle",
    "Rochette",
    "Roda",
    "Rodi",
    "Rodie",
    "Rodina",
    "Rois",
    "Romola",
    "Romona",
    "Romonda",
    "Romy",
    "Rona",
    "Ronalda",
    "Ronda",
    "Ronica",
    "Ronna",
    "Ronni",
    "Ronnica",
    "Ronnie",
    "Ronny",
    "Roobbie",
    "Rora",
    "Rori",
    "Rorie",
    "Rory",
    "Ros",
    "Rosa",
    "Rosabel",
    "Rosabella",
    "Rosabelle",
    "Rosaleen",
    "Rosalia",
    "Rosalie",
    "Rosalind",
    "Rosalinda",
    "Rosalinde",
    "Rosaline",
    "Rosalyn",
    "Rosalynd",
    "Rosamond",
    "Rosamund",
    "Rosana",
    "Rosanna",
    "Rosanne",
    "Rose",
    "Roseann",
    "Roseanna",
    "Roseanne",
    "Roselia",
    "Roselin",
    "Roseline",
    "Rosella",
    "Roselle",
    "Rosemaria",
    "Rosemarie",
    "Rosemary",
    "Rosemonde",
    "Rosene",
    "Rosetta",
    "Rosette",
    "Roshelle",
    "Rosie",
    "Rosina",
    "Rosita",
    "Roslyn",
    "Rosmunda"
]

class Class():
    def __init__(self, id, subject, building, exam_date) -> None:
        self.id = id
        self.subject = subject
        self.building = building
        self.exam_date = exam_date
class Teacher():
    def __init__(self, name) -> None:
        self.name = name
class Student():
    def __init__(self, name, nmec) -> None:
        self.name = name
        self.nmec = nmec
        
class Randomizer:
    @staticmethod
    def next_subject():
        return subjects[CLASS_ID_CNT]
    @staticmethod
    def next_class_id():
        global CLASS_ID_CNT
        CLASS_ID_CNT +=1 
        return CLASS_ID_CNT
    @staticmethod
    def next_nmec():
        global STUDENT_NMEC_CNT
        STUDENT_NMEC_CNT +=1 
        return STUDENT_NMEC_CNT
    @staticmethod
    def rand_building():
        return random.choice(BUILDING_LETTERS) + str(randrange(0, BUILDING_NUMBERS))
    @staticmethod
    def rand_exam_date():
        year = 2023
        month = randrange(1,3)
        day = randrange(1,28)
        date = datetime.datetime(year, month, day).strftime(DATE_FORMAT)
        return date
    @staticmethod
    def rand_name():
        return names[randrange(0,len(names))] + " " + surnames[randrange(0,len(surnames))] 

class IntegrityManager():
    def __init__(self) -> None:
        self.classes  = self.create_classes()
        self.teachers = self.create_teachers()
        self.students = self.create_students()   
    def create_classes(self):
        return [Class(id=Randomizer.next_class_id(), subject=Randomizer.next_subject(), building=Randomizer.rand_building(), exam_date=Randomizer.rand_exam_date()) for i in range(CLASSES_AMOUNT)]
    def create_teachers(self):
        return [Teacher(name=Randomizer.rand_name()) for i in range(TEACHERS_AMOUNT)]
    def create_students(self):
        return [Student(name=Randomizer.rand_name(), nmec=Randomizer.next_nmec()) for i in range(STUDENTS_AMOUNT)]
    def pop_class(self):
        return self.classes.pop(0)
    def pop_teacher(self):
        return self.teachers.pop(0)
    def pop_student(self):
        return self.students.pop(0)
    
       
def write_data(file, integrity_manager : IntegrityManager):
    headers = "class_id,subject,building,teacher_name,student_nmec,student_name,exam_date\n"
    file.write(headers)
    
    for i in range(CLASSES_AMOUNT):
        c = integrity_manager.pop_class()
        t = integrity_manager.pop_teacher()
            
        for i in range(STUDENTS_IN_CLASS):
            s = integrity_manager.pop_student()
            row = f"{c.id},{c.subject},{c.building},{t.name},{s.nmec},{s.name},{c.exam_date}\n"
            file.write(row)
            

if __name__ == "__main__":
    file = open("CBD_112169_EX4_SEEDDATA.csv", "w")
    integrity_manager = IntegrityManager()
    write_data(file, integrity_manager)
    