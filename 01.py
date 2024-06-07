# Instalando o Selenium
# !pip install selenium

# Atualizando o Ubuntu para executar corretamento o apt-install
# !apt-get update

# Instalando o ChromeDrive e Trazendo ele para a Pasta Local
# !apt install chromium-chromedriver

# !cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
import os
import numpy as np
"""# Configuração do Web-Driver"""

# Utilizando o WebDriver do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_argument('--log-level=3')


# Criação do WebDriver do Chrome
# wd_Chrome = webdriver.Chrome('chromedriver',options=options)
wd_Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


"""# Importando as Bibliotecas"""

import pandas as pd
import time
from tqdm import tqdm

"""# Iniciando a Raspagem de Dados"""

# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com/") 
time.sleep(2)