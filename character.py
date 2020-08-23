from creation_info import Creation_info

class Character:
    def __init__(self):
        self.ability_scores = [8,8,8,8,8,8]
        self.points = 27

    def _increase_score(self, attribute):
        """Attribute is an index number corrisponding to ability_scores"""
        if type(attribute) != int:
            raise TypeError('argument must be an integer')
        elif attribute < 0 or attribute > 5:
            raise ValueError('argument must be between 0 and 5 inclusive')
        current_score = self.ability_scores[attribute]
        if current_score >= 15:
            return None
        current_cost = Creation_info.point_cost_dict[current_score]
        increased_cost = Creation_info.point_cost_dict[current_score+1]
        if self.points + current_cost - increased_cost >= 0:
            self.ability_scores[attribute] += 1
            self.points = self.points + current_cost - increased_cost

    def _decrease_score(self, attribute):
        """Attribute is an index number corrisponding to ability_scores"""
        if type(attribute) != int:
            raise TypeError('argument must be an integer')
        elif attribute < 0 or attribute > 5:
            raise ValueError('argument must be between 0 and 5 inclusive')
        current_score = self.ability_scores[attribute]
        if current_score <= 8:
            return None
        current_cost = Creation_info.point_cost_dict[current_score]
        decreased_cost = Creation_info.point_cost_dict[current_score-1]
        self.points = self.points + current_cost - decreased_cost
        self.ability_scores[attribute] -= 1
        

    

    def score_to_modifier(score):
        return score//2 -5

    def get_str(self):
        return self.ability_scores[0]

    def inc_str(self):
        self._increase_score(0)

    def dec_str(self):
        self._decrease_score(0)

    def get_dex(self):
        return self.ability_scores[1]

    def inc_dex(self):
        self._increase_score(1)

    def dec_dex(self):
        self._decrease_score(1)

    def get_con(self):
        return self.ability_scores[2]

    def inc_con(self):
        self._increase_score(2)

    def dec_con(self):
        self._decrease_score(2)

    def get_int(self):
        return self.ability_scores[3]

    def inc_int(self):
        self._increase_score(3)

    def dec_int(self):
        self._decrease_score(3)

    def get_wis(self):
        return self.ability_scores[4]

    def inc_wis(self):
        self._increase_score(4)

    def dec_wis(self):
        self._decrease_score(4)

    def get_cha(self):
        return self.ability_scores[5]

    def inc_cha(self):
        self._increase_score(5)

    def dec_cha(self):
        self._decrease_score(5)

    
