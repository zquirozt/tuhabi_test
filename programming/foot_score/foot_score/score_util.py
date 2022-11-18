from typing import List


def find_first_match(value: int, input_list: List[int]) -> int:
    result = len(input_list)
    for index in range(result):
        if input_list[index] <= value:
            result = index
            break
    return result


def counts(team_a: List[int], team_b: List[int]) -> List[int]:
    result = []
    result_list = team_b.copy()
    dictionary = {}
    team_a.sort(reverse=True)
    team_b.sort(reverse=True)

    for score_b in team_b:
        first_match_position = find_first_match(score_b, team_a)
        dictionary[score_b] = len(team_a) - first_match_position
        team_a = team_a[first_match_position: len(team_a)]

    for list_value in result_list:
        result.append(dictionary[list_value])

    return result


def counts_brutforce(team_a: List[int], team_b: List[int]) -> List[int]:
    result = []
    for team_b_gol_number in team_b:
        result.append(
            len(list(filter(lambda x: (x <= team_b_gol_number), team_a)))
        )
    return result
