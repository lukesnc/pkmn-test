# All types
# Author: Luke Simone

from .base import Type as _Type

NoneType = _Type(
    name='???',
    attack_type=None,
    defend_type=None
)

Fire = _Type(
    name='Fire',
    attack_type={},
    defend_type={}
)
