import argparse
from debate.debate_runner import run_debate_sessions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shuffle-speakers", action = "store_true", dest = "shuffle_speakers", help="Shuffle order of debate speakers")
    args = parser.parse_args()
    print(args.shuffle_speakers)
    run_debate_sessions(args.shuffle_speakers)

if __name__ == "__main__":
    main()
