
def createTables(curr) :
	command = "CREATE TABLE responses (response_id SERIAL PRIMARY KEY, question VARCHAR(255) NOT NULL, response VARCHAR(255) NOT NULL)"
	conn = None
	curr.execute(command)

def insertData(curr) :
	question = "Who are you"
	response = "I am Chad. What is your name"
	sql = "INSERT INTO responses (question,response) VALUES ('{0}','{1}');"
	curr.execute(sql.format(question, response))
	response_id = curr.fetchone()[0]

def getData(curr) :
	sql = "SELECT * FROM responses"
	curr.execute(sql)
	for record in curr :
		print(record)