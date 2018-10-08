"""
Class for a player in FPL
"""

from .schema import Player
from .utils import get_player, get_predicted_points_for_player


class CandidatePlayer(object):
    """
    player class
    """

    def __init__(self, player,season="1819",gameweek=1):
        """
        initialize either by name or by ID
        """
        pdata = get_player(player)
        self.player_id = pdata.player_id
        self.name = pdata.name
        self.team = pdata.team(season,gameweek)
        self.position = pdata.position(season)
        self.current_price = pdata.current_price(season,gameweek)
        self.is_starting = True  # by default
        self.is_captain = False  # by default
        self.is_vice_captain = False  # by default
        self.predicted_points = {}

    def calc_predicted_points(self, method):
        """
        get expected points from the db.
        Will be a dict of dicts, keyed by method and gameweeek
        """
        if not method in self.predicted_points.keys():
            self.predicted_points[method] = get_predicted_points_for_player(
                self.player_id, method
            )

    def get_predicted_points(self, gameweek, method):
        """
        get points for a specific gameweek
        """
        if not method in self.predicted_points.keys():
            self.calc_predicted_points(method)
        if not gameweek in self.predicted_points[method].keys():
            print(
                "No prediction available for {} week {}".format(
                    self.data.name, gameweek
                )
            )
            return 0.
        return self.predicted_points[method][gameweek]