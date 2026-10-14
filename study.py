import random

jargon_db = { 
"subnet mask": "Splits IP into network ID and host ID. Like ZIP vs house number.", 
"default gateway": "Router IP connecting LAN to internet. Main exit door.", 
	"dhcp": "Hands out IP addresses automatically. Like hotel room keys.", 
	"apipa": "Backup 169.254.x.x IP when DHCP fails. Temporary visitor pass.", 
	"dns": "Translates website names into IP numbers. Phonebook (Port 53).", 
"mac address": "Physical burned-in hardware ID. Permanent fingerprint.", 
"switch": "Connects local devices using MAC addresses. Local hallway.", 
"router": "Connects different networks using IP addresses. Border checkpoint.", 
"port 80": "HTTP - Unencrypted web traffic.", 
"port 443": "HTTPS - Secure encrypted web traffic.", 
"port 25": "SMTP - Outgoing email delivery.", 
"port 53": "DNS - Name resolution.", 
"root": "Superuser account in Linux." } 
 

print("===========================================") 
print(" COMPTIA JARGON TRANSLATOR READY") 
print(" Type list to see all terms, or exit to quit.") 
print("===========================================") 

while True: 
	query = input ("Enter a term to look up: ").lower().strip() 
	
	if query == "exit": 
		print("Good study session! Closing translator...") 
		break

	elif query == "list": 
		print("\nAVAILABLE TERMS:") 
		for term in sorted(jargon_db.keys()): 
			print(" - " + term) 
	elif query == "quiz":
		term, definition = random.choice(list(jargon_db.items()))
		print("\n--- QUIZ QUESTION ---")
		print("DEFINITION: "+ definition)
		answer = input("What term is this?").lower().strip()
		if answer == term:
			print("[CORRECT!] Excellent recall!")
		else:
			print(f"[X] Incorrect. The correct term is:'{term.upper()}'")
	elif query in jargon_db: 
		print(">; " + query.upper() + ": " + jargon_db[query]) 
	else: 
		print("[X] " + query + " is not in your list yet.")