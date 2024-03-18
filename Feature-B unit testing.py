class TeamMember:
    def __init__(self, name, days_off, hours_committed_to_ceremonies, available_hours_range):
        self.name = name
        
        self.days_off = max(0, days_off)
        self.hours_committed_to_ceremonies = hours_committed_to_ceremonies
        self.available_hours_range = available_hours_range

    def calculate_available_hours(self, sprint_days):
        effective_days = sprint_days - self.days_off
        average_available_hours = sum(self.available_hours_range) / 2
      
        return max(0, (average_available_hours - self.hours_committed_to_ceremonies)) * effective_days

class TeamCapacityCalculator:
    def __init__(self):
        self.team_members = []

    def add_member(self, name, days_off, hours_committed_to_ceremonies, available_hours_range):
        member = TeamMember(name, days_off, hours_committed_to_ceremonies, available_hours_range)
        self.team_members.append(member)

    def calculate_team_capacity(self, sprint_days):
        total_effort_hours = sum(member.calculate_available_hours(sprint_days) for member in self.team_members)
        return total_effort_hours

# Unit tests
import unittest

class TestTeamMember(unittest.TestCase):
    def test_calculate_available_hours(self):
        member = TeamMember("Alice", 2, 5, (8, 10))
        expected_hours = (9 - 5) * (10 - 2)
        self.assertAlmostEqual(member.calculate_available_hours(10), expected_hours)

    def test_calculate_available_hours_no_days_off(self):
        member = TeamMember("Bob", 0, 5, (8, 10))
        expected_hours = (9 - 5) * 10
        self.assertAlmostEqual(member.calculate_available_hours(10), expected_hours)

    def test_negative_days_off(self):
        member = TeamMember("Charlie", -1, 5, (8, 10))
        expected_hours = (9 - 5) * 10  
        self.assertAlmostEqual(member.calculate_available_hours(10), expected_hours)

    def test_full_commitment_to_ceremonies(self):
        member = TeamMember("Dana", 0, 9, (8, 10))
        self.assertEqual(member.calculate_available_hours(10), 0)

class TestTeamCapacityCalculator(unittest.TestCase):
    def setUp(self):
        self.team = TeamCapacityCalculator()
        self.team.add_member("Alice", 2, 5, (8, 10))
        self.team.add_member("Bob", 0, 5, (8, 10))

    def test_calculate_team_capacity(self):
        alice_hours = (9 - 5) * (10 - 2)
        bob_hours = (9 - 5) * 10
        expected_capacity = alice_hours + bob_hours
        self.assertAlmostEqual(self.team.calculate_team_capacity(10), expected_capacity)

    def test_no_members(self):
        empty_team = TeamCapacityCalculator()
        self.assertEqual(empty_team.calculate_team_capacity(10), 0)

if __name__ == '__main__':
    unittest.main()
