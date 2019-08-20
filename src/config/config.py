#!/usr/bin/env python
import os


class Config():
    """
    Basic config
    """
    # Application config
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    BASE_DATA_DIR = BASE_DIR+"/data/"
    BASE_MODEL_DIR = BASE_DIR+"/core/models/"
