- [Python](#python)
  - [JSON](#json)
  - [Navigating Directories](#navigating-directories)
- [Environments](#environments)
  - [Requirements](#requirements)
- [Cool Links](#cool-links)
- [Bashing](#bashing)
- [Markdown](#markdown)
  - [Mermaid](#mermaid)


## Python
### JSON

    with open('idioms.json', 'w') as f:
        json.dump(idioms, f)

    with open(j_file, 'r') as file:
        plc_ai_d_v = json.load(file)

Debug

    print(variables, sep='\n')

Clipboard

    # shortcut for copy and pasting
    xl_paste = '''
    NI_T_DBR_5
    NI_T_DBR_6
    '''

    pt = str(xl_paste.split('\n')[1:-1])
    pyperclip.copy(pt)

### Navigating Directories

    # change directory to current script path
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

    def nav_dir(do_this):
        current_dir = os.getcwd()
        print(current_dir)

        # Navigate to the directory above
        os.chdir('..')
        os.chdir('..')
        
        f_results = do_this()

        # Navigate back to the original directory
        os.chdir(current_dir)
        print(current_dir)


        return f_results


    test_df = nav_dir(lambda: pd.read_excel('TestDF.xlsx', index_col='File')

    

## Environments

- python3 -m venv v_env
- sudo apt-get install python3-venv
- source .venv/bin/activate
- pip install
- enable spi
- sudo raspi-config

### Requirements
- install requirements…
- Create requirements file: pip freeze > requirements.txt
- Install requirements file: pip3 install -r requirements.txt


## Cool Links
- [NICEGUI Source](https://github.com/zauberzeug/nicegui/blob/main/main.py)
- [Windows ENV](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows)
- [.VENV](https://code.visualstudio.com/docs/python/environments)



## Bashing
& operator to run concurrent: python script1.py & python script2.py
    
    set py_exec="virtual_env/Scripts/python"
    set py_script_1="Lib/Labview/Py/NI_ACC_Reading.py"
    set py_script_2="Lib/Labview/Py/NI_AI_Reading.py"


    :: hide command line and print status
    @echo off
    cd ..
    cd ..
    cd ..

    :: virtual_env\Scripts\activate
    echo "running NI programs"
    start "ACC" %py_exec% %py_script_1%
    start "AI" %py_exec% %py_script_2%

    echo "running both"

    PAUSE

    deactivate


## Markdown

- [Table Maker](https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/)
- [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- ![image_name](link.png)
- Diagrams with [Mermaid](https://mermaid-js.github.io/mermaid/#/classDiagram?id=setting-the-direction-of-the-diagram)
- **Bold**
- *italics*
- ==highlight==
- break<br>break

### Mermaid
- [Mermaid Diagrams](https://mermaid.js.org/syntax/classDiagram.html#setting-the-direction-of-the-diagram)
- [Cheat Sheet](https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/)
- [Links](https://mermaid.js.org/#/flowchart?id=links-between-nodes)
- [Examples](https://dompl.medium.com/produce-great-looking-flowcharts-in-seconds-7f3bea64f2e2)