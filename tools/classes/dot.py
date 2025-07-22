from tools.classes.buff import Buff


class Dot(Buff):
    def to_asset(self):
        if self.buff_level:
            return {
                **super().to_asset(),
                **self.get_attributes("active")
            }
        else:
            return super().to_asset()
