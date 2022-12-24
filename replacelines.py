import re

'''
KeyNames = [
            'AUTH_KEY',         
            'SECURE_AUTH_KEY',  
            'LOGGED_IN_KEY',    
            'NONCE_KEY',        
            'AUTH_SALT',        
            'SECURE_AUTH_SALT', 
            'LOGGED_IN_SALT',   
            'NONCE_SALT'
           ];
'''

with open("wp-config.php", "r") as wpconfig, open("wp-config.php.bak", "w") as wpconfigbak:
    for line in wpconfig:
        found = re.search(r'AUTH_KEY|SECURE_AUTH_KEY|LOGGED_IN_KEY|NONCE_KEY|AUTH_SALT|SECURE_AUTH_SALT|LOGGED_IN_SALT|NONCE_SALT', line.strip());
        if (not found):
            wpconfigbak.write(line)
        else:
            continue

            
