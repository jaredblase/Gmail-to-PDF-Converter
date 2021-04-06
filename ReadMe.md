A python 3 project that converts emails to pdfs.
This is dependent on Nick Russler's <a href='https://github.com/nickrussler/email-to-pdf-converter'>Email to PDF Converter</a>.

<b>Minimum Requirements:</b>
<ul>
	<li><a href='https://www.python.org/downloads/'>Python 3 or above</a> to run the script</li>
	<li><a href='https://www.oracle.com/ph/java/technologies/javase-downloads.html'>Java JDK 8 or above</a> for the script to run the .eml to .pdf converter</li>
</ul>

Instructions:
<ol>
	<li>
		Setup config.json. Please enlose all values in double quotation marks. For Windows PCs, please use double backslashes ("\\") for the directory addresses.
		<ul>
			<li>"label-name": The set label of the emails to be printed from your gmail account.</li>
			<li>"get-mail-in-trash": If mails in trash with the matching label should also be processed. "True"/"False"</li>
			<li>"user": The email address to be used. For default user, just put "me" as the value.</li>
			<li>"dir-name": The parent directory url where the pdfs will be saved.</li>
			<li>"save-folder": The folder where the files will be saved.</li>
			<li>"jar-path": The absolute path of the emailconverter.jar</li>
		</ul>
	</li>
	<br>
	<li>
		After setting the config, you may now run the "convert.py" script. If you have python installed, then just fire up the command line in the directory and type in "python convert.py". If you have anaconda, you have to use the anaconda prompt and navigate to the directory first before typing the command.
	</li>
	<br>
	<li>
		If it is the first time running, google will ask you to sign in. Please sign in to your account that have the emails to processed.
	   	A token.json will be created so that you will not have to log in next time.
	</li>
</ol>


If there are any problems/suggested features, please contact me through jaredblase@gmail.com
