import argparse
import json

from src.inference import predict_query
from src.llm_refiner import refine_with_llm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Student Query Understanding – classify intent, topic, and difficulty."
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help='Student query in natural language, e.g., "I don\'t understand backpropagation".',
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="If set, refine ML predictions using the LLM refinement layer.",
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        default="gpt-4o-mini",
        help="LLM model name to use for refinement (only used when --use-llm is set).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ml_result = predict_query(args.query)

    if args.use_llm:
        result = refine_with_llm(args.query, ml_result, model=args.llm_model)
    else:
        result = ml_result

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
