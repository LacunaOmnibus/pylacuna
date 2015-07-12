#!/usr/bin/env python
import pylacuna.core.building as building
import pylacuna.core.star as star
import pylacuna.core.body as body


class Observatory(building.Building):
    def get_all_probed_stars(self):
        ''' Repeated call get_probed_stars until we've got them all '''
        pass

    def get_probed_stars(self, page_number=1):
        result = self.session.call_method_with_session_id(
            route='observatory',
            method='get_probed_stars',
            params=[self.id, page_number])
        stars = result['result']['stars']
        # Nested list comprehensions ftw! This basically creates a list of
        # star objects, each with an embedded list of body objects.
        stars = [star.Star(self.session, s['id'], s,
                 [body.Body(self.session, b['id'], b) for b in s['bodies']])
                 for s in stars]
        return stars

    def abandon_probe(self, star_id):
        return self.session.call_method_with_session_id(
            route='observatory',
            method='abandon_probe',
            params=[self.id, star_id])

    def abandon_all_probes(self):
        return self.session.call_method_with_session_id(
            route='observatory',
            method='abandon_all_probes',
            params=[self.id])
