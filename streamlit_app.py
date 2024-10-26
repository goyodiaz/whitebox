import io
import os
import stat
import zipfile
from pathlib import Path

import requests
import streamlit as st
import whitebox

WBT_PATH = "WhiteboxTools_linux_amd64/WBT"
WBT_URL = "https://www.whiteboxgeo.com/WBT_Linux/WhiteboxTools_linux_amd64.zip"


def download_wbt():
    response = requests.get(WBT_URL)
    with zipfile.ZipFile(io.BytesIO(response.content), "r") as zip_ref:
        zip_ref.extractall()
    exe_path = WBT_PATH + "/whitebox_tools"
    st_result = os.stat(exe_path)
    os.chmod(exe_path, st_result.st_mode | stat.S_IEXEC)


if not Path(WBT_PATH).exists():
    download_wbt()

os.environ["WBT_PATH"] = WBT_PATH
wbt = whitebox.WhiteboxTools()
wbt.set_whitebox_dir(WBT_PATH)
st.write(wbt.version())
