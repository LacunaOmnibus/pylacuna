#!/usr/bin/env python


class Building(dict):
    ''' Common methods for working with buildings '''
    def __init__(self, session, building_id, aDict):
        super(Building, self).__init__()
        self.update(aDict)

    def build(self, x, y):
        assert 'url' in self, "Must have a url to build"
        return self.session.call_method_with_session_id(
            route='buildings{}'.format(self['url']),
            method='build',
            params=[self.id, x, y])

    def view (self, building_id ):
        raise NotImplementedError

    def upgrade (self, building_id ):
        raise NotImplementedError

    def demolish (self, building_id ):
        raise NotImplementedError

    def downgrade (self, building_id ):
        raise NotImplementedError

    def get_stats_for_level (self, building_id, level ):
        raise NotImplementedError

    def repair (self, building_id ):
        raise NotImplementedError


# Todo. Make all these classes into their own files:
class Algae(Building):
    pass

class AlgaePond(Building):
    pass

class AmalgusMeadow(Building):
    pass

class Apple(Building):
    pass

class Archaeology(Building):
    pass

class AtmosphericEvaporator(Building):
    pass

class Beach(Building):
    pass

class Bean(Building):
    pass

class Beeldeban(Building):
    pass

class BeeldebanNest(Building):
    pass

class BlackHoleGenerator(Building):
    pass

class Bread(Building):
    pass

class Burger(Building):
    pass

class Capitol(Building):
    pass

class Cheese(Building):
    pass

class Chip(Building):
    pass

class Cider(Building):
    pass

class CitadelOfKnope(Building):
    pass

class CloakingLab(Building):
    pass

class Corn(Building):
    pass

class CornMeal(Building):
    pass

class CrashedShipSite(Building):
    pass

class Crater(Building):
    pass

class Dairy(Building):
    pass

class Denton(Building):
    pass

class DentonBrambles(Building):
    pass

class DeployedBleeder(Building):
    pass

class Development(Building):
    pass

class DistributionCenter(Building):
    pass

class Embassy(Building):
    pass

class EnergyReserve(Building):
    pass

class Entertainment(Building):
    pass

class Espionage(Building):
    pass

class EssentiaVein(Building):
    pass

class Fission(Building):
    pass

class Fissure(Building):
    pass

class FoodReserve(Building):
    pass

class Fusion(Building):
    pass

class GasGiantLab(Building):
    pass

class GasGiantPlatform(Building):
    pass

class GeneticsLab(Building):
    pass

class Geo(Building):
    pass

class GeoThermalVent(Building):
    pass

class GratchsGauntlet(Building):
    pass

class GreatBallOfJunk(Building):
    pass

class Grove(Building):
    pass

class HallsOfVrbansk(Building):
    pass

class Hydrocarbon(Building):
    pass

class Intelligence(Building):
    pass

class IntelTraining(Building):
    pass

class InterDimensionalRift(Building):
    pass

class JunkHengeSculpture(Building):
    pass

class KalavianRuins(Building):
    pass

class KasternsKeep(Building):
    pass

class Lake(Building):
    pass

class Lagoon(Building):
    pass

class Lapis(Building):
    pass

class LapisForest(Building):
    pass

class LibraryOfJith(Building):
    pass

class LostCityOfTyleon(Building):
    pass

class LuxuryHousing(Building):
    pass

class Malcud(Building):
    pass

class MalcudField(Building):
    pass

class MassadsHenge(Building):
    pass

class MayhemTraining(Building):
    pass

class MercenariesGuild(Building):
    pass

class MetalJunkArches(Building):
    pass

class Mine(Building):
    pass

class MiningMinistry(Building):
    pass

class MissionCommand(Building):
    pass

class MunitionsLab(Building):
    pass

class NaturalSpring(Building):
    pass

class Network19(Building):
    pass

class Observatory(Building):
    pass

class OracleOfAnid(Building):
    pass

class OreRefinery(Building):
    pass

class OreStorage(Building):
    pass

class Oversight(Building):
    pass

class Pancake(Building):
    pass

class PantheonOfHagness(Building):
    pass

class Park(Building):
    pass

class Pie(Building):
    pass

class PilotTraining(Building):
    pass

class PlanetaryCommand(Building):
    pass

class PoliticsTraining(Building):
    pass

class Potato(Building):
    pass

class Propulsion(Building):
    pass

class PyramidJunkSculpture(Building):
    pass

class Ravine(Building):
    pass

class RockyOutcrop(Building):
    pass

class Sand(Building):
    pass

class SAW(Building):
    pass

class Security(Building):
    pass

class Shake(Building):
    pass

class Shipyard(Building):
    pass

class Singularity(Building):
    pass

class Soup(Building):
    pass

class SpaceJunkPark(Building):
    pass

class SpacePort(Building):
    pass

class SpaceStationLab(Building):
    pass

class Stockpile(Building):
    pass

class SubspaceSupplyDepot(Building):
    pass

class SupplyPod(Building):
    pass

class Syrup(Building):
    pass

class TempleOfTheDrajilites(Building):
    pass

class TerraformingLab(Building):
    pass

class TerraformingPlatform(Building):
    pass

class TheDillonForge(Building):
    pass

class TheftTraining(Building):
    pass

class ThemePark(Building):
    pass

class Trade(Building):
    pass

class Transporter(Building):
    pass

class University(Building):
    pass

class Volcano(Building):
    pass

class WasteDigester(Building):
    pass

class WasteEnergy(Building):
    pass

class WasteExchanger(Building):
    pass

class WasteRecycling(Building):
    pass

class WasteSequestration(Building):
    pass

class WasteTreatment(Building):
    pass

class WaterProduction(Building):
    pass

class WaterPurification(Building):
    pass

class WaterReclamation(Building):
    pass

class WaterStorage(Building):
    pass

class Wheat(Building):
    pass

