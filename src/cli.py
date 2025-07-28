import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


def cmd_fetch(_):
    run(f"python {BASE_DIR/'data_fetch.py'}")


def cmd_process(_):
    run(f"python {BASE_DIR/'data_processing.py'}")


def cmd_analyze(_):
    run(f"python {BASE_DIR/'analysis.py'}")


def cmd_stats(_):
    run(f"python {BASE_DIR/'team_stats.py'}")


def cmd_homeaway(_):
    run(f"python {BASE_DIR/'home_away_stats.py'}")


def cmd_visualize(_):
    run(f"python {BASE_DIR/'visualization.py'}")


def cmd_all(_):
    cmd_fetch(None)
    cmd_process(None)
    cmd_analyze(None)
    cmd_stats(None)
    cmd_homeaway(None)
    cmd_visualize(None)


COMMANDS = {
    'fetch': cmd_fetch,
    'process': cmd_process,
    'analyze': cmd_analyze,
    'stats': cmd_stats,
    'homeaway': cmd_homeaway,
    'viz': cmd_visualize,
    'all': cmd_all,
}


def main():
    parser = argparse.ArgumentParser(description="Premier League analysis toolkit")
    parser.add_argument('command', choices=COMMANDS.keys(), help='Action to perform')
    args = parser.parse_args()
    COMMANDS[args.command](args)


if __name__ == '__main__':
    main()
