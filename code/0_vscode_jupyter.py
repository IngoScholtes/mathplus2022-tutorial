# In our interactive tutorial, we use jupyter notebooks to introduce 
# higher-order network analysis with the python package pathpy. 
# For each unit of the tutorial, we will provide you with a notebook, 
# that contains descriptions, TODOs, as well as code 
# cells, which we will fill together.
#
# There are essentially three ways in which you can complete this 
# hands-on tutorial: 
#
# 1. Editing a stand-alone .py file in an editor of your choice
# 2. Editing jupyter .ipynb notebook files in the browser
# 3. Editing a stand-alone .py file in Visual Studio Code, using 
#     VSCode's jupyter plug-in
#
# While it is your choice how you want to work, for the sake of 
# convenience we will use option 3. In the following we briefly 
# demonstrate how it works. If you want to use option 3 as well, 
# make sure to install VS Code and the associated plugins as 
# described in the setup instructions available at 
#
# https://ingoscholtes.github.io/kdd2018-tutorial/setup
#
# Once you have set up Visual Studio Code, launch it either by clicking 
# the icon or by executing `code` in a terminal.
#
# In the File menu, click 'File -> Open Folder' and navigate to your local 
# copy of the repository material, which you have preferably cloned via git 
# as described in the setup instructions.
# 
# Let us now explore how to work with jupyter in VS Code. In a py file, we can 
# simply add the comment tag #%% to the beginning of a line. This will mark 
# the beginning of a jupyter cell and a Code Lens 'Run Cell' will appear above that 
# line. Let's write the following python code below that Code Lens: 

#%%
x = 'Hello World'

# Let us now add a second comment tag, which marks the start of another cell. 
# Let's write the following code:

#%%
print(x)

# We can now execute the code in a jupyter cell (delimited by the two #%% tags) by 
# clicking the Code Lens. Try it with the first cell. When you first evaluate a cell
# you will be asked for the Notebook server in which the python kernel should be started.
# In the pop-up menu, you can just select "Start new Notebook". Visual Studio Code will 
# start a new kernel, and once it is ready you will see 'Python 3 Kernel (idle)' in the 
# status bar.

# Now our first line has been executed in our new kernel, and the kernel is waiting 
# to execute our python code. Click the second cell, which prints the string.

# The output will appear in a new Results window. By default, each evaluation of a cell
# overwrites prior output, but we can change this behavior by ticking the "Append Results"
# tickbox. Try it by executing the second cell multiple times.

# If for some reason we don't want to use the jupyter kernel, we can simply execute the 
# whole code file using our standard python interpreter. We can just hit F5 or click 
# 'Debug -> Start Debugging'. Try it.

# This execution mode is great to debug your code by setting breakpoints. Just click to the
# left of line 48 in this file such that the red circle appear. Then hit F5.

# VS Code will highlight syntax errors (and, to a certain extent type errors) as 
# you write your code. Try it by uncommenting 'x := 42' in the next line. Any problems will
# further appear in the problems window below the code editor.

#%% 
x:= 42


# VS Code will automatically show documentation extracted from the docstring of 
# python classes and methods. Try it by typing print(...
# With STRG+SPACE you will see a list of variables, methods, symbols that are 
# available at the current point in your code. Try it by uncommenting the next line,
# move the cursor after the dot and hit CTRL+SPACE.

#%% 
# x.


# Finally, VS Code comes with integrated support for git repository. In fact, in the bottom left
# corner of the status bar, you should see a branch symbol "master" and next to it a small 
# sync icon. Whenever you click this icon, you will automatically receive updates to all files in 
# the repository. We will use this mechanism to update the solutions as we move forward with 
# the tutorial.

# We are now ready to start unit 2 of the tutorial. You can navigate to the file 
# code/2_pathpy.py in the repository.