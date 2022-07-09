# pyuic6 ui\main_window.ui -o ui\main_window_gui.py

venv\Lib\site-packages\PySide6\uic.exe --generator python ui\main_window.ui -o ui\main_window_gui.py
venv\Lib\site-packages\PySide6\rcc.exe --generator python ui\resources.qrc -o resources_rc.py