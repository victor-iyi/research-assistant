# Research Assistant

Research assistant is an AI tool that helps you learn more about a given research.
You can generate summaries, questions, and answers from a research paper.

![Research Assistant][demo-image]

[demo-image]: ./res/images/research-assistant-demo.png

## Installation

You can install the tool using the following command:

```sh
poetry install
```

This will install all the dependencies required to run the tool.

You can optionally install the dev-dependencies using the following command:

```sh
poetry install --with dev
```

## Setup

By the default, the tool uses OpenAI's model. You need to set the `OPENAI_API_KEY`
by creating a `.env` file in the root directory of the project.

```sh
mv .env.example .env
```

Then open the `.env` file and set the `OPENAI_API_KEY` to your OpenAI API key.

```sh
OPENAI_API_KEY=sk-...
```

## Usage

Launch a local server using the following command:

```sh
streamlit run chat.py
```

This will open a browser window with the tool running on `localhost:8501`.
You can now interact with the tool. Upload a research paper and converse with
the AI to generate summaries, questions, and answers.

## Roadmap

- [x] Create a basic chat interface
- [ ] Make initial loading faster
- [ ] Use arxiv URL to fetch research paper
- [ ] Add configuration options

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository]. If you have made a fork with
substantial modifications that you feel may be useful, then please
[open a new issue on GitHub][issues] with a link and short description.

## License (MIT)

This project is opened under the [MIT][license] which allows very broad use for
both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright.
These images are included under the "fair usage" laws.

[original repository]: https://github.com/victor-iyi/research-assistant
[issues]: https://github.com/victor-iyi/research-assistant/issues
[license]: ./LICENSE
