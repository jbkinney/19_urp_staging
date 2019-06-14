# 19_urp
A Python tutorial designed for the 2019 Undergraduate Research Program at Cold Spring Harbor Laboratory.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jbkinney/19_urp/master)

## If installing on personal computers

Step 1 : Regardless of computer download repository to desktop and unzip
### Mac Instructions

    1. Open a new terminal and type `cd /Desktop/19_urp/` then hit enter. This should put you in the folder of the repository
    2. Type './mac_install.sh' and hit enter to run. Follow the prompts for installing. Type 'y' or 'yes' when prompted and hit enter when asked a non y/n question
    3. You've installed Python
    4. To start notebooks type `jupyter notebook` and hit enter

### Windows Instructions

    1. Go to this [website](https://docs.conda.io/en/latest/miniconda.html) and download the **64-bit (exe-installer)** in the table at the top of the site in the **Python 3.7** row for Windows 
    2. Click the exe file you downloaded and follow the prompts to complete the installation
    3. Open Anaconda Prompt
    4. type `conda install --file` but don't hit enter yet
    5. In Windows Explorer navigate to the /19_urp folder then drag the file titled `requirements_windows.txt` into the Anaconda Prompt and hit enter
    6. Answer Y or Yes to any y/n questions
    7. Type `pip install logomaker` and hit enter
    8. Type `jupyter-notebook` into the Anaconda Prompt and hit enter
