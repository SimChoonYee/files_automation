## See if the import could works
import imp
import zipfile
try:
    imp.find_module('zipfile36')
    from zipfile import ZipFile
    ##print("Found import zipfile36")
except ImportError:
    print("Failed to import zipfile36")
    
    
from pzip.pzipMain import PunzipClass

zipInstance = PunzipClass("test.zip")
print("End of Program")