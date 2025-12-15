class PlannerAgent:
    """
    Converts a QA test description into executable steps
    """

    def create_plan(self, test_case: str):
        test_case = test_case.lower()
        steps = []

        if "launch" in test_case or "open obsidian" in test_case:
            steps.append("LAUNCH_OBSIDIAN")

        if "create note" in test_case:
            steps.append("CREATE_NOTE")

        if "type" in test_case or "enter text" in test_case:
            steps.append("ENTER_TEXT")

        if "verify" in test_case:
            steps.append("VERIFY_PERSISTENCE")

        return steps
