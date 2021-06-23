import sys
# Could have been an array.
header1 = True;
header2 = False;
header3 = False;
header4 = False;
header5 = False;
header6 = False;
headers = [];
table="";
table_index=0;

# take file path as an argument
got_path=False
if(len(sys.argv)>1):
    header1 = False
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "h1":
            header1 = True;
        elif sys.argv[i] == "h2":
            header2 = True; 
        elif sys.argv[i] == "h3":
            header3 = True;
        elif sys.argv[i] == "h4":
            header4 = True;
        elif sys.argv[i] == "h5":
            header5 = True;
        elif sys.argv[i] == "h6":
            header6 = True; 
        else: 
            file_path = str(sys.argv[i]);
            got_path=True;
      
# If no file path was found as command line argument, ask the user to enter it manually. 
if got_path == False:
    file_path = str(input("File:"));

try:
    # open file as read only.
    with open(file_path, "r") as file_object:
        # Read the file content of the file_object 
        # line by line as an array called file_line.
        file_line = file_object.readlines();
        # look for headers
        if header1 == True:
            print("H1.");
            for i in range(len(file_line)):
                if file_line[i][:2] == "# ":
                    headers.append(file_line[i][2:].strip());
                    print("h1:"+str(file_line[i][2:]));
        if header2 == True:
            print("H2.");
            for i in range(len(file_line)):
                if file_line[i][:3] == "## ":
                    headers.append(file_line[i][3:].strip());
                    print("h2:"+str(file_line[i][3:]));
        if header3 == True:
            print("H3.");
            for i in range(len(file_line)):
                if file_line[i][:4] == "### ":
                    headers.append(file_line[i][4:].strip());
                    print("h3:"+str(file_line[i][4:]));
        if header4 == True:
            print("H4.");
            for i in range(len(file_line)):
                if file_line[i][:5] == "#### ":
                    headers.append(file_line[i][5:].strip());
                    print("h4:"+str(file_line[i][5:]));
        if header5 == True:
            print("H5.");
            for i in range(len(file_line)):
                if file_line[i][:6] == "##### ":
                    headers.append(file_line[i][6:].strip());
                    print("h5:"+str(file_line[i][6:]));
        if header6 == True:
            print("H6.");
            for i in range(len(file_line)):
                if file_line[i][:7] == "###### ":
                    headers.append(file_line[i][7:].strip());
                    print("h6:"+str(file_line[i][7:]));
        pass
    file_object.close()

    #Generate table of centent
    table+="### Table of content\n\n"
    for h in headers:
        table+=str(table_index)+". ["+h+"](#"+h.replace(" ", "-").lower()+")"+"\n\n"
        table_index+=1
    f = open(file_path,'r+')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write(table) # write new content at the beginning
    for line in lines: # write old content after new
        f.write(line)
    f.close()
except FileNotFoundError:
    print("Error: File not found")
    pass
    
#file_data.split("# ")
# read the file content as file_data
#file_data = file_object.read()
#print(file_data)
