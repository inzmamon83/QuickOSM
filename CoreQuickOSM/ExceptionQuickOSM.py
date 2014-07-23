'''
Created on 4 juil. 2014

@author: etienne
'''

from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException
from PyQt4.QtGui import QApplication

"""
QApplication.translate doesn't work in contructor's parameters
"""

'''
Error 10-19 - Overpass
'''
class OverpassBadRequestException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("QuickOSM", u"Bad request OverpassAPI")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 10
        
class OverpassTimeoutException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("Exception", u"OverpassAPI timeout")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 11

class NetWorkErrorException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = QApplication.translate("Exception", u"Network error")
        if suffix:
            msg = msg + " with " + suffix
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 12

'''
Error 20-29 - Nominatim
'''
class NominatimAreaException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("Exception", u"No nominatim area")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 20

'''
Error 30-39 - Other
'''
class DirectoryOutPutException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("Exception", u"The output directory does not exist.")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 30
        
class FileOutPutException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg= QApplication.translate("Exception", u"The output file already exist, set a prefix")
        if suffix:
            msg = msg + " " + suffix
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 31
        
class OutPutFormatException(GeoAlgorithmExecutionException):
    def __init__(self,msg=None):
        if not msg:
            msg = QApplication.translate("Exception", u"Output not available")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 32

class Ogr2OgrException(GeoAlgorithmExecutionException):
    def __init__(self,msg=None):
        if not msg:
            msg = QApplication.translate("Exception", u"Error with ogr2ogr")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 33
        
class FileDoesntExistException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg= QApplication.translate("Exception", u"The file doesn't exist")
        if suffix:
            msg = msg + " " + suffix
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 34
        
class MissingParameterException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg= QApplication.translate("Exception", u"A parameter is missing :")
        if suffix:
            msg = msg + " " + suffix
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 35
        
class NoLayerException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg= QApplication.translate("Exception", u"The layer is missing :")
        if suffix:
            msg = msg + " " + suffix
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 36
        
class OsmObjectsException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg= QApplication.translate("Exception", u"No osm objects selected")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 37
        
class OutPutGeomTypesException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg= QApplication.translate("Exception", u"No outputs selected")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 38
        
class QueryAlreadyExistsException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        if not msg:
            msg= QApplication.translate("Exception", u"This query already exists")
        GeoAlgorithmExecutionException.__init__(self,msg)
        self.errorNumber = 39