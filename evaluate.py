from rouge_score import rouge_scorer


def evaluate_rouge(reference, generated):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, generated)


if __name__ == "__main__":
    ref = "This paper proposes a new AI model"  # put reference summary here
    gen = "The study introduces an AI model"    # put generated summary here

    print(evaluate_rouge(ref, gen))