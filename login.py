# Credentials
patients = dict({'swapnil' : 'swapnil@123', 'nieless' : 'nieless@123', 'rajat' : 'rajat@123', 'ujjwal' : 'ujjwal@123'})
doctors = dict({'doct' : 'doct@123','doc' : 'doc@123', 'torr' : 'tor@123'})

def check_login(username, password):

	if username in patients:
		if(patients[username] == password):
			return 1

	if username in doctors:
		if(doctors[username] == password):
			return 2

	return 0