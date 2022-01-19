# S7-Raspberry-Telegram

This project was created to connect S7-PLC and Raspberry by using. It can be used following the [installation](#Installation-guide) guide. This repositorie was tested in S7-1200 and S7-1500.

This reposotory contains different elements, ones for raspberry and other to install it on Windows with Anaconda:


- For Raspberry:
    - raspberry_install.sh: intallation script to get the raspberry ready to plug and play.
    - S7_connect.py: the script to run for real time communication.
   
   
- Windows:
    - Siemens_env.yaml: intallation file to install all dependencies in Anaconda enviroment.
    - snap7.dll: the file to have in the same folder of the program in order to have no errors.
   
   
- Global:
    - S7_connect.py: The program wich you could run in order to activate/deactivate a digital output of the PLC
    - connect_test.ipynb: The python notebook to make tests of the connections of PLC and Telegram independently
    - ip_check.ipynb: The program to test the check whether different connection are available.


## Installation guide

As previously commented, there are different installation guides depending the SO.

- For the raspberry:

    Open the terminal and execute the following comands. Once having this done, the raspberry will be ready to execute the python script.
   
   
```git clone https://github.com/mikelalda/snap7-raspberry```

```cd snap7-raspberry```

```./raspberry_install.sh```


- For Windows:
    First of all, install [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2021.11-Windows-x86_64.exe) and download the repository. Create a new env via importing the Siemens_env.yaml file. This could be done by the GUI or by Anaconda Powershell Prompt. If you do it by shell, execute the following comands.
   
    Once inside shell:
   
```conda env create --name snap7-raspberry --file=snap7-raspberry-main/Siemens_env.yaml```

