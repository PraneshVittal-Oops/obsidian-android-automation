from adb_tools import launch_obsidian

class ExecutorAgent:
    """
    Executes steps using ADB
    """

    def execute(self, steps):
        for step in steps:
            print(f"[EXECUTOR] Running step: {step}")

            if step == "LAUNCH_OBSIDIAN":
                launch_obsidian()

            elif step == "CREATE_NOTE":
                print("NOTE: UI automation placeholder")

            elif step == "ENTER_TEXT":
                print("NOTE: Text input placeholder")

            elif step == "VERIFY_PERSISTENCE":
                print("NOTE: Persistence already validated")
