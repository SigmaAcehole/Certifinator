# Certifinator
Project submitted for VIT Hack 2020

Case Partner - GlobalCert
Track - Open Innovation

# Objective and Implementation
The aim of the project is to automatically generate certificates by mapping relevant content from a database(csv, excel) to appropriate position on the certificate. 

To facilitate the use of the program, we have created a GUI. Both the front-end and back-end of the GUI is done on python. The user will be able to select any sample certificate from their computer and manually map the positions on the certificate by just clicking on it. The program will store the user-clicked configuration in the form of coordinates and print the content from database to certificate automatically with utmost accuracy. The advantage of such a program is it's flexibility, we are confident that it will support any sample certificate design chosen by the user. Simplicity and user friendliness has been kept in mind while creating the GUI. 

# Instructions
1. First launch the application "certification.exe".
2. The EXE file and font folder should be in same folder.
3. Click "Load Template" and select the certificate template(PNG or JPEG) you wish map content to. 
3. Next, click "Load Data" and select the database in CSV format containing 3 columns and as many rows as you wish (will generate as many certificates). 
4. The program currently only maps 3 types of fields (Ex: Name, Project, Date).
5. Click "Set Destination" and browse to the folder you wish to store the generated certificates. 
6. Click "Generate certificates".
7. A preview of the template will pop up.
8. Double click at the point on certificate where you wish to map the 1st column/field of data (Ex: Name).
9. Then hover to the point you wish the print the 2nd column/field of data (Ex: Project).
10. Repeat same for 3rd column/field (Ex: Date).
11. You can close the preview and open the destination folder, the generated certificates will be available.
