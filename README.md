#بسم الله الرحمن الرحيم
# MARIE_assembler_python
This is a basic python-based assembler for **MARIE** assenbly language.
wrapped in PyQt5, we get our GUI ,combined with selenium ,we can automate testing the machine code (in hex) on [Maire simulator](https://marie.js.org/).
![](https://github.com/Mahmoussam/MARIE_assembler_python/blob/master/test.gif)
## instrallation
  assuming Python 3+ is installed we need the following packages
  ```
    PyQt5
    selenium
  ```
  you may need to download suitable webdriver according to Edge browser version from (here.)[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/] and replace with the driver exe inside project dir
## Running
  the main file is `main_c.py`
  > python main_c.py

## resources:
  ```
  Essentials of computer organization and architecture book ,by Linda Null
  https://medium.com/@manurahimsara/beginners-guide-to-marie-assembly-language-a22a8f04df8a
  Marie.js wiki
  https://github.com/luchko/QCodeEditor for QCodeEditor widget
  ```
....
/*thoughts and extras to do...
  handle assembling in separate thread ,to avoid freezing with big MAR codes
  add input/output files handling
  maybe spend more time on GUI visual imrpovments
*/
