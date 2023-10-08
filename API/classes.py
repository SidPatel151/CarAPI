from dataclasses import dataclass 
from typing import Optional, Union, Dict


@dataclass
class Comparable:
  def __eq__(self, other):
    self_id = getattr(self, 'id', None)
    self_name = getattr(self, 'name', None)
    other_id = getattr(other, 'id', None)
    other_name = getattr(other, 'name', None)
    if self_id and self_name and other_id and other_name:
      return self_id == other_id and self_name == other_name
    return False


@dataclass
class Make:
    id: int
    name: str
   
    def __repr__(self) -> str:
        return f"Make(id={self.id}, name={self.name})"


@dataclass
class Model(Comparable):
  id: int
  name: str
  make_id: int

  def __repr__(self) -> str:
    return f"Model(id={self.id}, name={self.name}, make_id={self.make_id})"


@dataclass
class Body:
    data: Dict

    @property
    def id(self) -> int:
        return self.data.get("id")

    @property
    def name(self) -> str:
        make_model_trim = self.data.get("make_model_trim", {})
        make_model = make_model_trim.get("make_model", {})
        make = make_model.get("make", {})
        return make.get("name", "Unknown Make Name")
    @property
    def type(self) -> str:
        return self.data.get("type")

    @property
    def doors(self) -> int:
        return self.data.get("doors")

    @property
    def length(self) -> float:
        return self.data.get("length")

    @property
    def width(self) -> float:
        return self.data.get("width")

    @property
    def height(self) -> float:
        return self.data.get("height")

    @property
    def wheel_base(self) -> float:
        return self.data.get("wheel_base")

    @property
    def cargo_capacity(self) -> float:
        return self.data.get("cargo_capacity")

    def __repr__(self) -> str:
        return (f"Body(id={self.id}, name={self.name}, type={self.type}, doors={self.doors}, "
                f"length={self.length}, width={self.width}, height={self.height}, "
                f"wheel_base={self.wheel_base}, cargo_capacity={self.cargo_capacity})")


@dataclass
class Engine:
    def __init__(self, data: Dict):
      self.data = data
      self.hp_msg = None
      self.fuel_msg = None

    @property
    def engine_type(self) -> str:
        return self.data.get("engine_type")

    @property
    def horsepower_hp(self) -> Union[int, None]:
        if self.data.get('horsepower_hp'):
            return self.data.get("horsepower_hp")
        else:
            return self.hp_msg if self.hp_msg else "No hp given"

    @horsepower_hp.setter
    def set_horsepower_hp(self, msg: str):
        self.hp_msg = msg

    @property
    def torque_ft_lbs(self) -> Union[int, None]:
        return self.data.get("torque_ft_lbs")

    @property
    def transmission(self) -> str:
        return self.data.get("transmission")

    @property
    def fuel_type(self, msg:str = None) -> str:
        if self.data.get('fuel_type'):
          return self.data.get("fuel_type")
        else:
          return self.fuel_msg if self.fuel.msg else "No fuel type given"

    @fuel_type.setter
    def set_fuel_type(self, msg: str):
      self.fuel_msg = msg

    def __repr__(self) -> str:
        return (f"Engine(engine_type={self.engine_type}, horsepower_hp={self.horsepower_hp}, "
                f"torque_ft_lbs={self.torque_ft_lbs}, transmission={self.transmission}, fuel_type={self.fuel_type})")


@dataclass
class Mileage:
    def __init__(self, data: Dict, custom: str = None):
      self.data = data
      self.custom = custom

    @property
    def fuel_tank_capacity(self) -> float:
        if self.data.get("fuel_tank_capacity"):
            return self.data.get("fuel_tank_capacity")
        else:
            return self.custom if self.custom else "No fuel_tank given"

    @property
    def combined_mpg(self) -> float:
        if self.data.get("combined_mpg"): 
            return self.data.get("combined_mpg")
        else:
            return self.custom if self.custom else "No mpg given"

    @property
    def battery_capacity_electric(self) -> float:
        if self.data.get("battery_capacity_electric"):
            return self.data.get("battery_capacity_electric")
        else:
            return self.custom if self.custom else "No capacity given"

    @property
    def epa_combined_mpg_electric(self) -> float:
        if self.data.get("epa_combined_mpg_electric"):
            return self.data.get("epa_combined_mpg_electric")
        else:
            return self.custom if self.custom else "No epa mpg given"

    def __repr__(self) -> str:
        return (f"Mileage(fuel_tank_capacity={self.fuel_tank_capacity}, "
                f"combined_mpg={self.combined_mpg}, "
                f"battery_capacity_electric={self.battery_capacity_electric}, "
                f"epa_combined_mpg_electric={self.epa_combined_mpg_electric})")


@dataclass
class Trim:
    data: Dict

    @property
    def msrp(self) -> int:
        return self.data.get("msrp")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def description(self) -> str:
        return self.data.get("description")