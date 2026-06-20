import unittest

from autonomous_agent_hive import AgentAction, evaluate_action


class GatekeeperTests(unittest.TestCase):
    def test_executes_low_risk_read_action(self):
        decision = evaluate_action(AgentAction("agent-1", "observe", 1, 0.1))

        self.assertTrue(decision.can_execute)

    def test_waits_during_cooldown(self):
        decision = evaluate_action(AgentAction("agent-1", "observe", 1, 0.1, 30))

        self.assertEqual(decision.route, "wait")

    def test_reviews_low_authority_write_action(self):
        decision = evaluate_action(AgentAction("agent-1", "deploy", 2, 0.2))

        self.assertEqual(decision.route, "review")

    def test_reviews_high_risk_action(self):
        decision = evaluate_action(AgentAction("agent-1", "observe", 5, 0.9))

        self.assertEqual(decision.route, "review")


if __name__ == "__main__":
    unittest.main()

