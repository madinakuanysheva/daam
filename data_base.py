import sqlite3

conn = sqlite3.connect('daam.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(50),
        user_surname VARCHAR(50),
        user_email VARCHAR(100),
        user_password VARCHAR(100),
        user_plan VARCHAR(50)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS submissions (
        submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_id INTEGER,
        submission_code TEXT,
        evaluation_result BOOLEAN,
        submitted_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (task_id) REFERENCES tasks(task_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS social_problems (
        social_problem_id INTEGER PRIMARY KEY AUTOINCREMENT,
        social_problem_name TEXT,
        social_problem_description TEXT
    )
''')

cursor.execute('''
    INSERT INTO social_problems (social_problem_name, social_problem_description) VALUES
        ('Gender Inequality', 'Issue related to unequal distribution of opportunities, resources, and rights between genders, leading to discrimination, inequality in access to education, employment, political participation, and other areas of life.'),
        ('Cultural Identity Loss', 'Gradual loss of traditional values, customs, language, and way of life, which may occur under the influence of globalization, migration, and cultural imperialism.'),
        ('Urbanization', 'Increase in the proportion of population living in cities, leading to problems such as overpopulation, housing shortage, environmental pollution, inefficient resource use, and social disintegration.'),
        ('Corruption', 'Abuse of trust and official position for personal gain, which can weaken institutions of governance, lead to unfair distribution of resources, and violate citizens\' rights.'),
        ('Waste Management Issues', 'Include insufficient collection, processing, and disposal of waste, leading to environmental pollution, health threats, and ecosystem destruction.'),
        ('Domestic Violence', 'Violence that occurs within the family or intimate relationships, including physical, psychological, sexual violence, and economic exploitation.'),
        ('Infrastructure Development', 'Need for development and modernization of infrastructure to ensure access to quality services such as transportation, energy, water, and communication for all layers of the population.'),
        ('Cybersecurity', 'Protection of information systems and data from cyber threats, including hacker attacks, viruses, fraud, and cyber espionage.'),
        ('Combatting Hunger and Malnutrition', 'Issue related to insufficient access to food and malnutrition, leading to negative consequences for health, development, and viability of individuals.')
''')





cursor.execute('''
    CREATE TABLE IF NOT EXISTS levels (
        level_id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_name TEXT,
        level_description TEXT
    )
''')

cursor.execute('''
    INSERT INTO levels (level_name, level_description) VALUES
        ('Social Activist', 'At this level, you explore issues related to social concerns and actively engage in solving these problems using Python programming.'),
        ('Reformer', 'Reformers strive for changes and improvements in society. At this level, you study tasks and solutions aimed at changing old approaches and implementing new ones.'),
        ('Global Innovator', 'At this level, you work on massive global issues, applying innovative approaches and technologies to create revolutionary changes in the world.')
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        social_problem_id INTEGER,
        level_id INTEGER,
        task_description TEXT,
        FOREIGN KEY (social_problem_id) REFERENCES social_problems(social_problem_id),
        FOREIGN KEY (level_id) REFERENCES levels (level_id)
    )
''')

cursor.execute('''
    INSERT INTO tasks (social_problem_id, level_id, task_description) VALUES
        (1, 1, 'Linear programs'),
        (2, 1, 'Conditions'),
        (3, 1, 'Basic operations'),
        (4, 2, 'Lists and Sets'),
        (5, 2, 'Strings'),
        (6, 2, 'Tuples and dictionaries'),
        (7, 3, 'Functions'),
        (8, 3, 'Stream input'),
        (9, 3, 'Libraries')
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS progress (
        progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INTEGER,
        task_id INTEGER,
        user_id INTEGER,
        status VARCHAR(50),
        score FLOAT,
        attempts_count INTEGER,
        last_updated DATE,
        FOREIGN KEY (level_id) REFERENCES levels(level_id),
        FOREIGN KEY (task_id) REFERENCES tasks(task_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
''')


conn.commit()
conn.close()