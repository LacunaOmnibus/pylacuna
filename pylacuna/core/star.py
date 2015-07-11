#!/usr/bin/env python


class Star(dict):
    def __init__(self, session, star_id):
        '''
        session -- a Session object
        star_id -- the id for the star
        '''
        super(Star, self).__init__()
        self.session = session
        self.id = star_id
        self.bodies = []

    def view(self):
        return self.get_bodies()

    def get_bodies(self):
        response = self.session.call_method_with_session_id(
            route='map',
            method='get_star',
            params=[self.id])
        results = response['result']
        self.update(results['star'])

        # if 'bodies' in results['star']:
        #     deletionlist = set([x.id for x in self.buildings]).difference(
        #         set([uid for uid in results['buildings']]))
        #     totalset = set([x.id for x in self.buildings])
        #     totalset.update([uid for uid in results['buildings']])
        #     for uid in totalset:
        #         if uid in deletionlist:
        #             # print 'DELETING {}'.format(uid)
        #             self.buildings.remove(uid)
        #         elif uid in self.buildings:
        #             # print "UPDATING {}".format(uid)
        #             idx = self.buildings.index(uid)
        #             self.buildings[idx].update(results['buildings'][uid])
        #         else:
        #             # print "ADDING {}".format(uid)
        #             self.buildings.append(building.Building(
        #                 session=self.session,
        #                 building_id=uid,
        #                 aDict=results['buildings'][uid]))
        return results

    def repair_list(self, building_ids):
        return self.session.call_method_with_session_id(
            route='body',
            method='repair_list',
            params=[self.id, building_ids])

    def rearrange_buildings(self, arrangement):
        return self.session.call_method_with_session_id(
            route='body',
            method='rearrange_buildings',
            params=[self.id, arrangement])

    def get_buildable(self, x, y, tag):
        '''
        tag -- TBD
        '''
        return self.session.call_method_with_session_id(
            route='body',
            method='get_buildable',
            params=[self.id, x, y, tag])

    def rename(self, name):
        return self.session.call_method_with_session_id(
            route='body',
            method='rename',
            params=[self.id, name])

    def abandon(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='abandon',
            params=[self.id])

    def view_laws(self):
        return self.session.call_method_with_session_id(
            route='body',
            method='view_laws',
            params=[self.id])

    def build(self, building_name, x, y):
        return self.session.call_method_with_session_id(
            route='/{}'.format(building_name),
            method='build',
            params=[self.id, x, y])
