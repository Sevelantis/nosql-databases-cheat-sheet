import time
from neo4j import GraphDatabase

class Neo4jDatabase:
    def __init__(self):
        self._driver = GraphDatabase.driver("bolt://127.0.0.1:7687")

    def execute(self, query):
        return list(self._driver.session().run(query))
    
    def clear_data(self):
        self._driver.session().run("MATCH (n) DETACH DELETE n")
        
    def add_nodes(self):
        self._driver.session().run(
            """
            LOAD CSV WITH HEADERS FROM 'file:///CBD_112169_EX4_SEEDDATA.csv' AS row
            MERGE (student: Student{name: row.student_name, nmec: row.student_nmec})
            MERGE (teacher: Teacher{name: row.teacher_name})
            MERGE (class: Class{id: row.class_id, subject: row.subject, building: row.building, exam_date: row.exam_date})
            MERGE (student)-[:ENROLLED_IN]->(class)
            MERGE (teacher)-[:LEADS]->(class)
            """)

    def close_connection(self):
        self._driver.close()
        
    def init_data(self):
        print("Clearing data...")
        self.clear_data()
        time.sleep(.5)
        print("Adding nodes...")
        self.add_nodes()
        time.sleep(.5)
        print(f'Data initialized.')
            
class Exercise:
    def __init__(self, neo4j : Neo4jDatabase) -> None:
        self.neo4j = neo4j
        self.queries = [
            #1 return total record count
            'MATCH (n) RETURN count(n)',
            #2 return teachers names
            'MATCH (t:Teacher) RETURN t.name',
            #3 return students nmecs enrolled to class with subject name 'Software Engineering'
            'MATCH (s)-[:ENROLLED_IN]->(c) WHERE c.subject = "Software Engineering" RETURN s.nmec as NMEC, c.subject as subject_name',
            #4 return teachers and classes they teach
            'MATCH (t:Teacher)-[leads:LEADS]->(c:Class) RETURN t.name, c.subject',
            #5 return teachers teaching more than one class
            'MATCH (t:Teacher)-[leads:LEADS]->(c:Class) WITH t, count(c) as classes_amount, count(t) AS teachers_total WHERE 1 < teachers_total RETURN t.name, classes_amount',
            #6 return classes with exam_date after '20-01-2023' ordered by date asc
            'MATCH (c:Class) WHERE c.exam_date > "2023-01-20" RETURN c.subject, c.exam_date ORDER BY c.exam_date ASC',
            #7 return students having exam on '21-01-2023' ordered by nmec desc
            'MATCH (s:Student)-[:ENROLLED_IN]->(c:Class) WHERE c.exam_date = "2023-01-22" RETURN s.name, s.nmec, c.subject, c.exam_date ORDER BY s.nmec DESC',
            #8 return students and their teachers ordered by nmec asc
            'MATCH (s:Student)-[:ENROLLED_IN]->(c:Class)<-[:LEADS]-(t:Teacher) RETURN DISTINCT t.name, s.name, s.nmec ORDER BY s.nmec ASC',
            #9 return number of exams performed in building B6 between date '2023-01-15' and '2023-02-15'
            'MATCH (c:Class) WHERE c.building="B6" AND c.exam_date > "2023-01-15" AND c.exam_date < "2023-02-15" RETURN count(c) as exams_total',
            #10 return students name and nmec, teacher, class subject name, building and date for exams having place in building B6 between date '2023-01-15' and '2023-02-15' ordered by exam_date ASC
            'MATCH (s:Student)-[:ENROLLED_IN]->(c:Class)<-[:LEADS]-(t:Teacher) WHERE c.building="B6" AND c.exam_date > "2023-01-15" AND c.exam_date < "2023-02-15" RETURN c.building AS building, t.name AS teacher_name, s.nmec AS NMEC, s.name AS student_name, c.subject AS subject, c.exam_date AS exam_date ORDER BY c.exam_date ASC',
        ]
    
    def run(self):
        i=1
        for query in self.queries:
            print(f'[{i}]Running query: {query}\n[{i}]Result:')
            result = self.neo4j.execute(query)
            [print(f'\t{line}') for line in result]
            i+=1
            time.sleep(.125)
    
def main():    
    neo4j = Neo4jDatabase()
    neo4j.init_data()
        
    exercise = Exercise(neo4j)
    exercise.run()

    neo4j.close_connection()

if __name__ == "__main__":
    main()
    