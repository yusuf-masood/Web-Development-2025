if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    # Remove duplicates from the list of scores and sort it in descending order
    unique_scores = sorted(set(scores), reverse=True)

    # Find the runner-up score
    runner_up_score = unique_scores[1]

    print(runner_up_score)
