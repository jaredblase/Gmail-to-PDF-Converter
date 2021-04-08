A python 3 project that converts emails to pdfs.
This is dependent on Nick Russler's <a href='https://github.com/nickrussler/email-to-pdf-converter'>Email to PDF Converter</a>. (The .jar file is already included in this repo)

<b>Script Requirements:</b>
<ul>
	<li><a href='https://www.python.org/downloads/'>Python 3 or above.</a>. Please tick the "add to PATH" option during installation.</li>
	<li><a href='https://developers.google.com/docs/api/quickstart/python'>The Google Python API</a> to connect with Google services.</li>
	<li><a href='https://www.oracle.com/ph/java/technologies/javase-downloads.html'>Java JDK 8 or above</a> for the script to run the .eml to .pdf converter</li>
	<li><a href='https://wkhtmltopdf.org/downloads.html'>wkhtmltopdf</a> to write PDF files. Please add the /bin directory to your environment paths.</li>
</ul>

Instructions:
<ol>
	<li>
		After installing the requirements, setup config.json. Please enlose all values in double quotation marks. For Windows PCs, please use double backslashes ("\\") for the directory addresses. Below are the following fields:
		<ul>
			<li>"label-name": The set label of the emails to be printed from your gmail account.</li>
			<li>"from": The sender of the emails to be printed. Leave blank to ignore this filter.</li>
			<li>"to": Ther receipient of the emails to be printed. Leave blank to ignore this filter</li>
			<li>"get-mail-in-trash": If mails in trash with the matching label should also be processed. "True"/"False"</li>
			<li>"user": The email address to be used. For default user, just put "me" as the value.</li>
			<li>"dir-name": The parent directory url where the pdfs will be saved. "default" uses the working directory of convert.bat.</li>
			<li>"save-folder": The folder where the files will be saved.</li>
			<li>"jar-path": The absolute path of the emailconverter.jar. "default" uses the working directory of convert.bat and looks for /src/emailconverter.jar.</li>
			<li>"start-date": Date in the format "yyyy/mm/dd". Use "default" to indicate no start date requirements.</li>
			<li>"end-date": Date in the format "yyyy/mm/dd". Use "default" to indicate no end date requirements. <strong>Note:</strong> this is exclusive, meaning setting January 6 as the end date will only include mails that were sent upto January 5 11:59 PM.</li>
		</ul>
	</li>
	<br>
	<li>
		After setting the config, just double click the "convert.bat", and it will automatically run the script for you.
	</li>
	<br>
	<li>
		If it is the first time running, google will ask you to sign in. Please sign in to your account that have the emails to be processed.
	   	A token.json will be created so that you will not have to log in the next time.
	</li>
</ol>


If there are any problems/suggested features, please contact me through jaredblase@gmail.com
