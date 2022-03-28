# XML-editor
### This project is intended to provide a suite for dealing with XML files, providing features like:
- [Checking XML files for errors and inconsistencies.](#check-xml)
- [Prettifying.](#prettify)
- [Compression.](#compress)
- [Minifying.](#minify)
- [Conversion to JSON.](#convert-to-json)
    
### All features provided through an easy to use GUI.  
  
---

# Features  
## [Check XML](Error_checking.py)  
### The error checking process uses a stack for the check and follows this pipeline:  
1. Import stack and initialize flags to be used later inside algorithm.  
2. Make sure that text is left stripped then split into a list of lines..  
3. Loop the characters of each line.  
4. Check the character is a start of tag while making sure that the tag is not a comment (<? or <!).   
5. If the tag is open tag:  
    - Find index of first space and “>” (to determine name of the tag).  
    - Check if the tag is open and close in the same time (will not be pushed as it doesn’t cause a problem).
    - Push the tag into stack.

6. If the tag is closed:
    - Pop the top most from stack and comparing it with the closed one to determine error.  

7. Check stack is empty for no errors (no extra open tags).  
8. Returning no error found
or returning the error.

---

## [Prettify](prettify.py)  
### The prettify process follows this pipeline:  

1. Opening file and initializing variables:
    - Create spaces variable: to store in it number of spaces for each line
    - Creating previous variable: to determine if the previous tag is open or close

2. Loop in every line in file and make sure that it is left stripped.

3. Determining indeces of “<”, “/” and ”>” to use them later.

4. Checking if the line is a comment or a data version tag to avoid shifting.

5. Setting prev to open(to run the algorithm for them) for the next line if the tag is comment or data.

6. If line contains open and close tags in the same time:  
It will be shifted if the previous is open only.

7. If line contains close tag only:   
It will be shifted backwards if the previous one is close only

8. If line contains open tag only:  
It will be shifted forward if the previous one is open only

9. Writing spaces before each line according to algorithm checks.

10. Returning the new prettified string to be written in the file 

---

## [Compress](Compress_JSON.py)  
Provides ability to compress and decompress XML documents through an algorithm which loops on every word in the file, adds each word as a key in a dictionary then assigns a value for this key.  
This value depends on a counter. If the word already exists in the dictionary, it is printed.Between every 2 values ‘s’ is printed indicating a whitespace that is also added to the dictionary.

---

## [Minify](minify.py)  
Removes all whitespace, and newlines from the whole XML document. 

---

## [Convert to JSON](JSON_Parser.py)  
The file is manipulated through multiple functions till it is converted to the convenient form.
These functions are present in three files.

---

### [JSON_Parser:](JSON_Parser.py)
Acts as the driver for the conversion process.  
Contains functions: 
- ### xml_to_dict:  
    Converts the XML file to a list of tags and filters comments and unnecessary tags then invokes jsonify to convert the list to one dictionary.  

- ### dict_to_json:  
    Writes python dictionary to a JSON file.  

### [Jsonify:](jsonify.py)  
Takes a list of tags and returns one python dictionary that is later converted to a JSON file.  

### [Utils:](utils.py)  
Contains many utility function used in both jsonify and JSON_Parser that perform a wide range of operations on both xml tags and the whole list of tags.
