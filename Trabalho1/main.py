import ctypes
from typing import NewType
import clr
import sys
sys.path.append(r"F:\Roger\Faculdade\Inteligencia Artificial Avançada\Trabalho1\AdrenaDLL")
clr.AddReference("ADReNA_API")

import ADReNA_API

#back = py_object(ADReNA_API)



my_func = getattr(ADReNA_API)

my_func()



print(back)

#adrenaDll = ctypes.WinDLL ("AdrenaDLL\\ADReNA_API.dll")
#newDll = ctypes.WinDLL ("AdrenaDLL\\Newtonsoft.Json.dll")


#adrenaDll = cdll.LoadLibrary("AdrenaDLL\\ADReNA_API.dll")

#backpropagation = adrenaDll.

