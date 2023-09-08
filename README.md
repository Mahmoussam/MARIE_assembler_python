#بسم الله الرحمن الرحيم
# MARIE_assembler_python
This is a basic Python-based assembler for **MARIE** assembly language.
wrapped in PyQt5, we get our GUI, Combined with selenium, we can automate testing the machine code (in hex) on [Maire simulator](https://marie.js.org/).
![](https://github.com/Mahmoussam/MARIE_assembler_python/blob/master/test.gif)
## installation
  assuming Python 3+ is installed we need the following packages
  ```
    PyQt5
    selenium
  ```
  You may need to download a suitable web driver according to Edge browser version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and replace it with the driver exe inside project dir
## Running
  the main file is `main_c.py`
  > python main_c.py

## resources:
  ```
  Essentials of Computer Organization and Architecture book,by Linda Null
  https://medium.com/@manurahimsara/beginners-guide-to-marie-assembly-language-a22a8f04df8a
  Marie.js wiki
  https://github.com/luchko/QCodeEditor for QCodeEditor widget
  ```
....
/*thoughts and extras to do...
  handle assembling in separate thread, in order to avoid freezing with big MAR codes
  add input/output files handling
  Maybe spend more time on GUI visual improvements
*/
