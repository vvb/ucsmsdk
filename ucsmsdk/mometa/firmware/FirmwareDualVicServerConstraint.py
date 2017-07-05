"""This module contains the general information for FirmwareDualVicServerConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareDualVicServerConstraintConsts:
    CHECK_RUNNING_VER_FALSE = "false"
    CHECK_RUNNING_VER_NO = "no"
    CHECK_RUNNING_VER_TRUE = "true"
    CHECK_RUNNING_VER_YES = "yes"


class FirmwareDualVicServerConstraint(ManagedObject):
    """This is FirmwareDualVicServerConstraint class."""

    consts = FirmwareDualVicServerConstraintConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareDualVicServerConstraint", "firmwareDualVicServerConstraint", "dual-vic-server-constraint", None, "InputOutput", 0x1f, [], ["read-only"], [u'firmwareConstraints'], [], [None])

    prop_meta = {
        "check_running_ver": MoPropertyMeta("check_running_ver", "checkRunningVer", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "min_bios_version": MoPropertyMeta("min_bios_version", "minBiosVersion", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "checkRunningVer": "check_running_ver", 
        "childAction": "child_action", 
        "dn": "dn", 
        "minBiosVersion": "min_bios_version", 
        "minCimcVersion": "min_cimc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.check_running_ver = None
        self.child_action = None
        self.min_bios_version = None
        self.min_cimc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareDualVicServerConstraint", parent_mo_or_dn, **kwargs)
