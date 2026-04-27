import logging
import os
from datetime import datetime

LOGFILE=f"{datetime.now().strftime("%m%d%Y__%H%M%S")}.log"
LOGPATH=os.path.join(os.getcwd(),"logs",LOGFILE)
os.makedirs(os.path.dirname(LOGPATH),exist_ok=True)

LOGFILEPATH=LOGPATH
logging.basicConfig(
    filename=LOGFILEPATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)   



