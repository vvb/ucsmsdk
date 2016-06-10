"""This module contains the general information for LstorageDiskSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageDiskSlotConsts:
    OWNERSHIP_CHASSIS_DEDICATED_SPARE = "chassis-dedicated-spare"
    OWNERSHIP_CHASSIS_GLOBAL_SPARE = "chassis-global-spare"
    OWNERSHIP_DEDICATED = "dedicated"
    OWNERSHIP_SHARED = "shared"
    OWNERSHIP_UNASSIGNED = "unassigned"
    OWNERSHIP_UNKNOWN = "unknown"


class LstorageDiskSlot(ManagedObject):
    """This is LstorageDiskSlot class."""

    consts = LstorageDiskSlotConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("LstorageDiskSlot", "lstorageDiskSlot", "disk-slot-[id]", VersionMeta.Version911z, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'lstorageDiskZoningConfigDef', u'lstorageDiskZoningPolicy'], [u'lstorageControllerRef'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version911z, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version911z, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-60"]), 
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["chassis-dedicated-spare", "chassis-global-spare", "dedicated", "shared", "unassigned", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "ownership": "ownership", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ownership = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageDiskSlot", parent_mo_or_dn, **kwargs)
