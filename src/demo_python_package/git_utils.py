import logging
import subprocess

logger = logging.getLogger(__name__)


def get_diff_files(
    source_branch: str, target_branch: str = "main"
) -> tuple[set[str], set[str], set[str]]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-status", target_branch, source_branch],
            capture_output=True,
            text=True,
            check=True,
        )
        added_files, changed_files, deleted_files = set(), set(), set()
        diff_lines = result.stdout.strip().split("\n")
        logger.info(f"Identified {len(diff_lines)} git file changes.")
        for line in diff_lines:
            if line.strip() == "":
                continue
            tokens = line.split()
            if len(tokens) != 2:
                raise ValueError(f"Line '{line}' has an unexpected format.")
            change_status, relative_filepath = tokens

            if change_status == "M":
                changed_files.add(relative_filepath)
            elif change_status == "A":
                added_files.add(relative_filepath)
            elif change_status == "D":
                deleted_files.add(relative_filepath)
            else:
                raise ValueError(
                    f"git diff line '{line}' had unknown change status '{change_status}'."
                )
        return added_files, changed_files, deleted_files
    except subprocess.CalledProcessError as ex:
        logger.error(f"Error executing git diff: {ex};\n{ex.stderr}")
        raise ex


def get_current_branch() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as ex:
        logger.error(f"Error executing git rev-parse: {ex};\n{ex.stderr}")
        raise ex
