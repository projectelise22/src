# Test File to test Tasks project
from tasks import Task

def test_asdict():
    """asdict() should return a dictionary"""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected

# Sample test to write test functions in pytest
def test_sample_01():
    random_parameter = "check"
    expected_list = ["hello", "what", "yes", "check"]
    assert random_parameter in expected_list, f"'{random_parameter}' not in expected list"

