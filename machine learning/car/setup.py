# -*- coding: utf-8 -*-
from setuptools import setup

# name, description, version등의 정보는 일반적인 setup.py와 같습니다.
setup(name="test_py2xxx",
      description="py2app test application",
      version="0.0.1",
      # 설치시 의존성 추가
      setup_requires=["py2app","sklearn"],
      app=["car-UI.py"],
      options={
          "py2app": {
              # PySide 구동에 필요한 모듈들은 포함시켜줍니다.
              "includes": ["PySide.QtCore",
                           "PySide.QtGui",
                           "PySide.QtWebKit",
                           "PySide.QtNetwork",
                           "PySide.QtXml"]
          }
      })