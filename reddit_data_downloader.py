import os
import json
from datetime import datetime, timedelta
import praw
import time
import prawcore

def initialize_reddit():
    return praw.Reddit(
        client_id="YOUR-CLIENT-ID",
        client_secret="YOUR-CLIENT-SECRET",
        user_agent="YOUR-USER-AGENT"
    )

def load_state(subreddit_list, state_folder_path):
    state_file_path = os.path.join(state_folder_path, 'state.json')
    try:
        with open(state_file_path, 'r') as state_file:
            state = json.load(state_file)
    except FileNotFoundError:
        state = {subreddit: {'counter': 1, 'last_run': None} for subreddit in subreddit_list}
    return state

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def format_subreddit_name(subreddit_name):
    return subreddit_name.replace('BNBinance', 'Binance Coin').replace('solana', 'Solana').replace(
        'dogecoin', 'Dogecoin').replace('ethereum', 'Ethereum')

def create_file_path(subreddit_folder_path, folder_name, counter):
    return os.path.join(subreddit_folder_path, f"{folder_name}_{counter}.txt")

def save_data_to_file(file_path, hot_posts_last_24_hours):
    with open(file_path, 'w', encoding='utf-8') as file:
        for post in hot_posts_last_24_hours:
            file.write(post.title)
            file.write(post.selftext)
            post.comments.replace_more(limit=2)
            post_comments = post.comments.list()
            unique_comments = set()
            for comment in post_comments:
                if comment.body not in unique_comments:
                    file.write(comment.body + '\n')
                    unique_comments.add(comment.body)
                    replies = comment.replies
                    for reply in replies:
                        if reply.body not in unique_comments:
                            file.write(reply.body + '\n')
                            unique_comments.add(reply.body)

def handle_exceptions(subreddit_name, e):
    if isinstance(e, prawcore.exceptions.ResponseException):
        print(f"HTTP error occurred for subreddit {subreddit_name}: {e}")
    elif isinstance(e, praw.exceptions.PRAWException):
        print(f"Error occurred for subreddit {subreddit_name}: {e}")
    elif isinstance(e, praw.exceptions.APIException):
        print(f"API error occurred for subreddit {subreddit_name}: {e}")
    elif isinstance(e, praw.exceptions.RequestException):
        print(f"Request error occurred for subreddit {subreddit_name}: {e}")
    else:
        print(f"Unexpected error occurred for subreddit {subreddit_name}: {e}")

def main():
    reddit = initialize_reddit()
    subreddit_list = ["BNBinance", "Bitcoin", "Cardano", "Chainlink", "solana",
                      "dogecoin", "ethereum", "Litecoin", "Polkadot", "XRP"]
    base_folder_path = r"D:\PyCharmProjects\RedditMood\reddit_data"
    state_folder_path = r"D:\PyCharmProjects\RedditMood"

    state = load_state(subreddit_list, state_folder_path)
    twenty_four_hours_ago = datetime.now() - timedelta(hours=24)  # Uwzględnienie różnicy czasu lokalnego

    for subreddit_name in subreddit_list:
        subreddit = reddit.subreddit(subreddit_name)
        folder_name = format_subreddit_name(subreddit_name)
        create_folder_if_not_exists(os.path.join(base_folder_path, folder_name))

        if folder_name not in state:
            state[folder_name] = {'counter': 1, 'last_run': None}

        if state[folder_name]['last_run'] is not None:
            time_since_last_run = datetime.now() - datetime.fromisoformat(state[folder_name]['last_run'])
            if time_since_last_run < timedelta(hours=24):
                next_run_time = datetime.fromisoformat(state[folder_name]['last_run']) + timedelta(hours=24)
                print(f"Not enough time has passed since the last run for {subreddit_name}.")
                print(f"Next data will be available at: {next_run_time}")
                continue

        try:
            hot_posts = subreddit.hot(limit=5)
            hot_posts_last_24_hours = [post for post in hot_posts if datetime.utcfromtimestamp(post.created_utc) > twenty_four_hours_ago]
            subreddit_folder_path = os.path.join(base_folder_path, folder_name)
            state[folder_name]['last_run'] = datetime.now().isoformat()  # Uwzględnienie różnicy czasu lokalnego

            counter = state[folder_name]['counter']
            file_path = create_file_path(subreddit_folder_path, folder_name, counter)
            save_data_to_file(file_path, hot_posts_last_24_hours)

            print(f"Saved data to file: {file_path}")
            print("Delay of 5 seconds enabled")
            time.sleep(5)
            print("\n")

        except Exception as e:
            handle_exceptions(subreddit_name, e)
            continue

        state[folder_name]['counter'] += 1

    with open(os.path.join(state_folder_path, 'state.json'), 'w') as state_file:
        state_to_save = {format_subreddit_name(k): v for k, v in state.items()}
        json.dump(state_to_save, state_file, indent=4)
        print("Updated state information")

if __name__ == "__main__":
    main()

