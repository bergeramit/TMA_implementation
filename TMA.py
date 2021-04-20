
class Person:
    def __init__(self, name, _id, preferences):
        self._id = _id
        self.name = name
        self._preferences = preferences
    
        # Start with the top preference
        self._next_preference_index = 0

    def _get_id_of_current_preferred(self):
        return self._preferences[self._next_preference_index]
    
    def _move_to_the_next_preference(self):
        self._next_preference_index += 1
    
    def __repr__(self):
        return "{}({})".format(self.name, self._id)
    
    def _get_prefrence_by_girl_id(self, boy_id):
        return self._preferences.index(boy_id)


class Boy(Person):
    pass


class Girl(Person):
    pass


class TMA:
    def __init__(self, optimal_side, wrost_side, amount_to_choose):
        self._boys, self._girls = optimal_side, wrost_side
        self._prev_state = None
        self._current_state = self._get_current_state()
        self._amount_to_choose = amount_to_choose

    def _get_current_state(self):
        # The state is represented by the favorite girl per boy.
        # When every boy favors one girl => we are done.
        return [boy._get_id_of_current_preferred() for boy in self._boys]

    @property
    def _changes_occurred(self):
        return self._prev_state != self._current_state

    def _get_candidates_by_girls(self):
        candidates_by_girls = {girl: [] for girl in self._girls}
        for boy in self._boys:
            girl_peaked = boy._get_id_of_current_preferred()
            candidates_by_girls[self._girls[girl_peaked]].append(boy)
        
        return candidates_by_girls

    def _update_preferences(self, girl, candidates):
        candidates = sorted(candidates, key= lambda x: girl._get_prefrence_by_girl_id(x._id))

        for candidate in candidates[self._amount_to_choose:]:
            self._boys[candidate._id]._move_to_the_next_preference()

    def _build_final_match(self):
        return [(boy, self._girls[boy._get_id_of_current_preferred()]) for boy in self._boys]
    
    def _print_girls_balcony_status(self, girl, candidates):
        boys_on_balcony = ", ".join([boy.name for boy in candidates])
        print("{}'s Balcony: {}".format(girl.name, boys_on_balcony))

    def _run(self):
        print("Begin TMA...")
        iteration = 0
        while self._changes_occurred:
            self._prev_state = self._current_state
            print("Day {}".format(iteration))

            candidates_by_girls = self._get_candidates_by_girls()
            for girl, candidates in candidates_by_girls.items():

                self._print_girls_balcony_status(girl, candidates)
                self._update_preferences(girl, candidates)

            iteration += 1
            self._current_state = self._get_current_state()
            print()

        print("Finished")

    def get_stable_matching(self):
        self._run()
        return self._build_final_match()
