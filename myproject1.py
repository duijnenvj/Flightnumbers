import csv, sqlite3
conn = sqlite3.connect('flightsdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS ONTIME;
DROP TABLE IF EXISTS CARRIERS;
DROP TABLE IF EXISTS AIRPORTS;

CREATE TABLE ONTIME (Year INTEGER, Month INTEGER, DayofMonth INTEGER, DayOfWeek INTEGER, DepTime INTEGER, CRSDepTime INTEGER, ArrTime INTEGER,
CRSArrTime INTEGER, UniqueCarrier TEXT, FlightNum TEXT, TailNum TEXT, ActualElapsedTime INTEGER, CRSElapsedTime INTEGER, AirTime INTEGER, ArrDelay INTEGER,
DepDelay INTEGER, Origin TEXT, Dest TEXT, Distance INTEGER, TaxiIn INTEGER, TaxiOut INTEGER, Cancelled INTEGER, CancellationCode TEXT, Diverted TEXT
);

CREATE TABLE CARRIERS (Code TEXT, Description TEXT
);

CREATE TABLE AIRPORTS (iata TEXT, airport TEXT, city TEXT, state TEXT, country TEXT, lat FLOAT, long FLOAT
);
''')

with open('testdata.csv', 'r') as testdatafile:
    reader = csv.reader(testdatafile, delimiter = ',')
    next(reader, None)	
    for row in reader:
        cur.execute('''INSERT INTO ONTIME (Year, Month, DayofMonth, DayOfWeek, DepTime, CRSDepTime, ArrTime, CRSArrTime, UniqueCarrier, FlightNum, TailNum,
        ActualElapsedTime, CRSElapsedTime, AirTime, ArrDelay, DepDelay, Origin, Dest, Distance, TaxiIn, TaxiOut, Cancelled, CancellationCode, Diverted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
        row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23]))
        conn.commit()

with open('carriers.csv', 'r') as carriersfile:
    reader2 = csv.reader(carriersfile, delimiter=',')
    next(reader2, None)	
    for row in reader2:
        cur.execute("INSERT INTO CARRIERS (Code, Description) VALUES (?, ?)", (row[0], row[1]))
        conn.commit()
    
with open('airports.csv', 'r') as airportsfile:
    reader3 = csv.reader(airportsfile, delimiter=',')
    next(reader3, None)	
    for row in reader3:
        cur.execute('INSERT INTO AIRPORTS (iata, airport, city, state, country, lat, long) VALUES (?, ?, ?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        conn.commit()

#cur.execute('ALTER TABLE ONTIME ADD COLUMN KeyFlightNum TEXT')
#conn.commit()
#conn.text_factory = str
#cur.execute('''SELECT UniqueCarrier||FlightNum||\' \'||Year||Month||DayofMonth FROM ONTIME''')
#rows = cur.fetchall()
#print 'Top', rows [:20]
#for row in rows:
#    cur.execute('''UPDATE ONTIME SET KeyFlightNum = ?''', [row])


#cur.execute('SELECT Origin, DepDelay FROM ONTIME')
#Orideplay = dict((rows[0], rows[1]) for rows[0], rows[1] in rows)
#delaycounts = dict()
#oriorgs = dict()
#for row in rows:
#   ori = rows[0]
#   oriorgs[ori] = oriorgs.get(ori, 0) + 1
#   delay = rows[1]
#   delaycounts[delay] = delaycounts(delay, 0) + 1

#x = sorted(delaycounts, key = delaycounts.get, reverse=True)
#for k in x[:howmany]:
#    print k, delaycounts[k]
#    if delaycounts[k] < 10 : break

#print ''
#print 'Top',howmany,'DepartureDealy'

#cur.execute('''CREATE INDEX DATE ON ONTIME(Year, Month, DayofMonth);
#CREATE INDEX Origin ON ONTIME(Origin);
#CREATE INDEX Dest ON ONTIME(Dest);''')
#conn.commit()
#allrows = [[str(item) for item in rows] for rows in cur.fetchall()]