# notebook-to-text

The code searches through all .ipynb files in the data directory and its subdirectories, loads each file as JSON using json.load(), and then extracts the source code from each cell in the notebook. It writes each line of source code to a new text file with a name based on the original notebook's path. Finally, it prints the number of text files created.
