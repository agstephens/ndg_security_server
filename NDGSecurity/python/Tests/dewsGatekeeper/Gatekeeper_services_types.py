################################################## 
# Gatekeeper_services_types.py 
# generated by ZSI.generate.wsdl2python
##################################################


import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED
from ZSI.generate.pyclass import pyclass_type

##############################
# targetNamespace
# ndg:security:Gatekeeper
##############################

class ns0:
    targetNamespace = "ndg:security:Gatekeeper"

    class get_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "get"
        schema = "ndg:security:Gatekeeper"
        def __init__(self, **kw):
            ns = ns0.get_Dec.schema
            TClist = [ZSI.TC.String(pname="userX509Cert", aname="_userX509Cert", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="userAttributeCertificate", aname="_userAttributeCertificate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="geoserverRequest", aname="_geoserverRequest", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("ndg:security:Gatekeeper","get")
            kw["aname"] = "_get"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._userX509Cert = None
                    self._userAttributeCertificate = None
                    self._geoserverRequest = None
                    return
            Holder.__name__ = "get_Holder"
            self.pyclass = Holder

    class getResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "getResponse"
        schema = "ndg:security:Gatekeeper"
        def __init__(self, **kw):
            ns = ns0.getResponse_Dec.schema
            TClist = [ZSI.TC.String(pname="geoServerResponse", aname="_geoServerResponse", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("ndg:security:Gatekeeper","getResponse")
            kw["aname"] = "_getResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._geoServerResponse = None
                    return
            Holder.__name__ = "getResponse_Holder"
            self.pyclass = Holder

# end class ns0 (tns: ndg:security:Gatekeeper)
