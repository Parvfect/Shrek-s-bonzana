import cx_Freeze

executables= [cx_Freeze.Executable('really.py')] #Defining the executable scripts
cx_Freeze.setup(
    name='Shrek''Bonzana', 
    options={'build_exe':{'packages':['pygame'],'include_files':['shrek.jpg']}},
    description='This is shrek''s bonzana, escape the blocks to make mr shrek save your soul',
    executables=executables)
