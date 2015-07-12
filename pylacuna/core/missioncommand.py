#!/usr/bin/env python
import pylacuna.core.building as building


class MissionCommand(building.Building):
    def get_missions(self):
        return self.session.call_method_with_session_id(
            route='missioncommand',
            method='get_missions',
            params=[self.id])

    def complete_mission(self, mission_id):
        return self.session.call_method_with_session_id(
            route='missioncommand',
            method='complete_mission',
            params=[self.id, mission_id])

    def skip_mission(self, mission_id):
        return self.session.call_method_with_session_id(
            route='missioncommand',
            method='skip_mission',
            params=[self.id, mission_id])
