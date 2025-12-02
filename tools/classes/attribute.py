from typing import TYPE_CHECKING

from base.attribute import *

if TYPE_CHECKING:
    from tools.classes.damage import DamageChain  # noqa


class Attribute(BaseAttribute):
    damage_chain: "DamageChain"

    def call_physical_damage(self, damage_base, damage_rand):
        self.damage_chain.physical_damage_call(damage_base, damage_rand)

    def call_solar_damage(self, damage_base, damage_rand):
        self.damage_chain.solar_damage_call(damage_base, damage_rand)

    def call_lunar_damage(self, damage_base, damage_rand):
        self.damage_chain.lunar_damage_call(damage_base, damage_rand)

    def call_neutral_damage(self, damage_base, damage_rand):
        self.damage_chain.neutral_damage_call(damage_base, damage_rand)

    def call_poison_damage(self, damage_base, damage_rand):
        self.damage_chain.poison_damage_call(damage_base, damage_rand)

    def call_physical_surplus(self, damage_base, damage_rand):
        self.damage_chain.physical_surplus_call(damage_base, damage_rand)

    def call_solar_surplus(self, damage_base, damage_rand):
        self.damage_chain.solar_surplus_call(damage_base, damage_rand)

    def call_lunar_surplus(self, damage_base, damage_rand):
        self.damage_chain.lunar_surplus_call(damage_base, damage_rand)

    def call_neutral_surplus(self, damage_base, damage_rand):
        self.damage_chain.neutral_surplus_call(damage_base, damage_rand)

    def call_poison_surplus(self, damage_base, damage_rand):
        self.damage_chain.poison_surplus_call(damage_base, damage_rand)

    def custom_damage_call(self):
        self.damage_chain.custom_damage_call()