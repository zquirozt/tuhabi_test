import pytest

from foot_score.score_util import counts, counts_brutforce
from tests.resources import test_case_1


data = [
    (test_case_1.get("team_a"),test_case_1.get("team_b"),test_case_1.get("expected_results")),
    ([2, 10, 5, 4, 8], [3, 1, 7, 8], [1, 0, 3, 4]),
    ([1, 2, 3], [2, 4], [2, 3])
]


@pytest.mark.parametrize("team_a_score_list, team_b_score_list, result", data)
def test_validate_team_goals_brutforce(team_a_score_list, team_b_score_list, result):
    assert counts_brutforce(team_a_score_list, team_b_score_list) == result

@pytest.mark.parametrize("team_a_score_list, team_b_score_list, result", data)
def test_validate_team_goals(team_a_score_list, team_b_score_list, result):
    assert counts(team_a_score_list, team_b_score_list) == result