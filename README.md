
# 📖 Study Script 📖 
### Start a study session in 2 seconds 

Study Files Bot is a command-line application designed to help students efficiently manage and access study materials associated with their courses. The application allows users to register subjects, link relevant documents and URLs, and open these resources directly in a web browser. Key features include listing available subjects, viewing associated files, and adding or modifying study materials.

The project is primarily aimed at university students who want to streamline their study processes by quickly accessing digital resources related to their coursework.

# Setup Instructions 🛠 

### 1. Download and Configure
- Download the project files to your local machine.

### 2. Create a .bat File
- Create a batch file (e.g., `study.bat`) that calls the Python script. Ensure that the file is located in a directory that you want to easily access from the command line.

### Add the .bat File to Environment Variables
To run the `study.bat` file from any command prompt, add its directory to your system's environment variables:
1. Right-click on 'This PC' or 'Computer' on your desktop or in File Explorer and select 'Properties.'
2. Click on 'Advanced system settings' and then 'Environment Variables.'
3. In the 'System variables' section, find and select the **Path** variable, then click **Edit.**
4. Add the path to the directory where you saved your `study.bat` file.

### 3. Add Python to Environment Variables
If Python is not already in your environment variables, you’ll need to add it:
1. In the same 'Environment Variables' window, locate the **Path** variable.
2. Click **Edit** and add the path to the directory where Python is installed (e.g., `C:\Python39\` or wherever your Python executable is located).
3. Ensure that the **Scripts** folder (e.g., `C:\Python39\Scripts\`) is also included in the **Path**.

### 4. Run the Application
- Open a command prompt and use the command `study "subject_name"` to access your study materials.



# Commands  🔽 🔽

### 1. List Subjects
- **Command**: `study list`
- **Description**: Displays all available subjects registered in the configuration file.

### 2. Open a Subject
- **Command**: `study "subject_name"`
- **Description**: Opens the files and URLs associated with the specified subject in the web browser. If the subject is not found, it prompts the user to enter the files associated with it.

### 3. Show Files for a Subject
- **Command**: `study "subject_name" files`
- **Description**: Displays a list of all files and URLs associated with the specified subject, allowing users to add a new file, modify or delete them.

### 4. Add a New File or Folder
- **Command**: `study "subject_name" add`
- **Description**: Prompts the user to enter a new file or URL to add to the specified subject. The new file will be saved in the configuration file.

- **Command**: `study "subject_name" add -f`
- **Description**: Prompts the user to enter a new folder to add to the specified subject. The new folder will be saved in the configuration file.

### 5. Help Command
- **Command**: `study help`
- **Description**: Displays a list of all available commands, along with their descriptions and usage examples.

### 6. Exit the Application
- **Command**: Type `exit` when prompted.
- **Description**: Exits the current operation and returns to the previous menu or closes the application.

## Modify Files and Subjects 🤙🤙
If you want to quickly modify all the files and subjects, you can do so directly in the `materias_config.json` file. Open the file with a text editor and make your changes as needed.

## ScreenShots 🔽

![Screenshot 2024-10-29 142533](https://github.com/user-attachments/assets/ba9cf0e5-ac0f-4cab-8c87-a63ab9e91697)
![image](https://github.com/user-attachments/assets/736d2188-0209-45fa-a5db-bd5293a5efe7)




