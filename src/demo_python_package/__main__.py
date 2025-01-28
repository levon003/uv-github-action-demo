import logging
import sys
import os
from demo_python_package import git_utils

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    current_branch_name = os.environ.get("CURRENT_BRANCH_NAME", "infer")
    if current_branch_name == "infer":
        current_branch_name = git_utils.get_current_branch()
    logger.info(f"Validating relative to branch '{current_branch_name}'.")

    added_files, changed_files, deleted_files = git_utils.get_diff_files(
        source_branch=current_branch_name,
    )
    total_files_changed = added_files | changed_files | deleted_files
    if len(total_files_changed) >= 20:
        logger.error(
            f"{len(total_files_changed)} files have changed, which is more than should be touched in a single change!"
        )
        sys.exit(1)
    logger.info("Validation succeeded.")


if __name__ == "__main__":
    main()
