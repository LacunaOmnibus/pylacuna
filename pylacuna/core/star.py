#!/usr/bin/env python


class Star(dict):
    def __init__(self, session, star_id, aDict=None, bodies=None):
        '''
        session -- a Session object
        star_id -- the id for the star
        aDict -- extra kv dict to add to the star
        bodies -- list of pylacuna body objects belonging to this star
        '''
        super(Star, self).__init__()
        self.session = session
        self.id = star_id
        if aDict is not None:
            self.update(aDict)
        if bodies is None:
            bodies = []
        self.bodies = bodies

    def view(self):
        return self.get_bodies()

    def get_bodies(self):
        response = self.session.call_method_with_session_id(
            route='map',
            method='get_star',
            params=[self.id])
        results = response['result']
        self.update(results['bodies'])

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
