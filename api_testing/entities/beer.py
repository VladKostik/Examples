from __future__ import annotations


class Beer:
    def __init__(
            self,
            id,
            name,
            tagline,
            first_brewed,
            abv,
            ibu,
            target_fg,
            target_og,
            ebc,
            srm,
            ph
    ):
        self.id = id,
        self.name = name,
        self.tagline = tagline,
        self.first_brewed = first_brewed,
        self.abv = abv,
        self.ibu = ibu,
        self.target_fg = target_fg,
        self.target_og = target_og,
        self.ebc = ebc,
        self.srm = srm,
        self.ph = ph

    def __eq__(self, other: Beer):
        return self.__dict__ == other.__dict__
