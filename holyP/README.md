# HolyP

Hi! This is a really badly documented programming language I wrote in two days, I never really took the time to come back to it and add documentation or more command, so it is very basic at the moment. The program **holyP.py** will convert any holyP supplied as a commmand line argument into a .c file where it can then be compiled with GCC or whatever C compiler you have available to you. **Note: The included powershell scripts for compiling use GCC, but may be modified to use any C compiler**. The programming language is somewhat inspired by holyC, although, holyC is very similar to C and I felt it lacked enough 'holy' terminology lol.

# Try it out!
#### If you would like to try out this repository, you can clone it and try out some of these commands on the included tests!

## Test the Compiler!
- If you would like to see a demonstration of the compilation from holyP to C, run the Compile.ps1 script and type the name of one of the included files such as **"add"** or **"average"** (note .holyP is automatically appended to the file name, so including the file extension will cause an error).  If you would like a more detailed look into how the program lexifies or parses the file, you can open the examine folder and run the **examine_holyP.ps1**, script and include the filename of the holyP file you would like to examine, it will print out first the lexification of the file, followed by the parsed version of the file.


- Note, if you don't trust powershell scripts you can manually type out the commands
	- **"python holyP.py '*input filename with extension*' '*output filename.c*' "**
	- **"gcc  '*output file.c*' -o '*output filename.exe*' "**
- **NOTE:** The only unique feature of this programming language is that it can compile files written ***vertically*** as well as ***horizontally***, try rotating a program 90 degrees and compiling!


# Syntax


### Creating Variables

Variables are created similar to JS , but rather than using let or var, you use **PRAY**, to pray that the variable exists

### Printing
Printing to standard out is achieved by the **PREACH** command followed by a string or expression.

### If statements

If statements are created by using the keywords **IF GOD PERMITS** followed by a comparison (parentheses are optional) followed by **THEN**, followed by the content of the if statement and finally, **ENDIF**

### While loops

While loops are extremely basic and follow the structure of the if statement, **WHILE** *comparison* **REPEAT**, followed by the *content*, and then **ENDWHILE**

### Unconditional Jumps
To define a valid jump statement, you must define a label and use the goto command to jump to the label. The proper syntax is **MARK** *label*, and **GOTO** *label*.

