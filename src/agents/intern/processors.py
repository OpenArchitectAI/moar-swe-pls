from src.agents.intern.generators.code_generator import CodeGenerator
from src.language_models import gpt4
import dspy

from src.models import Codebase, Ticket


def better_code_change(previous_code_change, pr, comments):
    # This function will be called from Intern.process_pr
    # It will take the previous code_change, the pr and the comments
    # and will return a new code_change
    # The previous code_change will be the last code_change that was pushed to the PR
    # The pr will be the PR that is being processed
    # The comments will be the comments that were made on the PR since the last code_change
    # The function will return a new code_change that will be pushed to the PR
    return "new_code_change"


def generate_code_change(ticket: Ticket, code_base: Codebase):
    # This function will be called from Intern.process_ticket
    # It will take the ticket and the code_base
    # and will return a new code_change
    dspy.configure(lm=gpt4)

    diff_generator = CodeGenerator()

    res = diff_generator(code_base, ticket)

    return res["new_files"], res["explanations"]
