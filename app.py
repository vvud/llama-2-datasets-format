"""
using the data from datasets/ directory
"""

from llama_formatter import llama_formatter


def main():
    formatter = llama_formatter()
    formatter.format_dataset_csv(
        input_filepath="datasets/csv/raw/data-raw.csv",
        output_filepath="datasets/csv/fmt/data-fmt.csv"
    )


if __name__ == "__main__":
    main()
