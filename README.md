Fitness Tracker

1. Översikt av projektet

Fitness Tracker är en Python-applikation för att logga och analysera träningspass och måltider. Applikationen använder SQLite för datalagring och Tkinter för GUI.

1.1 Installation och beroenden

För att köra applikationen behöver du följande Python-bibliotek:

sqlite3 (ingår i standardbiblioteket)

pandas

tkinter (ingår i standardbiblioteket)

Installera saknade beroenden med: "pip install pandas" i konsollen

1.2 Starta applikationen

Kör applikationen genom att köra main.py:

python main.py i konsollen eller klicka på start-knappen i VS Code när du är inne på main.py

2. Beskrivning av projektets filer

2.1 main.py

Startpunkt för applikationen.

Importerar och kör main_gui() från gui.py.

2.2 gui.py

Skapar huvud-GUI:t där användaren kan navigera mellan att lägga till, visa och radera träningspass och måltider.

2.3 workout.py

Funktioner för att hantera träningspass:

add_workout(): Lägger till ett träningspass i databasen.

view_workouts(): Visar lagrade träningspass och statistik.

delete_workout(): Tar bort ett träningspass från databasen.

2.4 meal.py

Funktioner för att hantera måltider:

add_meal(): Lägger till en måltid i databasen.

view_meals(): Visar lagrade måltider och statistik.

delete_meal(): Tar bort en måltid från databasen.

2.5 database.py

Hanterar skapandet av databasen fitness.db och dess tabeller:

workouts (id, date, type, duration, calories)

meals (id, date, name, calories, protein, carbs, fat)

2.6 utils.py

Innehåller hjälpfunktioner för att redigera och radera poster i databasen.

3. Kursmoment och val

Projektet inkluderar flera centrala kursmoment:

3.1 SQL Med Python

Användning av SQLite för att lagra och hämta data.

SQL-frågor för att lägga till, visa och ta bort poster.

Jag valde denna eftersom att kursen innan denna var databasteknik vilket fortfarande är väldigt färskt i minnet. Det gjorde det lättare för mig att använda och koppla till mitt projekt.

3.2 Filhantering

Koden är uppdelad i separata filer för bättre struktur.

Funktioner återanvänds för att undvika kodupprepning.

Jag använder mig utav filhantering i databasen för att kunna lagra träningspass och maträtter samt deras näringsvärden och innehållet av träningspassen.

3.3 Avancerad datahantering

pandas används för att sammanställa och analysera tränings- och måltidsdata.

Summering av totala kalorier ingår.

Jag valde det som en del av mitt projekt för att kunna sammanställa all totala kalorier och för att jag tyckte att det var ett bra sätt att göra det på.
