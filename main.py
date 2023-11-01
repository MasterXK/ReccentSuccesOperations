from src import masks, widget, processing, extra


def main() -> None:
    print(extra.get_dir_content('.', count_all=True))


if __name__ == "__main__":
    main()
