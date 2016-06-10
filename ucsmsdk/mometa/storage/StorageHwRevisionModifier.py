"""This module contains the general information for StorageHwRevisionModifier ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageHwRevisionModifierConsts:
    HW_TYPE_LOCAL_DISK = "local-disk"
    HW_TYPE_LOCAL_DISK_PCH = "local-disk-pch"
    HW_TYPE_STORAGE_CONTROLLER = "storage-controller"


class StorageHwRevisionModifier(ManagedObject):
    """This is StorageHwRevisionModifier class."""

    consts = StorageHwRevisionModifierConsts()
    naming_props = set([u'hwType'])

    mo_meta = MoMeta("StorageHwRevisionModifier", "storageHwRevisionModifier", "hw-rev-modifier-[hw_type]", VersionMeta.Version911z, "InputOutput", 0x3f, [], [""], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider', u'storageEnclosureCap'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version911z, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hw_type": MoPropertyMeta("hw_type", "hwType", "string", VersionMeta.Version911z, MoPropertyMeta.NAMING, 0x8, None, None, None, ["local-disk", "local-disk-pch", "storage-controller"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hwType": "hw_type", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, hw_type, **kwargs):
        self._dirty_mask = 0
        self.hw_type = hw_type
        self.child_action = None
        self.revision = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageHwRevisionModifier", parent_mo_or_dn, **kwargs)
