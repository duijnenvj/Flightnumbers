import csv, sqlite3
conn = sqlite3.connect('flightsdb.sqlite')
cur = conn.cursor()

cur.execute('ALTER TABLE ONTIME ADD COLUMN KeyFlightNum TEXT')
conn.commit()
conn.text_factory = str
cur.execute('''SELECT UniqueCarrier||FlightNum||\' \'||Year||Month||DayofMonth, FlightNum FROM ONTIME''')
rows = cur.fetchall()
print 'Top', rows[:20]
print 'Lengte', len(rows)
for row in rows:
    cur.execute('''UPDATE ONTIME SET KeyFlightNum = ? WHERE FlightNum = ?''', (row[0], row[1]) )
    conn.commit()




#Oridelay = dict((rows[0], rows[1]) for rows[0], rows[1] in rows)
#delaycounts = dict()
#oriorgs = dict()
#for row in rows:
#   ori = rows[0]
#    oriorgs[ori] = oriorgs.get(ori, 0) + 1
#    delay = rows[1]
#    delaycounts[delay] = delaycounts(delay, 0) + 1

#x = sorted(delaycounts, key = delaycounts.get, reverse=True)
#for k in x[:howmany]:
#    print k, delaycounts[k]
#    if delaycounts[k] < 10 : break

#print ''
#print 'Top',howmany,'ArrivalDealy'

