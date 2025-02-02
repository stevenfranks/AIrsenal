"""
test that we get valid responses from the API.
"""

import pytest

from ..framework.data_fetcher import *


def test_instantiate_fetchers():
    """
    check we can instantiate the classes
    """
    fpl = FPLDataFetcher()
    assert(fpl)
    fd = MatchDataFetcher()
    assert(fd)


def test_get_summary_data():
    """
    get summary of all players' data for this season.
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_current_summary_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)

@pytest.mark.skip("No team data before start of season")
def test_get_team_data():
    """
    should give current list of players in our team
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_fpl_team_data(1)
    assert(isinstance(data,list))
    assert(len(data)==15)


def test_get_team_history_data():
    """
    gameweek history for our team id
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_fpl_team_history_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)

@pytest.mark.skip("No league data before start of season")
def test_get_league_data():
    """
    gameweek history for our mini-league
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_fpl_league_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)


def test_get_event_data():
    """
    gameweek list with deadlines and status
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_event_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)


def test_get_player_summary_data():
    """
    summary for individual players
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_player_summary_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)


def test_get_current_team_data():
    """
    summary for current teams
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_current_team_data()
    assert(isinstance(data,dict))
    assert(len(data)>0)

@pytest.mark.skip("No data yet for gameweek 1")
def test_get_detailed_player_data():
    """
    for player_id=1, list of gameweek data
    """
    fetcher = FPLDataFetcher()
    data = fetcher.get_gameweek_data_for_player(1)
    assert(isinstance(data,dict))
    assert(len(data)>0)



def test_get_results():
    """
    test the matchdatafetcher
    """
    fetcher = MatchDataFetcher()
    data = fetcher.get_results(1)
    assert(isinstance(data,list))
    assert(len(data)==10)


def test_get_fixtures():
    """
    get fixtures from matchdatafetcher
    """
    fetcher = MatchDataFetcher()
    data = fetcher.get_fixtures(38)
    assert isinstance(data, list)
    assert(len(data)==10)
