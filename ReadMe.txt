This is an email to pdf converter.


Minimum Requirements:
	- Python 3 to run script
	- Java JDK 8 to run converter

Instructions:
	1. Setup config.json. Please enlose all values in double quotation marks.
	   For Windows PCs, please use double backslashes ("\\") for the directory addresses.

		1.1 "label-name": The set label of the emails to be printed from your gmail account.
		1.2 "get-mail-in-trash": If mails in trash with the matching label should also be processed. "True"/"False"
		1.3 "user": The email address to be used. For default user, just put "me" as the value.
		1.4 "dir-name": The parent directory url where the pdfs will be saved.
		1.5 "save-folder": The folder where the files will be saved.
		1.6 "jar-path": The absolute path of the emailconverter.jar

	2. After setting the config, you may now run the "convert.py" script. If you have python installed, then just fire up the command
	   line in the directory and type in "python convert.py". If you have anaconda, you have to use the anaconda prompt and navigate to the 
	   directory first before typing the command.

	3. If it is the first time running, google will ask you to sign in. Please sign in to your account that have the emails to processed.
	   A token.json will be created so that you will not have to log in next time.

	
Note: I recommend using jupyter notebook for editing the source code "Email to PDF Script".


If there are any problems/suggested features, please contact me through jared_sy@dlsu.edu.ph
